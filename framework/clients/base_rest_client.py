import json
import allure
import structlog
import requests


class BaseRestClient:

    def __init__(self, host):
        self.host = host
        self.log = structlog.get_logger(self.__class__.__name__).bind(service='rest-api')
        self.session = requests.session()

    def get(self, path: str, **kwargs):
        return self._send_request(
            'GET', path,
            **kwargs
        )

    def post(self, path: str, **kwargs):
        return self._send_request(
            'POST', path,
            **kwargs
        )

    def put(self, path: str, **kwargs):
        return self._send_request(
            'PUT', path,
            **kwargs
        )

    def patch(self, path: str, **kwargs):
        return self._send_request(
            'PATCH', path,
            **kwargs
        )

    def delete(self, path: str, **kwargs):
        return self._send_request(
            'DELETE', path,
            **kwargs
        )

    def _send_request(self, method: str, path: str, **kwargs):
        url = f'{self.host}{path}'
        log = self.log.bind()
        log.msg(
            'request',
            method=method,
            url=url,
            **kwargs
        )
        allure.attach(json.dumps(kwargs.get('json', {})), f'{method} {url}', allure.attachment_type.JSON)
        response = self.session.request(
            method=method,
            url=url,
            **kwargs
        )
        try:
            response_json = response.json()
        except ValueError:
            response_json = None
        if response_json:
            allure.attach(json.dumps(response_json), 'response', allure.attachment_type.JSON)
        log.msg(
            'response',
            status_code=response.status_code,
            json=response_json,
            text=response.text,
            headers=response.headers,
        )
        return response
