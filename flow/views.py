from django.shortcuts import render
from .models import instagram,Caption
# Create your views here.
def index(request): 
    return render(request, 'index.html')

def insta(request):
    my_image = instagram.all_images()
    return render(request, 'instagram.html', {"my_image":my_image})
