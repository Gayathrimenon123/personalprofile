from django.shortcuts import render
from . models import prof
# Create your views here.
def index(request):
    profs = prof.objects.all()
    return render(request, 'index.html', {'prof': profs})