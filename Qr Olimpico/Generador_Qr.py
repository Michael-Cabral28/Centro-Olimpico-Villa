import qrcode

contenido = "@sd2026@"

img = qrcode.make(contenido)

img.show()          # Abre el QR en el visor de imágenes
img.save("qr.png")  # También lo guarda