from django.contrib import admin
from django.urls import path
from home import views


urlpatterns = [
    path ("" , views.index, name = 'home'),
    # path('', include ('home.urls'))
    path ("about" , views.about, name = 'about'),
    path ("services" , views.services, name = 'services'),
    path ("contact" , views.contact, name = 'contact')
]
# we have copied the things from the project's url.
# here it means that when a client ask for the contact then it will access the views under the contact function and name is equal to contact