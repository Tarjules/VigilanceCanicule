from Source.ImportJsonCarteMeteoFrance import (
    ImportJsonCarteMeteoFrance as ImportJsonCarte)
from Source.ExtractDataCarte import ExtractDataCarte
from Source.Traitement import Traitement

l_2025_31 = ExtractDataCarte.data_year_and_departement(2023, 31)
print(l_2025_31)
trait = Traitement()
print(trait.nb_day_heatwave(l_2025_31))
print(trait.dept_heatwaves_per_year(31))
