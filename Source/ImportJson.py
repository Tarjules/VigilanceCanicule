import requests
import json
from bs4 import BeautifulSoup
from urllib.parse import urljoin

BASE = "https://files.data.gouv.fr/"


class ImportJson:
    @staticmethod
    def construct_url(year: int, month: int, day: int):
        """ Permet de construire l'URL poitant vers le fichier json contenant
        les textes de vigilances à 6h à la date fournie.

        Args:
            year(int): année
            month(int): mois
            day(int): jour
        Returns:
            link(str) : lien vers le json contenant les informations
            recherchées
                """

        # A partir des entiers fournis, il faut reconstituer une date
        if month < 10:
            month = "0" + str(month)
        else:
            month = str(month)
        if day < 10:
            day = "0" + str(day)
        else:
            day = str(day)
        url_page_html = BASE + "meteofrance/data/vigilance/metropole/"
        url_page_html += str(year) + "/" + month + "/" + day + "/"

        # Au vue de la structure des archives de Météo France (1er numéro
        # de dossier variant pour chaque date),
        # Il faut passer par la structure HTML de deux pages pour obtenir
        # le lien vers le json intéréssant

        html_content = requests.get(url_page_html).text
        soup = BeautifulSoup(html_content, 'html.parser')
        links = soup.find_all('a')
        link = urljoin(BASE, links[1].get('href'))

        html_content = requests.get(link).text
        soup = BeautifulSoup(html_content, 'html.parser')
        links = soup.find_all('a')
        link = urljoin(BASE, links[3].get('href'))
        return link

    @staticmethod
    def import_file(URL, loc: str, name: str):
        """Sauvegarde le fichier json pointé par l'URL dans le
        dossier 'loc' sous le nom 'name'

        Args:
            URL(str): URL poitant vers le json
            loc(str): dossier ou enregistrer le fichier (peut être vide)
            name(str): nom sauvegardé du json (sous la forme xxxx.json)
            """
        response = requests.get(URL)
        response_json = response.json()
        place = loc + "/" + name
        with open(place, 'w', encoding='utf-8') as fichier:
            json.dump(response_json, fichier, indent=4, ensure_ascii=False)
