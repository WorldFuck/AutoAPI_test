import allure
import pytest
import requests

import yaml
from selenium.webdriver.common.by import By

from test_case.rewrite_requests import RewriteRequests
from test_case.yamlapi import YamlApi

@pytest.mark.usefixtures("access_web")
class Testcase:
    yamlapi = YamlApi()

    @pytest.mark.skip("skip")
    @pytest.mark.parametrize("data", yamlapi.yamlapi(r"C:\Users\今晚打老虎\Desktop\pythonProject1\data\data.yaml"))
    def test_1(self, data):
        # res = RewriteRequests().rew_request(method=data["method"],url=data["url"],params=data["params"])
        res = requests.request(method=data["method"], url=data["url"], params=data["params"])
        print(res.text)


    @allure.feature("百度搜索")
    @pytest.mark.smoke
    def test_6(self,access_web):
        input_box = access_web.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[5]/div/div/form/span[1]/input")
        summit = access_web.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[5]/div/div/form/span[2]/input")
        input_box.send_keys("测试")
        summit.click()

