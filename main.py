import os

import pytest
import yaml

if __name__ == '__main__':
    pytest.main(["-vs"])
    #
    # os.system("allure generate ./result -o ./report -clean")

    # with open(r"C:\Users\今晚打老虎\Desktop\pythonProject1\data\data.yaml","r",encoding="utf-8") as f:
    #     re = yaml.load(stream=f,Loader=yaml.FullLoader)
    #     list = []
    #     for i in re:
    #         for j in i:
    #             print(i[j])
    #             list.append(i[j])
    #     print(len(list))





