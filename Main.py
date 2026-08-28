from Source.ExtractDataTexte import ExtractDataTexte
from Source.ImportJsonTexteMeteoFrance import (
    ImportJsonTexteMeteoFrance as ImportJsonTexte)
from Source.ImportJsonCarteMeteoFrance import ImportJsonCarteMeteoFrance as ImportJsonCarte

texte_importer = ImportJsonTexte()
texte_importer.dowload_month(2026, 7)
