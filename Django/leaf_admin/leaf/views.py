from django.shortcuts import render
from django.http import HttpResponse as HR


import urllib.request as ub
import gzip as gp
import json as js


def home(request):
    url = "http://data.taipei/youbike"
    ub.urlretrieve(url, "data.gz")
    f = gp.open('data.gz')
    jdata = f.read()
    f.close()
    data = js.loads(jdata)

    return render(request, 'home.html' ,locals())





      