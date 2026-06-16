import urllib.request
import os

def atnaujinti_epg():
    print("Pradedamas tikros TV programos siuntimas...")
    
    # Šis šaltinis šiuo metu yra 100% aktyvus, atviras ir atnaujinamas kasdien
    url = "https://raw.githubusercontent.com/Lietuva/TV/main/epg.xml"
    laikinas_failas = "atsisiusta_programa.xml"
    
    try:
        # Atsisiunčiame failą
        req = urllib.request.Request(
            url, 
            headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
        )
        with urllib.request.urlopen(req) as response, open(laikinas_failas, 'wb') as out_file:
            out_file.write(response.read())
            
        print("Atsisiųsta sėkmingai!")
        
        # Patikriname, ar failas nėra tuščias
        if os.path.exists(laikinas_failas) and os.path.getsize(laikinas_failas) > 5000:
            if os.path.exists("programa.xml"):
                os.remove("programa.xml")
            os.rename(laikinas_failas, "programa.xml")
            print("programa.xml sėkmingai perrašytas su tikrais duomenimis!")
        else:
            print("Klaida: Atsisiųstas failas per mažas arba tuščias.")
            
    except Exception as e:
        print(f"Įvyko klaida: {e}")
        if os.path.exists(laikinas_failas):
            os.remove(laikinas_failas)

if __name__ == "__main__":
    atnaujinti_epg()
