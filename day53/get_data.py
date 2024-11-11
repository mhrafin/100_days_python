from pprint import pp

import requests
from bs4 import BeautifulSoup


# https://forms.gle/57D6wCawfBcxdZyVA
class DataFromZillow:
    def __init__(self) -> None:
        self.addresses = []
        self.prices = []
        self.links_to = []

        response = requests.get("https://appbrewery.github.io/Zillow-Clone/")

        self.soup = BeautifulSoup(response.text, "html.parser")
        self.all_listings = self.soup.findAll(
            "li", class_="ListItem-c11n-8-84-3-StyledListCardWrapper"
        )

        self.get_addresses()
        self.get_prices()
        self.get_links()

    def get_addresses(self):
        # ul_listings = self.soup.find(class_="List-c11n-8-84-3-photo-cards")

        for listing in self.all_listings:
            self.addresses.append(listing.find("address").text.strip())

        pp(len(self.addresses))

    def get_prices(self):
        for listing in self.all_listings:
            self.prices.append(
                listing.find("span").text[1:6].replace("+", "").replace(",", "")
            )
        pp(len(self.prices))

    def get_links(self):
        for listing in self.all_listings:
            self.links_to.append(listing.find("a").get("href"))

        pp(len(self.links_to))


