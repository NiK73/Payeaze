from django.shortcuts import render, redirect
import paytmchecksum 
import requests
import random
from django.shortcuts import HttpResponseRedirect
from .Paytm import Checksum
from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

MERCHANT_KEY = 'ud83B8FzyApZt954'

import json

from django.http import HttpResponse

from django.contrib import messages

from .models import Customer, Order

from django.views.decorators.csrf import csrf_exempt

keys={}

trans = {}

names={}


#Register get OTP
def nik2(request):
    print('Entered request')
    if request.method == "POST":
        phone_number = str(request.POST.get('phone_number'))
        name = str(request.POST.get('name'))
        user = authenticate(request, username=phone_number, password="Success")
        if user is not None:
            raise NameError('UserExists')
            return render(request, 'acc/index.html')
        else:
            print(phone_number)
            print(name)
            call = requests.get('https://2factor.in/API/V1/9e757f67-ede1-11ea-9fa5-0200cd936042/SMS/+91'+phone_number+'/AUTOGEN/PAYEAZE')
            data = json.loads(call.text)
            keys[str(phone_number)] = {'name':name,'secret_key':data['Details']}
            with open('keys.json','w') as f:
                json.dump(keys,f)
            print(data)
            return HttpResponse("")

# Login get OTP
def nik(request):
    print('Entered request login')
    if request.method == "POST":
        phone_number = str(request.POST.get('phone_number'))
        user = authenticate(request, username=phone_number, password="Success")
        if user is not None:
            print(phone_number)
            print(type(phone_number))
            call = requests.get('https://2factor.in/API/V1/9e757f67-ede1-11ea-9fa5-0200cd936042/SMS/+91'+phone_number+'/AUTOGEN/PAYEAZE')
            data = json.loads(call.text)
            with open('keys.json','r') as f:
                keys = json.load(f)
            print(data['Details'])
            keys[str(phone_number)]['secret_key'] = data['Details']
            with open('keys.json','w') as f:
                json.dump(keys,f)
            print(data)
            return HttpResponse("")
        else:
            messages.success(request, 'Wrong details updated.')
            # else:

            #     messages.success(request, 'SignUp First!!!')

            #     return render(request, 'acc/index.html')

    #return None



def verifyotp2(request):
    print("verify Nikhil again")
    if request.method == 'POST':
        with open('keys.json') as f:
            data = json.load(f)
        otp = str(request.POST.get('votp'))
        phone_number = str(request.POST.get('phone_number1'))
        print(otp)
        print(phone_number)
        name = data[phone_number]['name']
        secret_key = data[phone_number]['secret_key']
        print(name)
        print(secret_key)
        check = requests.get('https://2factor.in/API/V1/9e757f67-ede1-11ea-9fa5-0200cd936042/SMS/VERIFY/'+secret_key+'/'+otp)

        result = json.loads(check.text)

        print(result['Status'])

        if result['Status']=='Success':
            print("h1")
            user = authenticate(request, username=phone_number, password="Success")
            if user is not None:
                print("h2")
                login(request, user)
                messages.success(request, 'Logged IN Successfully!!!!')
                params = {'user':user}
                return render(request, 'acc/logout.html', params)
            else:
                print("h3")
                messages.error(request, 'Invalid Username or Password')
                return redirect('/')
        else:
            messages.success(request, 'Wrong details updated.')
            return render(request, 'acc/error.html')
            #return render(request, 'acc/index.html')

            #return render(request, 'acc/index1.html/')

def home(request):
    if not request.user.is_authenticated:
        return redirect('../error/')
    else:
        return render(request, 'acc/logout.html')


def logoutt(request):
    logout(request)
    return redirect('../')


def callfun():

    return redirect('.r/index1/')


def verifyotp(request):
    if request.method == 'POST':
        with open('keys.json') as f:
            data = json.load(f)
        otp = str(request.POST.get('votp'))
        phone_number = str(request.POST.get('phone_number1'))
        name = data[phone_number]['name']
        secret_key = data[phone_number]['secret_key']
        check = requests.get('https://2factor.in/API/V1/9e757f67-ede1-11ea-9fa5-0200cd936042/SMS/VERIFY/'+secret_key+'/'+otp)
        result = json.loads(check.text)
        print(result['Status'])
        if result['Status']=='Success':
            user = User.objects.create_user(phone_number, name, "Success")
            user.save()
            # return redirect('../index1/')
            return render(request, 'acc/logout.html')
# Create your views here.

def index(request):
    print(request.method)
    if request.method == 'POST':
        print("loginn me enter")
        name = request.POST.get("phone_number")
        r_phone = request.POST.get("phone_number")
        print(name)
        params = {'name':name,'r_phone':r_phone}
        print(params)
        return render(request, 'acc/index1.html', params)
    return render(request, 'acc/index.html')



def index1(request):
    if not request.user.is_authenticated:
        return redirect('../error/')
    else:
        print(request.method)
        if request.method=='POST':
            param_dict = {}
            name = request.POST.get("r_name","kartik")
            r_phone = request.POST.get("r_phone","1234567898")
            phone = request.POST.get("tel")
            sim = request.POST.get("sim")
            state = request.POST.get("state")
            plan = request.POST.get("plan")
            validity = request.POST.get("validity","6")
            confirm = request.POST.get("confirm")
            param_dict = {r_phone:{'name':name,'phone':phone,'sim':sim,'state':state,'plan':plan,'validity':'6','confirm':confirm}}
            # with open('recharge.json','w') as f:
            #     json.dump(param_dict,f)
            orders = Order(r_name=name,r_phone=r_phone,phone=phone, sim=sim, state=state, plan=plan, validity=validity, confirm=confirm)
            orders.save()
       
            # return render(request, 'acc/paytm.html')
        return render(request, 'acc/index1.html')
    #return HttpResponse("Error 404")

# def newfun(param_dict):
#     return redirect('pay')

def contact(request):
    if not request.user.is_authenticated:
        return render(request, 'acc/contact.html')
    else:
        return render(request, 'acc/contact_loged.html')
    

def error(request):
    return render(request, 'acc/error.html')


def index2(request):
    if not request.user.is_authenticated:
        return redirect('../error/')
    else:
        # with open('names.json') as f:
        #     data3 = json.load(f)
        # a = data3.values()
        # for i in a:
        # data = Order.objects.filter(r_phone=i)
        data = Order.objects.all()
        a=[]
        for i in data:
            a.append(i.id_no)
        data = data[::-1]
        params = {'data':data, 'a':a}
        return render(request, 'acc/index2.html', params)

@csrf_exempt
def callback(request):
    TXNID = request.POST.get("ORDERID")
    STATUS = request.POST.get("STATUS")
    #username = request.POST.get("name")
    with open('recharge.json') as f:
        recharge_data = json.load(f)
    # print("call back")
    # print(request.user.username)
    # print(request.user.email)
    data = Order.objects.all()
    a=[]
    username = recharge_data[TXNID]
    for i in data:
        if i.r_phone==username:
            a.append(i)
    info = a[-1]
    r_name = info.r_name
    r_phone = info.r_phone
    phone = info.phone
    sim = info.sim
    state = info.state
    plan = info.plan
    confirm = info.confirm
    info.delete()
    t_status = STATUS
    t_token = TXNID
    orders = Order(t_status= t_status,t_token=t_token,r_name=r_name,r_phone=r_phone,phone=phone, sim=sim, state=state, plan=plan, confirm=confirm)
    orders.save()
    params = {'data':username,'TX':TXNID,'STATUS':STATUS}
    return redirect('../orders/')
    #return render(request, 'acc/callback.html', params)

def pay(request):
    print("pay wala")
    print(request.user.username)
    print(request.user.email)
    paytmParams = dict()
    oid = "ORDERID_"+str(random.randint(100,999999))
    cid = "CUST_005"
    price = "699.00"
    paytmParams["body"] = {
                "requestType"   : "Payment",
                "mid"           : "XSGpNa29724761433350",
                "websiteName"   : "WEBSTAGING",
                "orderId"       : oid,
                "callbackUrl"   : "https://payeaze.in/callback/",
                "txnAmount"     : {
                    "value"     : price,
                    "currency"  : "INR",
                },
                "userInfo"      : {
                    "custId"    : cid,
                    },
            }

                    # Generate checksum by parameters we have in body
                    # Find your Merchant Key in your Paytm Dashboard at https://dashboard.paytm.com/next/apikeys 
    checksum = paytmchecksum.generateSignature(json.dumps(paytmParams["body"]), "UG3N06L_aZji73d@")

    paytmParams["head"] = {
                        "signature" : checksum
                    }

    post_data = json.dumps(paytmParams)

                    # for Staging
    url = "https://securegw-stage.paytm.in/theia/api/v1/initiateTransaction?mid="+paytmParams['body']['mid']+"&orderId="+paytmParams['body']['orderId']

                    # for Production
                    # url = "https://securegw.paytm.in/theia/api/v1/initiateTransaction?mid=YOUR_MID_HERE&orderId=ORDERID_98765"

    response = requests.post(url, data = post_data, headers = {"Content-type": "application/json"}).json()
                    #print(response)
                    # print({'txnToken': response['body']['txnToken'],'CHECKSUMHASH':checksum ,'TXNAMOUNT': paytmParams['body']['txnAmount'],'mid':mid,'orderId':oid})
            
    param_dict = {oid:request.user.username}
    with open('recharge.json','w') as f:
        json.dump(param_dict,f)

    payment_data = {'txnToken': response['body']['txnToken'],'CHECKSUMHASH':checksum ,'txnAmount': paytmParams['body']['txnAmount']['value'],'merchant_id':paytmParams['body']['mid'],'orderId':paytmParams['body']['orderId'],'websiteName':paytmParams['body']['websiteName']}
    print(payment_data)

            #return redirect('../pay/', payment_data)
    return render(request, 'acc/paytm.html', payment_data)
        #return render(request, 'acc/paytm.html')

def paytm(request):
    pass

@csrf_exempt
def handlerequests(request):
    return HttpResponse("Done!!!!!!")