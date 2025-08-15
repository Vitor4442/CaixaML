document.addEventListener('DOMContentLoaded', () => {
    const startDateInput = document.getElementById('startDate');
    const endDateInput = document.getElementById('endDate');
    const dateRange = document.getElementById('dateRange');

    // Define a data atual (11/08/2025 21:41 -03)
    const hoje = new Date('2025-08-11T21:41:00-03:00');
    const primeiroDia = new Date(hoje.getFullYear(), hoje.getMonth(), 1);
    const ultimoDia = new Date(hoje.getFullYear(), hoje.getMonth() + 1, 0);

    // Define as datas padrão como o mês atual
    startDateInput.value = primeiroDia.toISOString().split('T')[0];
    endDateInput.value = ultimoDia.toISOString().split('T')[0];
    atualizarIntervaloData();

    // Atualiza o intervalo de data quando os campos mudam
    startDateInput.addEventListener('change', atualizarIntervaloData);
    endDateInput.addEventListener('change', atualizarIntervaloData);

    function atualizarIntervaloData() {
        const dataInicio = new Date(startDateInput.value);
        const dataFim = new Date(endDateInput.value);
        dateRange.textContent = `${dataInicio.toLocaleDateString('pt-BR')} a ${dataFim.toLocaleDateString('pt-BR')}`;
    }

        //Ação de clicar no botão
    const botao = document.querySelector('.add-btn')
    const fileinput = document.getElementById('fileInput')

    botao.addEventListener('click', () => fileinput.click());

    fileinput.addEventListener('change', (event) => {
                // O arquivo selecionado está em event.target.files
    const arquivoSelecionado = event.target.files[0];
                
    if (arquivoSelecionado) {
                console.log('Arquivo selecionado:', arquivoSelecionado);
                    alert(`Você selecionou: ${arquivoSelecionado.name}`);
                    
                    // Aqui você pode fazer o que quiser com o arquivo
                    // Por exemplo: enviar para um servidor, ler o conteúdo, etc.
                }
            });
    });

