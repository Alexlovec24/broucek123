from django.shortcuts import render
from django.http import HttpResponse
import random
from lorem_text import lorem

def blog_list(request):  # Add the 'request' parameter here
    random_text = lorem.words(10)
    return render(request, 'blog/list.html', {'random_text': random_text})  # Use 'request' in render and fix context dictionary
