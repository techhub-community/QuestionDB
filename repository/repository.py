import json

import os


class Repository:
    def __init__(self):

        dirname = os.path.dirname(__file__)

        self.dataFile = os.path.join(dirname, '../data.json')
        with open(self.dataFile, "r") as f:
            self.data = json.load(f)

    def getDB(self):
        return self.data

    def injectNewQuestion(self, url, title, date, qtype):
        try:
            dataToAppend = {
                "questionDate": date,
                "questionTitle": title,
                "questionUrl": url
            }
            self.data[qtype].append(dataToAppend)
            with open(self.dataFile, 'w') as outfile:
                json.dump(self.data, outfile, indent=2)
        except:
            raise Exception("Couldn't write to DB")

    def doesQuestionExistsInDb(self, title, qtype):

        for val in self.data[qtype]:

            if val["questionTitle"] == title:
                return True
        return False
