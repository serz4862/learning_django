from django.contrib import admin
from django.urls import path
from home import views


urlpatterns = [
    path ("" , views.index, name = 'home'),
    # path('', include ('home.urls'))
    path ("about" , views.about, name = 'about'),
    path ("services" , views.services, name = 'services'),
    path ("contact" , views.contact, name = 'contact'),
    path ("Saurav" , views.Saurav, name = 'Saurav')
]
# we have copied the things from the project's url.
# here it means that when a client ask for the contact then it will access the views under the contact function and name is equal to contact
"""
this is called the url dispatcher because we have received the request and then it is passed by referring 
here we have taken the input as Saurav then it will match with them and if it match 
then it will move to views and there is a function Saurav which will be executed

"""