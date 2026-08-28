from Source.ImportJsonMeteoFrance import ImportJsonMeteoFrance
from Source.Date import Date


class ImportJsonCarteMeteoFrance(ImportJsonMeteoFrance):
    def construct_URL(year: int, month: int, day: int):
        return ImportJsonMeteoFrance.construct_url("CDP_CARTE_EXTERNE",
                                                   year, month, day)

    @staticmethod
    def construct_path_json(year: int, name: str,):
        return ("data/" + str(year) + "/carte/" + name + ".json")

    @staticmethod
    def dowload_month(year, month):
        i = 1
        while i <= 31:
            name = Date.from_int_to_string_underscore(year, month, i)
            path = ImportJsonMeteoFrance.construct_path_json(year, name)
            try:
                url = ImportJsonCarteMeteoFrance.construct_url(year, month, i)
                ImportJsonCarteMeteoFrance.download_day(url, path)
            except FileExistsError:
                i = 32
                print("il n'y a plus de données pour ce mois")
            i += 1
