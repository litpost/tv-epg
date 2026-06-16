import urllib.request
import gzip
import xml.etree.ElementTree as ET
import os

def atnaujinti_epg():
    print("Pradedamas tikros TV programos siuntimas...")
    
    # Naudojame patikimą, didelį alternatyvų XMLTV šaltinį (pasaulinį / Europos)
    url = "https://github.com/iptv-org/epg/releases/download/LT_tv24.lt/LT_tv24.lt.xml.gz"
    gz_failas = "laikinas_epg.xml.gz"
    xml_failas = "laikinas_epg.xml"
    
    try:
        # 1. Atsisiunčiame suspaustą programos failą
        urllib.request.urlretrieve(url, gz_failas)
        print("Failas sėkmingai atsisiųstas. Išpakuojama...")
        
        # 2. Išpakuojame GZ failą
        with gzip.open(gz_failas, 'rb') as f_in:
            with open(xml_failas, 'wb') as f_out:
                f_out.write(f_in.read())
        
        print("Failas išpakuotas. Pradedamas filtravimas...")
        
        # 3. Nuskaitome XML duomenis
        tree = ET.parse(xml_failas)
        root = tree.getroot()
        
        # Sukuriame naują, švarų XML dokumentą
        naujas_root = ET.Element("tv", {
            "generator-info-name": "Automatinis Lietuvos EPG",
            "generator-info-url": "https://github.com/litpost/tv-epg"
        })
        
        # Nukopijuojame visus kanalus ir laidas
        kanalu_skaicius = 0
        laidu_skaicius = 0
        
        for elementas in root:
            if elementas.tag == "channel" or elementas.tag == "programme":
                # Šis šaltinis jau yra skirtas Lietuvai, todėl perkeliame viską tiesiogiai
                naujas_root.append(elementas)
                if elementas.tag == "channel":
                    kanalu_skaicius += 1
                else:
                    laidu_skaicius += 1
                    
        # 4. Išsaugome galutinį programa.xml failą
        naujas_tree = ET.ElementTree(naujas_root)
        ET.indent(naujas_tree, space="  ", level=0) # Padarome gražų formatavimą
        naujas_tree.write("programa.xml", encoding="utf-8", xml_declaration=True)
        
        print(f"Sėkmingai sugeneruota! Rasta kanalų: {kanalu_skaicius}, laidų: {laidu_skaicius}")
        
    except Exception as e:
        print(f"Klaida apdorojant duomenis: {e}")
        # Jei įvyko klaida, paliekame seną failą, kad nesugadintume svetainės
        
    finally:
        # Išvalome laikinus failus, kad neužkimštume talpyklos
        if os.path.exists(gz_failas): os.remove(gz_failas)
        if os.path.exists(xml_failas): os.remove(xml_failas)

if __name__ == "__main__":
    atnaujinti_epg()
