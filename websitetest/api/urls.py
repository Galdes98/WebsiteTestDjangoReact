#from django.urls import path
#from .views import main 

#urlpatterns = [
#    path('', main)
#]

from django.urls import path
from .views import RoomView

urlpatterns = [
    path('room', RoomView.as_view()),
]

