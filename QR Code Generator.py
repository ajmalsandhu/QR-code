import qrcode
img = qrcode.make("https://www.youtube.com/@BlackWolf-us1vz")
img.save("BlackWolf.png")