from django.shortcuts import render
from .models import Book, Review
from .utils import average_rating


def book_list(request):
    books = Book.objects.all()
    book_list = []
    for book in books:
        reviews = book.review_set.all()
        if reviews:
            book_rating = average_rating([review.rating for review in reviews])
            num_of_reviews = len(reviews)
        else:
            book_rating = 0
            num_of_reviews = 0
        book_list.append({'book': book, 'rating': book_rating, 'num_of_reviews': num_of_reviews})
    context = {'book_list': book_list}
    return render(request, 'reviews/books_list.html', context)