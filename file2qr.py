import qrcode
import base64
import os.path as path
import sys
import os

pathname = sys.argv[1]
filename = path.basename(pathname)
if len(sys.argv) > 3:
    savepath = sys.argv[2]
else:
    savepath = 'qrcodes'

if not path.exists(savepath):
    os.mkdir(savepath)

print(savepath)

file = open(pathname, mode="rb")
try:
    eof = False
    idx = 0
    while not(eof):
        buf = file.read(1024)
        s = base64.b64encode(buf)
        s = bytes(str(idx), encoding="ascii")+b"|"+s
        data = qrcode.util.QRData(s, check_data=False)
        print(data)
        img = qrcode.make(data, box_size=4)
        target = path.join(savepath, filename+"-"+str(idx)+".jpg")
        img.save(target)
        idx = idx + 1
        if (len(buf) < 1024):
            eof = True
finally:
    file.close()

print("done! total ", idx)