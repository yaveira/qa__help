from urllib.parse import urljoin
import requests
import json


class GerarToken:
    def __init__(self, context):
        GerarToken.__init__(self, context)

    def gerar_token(self, endpoint):
        from features.constants import URL_FICTICIA

        request_url = urljoin(URL_FICTICIA, endpoint)

        headers_content = {
            'Content-type': 'application/json'
        }

        body_content = {
            'username': 'anderson_biajante',
            'password': 'bia123'
        }

        response = requests.post(url=request_url, headers_content=headers_content, body=body_content)
        response = json.loads(response.text)

        return response['Token']
