from django.urls import path
from . import views

app_name = 'catalog'

urlpatterns = [
    path('', views.index, name='index'),
    path('create_book/', views.BookCreate.as_view(), name='create_book'),
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book_detail'),
]
