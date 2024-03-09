import os
import warnings
warnings.filterwarnings('ignore')
import requests

class KISClient:
    def __init__(self) -> None:
        self.cano: str = os.getenv('KIS_CANO')
        if not self.cano:
            raise ValueError('KIS_CANO is not set')
        self.appkey: str = os.getenv('KIS_APP_KEY')
        if not self.appkey:
            raise ValueError('KIS_APP_KEY is not set')
        self.appsecret: str = os.getenv('KIS_APP_SECRET')
        if not self.appsecret:
            raise ValueError('KIS_APP_SECRET is not set')
    
    def get_access_token(self) -> dict:
        url = 'https://openapi.koreainvestment.com:9443'
        payload = dict(
                    grant_type='client_credentials',
                    appkey=self.appkey,
                    appsecret=self.appsecret)
        response = requests.post(
                    url + '/oauth2/tokenP',
                    json=payload)
        response.raise_for_status()
        data = response.json()
        return dict(
            access_token=data['access_token'],
            token_expired=data['access_token_token_expired'],
        )

if __name__ == "__main__":
    from dotenv import load_dotenv
    load_dotenv()
    kis = KISClient()
    print(kis.get_access_token())