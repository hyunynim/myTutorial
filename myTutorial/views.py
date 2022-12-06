from django.shortcuts import render

def IndexPage(_request):
    return render(_request, 'index.html')