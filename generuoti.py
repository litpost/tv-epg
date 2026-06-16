import urllib.request
import os

def atnaujinti_epg():
    print("Siunčiama tikra TV programa...")
    
    # Šis šaltinis yra stabilus ir atviras Lietuvos EPG XML formatu
    url = "https://raw.githubusercontent.com/skid9000/epg/master/epg.xml"
    laikinas_failas = "atsisiusta_programa.xml"
    
    try:
        # Atsiunčiame failą iš patikimo šaltinio
        urllib.request.urlretrieve(url, laikinas_failas)
        print("Atsisiųsta sėkmingai!")
        
        # Kadangi failas jau yra XML formato, tiesiog perperkeliame ir perrašome programa.xml
        if os.path.exists(laikinas_failas) and os.path.getsize(laikinas_failas) > 1000:
            if os.path.exists("programa.xml"):
                os.remove("programa.xml")
            os.rename(laikinas_failas, "programa.xml")
            print("programa.xml sėkmingai atnaujintas su tūkstančiais tikrų laidų!")
        else:
            print("Klaida: Atsisiųstas failas per mažas arba tuščias.")
            
    except Exception as e:
        print(f"Įvyko klaida: {e}")
        if os.path.exists(laikinas_failas):
            os.remove(laikinas_failas)

if __name__ == "__main__":
    atnaujinti_epg()
