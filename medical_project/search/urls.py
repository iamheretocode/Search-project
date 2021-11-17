from django.urls import path
from . import views

app_name = 'search'

urlpatterns = [
    path('',views.HomePage.as_view(), name="home"), 
    path('details',views.DetailsPage.as_view(), name="details"), 
    path('result',views.search_med,name="result"),

]

