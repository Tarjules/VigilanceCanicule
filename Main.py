from Source.ExtractDataTexte import ExtractDataTexte as Datatexte
from Source.ImportJsonTexteMeteoFrance import (
    ImportJsonTexteMeteoFrance as ImportJsonTexte)
from Source.ImportJsonCarteMeteoFrance import ImportJsonCarteMeteoFrance as ImportJsonCarte


dict = Datatexte.load_json("data/2026/texte/2026_06_25.json")
print(Datatexte.extract_date(dict))
dict_dep = Datatexte.extract_dict_departement(dict, 31)
print(Datatexte.extract_heatwave_level(dict_dep))
print(Datatexte.data_year_and_departement(2025, 31))

