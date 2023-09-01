import qrcode
import os
#Create an instance of PdfFileMerger() class
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import white,red,black
from reportlab.lib.units import mm
from PyPDF2 import PdfWriter, PdfReader
import io
pdfmetrics.registerFont(TTFont('Exo2', 'Exo2-Regular.ttf'))
import numpy as np 

print("Gerador de etiquetas!!!")

print("Etiqueta para:")
print("1 - H1.2")
print("2 - H1.3")
sensor_base=int(input())

if sensor_base==1:
    base_pdf = 'base_h12.pdf'
if sensor_base==2:
    base_pdf = 'base_h13.pdf'


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
    final=int(input())
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
    link = "https://sensor.hedro.com.br?sn="+str(i).zfill(5)
    qr.add_data(link)
    qr.make()
    img = qr.make_image(fill_color="black", back_color="transparent")
    name = path+"/qrcodes/"+str(i)
    img.save(name)
# # adicionar as fontes que vou usar no projeto


output_pdf = 'final.pdf'

pdf = PdfReader(base_pdf)

count = 0

output = PdfWriter()

for i in lista:
    output.add_page(pdf.pages[0])

outputStream = open(output_pdf, "wb")
output.write(outputStream)
outputStream.close()

out_canvas = 'infos.pdf'
pdf_canvas = canvas.Canvas(out_canvas)

if sensor_base==1:
    for i in lista:
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
if sensor_base==2:       
    for i in lista:
        pdf_canvas.setPageSize((45*mm, 51*mm))
        pdf_canvas.setFont('Exo2', 12)
        pdf_canvas.rotate(0)
        name = path+"/qrcodes/"+str(i)
        pdf_canvas.drawImage(name, 32, -150, width=64,
                            preserveAspectRatio=True, mask='auto')
        pdf_canvas.rotate(90)
        pdf_canvas.setFillColor(black)
        pdf_canvas.drawString(40, -28, str(i).zfill(5))
        pdf_canvas.rotate(0)
        pdf_canvas.showPage()

pdf_canvas.save()

pdf_base = PdfReader('final.pdf')
pdf_canvas = PdfReader('infos.pdf')

output2 = PdfWriter()
count = 0

for i in lista:
    pdf_base.pages[count].merge_page(pdf_canvas.pages[count])
    output2.add_page(pdf_base.pages[count])
    count = count+1

output2.add_page(pdf.pages[1])
outputStream = open('lista_impressao.pdf', "wb")
output2.write(outputStream)
outputStream.close()