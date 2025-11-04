def teilnehmer(**daten):
    vorname = daten.get("vorname")
    nachname = daten.get("nachname")
    alter = daten.get("alter", 18)
    geschlecht = daten.get("geschlecht", "N/A")
    print(f"{vorname} {nachname};{alter};{geschlecht}")

teilnehmer (geschlecht = "männlich")