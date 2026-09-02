from Source.ImportJsonMeteoFrance import ImportJsonMeteoFrance


class ImportJsonCarteMeteoFrance(ImportJsonMeteoFrance):
    def __init__(self):
        pass
    
    def construct_url(self, year: int, month: int, day: int):
        return super().construct_url("CDP_CARTE_EXTERNE",
                                     year, month, day)

    def construct_path_json(self, year: int, name: str,):
        return ("data/" + str(year) + "/carte/" + name + ".json")