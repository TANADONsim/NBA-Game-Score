import urllib3
import csv
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from bs4 import BeautifulSoup

def scrape(date):
    http = urllib3.PoolManager()
    url = "https://www.basketball-reference.com/playoffs/NBA_"+str(date)+".html#all_team-stats-base"
    response = http.request('GET', url)
    soup = BeautifulSoup(response.data, 'html.parser')
    tags = soup.find_all("div", attrs={"class": "overthrow table_container", "id": "div_team-stats-per_game"})
    tags = tags[0].tbody.contents
    team_stats = []
    for i in range(1, len(tags), 2):
        contents = tags[i].contents
        stats = []
        stats.append(contents[1].text)
        for j in range(2, len(contents)):
            stats.append(contents[j].text)
        team_stats.append(stats)

    with open(str(date)+".csv", "w") as f:
        writer = csv.writer(f)
        writer.writerows(team_stats)

for date in range(1950, 2018):
    print(date)
    try:
        scrape(date)
    except:
        print("broke at", date)