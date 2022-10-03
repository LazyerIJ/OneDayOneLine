from django.shortcuts import render

def login(request):
    if request.method == 'POST':
        pass
    else:
        return render(request, 'login.html')