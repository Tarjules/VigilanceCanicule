import json


class ExtractData:
    @staticmethod
    def load_json(path: str):
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
        try:
            return dict["product"]["update_time"][:10]
        except TypeError:
            return None

    @staticmethod
    def extract_heatwave_level(dict: dict, dept: str): #2A et 2B !
        if type(dept) is int:
            dept = str(dept)
        try:
            for domain in dict["product"]["text_bloc_items"]:
                if domain["domain_id"] == dept:
                    info_dept = domain
                    if len(domain["bloc_items"]) <= 1:
                        raise ValueError
                    info_dept = domain["bloc_items"][1]["text_items"][0]
        except (TypeError, ValueError):
            return [dept, None, None]
        else:
            vigilance = info_dept["hazard_name"]
            level = info_dept["term_items"][0]["risk_name"]
            return [dept, vigilance, level]
