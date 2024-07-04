from django.urls import path
from .views import *

urlpatterns = [
    path('',all_chai),
    path('<int:chai_id>/',chai_detail,name='chai_detail'),
    path('chai_stores/',chai_store_view,name='chai_stores')
]