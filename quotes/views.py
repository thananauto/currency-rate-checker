from django.shortcuts import render, redirect
from django.contrib import messages
from . forms import CurrencyForm
from . models import Currency


# Create your views here.


def home(request):
    import requests
    import json

    if request.method == 'POST':
        currency = request.POST['currency']
        api_request = requests.get(f'https://api.exchangeratesapi.io/latest?symbols=USD,GBP,EUR&base={currency}')

        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = {'msg': 'error in api response'}

        return render(request, 'stocks/home.html', {'api' : api})

    else:

        return render(request, 'stocks/home.html', {'ticker' : 'Select the currency in right corner of web page'})


    


def about(request):
    return render(request, 'stocks/about.html', {})

def add_currency(request):
    import requests
    import json
    output = []

    if request.method == 'POST':
        form = CurrencyForm(request.POST or None)
        
        if form.is_valid():
            currency = form.data['cur']
            form.save()
            messages.success(request, (f'Currency {currency} has been added'))
            return redirect('stocks:add_currency')
        else:
             return render(request, 'stocks/add_currency.html', {'error': 'Add the correct currency in the list'})    
    else:    
        currency = Currency.objects.all()
        for cur in currency:
            api_request = requests.get(f'https://api.exchangeratesapi.io/latest?symbols=USD,GBP,EUR,AUD,INR&base={cur}')

            try:
                api = json.loads(api_request.content)
                output.append(api)
            except Exception as e:
                api = {'msg': 'error in api response'}
                output.append(api)

    return render(request, 'stocks/add_currency.html', {'currency': currency, 'output': output })    


def del_currency(request, cur_id):
    item = Currency.objects.get(pk=cur_id)
    item.delete()
    messages.success(request, (f'Currency {item} has been deleted'))
    return redirect('stocks:add_currency')