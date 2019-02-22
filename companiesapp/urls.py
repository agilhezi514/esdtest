from django.urls import path, include
from .views import Company_view

urlpatterns = [
    path("", Company_view.as_view(), name = "hompage" )

]