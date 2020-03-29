import requests
import json


class RequestMethod:
    def go_post(self, url, data, header=None):
        res = None
        try:
            if header != None:
                res = requests.post(url=url, data=data, header=header)
            else:
                res = requests.post(url=url, data=data)
            return res
        except Exception as e:
            print(e)

    def go_get(self, url, params, header=None):
        res = None
        try:
            if header != None:
                res = requests.get(url=url, params=params, header=header)
            else:
                res = requests.get(url=url, params=params)
            return res
        except Exception as e:
            print(e)

    def main_json_to_str(self, method=None, url=None, data=None, header=None) -> json:
        res = None
        if method == 'post':
            res = self.go_post(url, data, header)
        elif method == 'get':
            res = self.go_get(url, data, header)
        else:
            print("method is error, pls input post or get")
            return False
        return res
