class OverFlow(Exception):
    def __init__(self, args):
        self.args = args
        self.message = " is overflow."

    def __str__(self):
        return str(str(self.args) + self.message)


class UnderFlow(Exception):
    def __init__(self, args):
        self.args = args
        self.message = " is underflow."

    def __str__(self):
        return str(str(self.args) + self.message)


class InvalidArgs(Exception):
    def __init__(self, args):
        self.args = args
        self.message = " is not Invalid Arguments"

    def __str__(self):
        return str(self.args + self.message)


class InvalidCategory(Exception):
    def __init__(self, category):
        self.category = category
        self.message = " is not valid."

    def __str__(self):
        return str(self.category + self.message)


class InvalidYear(Exception):
    def __init__(self, startyear, endyear):
        self.startyear = startyear
        self.endyear = endyear
        self.message = str(startyear) + "(startyear) is bigger than " + str(self.endyear) +"(endyear)"

    def __str__(self):
        return str(self.message)


class InvalidMonth(Exception):
    def __init__(self, month):
        self.month = month
        self.message = str(month) + " is an invalid month"

    def __str__(self):
        return str(self.message)

class InvalidDay(Exception):
    def __init__(self, day):
        self.day = day
        self.message = str(day) + " is an invalid month"

    def __str__(self):
        return str(self.message)


class OverbalanceMonth(Exception):
    def __init__(self, start_month, end_month):
        self.start_month = start_month
        self.end_month = end_month
        self.message = "start_month(" + str(self.start_month) + ") is an overbalance with end_month" + "(" + str(self.end_month) + ")"

    def __str__(self):
        return str(self.message)

class OverbalanceDay(Exception):
    def __init__(self, start_day, end_day):
        self.start_day = start_day
        self.end_day = end_day
        self.message = "start_day(" + str(self.start_day) + ") is an overbalance with end_month" + "(" + str(self.end_day) + ")"

    def __str__(self):
        return str(self.message)

class ResponseTimeout(Exception):
    def __init__(self):
        self.message = "Couldn't get the data"

    def __str__(self):
        return str(self.message)
