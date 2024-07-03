from django.urls import path
from .views import *

urlpatterns = [
    path('',all_chai),
    path('<int:chai_id>/',chai_detail,name='chai_detail'),
]