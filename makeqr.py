#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3.6
import qrcode
i=360*360
#for i in range(5):
qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=1,
)
qr.add_data('https://nofb.github.io')
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
print(img)
img.resize((360,360)).save("mynewface"+str(i)+".png", "PNG")
