from django.shortcuts import render
import requests
from urllib3.exceptions import InsecureRequestWarning
from urllib3 import disable_warnings

# Create your views here.
def index(request):
    headers = { 'apikey': 'l7xx1f2691f2520d487b902f4e0b57a0b197' }
    disable_warnings(InsecureRequestWarning)
    data=0
    if 'search' in request.GET:
        search = request.GET['search']
        if search.isdigit():
            if len(search)==8:
                out=search
                params = { 'kvkNummer': out,}
                response = requests.get('https://api.kvk.nl/test/api/v1/zoeken', headers=headers, params=params, verify=False)
                data = response.json()
            else:
                out=search
                params = { 'vestigingsnummer': out,}
                response = requests.get('https://api.kvk.nl/test/api/v1/zoeken', headers=headers, params=params, verify=False)
                data = response.json()
            return render(request,'index.html',{'data':data})
        else:
            out=search
            params = {'handelsnaam': out,}
            response = requests.get('https://api.kvk.nl/test/api/v1/zoeken', headers=headers, params=params, verify=False)
            data = response.json()
            
        return render(request,'index.html',{'data':data})
    return render(request,'index.html',{'data':data})