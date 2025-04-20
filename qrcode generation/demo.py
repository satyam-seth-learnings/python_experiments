import qrcode

# Example-1
img = qrcode.make("Some data here")
print(type(img))  # qrcode.image.pil.PilImage
img.save("ex1_some_file.png")

# Example -2
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data("Some data")
qr.make(fit=True)

img = qr.make_image(back_color=(255, 195, 235), fill_color=(55, 95, 35))
# img = qr.make_imaxge(fill_color="black", back_color="white")
img.save("ex2_some_file.png")
