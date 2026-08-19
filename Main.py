from Source.Date import Date
from Source.ImportJson import ImportJsonTexteVigilanceMeteoFrance as Vigijson
from Source.ExtractData import ExtractData as e


Vigijson.download_month(2026, 8)

data = e.load_json("data/2026/2026_2_6.json")
print(e.extract_heatwave_level(data, "83"))

print(Date.valid(2026, 4, 30))
print(Date.from_int_to_string(2026, 4, 2))
