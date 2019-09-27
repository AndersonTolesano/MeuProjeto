from django.urls import path
from .views import persons_list
from .views import persons_new
from .views import persons_update


urlpatterns = [
    path('update/<int:id>/', persons_update, name='person_update'),
    path('new/', persons_new, name='person_new'),
    path('list/', persons_list, name='person_list'),
]
