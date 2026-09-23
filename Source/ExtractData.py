import json
from abc import ABC


class ExtractData(ABC):
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
        """Permet d'obtenir la date d'émission du json de vigilance

        Args:
            dict(dict) : Le dictionnaire contenant les textes de vigilance
        Returns:
            date(str): la date d'émission ou None si elle n'est pas trouvé
        """
        pass

    @staticmethod
    def extract_dict_departement(dict: dict, dept):
        """Depuis le dictionnaire général (carte ou texte),
        permet d'en extraire le sous dictionnaire relatif au
        département recherché.

        Args:
            dict(dict) : dictionnaire général
        Returns:
            dept(dict) : dictionnaire du département voulu
        """
        pass

    @staticmethod
    def extract_heatwave_level(dept: dict):
        """Depuis un dictionnaire de département spécifique,
        renvoie une liste [type de vigilance, niveau d'alerte]
        Attention : selon le json (carte ou texte) utilisé,
        la fonction peut renvoyer un autre type de vigilance que
        celui canicule.

        Args:
            dept(dict) : dictionnaire département issue du json original
        Returns:
            heatwave_level (list) : [alerte(string), niveau(string or int)]"""
        pass

    @staticmethod
    def data_year_and_departement(year: int, dept):
        """Selon le département et l'année désirée,
        renvoie une liste contenant des informations
        de vigilance pour chaque jour de l'année et du
        département demandé.

        Args:
            year(int) : Année désirée
            dept(str or int): Département désirée
        Returns:
            (list) : [[date, dept, vigilance, niveau], ...]"""
        pass
