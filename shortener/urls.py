from django.urls import path
from shortener import views

urlpatterns = [
    path('shorten/', views.URLShortenerView.as_view(), name='shorten-url'),
    path('original/<str:shortened_url>/', views.OriginalURLView.as_view(), name='original-url'),
]
