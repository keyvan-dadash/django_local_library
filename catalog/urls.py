from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

app_name = 'catalog'

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('books/', views.BookListView.as_view(), name='books'),
    path('book/<int:pk>', views.BookDetailViews.as_view(), name="book_detail"),
    path('mybooks/', views.LoanListView.as_view(), name='borrowed-book'),
    path('book/<pk>/renew/', views.renew_book, name='renew_book'),
    path('author/create/', views.AuthorCreate.as_view(), name='author_create'),
    path('author/<pk>/delete/', views.AuthorDelete.as_view(), name='author_create'),
    path('author/<pk>/update/', views.AuthorUpdate.as_view(), name='author_create'),
]
