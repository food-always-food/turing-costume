import requests
from time import sleep
from Adafruit_Thermal import *

printer = Adafruit_Thermal("/dev/serial0", 19200, timeout=5)

count = 0

while count < 5:
    url = "http://enigma.thompsongroup.io/api/get-message"
    response = requests.get(url=url)
    data = response.json()
    if data != False:
        printer.inverseOn()
        printer.justify('C')
        printer.println("   Message Intercepted   ")
        printer.inverseOff()
        printer.feed(1)
        printer.justify('L')
        printer.println(data['plaintext'])
        printer.feed(1)
        printer.inverseOn()
        printer.justify('C')
        printer.println("   End Intercept   ")
        printer.inverseOff()
        printer.feed(2)
    sleep(10)
    print("sleeping")
    print(count)
    count += 1