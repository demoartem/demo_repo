import allure
from framework.clients.base_rest_client import BaseRestClient


class HTTPBINClient(BaseRestClient):

    def __init__(self):
        super().__init__(host='https://httpbin.org')
    
    allure.step('DELETE /delete')
    def delete_(self, json=None, headers=None):
        return self.delete(path='/delete',
                           json=json,
                           headers=headers)
