from datetime import datetime, timedelta

def generuoti_epg():
    # Gauname šiandienos datą formatu YYYYMMDD
    today = datetime.now().strftime("%Y%m%d")
    
    # Šabloninės dienos laidos, kurios keičiasi pagal realų laiką
    laidos_sarasas = [
        ("06:00", "06:30", "Ryto programa", "Pradėkite dieną žvaliai."),
        ("06:30", "09:00", "Informacinė ryto laida", "Karščiausios naujienos, apžvalgos ir interviu."),
        ("09:00", "12:00", "Dienos vaidybinis filmas", "Įtraukianti istorija visai šeimai."),
        ("12:00", "13:00", "Dienos žinios ir komentarai", "Svarbiausi įvykiai Lietuvoje."),
        ("13:00", "15:00", "Dokumentinis serialas", "Gamta, mokslas ir atradimai."),
        ("15:00", "17:00", "Popietės pokalbių laida", "Diskusijos aktualiomis temomis."),
        ("17:00", "18:30", "Populiarus serialas", "Naujausia užsienio produkcijos serija."),
        ("18:30", "19:30", "Vakaro Žinios", "Išsamus dienos įvykių reportažas."),
        ("19:30", "21:00", "Aktualijų ir pramogų šou", "Gera nuotaika bei analizė."),
        ("21:00", "23:00", "Vakaro kino filmas", "Geriausių reitingų vaidybinis kinas."),
        ("23:00", "23:59", "Dienos apžvalga ir naktinis kinas", "Svarbiausių akcentų santrauka.")
    ]

    kanalai = [
        ("LRT", "LRT Televizija"),
        ("TV3", "TV3"),
        ("LNK", "LNK"),
        ("BTV", "BTV"),
        ("TV6", "TV6")
    ]

    xml_lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<tv generator-info-name="Išmanusis Vietinis EPG">'
    ]

    # Sugeneruojame kanalų sąrašą
    for ch_id, ch_name in kanalai:
        xml_lines.append(f'  <channel id="{ch_id}"><display-name>{ch_name}</display-name></channel>')

    xml_lines.append("")

    # Sugeneruojame programas kiekvienam kanalui
    for ch_id, _ in kanalai:
        for nuo, iki, pavadinimas, aprasymas in laidos_sarasas:
            # Pašaliname dvitaškius iš laiko formato
            start_laikas = f"{today}{nuo.replace(':', '')}00 +0300"
            stop_laikas = f"{today}{iki.replace(':', '')}00 +0300"
            
            # Pridedame unikalumo skirtingiems kanalams, kad programa nebūtų visiškai identiška
            pataisytas_pavadinimas = f"{pavadinimas}"
            if ch_id != "LRT" and "Žinios" in pavadinimas:
                pataisytas_pavadinimas = f"{ch_id} Žinios"
            elif ch_id == "TV6" and "filmas" in pavadinimas:
                pataisytas_pavadinimas = "Veiksmo filmas"

            xml_lines.append(f'  <programme start="{start_laikas}" stop="{stop_laikas}" channel="{ch_id}">')
            xml_lines.append(f'    <title>{pataisytas_pavadinimas}</title>')
            xml_lines.append(f'    <desc>{aprasymas}</desc>')
            xml_lines.append('  </programme>')

    xml_lines.append('</tv>')

    with open("programa.xml", "w", encoding="utf-8") as f:
        f.write("\n".join(xml_lines))
    print("programa.xml sėkmingai sugeneruotas iš naujo!")

if __name__ == "__main__":
    generuoti_epg()
