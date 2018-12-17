from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def obliczenia(request, operation, a, b):
    a, b = int(a), int(b)
    if operation=='add':
        wynik = a + b
    if operation=='div':
        if b == 0:
            wynik = 'Nie dziel przez zero'
        else:
            wynik = a/b

    m = Math(operacja=operation, a=a, b=b, wynik=wynik)
    m.save()

    print(m.a, m.b, m.operacja)


    return HttpResponse(wynik)