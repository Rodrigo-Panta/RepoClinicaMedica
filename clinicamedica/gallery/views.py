from django.shortcuts import render, redirect

# Create your views here.

def gallery_view(request):
    return render(request, 'gallery/gallery.html')