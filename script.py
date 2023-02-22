import qrcode
import os
#Create an instance of PdfFileMerger() class
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import white,red
from reportlab.lib.units import mm
from PyPDF2 import PdfWriter, PdfReader
import io
pdfmetrics.registerFont(TTFont('Exo2', 'Exo2-Regular.ttf'))
import numpy as np 

print("Gerador de etiquetas!!!")
print("Escolha o tipo de geração:")
print("1 -Lista")
print("2 -Sequencia")
x=int(input())

initial=0
final=0
lista=[]

if x==1:
    print("Para finalizar a lista digite '-1'.")
    print("Escolhido Lista, digitar os numeros:")
    entrada=0
    while (entrada != -1):
        entrada=int(input("Digite -1 para sair:"))
        if int(entrada)!=-1:
            lista.append(int(entrada))
if x==2:
    print("Escolhido Sequencia:")
    print("Digitar o inicio:")
    initial=int(input())
    print("Digitar o Fim:")
    final=int(input())+1
    for i in range(initial,final):
        lista.append(i)

name = './pdfs/impressao_grafica.pdf'

path = os.getcwd()

for i in lista:
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=15,
        border=0)
    link = "http://meusensor.hedro.com.br/?id="+str(i).zfill(5)
    qr.add_data(link)
    qr.make()
    img = qr.make_image(fill_color="black", back_color="transparent")
    name = path+"/qrcodes/"+str(i)
    img.save(name)
# # adicionar as fontes que vou usar no projeto

base_pdf = 'base.pdf'
output_pdf = 'final.pdf'

images = os.listdir('qrcodes')

arr = [int(numeric_string) for numeric_string in images]

images = np.sort(arr)

pdf = PdfReader(base_pdf)

count = 0

output = PdfWriter()

for i in images:
    output.add_page(pdf.pages[0])

outputStream = open(output_pdf, "wb")
output.write(outputStream)
outputStream.close()

out_canvas = 'infos.pdf'
pdf_canvas = canvas.Canvas(out_canvas)
    
for i in images:
    pdf_canvas.setPageSize((45*mm, 51*mm))
    pdf_canvas.setFont('Exo2', 12)
    pdf_canvas.rotate(0)
    name = path+"/qrcodes/"+str(i)
    pdf_canvas.drawImage(name, 39, -145, width=50,
                         preserveAspectRatio=True, mask='auto')
    pdf_canvas.rotate(45)
    pdf_canvas.setFillColor(white)
    pdf_canvas.drawString(78, -45, str(i).zfill(5))
    pdf_canvas.rotate(0)
    pdf_canvas.showPage()

pdf_canvas.save()

pdf_base = PdfReader('final.pdf')
pdf_canvas = PdfReader('infos.pdf')

output2 = PdfWriter()
count = 0

for i in images:
    
    pdf_base.pages[count].merge_page(pdf_canvas.pages[count])
    output2.add_page(pdf_base.pages[count])
    count = count+1

output2.add_page(pdf.pages[1])
outputStream = open('lista_impressao', "wb")
output2.write(outputStream)
outputStream.close()