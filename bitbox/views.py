from django.shortcuts import render
from django.utils import timezone
from .models import reg, bitboxc

def index(request):
	inf= bitboxc.objects.filter()
	return render(request,'bitbox/home.html',{'inf': inf})


def search_product(request):
    if request.method == "POST":
        query_phone = request.POST['searched']
        if query_phone:	
            results = bitboxc.objects.filter(phonenumber__contains=query_phone)
            return render(request, 'bitbox/search.html', {"results":results})
    return render(request, 'bitbox/search.html')
