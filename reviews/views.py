from django.shortcuts import render
import requests


def index(request):
    
    return render(request, "base.html")

def search_result(request, searched_book):
    
    return render(request, 'search.html', {'searched_book': searched_book})