import requests
import json
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from Source.Date import Date

BASE = "https://files.data.gouv.fr/"
# data base = https://files.data.gouv.fr/meteofrance/data/vigilance/metropole/
# phenomenon_id	"6" : canicule
# phenomenon_max_color_id	3 = orange (1 = vert, 2 = jaune, 3 = rouge)


def construct_url(filename: str, year: int, month: int, day: int):
    # A partir des entiers fournis, il faut reconstituer une date
    date = Date.from_int_to_string_slash(year, month, day)
    url_page_html = BASE + "meteofrance/data/vigilance/metropole/"
    url_page_html += date + "/"

    # Au vue de la structure des archives de Météo France (1er numéro
    # de dossier variant pour chaque date),
    # Il faut passer par la structure HTML de deux pages pour obtenir
    # le lien vers le json intéréssant

    html_content = requests.get(url_page_html).text
    soup = BeautifulSoup(html_content, 'html.parser')
    title = soup.find("title")
    if "No Files Available for Listing" == title.text:
        raise FileExistsError
    soup = BeautifulSoup(html_content, 'html.parser')
    links = soup.find_all('a')
    link = urljoin(BASE, links[1].get('href'))

    html_content = requests.get(link).text
    soup = BeautifulSoup(html_content, 'html.parser')
    links = soup.find_all('a')
    try:
        i = 0
        presence_fichier = False
        while i < len(links):
            href = links[i].get('href')
            if filename in href:
                link_json = href
                i = len(links)
                presence_fichier = True
            i = i+1
        if not presence_fichier:
            raise FileNotFoundError
    except FileNotFoundError:
        print("Il n'y a pas de fichier " +
              filename+".json pour la date du " + date)
        return None
    else:
        link = urljoin(BASE, link_json)
        return link


def construct_path_json(loc: str, name: str):
    '''
    Args:
        loc(str): Dossier
        name(str): Nom du fichier

    Returns:
        "loc/name.json"'''
    return loc + "/" + name + ".json"


def test_file_ever_exist(path: str):
    try:
        with open(path, "r"):
            return True
    except FileNotFoundError:
        return False
    except IOError:
        return False


def download_day(url, path: str):
    """Sauvegarde le fichier json pointé par l'URL dans le
    dossier 'loc' sous le nom 'name'

    Args:
        URL(str): URL poitant vers le json
        path(str): chemin relatif où enregistrer le json
        """
    try:
        if url is None:
            raise FileNotFoundError
    except FileNotFoundError:
        pass
    else:
        e = test_file_ever_exist(path)
        if not e:
            response = requests.get(url)
            response_json = response.json()
            with open(path, 'w', encoding='utf-8') as fichier:
                json.dump(response_json, fichier,
                          indent=4, ensure_ascii=False)
        else:
            pass


class ImportJsonTexteVigilanceMeteoFrance:
    @staticmethod
    def construct_url(year: int, month: int, day: int):
        return construct_url("CDP_TEXTES_VIGILANCE", year, month, day)

    @staticmethod
    def download_month(year: int, month: int):
        '''Permet de télécharger tout un mois de donnée de
        vigilance jour par jour si elles existent. Les fichiers sont
        enregistrés dans un dossier "year" sous le format Année_mois_jour.json
        Attention :  programme lent

        Args:
            year(int): Année concernée
            month(int): mois concerné
        '''
        i = 1
        while i <= 31:
            name = Date.from_int_to_string_underscore(year, month, i)
            path = construct_path_json("data/" + str(year) + "/texte", name)
            try:
                url = ImportJsonTexteVigilanceMeteoFrance.construct_url(year,
                                                                        month,
                                                                        i)
                download_day(url, path)
            except FileExistsError:
                i = 32
                print("il n'y a plus de données pour ce mois")
            i += 1

    @staticmethod
    def download_year(year: int):
        '''Permet de télécharger toute une année de donnée de vigilance jour
        par jour si elles existent. Les fichiers sont enregistrés dans un
        dossier "year" sous le format Année_mois_jour.json
        Peut-être utilisé même si l'année est incomplète.
        Attention :  programme lent

        Args:
            year(int): Année concernée
        '''
        try:
            if year < 2022 or year > 2026:
                raise IndexError
        except IndexError:
            print(f"l'année {year} est indisponible")
            pass
        else:
            m = 1
            while m <= 12:
                ImportJsonTexteVigilanceMeteoFrance.download_month(year, m)
                m += 1


class ImportJsonCDPCarteExterneMeteoFrance:
    def construct_URL(year: int, month: int, day: int):
        return construct_url("CDP_CARTE_EXTERNE", year, month, day)

    @staticmethod
    def download_year(year: int):
        '''Permet de télécharger toute une année de donnée de vigilance jour
        par jour si elles existent. Les fichiers sont enregistrés dans un
        dossier "year" sous le format Année_mois_jour.json
        Peut-être utilisé même si l'année est incomplète.
        Attention :  programme lent

        Args:
            year(int): Année concernée
        '''
        try:
            if year < 2022 or year > 2026:
                raise IndexError
        except IndexError:
            print(f"l'année {year} est indisponible")
            pass
        else:
            m = 1
            while m <= 12:
                ImportJsonCDPCarteExterneMeteoFrance.download_month(year, m)
                m += 1

    @staticmethod
    def download_month(year: int, month: int):
        '''Permet de télécharger tout un mois de donnée de
        vigilance jour par jour si elles existent. Les fichiers sont
        enregistrés dans un dossier "year" sous le format Année_mois_jour.json
        Attention :  programme lent

        Args:
            year(int): Année concernée
            month(int): mois concerné
        '''
        i = 1
        while i <= 31:
            name = Date.from_int_to_string_underscore(year, month, i)
            path = construct_path_json("data/" + str(year) + "/carte", name)
            try:
                url = ImportJsonCDPCarteExterneMeteoFrance.construct_url(year,
                                                                         month,
                                                                         i)
                download_day(url, path)
            except FileExistsError:
                i = 32
                print("il n'y a plus de données pour ce mois")
            i += 1
