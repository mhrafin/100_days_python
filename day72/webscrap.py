from pprint import pp

import requests
from bs4 import BeautifulSoup

with open(file="day72/webhtml.txt", mode="r") as file:
    soup = BeautifulSoup(file, "html.parser")


# pp(soup)

table_of_majors = soup.find("table", class_="data-table")
# print(table_of_majors)

majors = table_of_majors.find_all("tr")
# print(majors[1])

# one = majors[1].find_all("span", class_="data-table__value")
# pp(one[1].text)

with open(file="day72/data.csv", mode="w") as file:
    ths = table_of_majors.find("thead").find_all("th")
    for th in ths:
        file.write(f"{th.text},")
    file.write("\n")

    for major in majors[1:]:
        to_be_added = ""
        list_of_info = major.find_all("span", class_="data-table__value")
        for info in list_of_info:
            to_be_added += info.text
            to_be_added += ","
        file.write(f"{to_be_added}\n")
