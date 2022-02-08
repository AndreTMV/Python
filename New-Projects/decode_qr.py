from pyzbar.pyzbar import decode
from PIL import Image

img = Image.open('/home/andrew/Imágenes/my_new_qrcode.jpg')
result = decode(img)
print(result)
