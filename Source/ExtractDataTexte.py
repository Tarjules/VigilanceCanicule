import os
from Source.ExtractData import ExtractData


class ExtractDataTexte(ExtractData):

    @staticmethod
    def extract_date(dict: dict):
        try:
            return dict["product"]["update_time"][:10]
        except TypeError:
            return None

    @staticmethod
    def extract_dict_departement(dict: dict, dept):
        if type(dept) is int:
            dept = str(dept)
        for departement in dict["product"]["text_bloc_items"]:
            if departement["domain_id"] == dept:
                return departement
        return None

    @staticmethod
    def extract_heatwave_level(dept: dict): 
        try:
            for bloc in dept["bloc_items"]:
                if bloc["id"] in ["DEP_SUIVI",
                                  "DEP_QUALIFICATION_ZONAL",
                                  "DEP_EVOLUTION_ZONAL"]:
                    bloc_text = bloc["text_items"][0]
                    return [bloc_text["hazard_name"],
                            bloc_text["term_items"][0]["risk_name"]]
        except TypeError:
            print("pas de valeur pour cette journée")
            return [None, None]
        else:
            return [None, None]

    def data_year_and_departement(year: int, dept):
        filenames = os.listdir("data/"+str(year)+"/texte")
        list.sort(filenames, key=lambda x: x[:10])
        year_dept = []
        for filename in filenames:
            donnees = ExtractDataTexte.load_json("data/"+str(year) +
                                                 "/texte/"+filename)
            day = []
            day.append(ExtractDataTexte.extract_date(donnees))
            dict_dep = ExtractDataTexte.extract_dict_departement(donnees, dept)
            day += (ExtractDataTexte.extract_heatwave_level(dict_dep))
            year_dept.append(day)
        return year_dept
