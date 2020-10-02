
import urllib
import urllib3
import json,requests


class SendData():
    def __init__(self):
        self.url_put = "https://yundorr.xyz/api/user/publish"
        self.get_url = 'https://yundorr.xyz/api/user/search?eid='

    def SetGeturlID(self,id):

        if id != "设备1" and id != "设备2" and id != "设备3":
            return False
        self.get_url = self.get_url + id



    def send(self,dataa):
        headers = {'content-type': 'application/json'}

        data = {
        "eid": "设备1",
        "temperature": "25",
        "humidity": "30",
        "smokescope": "45",
        "flame": "30",
        "pressure": "23",
        "wind": "90",
        "direction": "东风",
        "misfile": "否",
        "rain": "否"
        }

        # jdata = json.dump(values)
        try:
            jdata = json.dumps( dataa )
        # req = urllib.

            r = requests.post(self.url_put,data = jdata,headers = headers)
        except Exception as err:
            print("send err.")
            print(str(err))
            return False


        res = str(r)
        if res == "<Response [200]>":
            return True
        else:
            print(res)
            print("send error,Data inconsis.")
            return False



    def http_get(self):
        url = self.get_url
        #'https://yundorr.xyz/api/user/search?eid=设备1'
        res = requests.get(url)

        return str(res)





if __name__ == '__main__':
    s = SendData()
    s.SetGeturlID("设备1")
    # s.send(1)
    if s.send(1):
        print('success')
    else:
        print('faild')