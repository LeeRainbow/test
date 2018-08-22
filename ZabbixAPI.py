import json
import pprint
from urllib import request, parse

class Test:
    def __init__(self):
        self.count = 1

    def get_top(self):
        authid = self.login()
        print("get top" + str(authid))


    def script_create(self):
        authid = self.login()
        self.url = 'http://192.168.253.128/zabbix/api_jsonrpc.php'
        self.headers = {'Content-Type': 'application/json'}
        auth = {
            "jsonrpc": "2.0",
            "method": "script.create",
            "params": {
                "name": "cpu top-4",
                "command": "ps -e -o pid,user,pri,ni,vsize,rss,s,%cpu,%mem,time,cmd --sort=+pid |head -n 26",
            },
            "id": 1,
            "auth": authid,
        }
        value = json.dumps(auth).encode('utf-8')
        req = request.Request(self.url, headers=self.headers, data=value)
        try:
            result = request.urlopen(req)
        except Exception as e:
            print("Script create Failed, Please Check Your command:", e)
        else:
            response = result.read()
            page = response.decode('utf-8')
            page = json.loads(page)
            result.close()
            print("page" + str(page))
            # print("Script create Successful. The script ID Is: " .format(page.get('result')))
            # scriptid = page.get('result')
            # print('authid'+str(authid))
            # return scriptid

    def script_delete(self):
        authid = self.login()
        self.url = 'http://192.168.253.128/zabbix/api_jsonrpc.php'
        self.headers = {'Content-Type': 'application/json'}
        auth = {
            "jsonrpc": "2.0",
            "method": "script.delete",
            "params": [
                "8"

            ],
            "id": 1,
            "auth": authid,
        }
        value = json.dumps(auth).encode("utf-8")
        req = request.Request(self.url, headers=self.headers, data=value)
        try:
            result = request.urlopen(req)
        except Exception as e:
            print("Script create Failed, Please Check Your command:", e)
        else:
            response = result.read()
            page = response.decode('utf-8')
            page = json.loads(page)
            result.close()
            print("page" + str(page))


    def script_execute(self):
        authid = self.login()

        exec = {
            "jsonrpc": "2.0",
            "method": "script.execute",
            "params": {
                "scriptid": "9",
                "hostid": "10084"
            },
            "auth": authid,
            "id": 1
        }

        value = json.dumps(exec).encode('utf-8')
        req = request.Request(self.url, headers=self.headers, data=value)
        try:
            result = request.urlopen(req)
        except Exception as e:
            print("Auth Failed, Please Check Your Name And Password:", e)
        else:
            response = result.read()
            page = response.decode('utf-8')
            page = json.loads(page)
            result.close()
            print("Auth Successful. The Auth ID Is: {}".format(page.get('result')))
            authid = page.get('result')
            test = authid['value']
            print("test---"+ str(test))
            # print('authid'+str(authid))


    def script_get(self):
        authid = self.login()
        self.url = 'http://192.168.253.128/zabbix/api_jsonrpc.php'
        self.headers = {'Content-Type': 'application/json'}
        auth = {
            "jsonrpc": "2.0",
            "method": "script.get",
            "params": {
                "scriptid": '7',
            },
            "id": 1,
            "auth": authid,
        }
        value = json.dumps(auth).encode('utf-8')
        req = request.Request(self.url, headers=self.headers, data=value)
        try:
            result = request.urlopen(req)
        except Exception as e:
            print("Script create Failed, Please Check Your command:", e)
        else:
            response = result.read()
            page = response.decode('utf-8')
            page = json.loads(page)
            result.close()
            print("page script_get " + str(page))

    def script_update(self):
        authid = self.login()
        self.url = 'http://192.168.253.128/zabbix/api_jsonrpc.php'
        self.headers = {'Content-Type': 'application/json'}
        auth = {
            "jsonrpc": "2.0",
            "method": "script.update",
            "params": {
                "scriptid": '9',
                "name": "cpu top"
            },
            "id": 1,
            "auth": authid,
        }
        value = json.dumps(auth).encode('utf-8')
        req = request.Request(self.url, headers=self.headers, data=value)
        try:
            result = request.urlopen(req)
        except Exception as e:
            print("Script create Failed, Please Check Your command:", e)
        else:
            response = result.read()
            page = response.decode('utf-8')
            page = json.loads(page)
            result.close()
            print("page script_get " + str(page))

    def login(self):
        self.url = 'http://192.168.253.128/zabbix/api_jsonrpc.php'
        self.headers = {'Content-Type': 'application/json'}
        auth = {
            "jsonrpc": "2.0",
            "method": "user.login",
            "params": {
                "user": "Admin",
                "password": "135246"
            },
            "id": 1,
            "auth": None,
        }

        value = json.dumps(auth).encode('utf-8')
        req = request.Request(self.url, headers=self.headers, data=value)
        try:
            result = request.urlopen(req)
        except Exception as e:
            print("Auth Failed, Please Check Your Name And Password:", e)
        else:
            response = result.read()
            page = response.decode('utf-8')
            page = json.loads(page)
            result.close()
            print("Auth Successful. The Auth ID Is: {}".format(page.get('result')))
            authid = page.get('result')
            # print('authid'+str(authid))
            return authid

    def logout(self):
        authid = self.login()
        self.url = 'http://192.168.253.128/zabbix/api_jsonrpc.php'
        self.headers = {'Content-Type': 'application/json'}
        auth = {
            "jsonrpc": "2.0",
            "method": "user.logout",
            "params": [],
            "id": 1,
            "auth": authid,
        }

        value = json.dumps(auth).encode('utf-8')
        req = request.Request(self.url, headers=self.headers, data=value)
        try:
            result = request.urlopen(req)
        except Exception as e:
            print("Auth Failed, Please Check Your Name And Password:", e)
        else:
            response = result.read()
            page = response.decode('utf-8')
            page = json.loads(page)
            result.close()
            print("Auth Successful. The Auth ID Is: {}".format(page.get('result')))
            authid = page.get('result')
            # print('authid'+str(authid))
            return authid

if( __name__ =='__main__' ):
    pp = pprint.PrettyPrinter(indent=2)
    profiler = Test()
    # pp.pprint(profiler.get_top())
    # pp.pprint(profiler.script_create())
    # pp.pprint(profiler.script_delete())
    # pp.pprint(profiler.script_execute())
    # pp.pprint(profiler.script_get())
    # pp.pprint(profiler.script_update())
    pp.pprint(profiler.logout())
