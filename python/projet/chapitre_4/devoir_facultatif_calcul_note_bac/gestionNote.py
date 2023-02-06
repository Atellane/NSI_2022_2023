def obtenirNoteBac(histoireGeoPremiere: float, histoireGeoTerminale: float, lvaPremiere: float, lvaTerminale: float, lvbPremiere: float, lvbTerminale: float, eScientifiquePremiere: float, eScientifiqueTerminale: float, eSpePremiere: float, eps: float, emcPremiere: float, emcTerminale: float, eSpeTerminalUn: float, eSpeTerminalDeux: float, oralFr: float, ecritFr: float, philo: float, grandOral: float) -> float:
    """Renvoie notre note au bac"""
    histoireGeoPremiere *= 3.0
    histoireGeoTerminale *= 3.0
    histoireGeo: float = histoireGeoPremiere + histoireGeoTerminale
    lvaPremiere *= 3.0
    lvaTerminale *= 3.0
    lva: float = lvaPremiere + lvaTerminale
    lvbPremiere *= 3.0
    lvbTerminale *= 3.0
    lvb: float = lvbPremiere + lvbTerminale
    eScientifiquePremiere *= 3.0
    eScientifiqueTerminale *= 3.0
    eScientifique: float = eScientifiquePremiere + eScientifiqueTerminale
    eSpePremiere *= 8
    eps *= 6
    emc: float = emcPremiere + emcTerminale
    eSpeTerminalUn *= 16
    eSpeTerminalDeux *= 16
    oralFr *= 5
    ecritFr *= 5
    philo *= 8
    grandOral *= 10
    totalNote: float = histoireGeo + lva + lvb + eScientifique + eSpePremiere + eps + emc + eSpeTerminalUn + eSpeTerminalDeux + oralFr + ecritFr + philo + grandOral
    resultat: float = totalNote/100.0
    return resultat

assert obtenirNoteBac(20, 16, 10, 11, 13, 17, 10, 10, 17, 20, 16, 10, 11, 13, 17, 10, 10, 17) == 13.72, "wtf ?"

def obtenirMentionBac(note: float) -> str:
    """Renvoie notre mention au bac"""
    if note < 10.0:
        resultat: str = "Éliminé !!"
    elif note < 12.0:
        resultat: str = "Passable !"
    elif note < 14.0:
        resultat: str = "Assez Bien."
    elif note < 16.0:
        resultat: str = "Bien !"
    else:
        resultat: str  = "Très Bien !!"

    return resultat

assert obtenirMentionBac(9.0) == "Éliminé !!", "ça fonctionne pas pour note < 10"
assert obtenirMentionBac(11.0) == "Passable !", "ça fonctionne pas pour note < 12"
assert obtenirMentionBac(13.0) == "Assez Bien.", "ça fonctionne pas pour note < 14"
assert obtenirMentionBac(15.0) == "Bien !", "ça fonctionne pas pour note < 16"
assert obtenirMentionBac(20.0) == "Très Bien !!", "ça fonctionne pas pour note >= 15"

try:
    histoireGeoPremiere: float = float(input("Entrez votre note d'histoire geographie en premiere :\n"))
    histoireGeoTerminale: float = float(input("Entrez votre note d'histoire geographie en terminale :\n"))
    lvaPremiere: float = float(input("Entrez votre note de langue vivante A en premiere :\n"))
    lvaTerminale: float = float(input("Entrez votre note de langue vivante A en terminale :\n"))
    lvbPremiere: float = float(input("Entrez votre note de langue vivante B en premiere :\n"))
    lvbTerminale: float = float(input("Entrez votre note de langue vivante B en terminale :\n"))
    eScientifiquePremiere: float = float(input("Entrez votre note d'enseignement scientifique en premiere :\n"))
    eScientifiqueTerminale: float = float(input("Entrez votre note d'enseignement scientifique en premiere :\n"))
    eSpePremiere: float = float(input("Entrez votre note de spe abandonnée en premiere :\n"))
    eps: float = float(input("Entrez votre note d'eps en terminale :\n"))
    emcPremiere: float = float(input("Entrez votre note d'emc en premiere :\n"))
    emcTerminale: float = float(input("Entrez votre note d'emc en terminale :\n"))
    eSpeTerminalUn: float = float(input("Entrez votre note de spe 1 en terminale :\n"))
    eSpeTerminalDeux: float = float(input("Entrez votre note de spe 2 en terminale :\n"))
    oralFr: float = float(input("Entrez votre note d'oral de français en premiere :\n"))
    ecritFr: float = float(input("Entrez votre note d'écrit de français en premiere :\n"))
    philo: float = float(input("Entrez votre note de philo en terminale :\n"))
    grandOral: float = float(input("Entrez votre note de grand oral en terminale :\n"))
    note: float = obtenirNoteBac(histoireGeoPremiere, histoireGeoTerminale, lvaPremiere, lvaTerminale, lvbPremiere, lvbTerminale, eScientifiquePremiere, eScientifiqueTerminale, eSpePremiere, eps, emcPremiere, emcTerminale, eSpeTerminalUn, eSpeTerminalDeux, oralFr, ecritFr, philo, grandOral)
    print(f"Votre note au bac est : {note}\nVotre mention au bac est donc : {obtenirMentionBac(note)}")
except ValueError:
    print("Les notes sont des chiffres, pas des lettres, recommence :)")
