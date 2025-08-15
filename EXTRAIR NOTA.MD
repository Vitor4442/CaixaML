1. Definição da Ideia e Objetivo
    O que vai ser feito? → site
    Qual problema resolve? → Melhorar processo em realizar livro caixa.
    Quem vai usar? → Contribuidores da JVF.

2. Levantamento de Requisitos
    Funcionais → O sisteme ira coletar dados de notas fiscais do Mercado livre em PDF ira organizar em ordem decrescente
    e em seguida ira colocar em um excel os seguintes dados: (numero da anota, data, nome, nome do produto, quantiade, valor da nota, nome do cliente).
    Não funcionais → Desempenho, tempo de resposta e interface amigável.
    Restrições → Coletar somente certo dados.

3. Análise e Planejamento

    Python + Flask (servidor)
    pdfplumber (ler PDFs)
    pandas + openpyxl (gerar Excel)
    HTML/CSS/JS (interface simples)

   [Contribuidor da JVF] ---> (Fazer upload PDF)
                         ---> (Extrair dados da nota)
                         ---> (Organizar em ordem decrescente)
                         ---> (Gerar arquivo Excel)
                         ---> (Baixar planilha) ou (adicionar dados a planilha)
 

Diagrama de Classes (exemplo em Python/Flask)
Classes sugeridas:

UploadHandler → Lida com o envio e armazenamento temporário do PDF
PDFExtractor → Lê e extrai dados usando pdfplumber
DataOrganizer → Ordena os dados
ExcelExporter → Gera e salva o Excel
WebInterface → Roda o Flask e interage com o usuário

Exemplo simplificado:

diff
Copiar
Editar
+----------------+
| UploadHandler  |
+----------------+
| +upload_file() |
+----------------+

+----------------+
| PDFExtractor   |
+----------------+
| +extract_data()|
+----------------+

+----------------+
| DataOrganizer  |
+----------------+
| +sort_data()   |
+----------------+

+----------------+
| ExcelExporter  |
+----------------+
| +generate_excel() |
+----------------+

+----------------+
| WebInterface   |
+----------------+
| +run_app()     |
+----------------+
Relacionamentos:

WebInterface chama UploadHandler
UploadHandler passa PDF para PDFExtractor
PDFExtractor envia dados para DataOrganizer
DataOrganizer envia dados organizados para ExcelExporter
