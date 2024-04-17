from django.urls import path
from . import views as vi

urlpatterns = [
    path('', vi.index_page),
    path('about/', vi.about_page),
    path('news/', vi.news_page)
]
