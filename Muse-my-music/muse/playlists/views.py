from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'Playlist.html')
def Artists(request):
    return render(request, 'Artists.html')
def Albums(request):
    return render(request, 'Albums.html')