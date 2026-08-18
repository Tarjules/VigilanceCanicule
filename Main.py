
from Source.ExtractData import ExtractData as e

data = e.load_json("data/2026/2026_2_6.json")
print(e.extract_heatwave_level(data, "83"))

