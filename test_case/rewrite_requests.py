import requests



class RewriteRequests:

    def rew_request(self,method = "get", url= "", data="",params = "",*args):

        if method =="get":
            return requests.request(method="get",url =url,params=params)

        elif method == "post":
            return requests.request(method="post",url =url,data=data)

        elif method == "delete":
            return requests.request(method="delete",url =url,data=data)

        elif method == "put":
            return requests.request(method="put",url =url,data=data)
