from django.shortcuts import render
from django.utils import timezone
from .models import reg

def index(request):
	inf= reg.objects.filter()
	return render(request,'bitbox/home.html',{'inf': inf})


def search_product(request):
    if request.method == "POST":
        query_phone = request.POST.get('searched')

        # 🔒 validation
        if not query_phone or len(query_phone) != 11 or not query_phone.isdigit():
            return render(request, 'bitbox/search.html', {
                "error": "মোবাইল নাম্বার অবশ্যই ১১ সংখ্যার হতে হবে"
            })

        # ✅ valid হলে search
        results = reg.objects.filter(phone=query_phone)

        return render(request, 'bitbox/search.html', {
            "results": results
        })

    return render(request, 'bitbox/search.html')
