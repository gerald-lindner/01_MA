import requests
r = requests.get('http://icanhazip.com/')
from stem import Signal
from stem.control import Controller

with Controller.from_port(port = 9051) as controller:
    controller.authenticate(password = 'geri')
    controller.signal(Signal.NEWNYM)
    controller.close()

r = requests.get('http://icanhazip.com/')
print(r.content)