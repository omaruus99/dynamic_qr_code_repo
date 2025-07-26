import qrcode

base_url = "https://github.com/"

client_id = input("Identifiant unique du client (ex: client001) : ")
full_url = base_url + client_id

qr = qrcode.QRCode(version=1, box_size=10, border=5)
qr.add_data(full_url)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save(f"qr_{client_id}.png")

print(f"✅ QR code généré : {full_url}")
