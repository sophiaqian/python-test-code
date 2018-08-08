#!/usr/bin/python
#!/usr/bin/python
# coding=utf-8
import requests
import unittest
import hashlib


class TestLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.login_url = 'http://mis.test.ds.gome.com.cn/permission/loginToken'
        cls.saveproject_url = 'http://mshop.intra.test.ds.gome.com.cn/mshop/saveProject'
        cls.loginName = 'qianwenhui'
        cls.password = '8456f88bfaa29b6ffb47a7c0d7ed9ab2e03c3cab752495ab9a08727e024f0cc6e5dfeb9afdd4a2130c84a9ac431ad68e9cf9ea3e80412d30b8326fd534df3b0a99558b4d286d8b3fa39a5e40c76121da81e4da103b8f33356d5774afd9f73a45814a1c8cbf552fae7d0e8ce802444f19672f8b409cb10cda01660aa1aa05dada'
        cls.mode = "1"
        cls.effectiveStartTime = "2018-08-13 10:10:50"
        cls.effectiveEndTime = "2018-08-13 11:05:50"
        cls.giftTotalCount = "1"
        cls.budgetNumber = "004000000804"
        cls.regularContent = "[{\"regularId\":\"P799052\",\"count\":\"1\"}]"
        cls.isNotice = "Y"
        cls.noticeCount = "1"
        cls.noticeMobile = "15901014062"


    def test_login(self):
        """
        测试登录
        """
        json1 = {
            'loginName': self.loginName,
            'password': self.password
        }

        response = requests.post(self.login_url,json=json1)
        print(response)
        assert response.status_code == 200
        return (response.json()['data']['loginToken'],response.json()['data']['id'])

    def test_saveproject(self):

        token,id = self.test_login()
        print(token)
        header = {
            "Host": "mshop.intra.test.ds.gome.com.cn",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
            "Accept": "application/json",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Accept-Encoding": "gzip, deflate",
            "Content-Type": "application/json;UTF-8",
            "X-Requested-With": "XMLHttpRequest",
            "Connection": "keep-alive",
            "Content-Length": "227",
            "Referer": "http://mshop.intra.test.ds.gome.com.cn/app/mshop/vipCouponList.html?module=mshop.intra",
            "x-gomeplus-admin-user-id": str(id),
            "x-gomeplus-admin-login-token": token,
            "Cookie": "loginToken=" + token
        }

        json2 = {
            'mode': self.mode,
            'effectiveStartTime': self.effectiveStartTime,
            'effectiveEndTime': self.effectiveEndTime,
            'giftTotalCount': self.giftTotalCount,
            'budgetNumber': self.budgetNumber,
            'regularContent': self.regularContent,
            'isNotice': self.isNotice,
            'noticeCount': self.noticeCount,
            'noticeMobile': self.noticeMobile,
        }

        response = requests.post(self.saveproject_url, headers=header, json=json2)
        # print(response.json())
        assert response.status_code == 200


if __name__ == '__main__':
     unittest.main()




















