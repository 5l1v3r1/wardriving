#baycomard - Türk mitolojisinde av tanırısı olduğu için kullanılmıştır.
konumDosya=open("konum.txt","r")
konumIcerik=konumDosya.readlines()
konumDosya.close()
ssidDosya=open("ssid.txt","r")
ssidIcerik=ssidDosya.readlines()
ssidDosya.close()
logListe=[]
for konum in konumIcerik:
    konumZaman = konum.split("|")[2].splitlines()[0]
    for ssid in ssidIcerik:
        konum=konum.splitlines()[0]
        ssid=ssid.splitlines()[0]
        if konumZaman in ssid:
            log=konum+"|"+ssid.split("|")[1]+"|"+ssid.split("|")[2]+"\n"
            if not log in logListe:
                wardrivingDosya=open("wardriving.txt","a")
                wardrivingDosya.write(log)
                wardrivingDosya.close()
                logListe.append(log)
