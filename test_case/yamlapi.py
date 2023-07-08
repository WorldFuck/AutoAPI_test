import yaml

class YamlApi:

    def yamlapi(self,path):
        with open(path, "r", encoding="utf-8") as f:
            re = yaml.load(stream=f, Loader=yaml.FullLoader)
            return re

        # list = []
        # for i in re:
        #     for j in i:
        #         list.append(i[j])
        #
        # return list

if __name__ == '__main__':
    a = YamlApi()
    print(a.yamlapi())