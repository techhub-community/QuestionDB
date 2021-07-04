from service.service import Service


class Controller:
    def __init__(self):

        self.service = Service()

    def fetchAndInject(self):

        platforms = self.service.getPlatforms()
        for key in ["basics", "alpha", "beta"]:
            title, url = self.service.fetchFromCodechef(
                platforms[0]["details"][key]["url"], key)

            self.service.injectToDB(key, url, title)
