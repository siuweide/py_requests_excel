import json
import requests

from data.get_data import GetData


class RunMethod():

    def run_get(self, url, params=None, headers=None,verify=False):
        """ get请求 """
        res = requests.get(url=url, params=params, headers=headers, verify=verify)
        return res

    def run_post(self,url, data=None, headers=None, verify=False):
        """ post请求 """
        res = requests.post(url=url, data=data, headers=headers, verify=verify)
        return res

    def run_main(self,url, method, data=None, params=None, headers=None, verify=False):
        """ get/post请求集合 """
        res = None
        if method == 'get':
            res = self.run_get(url=url, params=params, headers=headers, verify=verify)
        elif method == 'post':
            res = self.run_post(url, data=data, headers=headers, verify=verify)
        return res

if __name__ == '__main__':
    # url = 'https://172.16.3.116:1182/OPC/User/checkLogin'
    url1 = 'https://172.16.3.205:1182/OPC/GFSOrder/ajaxProcess'
    # data = {"account":"rebecca","password":"888","isVerify":"N"}
    data = {"sEcho":2,"iDisplayStart":0,"iDisplayLength":10,"aSorting[0][sName]":"payment_date","aSorting[0][sValue]":"desc","form[status]":"WFD","form[saleDateStart]":"2020-03-15","form[saleDateEnd]":"2020-04-15","form[platform]":"wish","api":"gfs.order.list"}
    test = RunMethod()
    get_data = GetData()
    cookie = get_data.read_cookie()
    req = test.run_main(url1,'post', data=data, headers=cookie)
    print(req.text)
    # print(json.loads(req.text))
    # orderId = json.loads(req.text)['aoData'][0]['orderId']
    # print('第一条用例通过')
    # data1 = '{"form[gfsOrderList][0][gfsOrderId]":%d,"form[platform]":"ebay","api":"gfs.order.cancelOrder","ajax":1}' % orderId
    # data1 = json.loads(data1)
    # quxiao = test.run_main(url1,'post', data=data1, headers=cookie)
    # print(quxiao.text)

