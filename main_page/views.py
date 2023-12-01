from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import *

# def index(request):
#     return HttpResponse("hello !")

def weblist_view(request):
    weblists = Weblist.objects.all() # Weblist 테이블의 모든 객체 불러와서 weblists에 저장
    return render(request, 'main_page/index.html', {"weblists" : weblists})

def save_word(request):
    if request.method == 'POST':
        word = request.POST.get('item_word')
        
        SearchKeywords.objects.create(keyword_name=word)
        
        return redirect('weblist')