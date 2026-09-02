from Source.ImportJsonMeteoFrance import ImportJsonMeteoFrance


class ImportJsonTexteMeteoFrance(ImportJsonMeteoFrance):
    def __init__(self):
        pass

    def construct_url(self, year: int, month: int, day: int):
        return super().construct_url("CDP_TEXTES_VIGILANCE",
                                     year, month, day)

    def construct_path_json(self, year: int, name: str,):
        return ("data/" + str(year) + "/texte/" + name + ".json")
