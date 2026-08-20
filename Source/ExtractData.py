import json
import os

class ExtractData:
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
                    if len(domain["bloc_items"]) <= 1:
                        raise ValueError
                    info_dept = domain["bloc_items"][1]["text_items"][0]
                    # soit DEP_QUALIFICATION_ZONAL, soit DEP_SUIVI, bref, code valide mais à revoir pour extraire le max d'infos 
        except (TypeError, ValueError):
            return [dept, None, None]
        else:
            vigilance = info_dept["hazard_name"]
            level = info_dept["term_items"][0]["risk_name"]
            return [dept, vigilance, level]

    def data_year_and_departement(year: int, dept):
        filenames = os.listdir("data/"+str(year))
        print(filenames)
        year_dept = []
        for filename in filenames:
            print(filename)
            donnees = ExtractData.load_json("data/"+str(year)+"/"+filename)
            day = []
            day.append(ExtractData.extract_date(donnees))
            day += (ExtractData.extract_heatwave_level(donnees, dept))
            year_dept.append(day)
        return year_dept
