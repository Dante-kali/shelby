from django.contrib import admin
from django.urls import path

from .views import home, contact, about, process_contact_form

app_name = 'dog'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path("acercade/", about),
    path('contact/', contact),
    path('process-contact/', process_contact_form, name='process_contact')
]
 