from django.shortcuts import render
from .models import produto

# Create your views here.
def index(request):
    produtos = produto.objects.all()
    return render(request, 'index.html', {'produtos':produtos})