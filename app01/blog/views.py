from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request,'blog/index/index.html')


def add(request):
    if request.method == 'POST':
        a = request.POST['a']
        b = request.POST['b']
        c = int(a) + int(b)
        return HttpResponse(c)
    else:
        return render(request,'blog/test/add.html')