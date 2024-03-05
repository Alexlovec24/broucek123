from django.shortcuts import render
from django.http import HttpResponse
import random
from lorem_text import lorem

def blog_list(request):  # Add the 'request' parameter here
    random_number = random.randint(a = 1, b = 300)
    return render(request, 'blog/list.html', {'random_number': random_number})  # Use 'request' in render and fix context dictionary
