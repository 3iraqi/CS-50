# 3- extensions.py
"""
.gif
.jpg
.jpeg
.png
.pdf
.txt
.zip
"""
ex =[".gif", ".jpg", ".jpeg", ".png", ".pdf", ".txt", ".zip"]

x = input("File name: ").lower().strip()
if not x.endswith(tuple(ex)):
    print("application/octet-stream")
else:
    if x.endswith(ex[0]):
        print("image/gif")
    elif x.endswith(ex[1]) or x.endswith(ex[2]):
        print("image/jpeg")
    elif x.endswith(ex[3]):
        print("image/png")
    elif x.endswith(ex[4]):
        print("application/pdf")
    elif x.endswith(ex[5]):
        print("text/plain")
    elif x.endswith(ex[6]):
        print("application/zip")
