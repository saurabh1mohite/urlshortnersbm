from django.shortcuts import render, redirect
import uuid
from .models import Urls
from django.http import HttpResponse
# Create your views here.

def index(requests):
    return render(requests, 'index.html')

def create(requests):
    if requests.method == 'POST':
        link = requests.POST['link']
        uid = str(uuid.uuid4())[:5]
        new_url =  Urls(link=link, uuid=uid)
        new_url.save()
        return HttpResponse(uid)

def go(requests, pk):
    url_details = Urls.objects.get(uuid=pk)
    return redirect(url_details.link)