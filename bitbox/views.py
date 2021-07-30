from django.shortcuts import render
from django.utils import timezone
from .models import reg

def index(request):
	inf= reg.objects.filter()
	return render(request,'bitbox/home.html',{'inf': inf})


def search_product(request):
    if request.method == "POST":
        query_phone = request.POST['searched']
        if query_phone:	
            results = reg.objects.filter(phone__contains=query_phone)
            return render(request, 'bitbox/search.html', {"results":results})
    return render(request, 'bitbox/search.html')
