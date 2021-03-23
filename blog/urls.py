from django.urls import path  # do tohoto noveho suboru pridanie tychto 2-och riadkov
from . import views           # path je Djago funkia a views je z nasho blog-u

urlpatterns = [                                   #  priradenie view s nazvom post_list k root URL
    path('', views.post_list, name='post_list'),  #  views.post_list je to spravne miesto kam ist
]                                                 #  pri vstupe na stranku 127.0.0.1:8000
