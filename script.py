initial = 1051
final = 1059+1

lista = [
    892,
    959,
    971,
    972,
    973,
    974,
    975,
    976,
    977,
    978,
    979,
    980,
    981,
    982,
    983,
    984,
    985,
    986,
    987,
    988,
    989,
    990,
    1011,
    1012,
    1013,
    1014,
    1015,
    1016,
    1017,
    1018,
    1019,
    1020,
    1021,
    1022,
    1023,
    1024,
    1028,
    1030,
    1031,
    1032,
    1033,
    1034,
    1035,
    1036,
    1037,
    1038,
    1039,
    1040,
    1041,
    1042,
    1043,
    1044,
    1045,
    1046,
    1047,
    1048,
    1049,
    1050,
    1051,
    1052
]

name = 'impressao_grafica.pdf'

path = os.getcwd()
# for i in range(initial,final):
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
# adicionar as fontes que vou usar no projeto

base_pdf = 'base.pdf'
output_pdf = 'final.pdf'

images = os.listdir('qrcodes')
arr = [int(numeric_string) for numeric_string in images]
arr
images = np.sort(arr)


pdf = PdfFileReader(base_pdf)

count = 0
path = os.getcwd()
output = PdfFileWriter()

for i in range(len(images)):
    output.addPage(pdf.getPage(0))
outputStream = open(output_pdf, "wb")
output.write(outputStream)
outputStream.close()

out_canvas = 'infos.pdf'
pdf_canvas = canvas.Canvas(out_canvas)

# for i in range(initial,final):
for i in images:
    pdf_canvas.setPageSize((45*mm, 51*mm))
    pdf_canvas.setFont('Exo2', 12)
    pdf_canvas.rotate(0)
    pdf_canvas.drawImage(name, 39, -145, width=50,
                         preserveAspectRatio=True, mask='auto')
    pdf_canvas.rotate(45)
    pdf_canvas.setFillColor(white)
    pdf_canvas.drawString(78, -45, str(i).zfill(5))
    pdf_canvas.rotate(0)
    name = path+"/qrcodes/"+str(i)
    pdf_canvas.showPage()

pdf_canvas.save()

pdf_base = PdfFileReader('final.pdf')
pdf_canvas = PdfFileReader('infos.pdf')

output2 = PdfFileWriter()
count = 0
for i in images:
    # for i in range(initial,final):
    pdf_base.getPage(count).mergePage(pdf_canvas.getPage(count))
    output2.addPage(pdf_base.getPage(count))
    count = count+1
output2.addPage(pdf.getPage(1))
outputStream = open('lista_impressao', "wb")
output2.write(outputStream)
outputStream.close()

initial = 1051
final = 1059+1

lista = [
    892,
    959,
    971,
    972,
    973,
    974,
    975,
    976,
    977,
    978,
    979,
    980,
    981,
    982,
    983,
    984,
    985,
    986,
    987,
    988,
    989,
    990,
    1011,
    1012,
    1013,
    1014,
    1015,
    1016,
    1017,
    1018,
    1019,
    1020,
    1021,
    1022,
    1023,
    1024,
    1028,
    1030,
    1031,
    1032,
    1033,
    1034,
    1035,
    1036,
    1037,
    1038,
    1039,
    1040,
    1041,
    1042,
    1043,
    1044,
    1045,
    1046,
    1047,
    1048,
    1049,
    1050,
    1051,
    1052
]

name = 'impressao_grafica.pdf'

path = os.getcwd()
# for i in range(initial,final):
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
# adicionar as fontes que vou usar no projeto

base_pdf = 'base.pdf'
output_pdf = 'final.pdf'

images = os.listdir('qrcodes')
arr = [int(numeric_string) for numeric_string in images]
arr
images = np.sort(arr)


pdf = PdfFileReader(base_pdf)

count = 0
path = os.getcwd()
output = PdfFileWriter()

for i in range(len(images)):
    output.addPage(pdf.getPage(0))
outputStream = open(output_pdf, "wb")
output.write(outputStream)
outputStream.close()

out_canvas = 'infos.pdf'
pdf_canvas = canvas.Canvas(out_canvas)

# for i in range(initial,final):
for i in images:
    pdf_canvas.setPageSize((45*mm, 51*mm))
    pdf_canvas.setFont('Exo2', 12)
    pdf_canvas.rotate(0)
    pdf_canvas.drawImage(name, 39, -145, width=50,
                         preserveAspectRatio=True, mask='auto')
    pdf_canvas.rotate(45)
    pdf_canvas.setFillColor(white)
    pdf_canvas.drawString(78, -45, str(i).zfill(5))
    pdf_canvas.rotate(0)
    name = path+"/qrcodes/"+str(i)
    pdf_canvas.showPage()

pdf_canvas.save()

pdf_base = PdfFileReader('final.pdf')
pdf_canvas = PdfFileReader('infos.pdf')

output2 = PdfFileWriter()
count = 0
for i in images:
    # for i in range(initial,final):
    pdf_base.getPage(count).mergePage(pdf_canvas.getPage(count))
    output2.addPage(pdf_base.getPage(count))
    count = count+1
output2.addPage(pdf.getPage(1))
outputStream = open('lista_impressao', "wb")
output2.write(outputStream)
outputStream.close()
