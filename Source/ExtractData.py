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
        pass

    @staticmethod
    def extract_heatwave_level(dict: dict, dept):
        pass

    @staticmethod
    def data_year_and_departement(year: int, dept):
        pass
