import time

while True:
    try:
        f = open("C:\\Users\\Gilce\\AppData\\Roaming\\MetaQuotes\\Terminal\\D0E8209F77C8CF37AD8BF550E51FF075\\MQL5\\Files\\teste.txt", "r")
        valor = f.readline()
        print(valor[2:50])
        f.close()
    except:
        print("Deu erro")
    time.sleep(1)