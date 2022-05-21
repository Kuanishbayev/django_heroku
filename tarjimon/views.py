from django.shortcuts import render
from django.http import HttpResponse
from .models import Lugat


def index(request):
    soz = request.GET.get('q', '')
    natija = Lugat.objects.filter(inglizcha=soz).all()
    return render(request, 'index.html', {'q': soz, 'natija': natija})