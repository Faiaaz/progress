from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    my_dict = {'insert_me': 'yoyo bro!'}
    return render(request, 'progress_report/index.html', context=my_dict)
