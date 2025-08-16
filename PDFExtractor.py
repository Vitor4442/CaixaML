#importando bibliotecas
from flask import Flask, request, jsonify, render_template
import os
import PyPDF2
import re  

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/upload_pdf', methods=['POST'])
def upload_pdf():
    if 'pdf' not in request.files:
        return jsonify({"erro": "Nenhum arquivo enviado"}), 400

    pdf_file = request.files['pdf']

    if pdf_file.filename == '':
        return jsonify({"erro": "Nenhum arquivo selecionado"}), 400

    caminho_temp = os.path.join('uploads', pdf_file.filename)
    os.makedirs('uploads', exist_ok=True)
    pdf_file.save(caminho_temp)

    # Extrair texto cru
    texto = ""
    with open(caminho_temp, 'rb') as f:
        reader = PyPDF2.PdfReader(f)
        for page in reader.pages:
            texto += page.extract_text() or ""

    # Quebrar em linhas organizadas
    linhas = [l.strip() for l in texto.splitlines() if l.strip()]

    # ---------- NF ---------- c
    nf = None
    match_nf = re.search(r"000\.(\d{3}\.\d{3})", texto)
    if match_nf:
        nf = f"NF{match_nf.group(1)}"

    # ---------- Nome e Endereço ----------
    nome, endereco = None, None
    for i, linha in enumerate(linhas):
        if "NOME/RAZÃO SOCIAL" in linha:
            if i+1 < len(linhas):
                partes_nome = linhas[i+1].split()
                if len(partes_nome) >= 2:
                    nome = partes_nome[0] + " " + partes_nome[1]  # só nome + sobrenome
            if i+2 < len(linhas):
                endereco = linhas[i+2]  # linha logo após o nome
            break

    # ---------- Município + UF ----------
    municipio, uf = None, None
    for i, linha in enumerate(linhas):
        if re.search(r"\b(SP|SC|RJ|MG|RS|PR|BA|PE|CE|GO|MT|MS|ES|PA|AM|RN|RO|RR|TO|MA|PI|PB|AL|SE|DF)\b", linha):
            partes = linha.split()
            uf = partes[-1]
            municipio = " ".join(partes[:-1])
            break

    # ---------- Valor total da nota ----------
    valor_total = None
    for i, linha in enumerate(linhas):
        if "VALOR TOTAL DA NOTA" in linha:
            # procurar número válido nessa linha ou na seguinte
            trecho = " ".join(linhas[i:i+2])
            match_valor = re.search(r"(\d{1,3}(?:\.\d{3})*,\d{2})", trecho)
            if match_valor:
                valor_total = match_valor.group(1)
            break

    # ---------- Produtos ----------
    produtos = []
    for i, linha in enumerate(linhas):
        # regra simples: se tem número no fim da linha, pode ser produto
        prod_match = re.search(r"(.+?)\s+(\d{1,3}(?:\.\d{3})*,\d{2})$", linha)
        if prod_match:
            descricao = prod_match.group(1).strip()
            valor = prod_match.group(2)
            produtos.append({
                "descricao": descricao,
                "valor": valor
            })

    dados = {
        "nota": nf,
        "nome": nome,
        "endereco": endereco,
        "municipio": municipio,
        "uf": uf,
        "valor_total": valor_total,
        "produtos": produtos
    }

    return jsonify(dados)


if __name__ == "__main__":
    app.run(debug=True)
