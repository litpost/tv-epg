from datetime import datetime

def generuoti_epg():
    # Gauname šiandienos datą formatu YYYYMMDD
    today = datetime.now().strftime("%Y%m%d")
    
    xml_data = f"""<?xml version="1.0" encoding="UTF-8"?>
<tv generator-info-name="Automatinis Vietinis EPG">
  <channel id="LRT"><display-name>LRT Televizija</display-name></channel>
  <channel id="TV3"><display-name>TV3</display-name></channel>
  <channel id="LNK"><display-name>LNK</display-name></channel>
  <channel id="BTV"><display-name>BTV</display-name></channel>

  <programme start="{today}060000 +0300" stop="{today}090000 +0300" channel="LRT">
    <title>Labas rytas, Lietuva</title>
    <desc>Informacinė-pramoginė laida.</desc>
  </programme>
  <programme start="{today}183000 +0300" stop="{today}193000 +0300" channel="LRT">
    <title>LRT Žinios</title>
    <desc>Svarbiausios naujienos iš Lietuvos ir pasaulio.</desc>
  </programme>
  <programme start="{today}210000 +0300" stop="{today}230000 +0300" channel="LRT">
    <title>Vakaro vaidybinis filmas</title>
    <desc>Geriausias europietiškas kinas jūsų namuose.</desc>
  </programme>

  <programme start="{today}063000 +0300" stop="{today}083000 +0300" channel="TV3">
    <title>TV3 Žinios. Ryto santrauka</title>
    <desc>Svarbiausios ryto naujienos.</desc>
  </programme>
  <programme start="{today}183000 +0300" stop="{today}193000 +0300" channel="TV3">
    <title>TV3 Žinios</title>
    <desc>Karščiausi dienos įvykiai.</desc>
  </programme>

  <programme start="{today}183000 +0300" stop="{today}193000 +0300" channel="LNK">
    <title>KK2</title>
    <desc>Apžvalginė aktualijų laida.</desc>
  </programme>
  <programme start="{today}193000 +0300" stop="{today}210000 +0300" channel="LNK">
    <title>KK2 Penktadienis</title>
    <desc>Smagi savaitgalio pokalbių laida.</desc>
  </programme>

  <programme start="{today}200000 +0300" stop="{today}220000 +0300" channel="BTV">
    <title>Sava savaitė</title>
    <desc>Informacinė analitinė laida.</desc>
  </programme>
</tv>
"""
    with open("programa.xml", "w", encoding="utf-8") as f:
        f.write(xml_data)
    print("programa.xml sėkmingai sugeneruotas šiandienai!")

if __name__ == "__main__":
    generuoti_epg()
