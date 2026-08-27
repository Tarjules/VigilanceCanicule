from Source.ExtractDataTexte import ExtractDataTexte
from Source.ImportJson import ImportJsonTexteVigilanceMeteoFrance as ImportJson
from Source.ImportJson import construct_url

print(construct_url("CDP_TEXTES_VIGILANCE", 2022, 12, 1))

ImportJson.download_month(2023,1)
print(ExtractDataTexte.extract_heatwave_level(ExtractData.load_json("data/2023/2023_08_25.json"), 31))
print(ExtractData.data_year_and_departement(2026, 31))