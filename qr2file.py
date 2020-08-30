import os
import base64
from PIL import Image
from PIL import ImageGrab
from pyzbar import pyzbar
from pyzbar.wrapper import ZBarSymbol
from pyzbar.pyzbar import decode
import time

total = 869
output_filename = "数据核查分析-20200828.xlsx"

dic = dict()

while True:
    img = ImageGrab.grab()
    qrcodes = decode(img, symbols=[ZBarSymbol.QRCODE])
    if len(qrcodes) > 0:
        parts = qrcodes[0].data.split(b'|')
        seq = int(parts[0])
        if seq not in dic:
            data = base64.decodebytes(parts[1])
            dic[seq] = data
            print(seq)
        if len(dic) >= total: 
            break
    time.sleep(0.1)

f = open(output_filename, mode="wb")
try:
    for i in range(len(dic)):
        f.write(dic[i])
finally:
    f.close()