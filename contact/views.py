from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

contact = [
    {
        'name': 'Moks',
        'number': 123456,
        'email': 'nbonvpo@snv.com',
        'gender': 'Male',
    },
    {
        'name': 'Jane',
        'number': 12345,
        'email': 'JD@snv.com',
        'gender': 'Female',
    },
]


def home(request):
    context = {
        'contacts': contact
    }
    return render(request, 'contact/home.html', context)


def cover(request):
    return render(request, 'contact/cover.html')
