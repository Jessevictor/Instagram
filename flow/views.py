from django.http  import HttpResponse,Http404
from django.shortcuts import render, redirect
from .forms import NewPostForm
from .models import Image

def home(request):
    all_posts = Image.all_images()
    print(all_posts)
    return render(request, 'index.html', {'all_posts':all_posts})

def new_post(request):
    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)

        if form.is_valid():
            image = form.save(commit = False)
            image.image_poster = request.user
            image.save()
        return redirect('index')

    else:
        form = NewPostForm()
    return render(request, 'post_image.html', {'form': form})

def profile(request):
    return render(request, 'profile.html')
