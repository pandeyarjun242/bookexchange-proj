from django.urls import path
from . import views

urlpatterns = [
    path('add', views.add, name = "add"),
    path('<int:book_id>', views.detail, name = "detail"),
    path('<int:book_id>/bid', views.bid, name = "bid")
]
