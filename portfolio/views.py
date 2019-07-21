from django.shortcuts import render

from .models import Portfolio
# Create your views here.

def portfolio(request):
    portfolios = Portfolio.objects
    return render(request, 'portfolio.html', {'portfolios': portfolios})

def upload(request):
    return render(request, 'upload.html')

def file_upload(request):
    port = Portfolio()
    port.title = request.GET['title']
    port.image = request.GET['file']
    # port.description = request.GET['description']
    port.save()
    return render(request, 'upload.html')