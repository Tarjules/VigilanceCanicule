from Source.ExtractData import ExtractData
import os


class ExtractDataCarte(ExtractData):
    @staticmethod
    def extract_date(dict: dict):
        """Permet d'obtenir la date d'émission de la carte de vigilance

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
    def extract_dict_departement(dict: dict, dept):
        if type(dept) is int:
            dept = str(dept)
        L_dict_dept = dict["product"]["periods"][0]["timelaps"]["domain_ids"]
        for departement in L_dict_dept:
            if departement["domain_id"] == dept:
                return departement
        return None

    @staticmethod
    def extract_heatwave_level(dept: dict):
        for phenomenon in dept["phenomenon_items"]:
            if phenomenon["phenomenon_id"] == "6":
                return ["Canicule", phenomenon["phenomenon_max_color_id"]]
        return ["Hors période", None]

    @staticmethod
    def data_year_and_departement(year: int, dept):
        filenames = os.listdir("data/"+str(year)+"/carte")
        list.sort(filenames, key=lambda x: x[:10])
        year_dept = []
        for filename in filenames:
            donnees = ExtractDataCarte.load_json("data/"+str(year) +
                                                 "/carte/"+filename)
            day = []
            day.append(ExtractDataCarte.extract_date(donnees))
            dict_dep = ExtractDataCarte.extract_dict_departement(donnees, dept)
            day += (ExtractDataCarte.extract_heatwave_level(dict_dep))
            if day[1] == "Canicule":
                year_dept.append(day)
        return year_dept
