import os
import openpyxl #importa funçoes do excel

diretorio = 'PDF' #pasta onde vai receber os pdfs
files = os.listdir(diretorio) # os.listdir faz a listagem de arquivos 
files_quantity = len(files)  # len numero a quantiade de arquivos

if files_quantity == 0:
    raise Exception("Não foi encontrado nenhum arquivo nessa pasta")

lc = LivroCaixa() #instancia do objto livro caixa
le = lc.active 
le.titulo = 'PDF IMPORTADO'

print(files_quantity)
print(le.titulo)