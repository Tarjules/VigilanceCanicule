import os
from Source.ImportJsonCarteMeteoFrance import (
    ImportJsonCarteMeteoFrance as ImportJsonCarte)
from Source.Traitement import Traitement
from Source.Graphique import Graphique


def download_data(): ### A TESTER ce qu'il fait si les données sont déjà téléchargés + Si il télécharge correctement
    importer = ImportJsonCarte()
    try:
        os.makedirs("data", exist_ok=True)
    except OSError:
        pass
    for year in range(2022, 2027):
        try:
            os.makedirs("data/"+str(year)+"/carte", exist_ok=True)
        except OSError:
            pass
        importer.download_year(year)


def hist_nbjours_cannicule_département(dept):
    trait = Traitement()
    graph = Graphique()
    graph.histogramme_dept_years(trait.dept_heatwaves_per_year(dept))
