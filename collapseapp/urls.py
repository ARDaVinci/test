from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^collapse' , views.TestPage.as_view() , name= 'test'),
]