from Source.ImportJsonMeteoFrance import ImportJsonMeteoFrance
from Source.Date import Date


class ImportJsonTexteMeteoFrance(ImportJsonMeteoFrance):
    def __init__(self):
        pass

    def construct_url(self, year: int, month: int, day: int):
        return super().construct_url("CDP_TEXTES_VIGILANCE",
                                     year, month, day)

    def construct_path_json(self, year: int, name: str,):
        return ("data/" + str(year) + "/texte/" + name + ".json")

    def dowload_month(self, year, month):
        i = 1
        while i <= 31:
            name = Date.from_int_to_string_underscore(year, month, i)
            path = self.construct_path_json(year, name)
            try:
                url = self.construct_url(year, month, i)
                self.download_day(url, path)
            except FileExistsError:
                i = 32
                print("il n'y a plus de données pour ce mois")
            i += 1
