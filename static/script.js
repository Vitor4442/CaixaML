document.getElementById("fileInput").addEventListener("change", async function () {
    const file = this.files[0];
    if (!file) return;

    let formData = new FormData();
    formData.append("pdf", file);

    try {
        const response = await fetch("/upload_pdf", {
            method: "POST",
            body: formData
        });

        const data = await response.json();

        if (data.erro) {
            alert("Erro: " + data.erro);
            return;
        }

        // ---------- Preencher tabela ----------
        const tbody = document.querySelector("table tbody");
        tbody.innerHTML = ""; // limpar antes

        let saldo = 0;

        data.produtos.forEach(prod => {
            saldo += parseFloat(prod.valor.replace(".", "").replace(",", "."));

            const row = `
                <tr>
                    <td>${new Date().toLocaleDateString("pt-BR")}</td>
                    <td>${prod.descricao}</td>
                    <td>Produto</td>
                    <td>Entrada</td>
                    <td>${prod.valor}</td>
                    <td>${saldo.toFixed(2).replace(".", ",")}</td>
                </tr>
            `;
            tbody.insertAdjacentHTML("beforeend", row);
        });

        // ---------- Preencher Resumo ----------
        document.querySelectorAll(".summary-value")[0].textContent = "R$ " + (data.valor_total || "0,00");
        document.querySelectorAll(".summary-value")[1].textContent = "R$ 0,00"; // Saídas
        document.querySelectorAll(".summary-value")[2].textContent = "R$ " + (data.valor_total || "0,00");

        // ---------- Observações ----------
        let obs = document.querySelector(".observations textarea");
        obs.value = `
NF-e: ${data.nota}
Cliente: ${data.nome}
Endereço: ${data.endereco}
Município: ${data.municipio} - ${data.uf}
Valor Total: R$ ${data.valor_total}
        `.trim();

    } catch (err) {
        console.error(err);
        alert("Erro ao processar o PDF");
    }
});
