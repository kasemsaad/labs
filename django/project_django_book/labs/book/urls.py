from django.urls  import path
from .views import *

urlpatterns = [
    path('show/',listbook,name='listbook'),
    path('add/',book_add,name='book_add'),
    path('update/<str:title>/',book_update,name='book_update'),
    path('details/<int:id>',book_details,name='book_details'),
    path('Delete/<int:id>/',book_delete,name='book_delete'),


]   