from django.urls import path
from . import views

app_name = 'catalog'

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('books/', views.BookListView.as_view(), name='books')
]
