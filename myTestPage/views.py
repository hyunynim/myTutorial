from django.shortcuts import render

def IndexPage(_request):
    return render(_request, 'myTestPage/index.html')

def UploadInfo(_request):
    name = _request.POST.get('name')
    age = _request.POST.get('age')
    return render(_request, 'myTestPage/index.html')