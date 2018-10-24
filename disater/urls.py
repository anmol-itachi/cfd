from django.urls import path

from . import views

urlpatterns = [

    path('' , views.index , name='index'),
    #disater/person_status
    path('person_status/', views.person_status , name='person_status'),

    #disater/person_status
    path('person_status/<int:person_id>', views.details , name='details'),

]
