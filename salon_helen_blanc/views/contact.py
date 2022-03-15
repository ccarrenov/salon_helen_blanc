from django.shortcuts import render

def contact(request):
    print('index')
    return render(request, 'contact.html')