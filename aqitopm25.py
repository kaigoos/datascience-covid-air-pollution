import datetime

"""
All credit for InvLinear and ConcPM25 go to airnow.gov and their aqi-conc.js file
"""
def InvLinear(AQIhigh, AQIlow, Conchigh, Conclow, a):
    return ((a - AQIlow) / (AQIhigh - AQIlow)) * (Conchigh - Conclow) + Conclow


def ConcPM25(a):
    ConcCalc = 0
    if 0 <= a <= 50:
        ConcCalc = InvLinear(50, 0, 12, 0, a)
    elif 50 < a <= 100:
        ConcCalc = InvLinear(100, 51, 35.4, 12.1, a)
    elif 100 < a <= 150:
        ConcCalc = InvLinear(150, 101, 55.4, 35.5, a)
    elif 150 < a <= 200:
        ConcCalc = InvLinear(200, 151, 150.4, 55.5, a)
    elif 200 < a <= 300:
        ConcCalc = InvLinear(300, 201, 250.4, 150.5, a)
    elif 300 < a <= 400:
        ConcCalc = InvLinear(400, 301, 350.4, 250.5, a)
    elif 400 < a <= 500:
        ConcCalc = InvLinear(500, 401, 500.4, 350.5, a)
    else:
        ConcCalc = "Error"

    return ConcCalc

def shutDownDate(city):
    startShutDown = {
        'Portland': datetime.date(2020, 3, 23),
        'NY': datetime.date(2020, 3, 20),
        'LA': datetime.date(2020, 3, 19),
        'Rome': datetime.date(2020, 3, 10),
        'Wuhan': datetime.date(2020, 1, 23),
        'Beijing': datetime.date(2020, 1, 26),
        'Madrid': datetime.date(2020, 3, 14),
        'New_Delhi': datetime.date(2020, 3, 25)
    }

    return startShutDown[city]