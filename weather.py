import requests
import geocoder
import datetime

API_KEY = 'f064e15e2058a64eb4c89af4dc432ffd'
HOST = 'https://api.openweathermap.org/data/2.5'
DAYS = [
    {'num': 0, 'title': 'Понедельник', 'active': False, 'color': '#FFE739', 'order': [0, 1, 2, 3, 4, 5, 6], 'temp': 0,
     'type': '-'},
    {'num': 1, 'title': 'Вторник', 'active': False, 'color': '#FFE739', 'order': [1, 2, 3, 4, 5, 6, 0], 'temp': 0,
     'type': '-'},
    {'num': 2, 'title': 'Среда', 'active': False, 'color': '#FFE739', 'order': [2, 3, 4, 5, 6, 0, 1], 'temp': 0,
     'type': '-'},
    {'num': 3, 'title': 'Четверг', 'active': False, 'color': '#FFE739', 'order': [3, 4, 5, 6, 0, 1, 2], 'temp': 0,
     'type': '-'},
    {'num': 4, 'title': 'Пятница', 'active': False, 'color': '#FFE739', 'order': [4, 5, 6, 0, 1, 2, 3], 'temp': 0,
     'type': '-'},
    {'num': 5, 'title': 'Суббота', 'active': False, 'color': '#36FF72', 'order': [5, 6, 0, 1, 2, 3, 4], 'temp': 0,
     'type': '-'},
    {'num': 6, 'title': 'Воскресенье', 'active': False, 'color': '#36FF72', 'order': [6, 0, 1, 2, 3, 4, 5], 'temp': 0,
     'type': '-'},
]


def today():
    geo = geocoder.ip('me')

    city = geo.city
    lat = geo.lat
    lon = geo.lng

    req = requests.get(f'{HOST}/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric&lang=ru').json()
    res = {
        'city': req['name'],
        'dis': req['weather'][0]['description'],
        'temp': int(round(req['main']['temp'])),
        'fells': str(round(req['main']['feels_like'])) + '°C',
        'pressure': str(round(req['main']['pressure'] / 1000 * 750, 2)),
        'wind': req['wind']['speed'],
    }
    return res


def week():
    today = datetime.datetime.today()
    DAYS[today.weekday()]['active'] = True

    for i in DAYS:
        if DAYS[today.weekday()]['active']:
            order = DAYS[today.weekday()]['order']

    geo = geocoder.ip('me')
    city = geo.city
    lat = geo.lat
    lon = geo.lng

    req = requests.get(f'{HOST}/onecall?/exclude=daily&lat={lat}&lon={lon}&appid={API_KEY}&units=metric&lang=ru').json()
    res = [DAYS[i] for i in order]

    for i in req['daily']:
        index = req['daily'].index(i)
        if index == 7:
            break
        res['index']['temp'] = i['temp']['day']
        res['index']['temp'] = i['weather'][0]['description']

    return res


today()
