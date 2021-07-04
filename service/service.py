import requests
from bs4 import BeautifulSoup

import random

from repository.repository import Repository

from helpers.helper import Helper


class Service:
    def __init__(self):
        self.repository = Repository()
        self.helper = Helper()

        self.platforms = [{
            "name": "codechef",
            "details": {
                "basics": {
                    "url": "https://www.codechef.com/problems/school/",
                    "successfulSubmissionPercentage": 60
                },
                "alpha": {
                    "url": "https://www.codechef.com/problems/easy/",
                    "successfulSubmissionPercentage": 40
                },
                "beta": {
                    "url": "https://www.codechef.com/problems/medium/",
                    "successfulSubmissionPercentage": -1
                }
            }
        }]

    def getPlatforms(self):
        return self.platforms

    def fetchFromCodechef(self, url, qtype):

        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, "html.parser")
            questions = soup.findAll("tr", {"class": "problemrow"})
            retryCount = 0
            while retryCount < 15:
                question = random.choice(questions)
                title = question.find("b").text
                if (self.repository.doesQuestionExistsInDb(title, qtype)):
                    retryCount += 1
                    continue
                url = "https://codechef.com" + \
                    str(question.find("a")).split()[1].split("\"")[1]
                return title, url
        except:

            raise Exception("Couldn't fetch")

    def injectToDB(self, qtype, url, title):

        date = self.helper.getNextDate(self.repository.getDB(), qtype)
        self.repository.injectNewQuestion(url, title, date, qtype)