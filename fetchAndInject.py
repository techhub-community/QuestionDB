import requests
from bs4 import BeautifulSoup
from datetime import datetime
from datetime import timedelta
import json
import random
with open("data.json", "r") as f:
    data = json.load(f)


platforms = [{
    "name": "codechef",
    "urls": {
        "basics": "https://www.codechef.com/problems/school/",
        "alpha": "https://www.codechef.com/problems/easy/",
        "beta":    "https://www.codechef.com/problems/medium/"
    }
}]


def injectToDb(url, title, date, qtype):

    try:
        dataToAppend = {
            "questionDate": date,
            "questionTitle": title,
            "questionUrl": url
        }
        data[qtype].append(dataToAppend)
        with open('data.json', 'w') as outfile:
            json.dump(data, outfile, indent=2)
    except:
        print("Couldn't write to DB")


def doesQuestionExistsInDb(title, qtype):
    for val in data[qtype]:
        if val["questionTitle"] == title:
            return True
    return False


def getNextDate(qtype):
    dates = []
    for val in data[qtype]:
        dates.append(str(val["questionDate"]))
    maxDate = max(dates, key=lambda d: datetime.strptime(d, '%d/%m/%Y'))
    nextDate = datetime.strptime(maxDate, "%d/%m/%Y") + timedelta(days=1)
    date = nextDate.strftime("%d/%m/%Y")
    return date


def fetchFromCodechef(url, qtype):

    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        questions = soup.findAll("tr", {
            "class": "problemrow"
        })
        foundUnMatchedQuestion = False
        while not foundUnMatchedQuestion:
            question = random.choice(questions)
            title = question.find("b").text
            if(doesQuestionExistsInDb(title, qtype)):
                continue
            url = "https://codechef.com" + \
                str(question.find("a")).split()[1].split("\"")[1]
            date = getNextDate(qtype)
            injectToDb(url, title, date, qtype)
            foundUnMatchedQuestion = True

    except:

        print("Couldn't fetch")


keys = ['basics', "alpha", "beta"]

for key in keys:
    fetchFromCodechef(platforms[0]["urls"][key], key)






