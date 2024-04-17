from django.urls import path
from . import views as vi

urlpatterns = [
    path('', vi.index_page),
    path('picture/', vi.picture_page)
]