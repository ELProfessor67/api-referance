from django.shortcuts import render, HttpResponse
import requests
from datetime import datetime
from json import dumps
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

# payment_processor_url = 'http://localhost:8000'
payment_processor_url = 'https://payment-processor.onrender.com'

def home(request):
    return render(request,'index.html')



def api_ref(request):
    return render(request,'api-reference.html')



def endpoints(request):
    return render(request,'endpoint.html')



def transaction_add(request):
    return render(request,'transaction_add.html')



def transaction_endpoint(request):
    return render(request,'transaction_endpoint.html')


def batchs_add(request):
    return render(request,'batchs_add.html')


def batchs_endpoint(request):
    return render(request,'batchs_endpoint.html')




def auth(request):
    secret = request.GET.get('secret')
    key = request.GET.get('key')
    account_id = request.GET.get('account')
    url = payment_processor_url + f"/auth?secret={secret}&key={key}&account={account_id}"
    res = requests.get(url)
    print(res)
    
    response = {};

    response['status_code'] = res.status_code
    response['response'] = res.text
    response['time'] = str(datetime.now())

    return HttpResponse(dumps(response),status=res.status_code)



@csrf_exempt
def auth_transaction_add(request):
    secret = request.GET.get('secret')
    key = request.GET.get('key')
    account_id = request.GET.get('account')
    json_data = request.GET
    print(json_data)
    transaction = {
        "first_name" : json_data.get('first_name'),
        "last_name" : json_data.get('last_name'),
        "company" : json_data.get('company'),
        "address" : json_data.get('address'),
        "city" : json_data.get('city'),
        "state" : json_data.get('state'),
        "zip_code" : json_data.get('zip_code'),
        "country" : json_data.get('country'),
        "phone_number" : json_data.get('phone_number'),
        "amount" : json_data.get('amount'),
        "payment_method" : json_data.get('payment_method'),
        "transaction_type" : json_data.get('transaction_type'),
        "card_number" : json_data.get('card_number'),
        "exp_year" : json_data.get('exp_year'),
        "exp_month" : json_data.get('exp_month'),
        "cvv" : json_data.get('cvv'),
        "email" : json_data.get('email'),
        "transaction_id" : json_data.get('transaction_id'),
        "authusername" : json_data.get('authusername')
    }
    url = payment_processor_url + f"/transation/add/?secret={secret}&key={key}&account={account_id}"
    res = requests.post(url,data=transaction)
    # print(res.text)
    response = {};

    response['status_code'] = res.status_code
    response['response'] = res.text
    response['time'] = str(datetime.now())

    return HttpResponse(dumps(response),status=res.status_code)