from django.shortcuts import render

def picture(request):
    print('index')
    return render(request, 'picture.html')