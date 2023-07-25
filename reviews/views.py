from django.shortcuts import render
import requests


def index(request):
    return render(request, "base.html")


def search_result(request, book_to_search):
    return render(request, 'search.html', {'searched_book': book_to_search})