from django.shortcuts import render
from django.http import JsonResponse,HttpResponse,Http404
from .models import Main
from .form import IdeaForm
# Create your views here.


def bet_list(response):
    obj = Main.objects.all()
    data = {}
    status = 200
    try:
       li = [{"Id":i.id ,"Title":i.Title} for i in obj]
       data['response'] = li
    except:
       status = 404
       data['response'] = "Error Fetching"
    return JsonResponse(data,status=status)

def home(response):
    return render(response,"homepage/home.html")

def form(response):
    form = IdeaForm(response.POST or None)
    if(form.is_valid()):
        obj = form.save(commit=False)
        obj.save()
        form = IdeaForm()
    return render(response,"form.html",{"form":form})
    