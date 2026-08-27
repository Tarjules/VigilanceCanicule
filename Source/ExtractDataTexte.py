import json
import os


class ExtractDataTexte:
    @staticmethod
    def load_json(path: str):
        """Permet de charger les données json stockées à 
        l'adresse relative path

        Args:
            path(string): chemin relatif du json à charger
        returns:
            donnees(dict): dictionnaire contenant les données du json"""
        try:
            with open(path, 'r', encoding='utf-8') as fichier:
                donnees = json.load(fichier)
        except FileNotFoundError:
            print("Il n'y a aucun fichier à l'adresse: " + path)
            return None
        else:
            return donnees

    @staticmethod
    def extract_date(dict: dict):
        """Permet d'obtenir la date d'émission du texte de vigilance

        Args:
            dict(dict) : Le dictionnaire contenant les textes de vigilance
        Returns:
            date(str): la date d'émission ou None si elle n'est pas trouvé
        """
        try:
            return dict["product"]["update_time"][:10]
        except TypeError:
            return None

    @staticmethod
    def extract_heatwave_level(dict: dict, dept): 
        """A partir du dictionnaire fournit, retourne la vigilance et son
        niveau pour le département demandé

        Args:
            dict(dict) : Le dictionnaire contenant les textes de vigilance
            dept(str ou int): Le département d'intéret
        Returns:
            ([str, str, str]): [departement, Vigilance, niveau] ou
            [departement, None, None]"""
        if type(dept) is int:
            dept = str(dept)
        try:
            for domain in dict["product"]["text_bloc_items"]:
                if domain["domain_id"] == dept:
                    info_dept = domain
            for bloc in info_dept["bloc_items"]:
                if bloc["id"] in ["DEP_SUIVI",
                                  "DEP_QUALIFICATION_ZONAL",
                                  "DEP_EVOLUTION_ZONAL"]:
                    bloc_text = bloc["text_items"][0]
                    return [dept, bloc_text["hazard_name"],
                            bloc_text["term_items"][0]["risk_name"]]
        except TypeError:
            print("pas de valeur pour cette journée")
            return [dept, None, None]
        else:
            return [dept, None, None]

    def data_year_and_departement(year: int, dept):
        filenames = os.listdir("data/"+str(year)+"/texte")
        list.sort(filenames, key=lambda x: x[:10])
        year_dept = []
        for filename in filenames:
            donnees = ExtractDataTexte.load_json("data/"+str(year) +
                                                 "/texte/"+filename)
            day = []
            day.append(ExtractDataTexte.extract_date(donnees))
            day += (ExtractDataTexte.extract_heatwave_level(donnees, dept))
            print(day)
            year_dept.append(day)
        return year_dept
