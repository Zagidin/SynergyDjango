from django.urls import path
from . import views as vw


urlpatterns = [
    path('', vw.index_page),
    path('news/', vw.news_page)
]
