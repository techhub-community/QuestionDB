from datetime import datetime
from datetime import timedelta


class Helper:
    def getNextDate(self, data, qtype):
        dates = []
        for val in data[qtype]:
            dates.append(str(val["questionDate"]))
        maxDate = max(dates, key=lambda d: datetime.strptime(d, '%d/%m/%Y'))
        nextDate = datetime.strptime(maxDate, "%d/%m/%Y") + timedelta(days=1)
        date = nextDate.strftime("%d/%m/%Y")
        return date