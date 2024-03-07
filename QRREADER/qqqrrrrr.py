import qrcode as qr

print("Uygulamamıza hoş geldiniz, metin link vb. QR'a dönüştürmekte kullanılır.")
cevirilecek = input("Resim için bir isim giriniz: ")
input_text = input("Lütfen QR'a dönüştürmek istediğiniz metni giriniz: ")

code = qr.make(input_text)
code.save(f'{cevirilecek}.png')

print("Dönüştürme tamamlandı.")
