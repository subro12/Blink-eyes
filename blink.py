import requests
from bs4 import BeautifulSoup
import time
from plyer import notification


while True:
    d = "Close your Eyes blink your eyes"
    notification.notify(
        title = 'Blink your eyes',
        message = str(d),
        app_name = "Subbu's APP",
        # timeout = 15,
        
    )
    time.sleep(1200)

