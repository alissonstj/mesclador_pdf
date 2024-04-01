import PyPDF2
import os

merger = PyPDF2.PdfMerger("arquivos")

lista_arquivos = os.listdir("arquivos")
lista_arquivos.sort()
print(lista_arquivos)

for arquivo in lista_arquivos:
    if ".pdf" in arquivo:
        merger.append(f"arquivos/{arquivo}") #função append adiciona o novo arquivo

merger.write("arquivo_mesclado.pdf")        #write escreve\cria o novo arquivo