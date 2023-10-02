from django.urls import path                    # pridane az dole
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
]