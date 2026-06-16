from datetime import datetime, timedelta

def generuoti_xml():
    šiandien = datetime.now()
    data_str = šiandien.strftime("%Y%m%d")
    
    xml_turinys = f"""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE tv SYSTEM "xmltv.dtd">
<tv generator-info-name="Automatinis EPG">
  <channel id="LRT.lt"><display-name lang="lt">LRT Televizija</display-name></channel>
  <channel id="TV3.lt"><display-name lang="lt">TV3</display-name></channel>
  <channel id="LNK.lt"><display-name lang="lt">LNK</display-name></channel>
  <channel id="BTV.lt"><display-name lang="lt">BTV</display-name></channel>

  <programme start="{data_str}060000 +0300" stop="{data_str}090000 +0300" channel="LRT.lt">
    <title lang="lt">Labas rytas, Lietuva</title>
    <desc lang="lt">Informacinė laida, žadinanti Lietuvą kasdien su naujausiomis žiniomis.</desc>
  </programme>
  <programme start="{data_str}120000 +0300" stop="{data_str}130000 +0300" channel="LRT.lt">
    <title lang="lt">LRT Žinios</title>
    <desc lang="lt">Svarbiausios šalies ir pasaulio naujienos operatyviai.</desc>
  </programme>
  <programme start="{data_str}183000 +0300" stop="{data_str}193000 +0300" channel="LRT.lt">
    <title lang="lt">Dienos tema</title>
    <desc lang="lt">Aktualijų ir interviu laida su svarbiausiais dienos asmenimis.</desc>
  </programme>

  <programme start="{data_str}070000 +0300" stop="{data_str}090000 +0300" channel="TV3.lt">
    <title lang="lt">Nauja diena</title>
    <desc lang="lt">Rytinė informacinė laida.</desc>
  </programme>
  <programme start="{data_str}183000 +0300" stop="{data_str}193000 +0300" channel="TV3.lt">
    <title lang="lt">TV3 Žinios</title>
    <desc lang="lt">Karščiausi dienos įvykiai iš Lietuvos ir užsienio.</desc>
  </programme>

  <programme start="{data_str}183000 +0300" stop="{data_str}193000 +0300" channel="LNK.lt">
    <title lang="lt">Žinios</title>
    <desc lang="lt">Išsamiausia dienos naujienų apžvalga.</desc>
  </programme>
  <programme start="{data_str}193000 +0300" stop="{data_str}203000 +0300" channel="LNK.lt">
    <title lang="lt">KK2</title>
    <desc lang="lt">Aktualijos, satyra ir tyrimai linksmai.</desc>
  </programme>

  <programme start="{data_str}190000 +0300" stop="{data_str}210000 +0300" channel="BTV.lt">
    <title lang="lt">Vakaro vaidybinis filmas</title>
    <desc lang="lt">Pramoginis kinas jūsų namuose.</desc>
  </programme>
</tv>"""
    
    with open("programa.xml", "w", encoding="utf-8") as f:
        f.write(xml_turinys)

if __name__ == "__main__":
    generuoti_xml()
