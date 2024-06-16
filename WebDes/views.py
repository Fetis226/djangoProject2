from django.shortcuts import render
from .models import main_tovar
# Create your views here.
def index(request):
    return render(request, "index.html")
def katalog(request):
    tovari = main_tovar.objects.all()
    return render(request, "katalog.html", {"tovari":tovari})


