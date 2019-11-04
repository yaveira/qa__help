from urllib.parse import urljoin
import requests
import json


class Emprestimo:
    def __init__(self, context):
        Emprestimo.__init__(self, context)

    def criar_emprestimo(self, endpoint):
        from features.constants import URL_FICTICIA

        request_url = urljoin(URL_FICTICIA, endpoint)

        headers_content = {
            'Content-type': 'application/json',
            'Authorization': self.token
        }

        body_content = self.dados_emprestimo

        self.response = requests.post(url=request_url, headers_content=headers_content, body=body_content)
        return self.response

    def consultar_emprestimo(self, endpoint):
        from features.constants import URL_FICTICIA

        request_url = urljoin(URL_FICTICIA, endpoint.format(self.dados_emprestimo['id']))

        headers_content = {
            'Authorization': self.token
        }

        self.response = requests.get(url=request_url, headers_content=headers_content)
        return self.response
