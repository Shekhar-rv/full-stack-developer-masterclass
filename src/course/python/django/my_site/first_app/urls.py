from django.urls import path
from . import views


# first_app/
urlpatterns = [
    path('<int:num_page>', views.num_page_view),
    path('<str:topic>/', views.news_view),
    path('<int:num1>/<int:num2>/', views.add_view),
]