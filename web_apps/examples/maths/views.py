from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

from .models import Maths

def obliczenia(request, operation, a, b):
    a, b = int(a), int(b)
    if operation=='dodawanie':
        wynik = a + b
    if operation == "odejmowanie":
        wynik = a-b
    if operation == "mnożenie":
        wynik = a*b
    if operation=='dzielenie':
        if b == 0:
            wynik = 'Nie dziel przez zero'
        else:
            wynik = a/b

    m = Maths(operacja=operation, a=a, b=b, wynik=wynik)
    m.save()

    print(m.a, m.b, m.operacja)


    return HttpResponse(wynik)