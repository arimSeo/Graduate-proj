from django.shortcuts import render
# from .models import 

def index(request):
    _context = {'check':False}
    if request.session.get('access_token'):
        _context['check'] = True
    return render(request, 'index.html', _context)

def gamseong(request):
    return render(request,'gamseong.html')

def main(request):
    return render(request,'main.html')