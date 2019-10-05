from rest_framework.response import Response
from .portalSerializer import portalSerializer
from rest_framework import viewsets, generics
from .models import portal
from rest_framework.views import APIView
import requests
import json
from .sfdc import * 
from rest_framework.permissions import AllowAny
# Create your views here.

class store(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    #
    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)


    queryset = portal.objects.all()
    serializer_class = portalSerializer
    def notify(self,data,msg):
        headers = {
            'Content-Type': 'application/json; charset=UTF-8',
            'Authorization': 'Bearer YWI2ODUxZmYtMDA5Ni00YTg1LTlmYzQtOTUxMjA5Y2MzZmU5ZDNjNTI1MzItY2Q4_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f'
        }
        message = 'User :  ' + data['name'] + ', Requested : ' + str(data['product']) + ', for : ' + str(data['duration']) + ' days , The deal ID : '  + str(data['did'])+ ', Opportunity Name : ' + msg['msg'][0]['Name'] + ' , SE Name  :  ' + msg['more'][0]['Name']
        payload = {
            'toPersonEmail': 'adallah@cisco.com',
            #'roomId': 'Y2lzY29zcGFyazovL3VzL1JPT00vZTkwNWZhZjktNWZiNC0zMWE1LWEzMTQtNTUyZWQ3YjY4NDJk',
            'text': message,
        }
        #webex api
        #url = 'https://api.ciscospark.com/v1/rooms'
        url = 'https://api.ciscospark.com/v1/messages'
        r = requests.post(url, data=json.dumps(payload), headers=headers)
        return r
      

    def directsfdc(self,data,username,password):
        message = main(str(data['did']))
        self.notify(data,message) 


    def create(self, request):
        serializer = portalSerializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            r = self.directsfdc(serializer.data,request.data['username'],request.data['password'])
            return Response(r)
        return Response(serializer.errors, 400)


class hardware(APIView):
    permission_classes = (AllowAny,)
    def post(self,request):
        querystring = {
           
        }

        headers = {
            'authorization': "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6ImJmNTVkMGY5NzQxY2EwYTFjZDBhNDgwZGY0NGJlODAzN2U4NzBhMWFjZjZmMzJhMGY5ZWMzYTA0MTQxMjUwMDczOWY1NjZhMjc5OGFmZTA1In0.eyJhdWQiOiIxIiwianRpIjoiYmY1NWQwZjk3NDFjYTBhMWNkMGE0ODBkZjQ0YmU4MDM3ZTg3MGExYWNmNmYzMmEwZjllYzNhMDQxNDEyNTAwNzM5ZjU2NmEyNzk4YWZlMDUiLCJpYXQiOjE1NjkzOTU2NDksIm5iZiI6MTU2OTM5NTY0OSwiZXhwIjoxNjAxMDE4MDQ5LCJzdWIiOiIyMzQiLCJzY29wZXMiOltdfQ.pRlTNSsS43z1AHxgKOTomy616bcaw5513rht8KjyO_zuwFKxAymd2RLAKywAjxVJ-tSYdvzNcdwH5hCs8Z1pF001BsvmESJQfaxEoLvfLRDQAhrW0q6CeFplhQLeaIAkjl4iBl8Ucy40CMJe5sqLO0AZm43544Kx716-xeFcWaKCp1qrchfkBL308ZhApocZ-2abObSSDoxwU09zuZh4y4ngWc5w7huhGikafenyF1zVwAW-VKyq93gUZBA9D3ZJl1_lzkKlbyH482lcywflmRwaA8uapkwGBSUqEDuOTPIhf3yDkHVB68tRmgDtE2ZGMm_cTx_7A9-_2dxU82YtXKALuSzvrQ5KFDyu2mcGjjzqzfuhQOYFC3yBDdJJeFvreVafe6pfMz974_sZP_N6AH2q6I02tDhQFQtleTJdinvN72CdUYGOTOlrmnnW1uRv1W4sDUriQSp-GAUxhI-GzEd6aJ5sbS7BscLYlwIJZjR6seNM6yoMleKrxgLHxb7WwFuHsGX_xHI2vin-4ZgQ7U19GslVs3YRyyALTmfhMR3e452TcvcS2h7xERXIwKUH3sfS8nXRqVbk1HjLOVjh8aSgle4yVDHQMMNzSH_1bXqlTo58cTLGI-rCKU6WzFRJp87dv8g07sq1XnHBrRZJT-TkSdlrfWhOerY38bKK69g",
            'accept': "application/json",
            'content-type': "application/json"
            }
            
       
        #inventory.cisco.com
        url = 'http://inventory.cisco.com/api/v1/hardware?limit=10000'
        # url = 'https://jsonplaceholder.typicode.com/todos'
        r = requests.get(url,  headers=headers, params=querystring, verify=False)
        print(r)
        return Response(r.text)
