from django.shortcuts import render

def home(request):
    import requests
    import json
    # Grab crypto price data
    # https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,XRP&tsyms=USD
    price_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,XRP,BCH,EOS,LTC,XLM,ADA,USDT,MIOTA,TRX&tsyms=USD")
    price = json.loads(price_request.content)

    # Grab crypto news data
    # https://min-api.cryptocompare.com/data/v2/news/?lang=EN
    api_request = requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
    api = json.loads(api_request.content)
    return render(request, 'home.html', {'api': api, 'price': price})


def prices(request):
    if request.method == 'POST':
        import requests
        import json

        quote = request.POST['quote']
        quote = quote.upper()

        crypto_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=" + quote + "&tsyms=USD")
        crypto = json.loads(crypto_request.content)
        return render(request, 'prices.html', {'quote': quote,'crypto':crypto})

    else:
        notfound = "Enter a crypto currency symbol info the form above..."
        return render(request, 'prices.html',{'notfound': notfound })