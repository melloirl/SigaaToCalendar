import requests
import os
from dotenv import load_dotenv

load_dotenv()

def getUserData():
    targetUrl = 'https://sigaa.unb.br/sigaa/logar.do?dispatch=logOn'
    payload = {
        'user.login': os.getenv('LOGIN'),
        'user.senha': os.getenv('PASSWORD')
    }

    with requests.Session() as s:
        p = s.post(targetUrl, data=payload)

        print(p.status_code)

        r = s.get('https://sigaa.unb.br/sigaa/portais/discente/discente.jsf')
        return r
