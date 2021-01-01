from django.shortcuts import render
from .models import FEES, FeeSem, Payments, FeeUpdate
import json
from django.views.decorators.csrf import csrf_exempt
from PayTm import Checksum
# Create your views here.
from django.http import HttpResponse
MERCHANT_KEY = 'zmsJcdF_v&oU5Drx';

def fee(request):
    allProds = []
    catprods = FEES.objects.values('fee_sub')
    cats = {item['fee_sub'] for item in catprods}
    for cat in cats:
      prod = FEES.objects.filter(fee_sub=cat)
      n = len(prod)
      allProds.append([prod, range(1, n)])
    params = {'allProds':allProds}
    return render(request, 'fee/fees.html',params)

def semfee(request):
        allProds = []
        catprods = FeeSem.objects.values('typee')
        cats = {item['typee'] for item in catprods}
        for cat in cats:
            prod = FeeSem.objects.filter(typee=cat)
            n = len(prod)
            allProds.append([prod, range(1, n)])
        params = {'allProds': allProds}
        return render(request, 'fee/semfe.html', params)

def checkout(request):
    if request.method=="POST":
        name = request.POST.get('name', '')
        amount = request.POST.get('amount', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address', '')
        roll_number = request.POST.get('roll_number', '')
        phone = request.POST.get('phone', '')
        payment = Payments( name=name, email=email, address=address,
                       roll_number=roll_number, phone=phone, amount=amount)
        payment.save()
        update = FeeUpdate(payment_id=payment.payment_id,name=payment.name, email=payment.email, address=payment.address,roll_number=payment.roll_number, phone=payment.phone, amount=payment.amount, update_desc="InQueue")
        update.save()
        param_dict = {

                'MID': 'xIVIoz54669135199172',
                'ORDER_ID': str(payment.payment_id),
                'TXN_AMOUNT': str(amount),
                'CUST_ID': email,
                'INDUSTRY_TYPE_ID': 'Retail',
                'WEBSITE': 'WEBSTAGING',
                'CHANNEL_ID': 'WEB',
                'CALLBACK_URL':'http://127.0.0.1:8000/fee/handlerequest/',

        }
        param_dict['CHECKSUMHASH'] = Checksum.generate_checksum(param_dict, MERCHANT_KEY)
        return render(request, 'fee/paytm.html', {'param_dict': param_dict})

    return render(request, 'Fee/checkout.html')


@csrf_exempt
def handlerequest(request):
    # paytm will send you post request here
    form = request.POST
    response_dict = {}
    for i in form.keys():
        response_dict[i] = form[i]
        if i == 'CHECKSUMHASH':
            checksum = form[i]

    verify = Checksum.verify_checksum(response_dict, MERCHANT_KEY, checksum)
    if verify:
        if response_dict['RESPCODE'] == '01':
            print('order successful')
            if request.method == "POST":
                payment_id = request.POST.get('payment_id','')
                amount = request.POST.get('TXNAMOUNT', '')
                transaction_id = request.POST.get('TXNID', '')
                transaction_status = request.POST.get('STATUS', '')
                update = FeeUpdate(amount=amount,payment_id=payment_id,update_desc="InQueue",transaction_id=transaction_id, payment_status=transaction_status)
                update.save()
        else:
            print('order was not successful because' + response_dict['RESPMSG'])
    return render(request, 'fee/paymentstatus.html', {'response': response_dict})