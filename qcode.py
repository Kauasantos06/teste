import qrcode 

# Lista de links para gerar QR Codes
links = {
    'https://www.linkedin.com/in/kau%C3%A3-santos-71214a32a/',
    'https://www.instagram.com/kaua_santoss06/',
    'https://x.com/Kaua_Santoss06'
}

# Loop para gerar QR codes automaticamente
for i, link in enumerate(links, start=1):
    qr = qrcode.QRCode(version = 1, box_size = 10, border = 4)
    qr.add_data(link)
    qr.make()

    qr.print_ascii()

    img = qr.make_image(fill_color = 'black', back_color = 'white')
    img.save('lenkedin_qr.png') 

    print(f"QR Code {i} gerado para: {link}")
   
print("Todos os QR Codes foram gerados com sucesso!")

