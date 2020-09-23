#from .models import recharge
import json
import requests

keys = {}

class ImageField404Middleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if (request.method == 'POST' and 'nik'):
            phone_number = str(request.POST.get('phone'))
            self.sendotp(phone_number)

    def sendotp(self, phone_number):
        call = requests.get('https://2factor.in/API/V1/1d2af4d7-e787-11ea-9fa5-0200cd936042/SMS/+91'+phone_number+'/AUTOGEN')
        data = json.loads(call.text)
        keys[str(phone_number)] = data['Details']