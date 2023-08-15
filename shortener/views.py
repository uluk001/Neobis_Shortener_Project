from rest_framework import generics, status
from rest_framework.response import Response
from .models import URL
from .serializers import URLSerializer
import string, random
from urllib.parse import urlparse


class URLShortenerView(generics.CreateAPIView):
    queryset = URL.objects.all()
    serializer_class = URLSerializer

    def create(self, request, *args, **kwargs):
        original_url = request.data.get('original_url')
        scheme = urlparse(original_url).scheme
        
        shortened_url = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
        
        url, created = URL.objects.get_or_create(original_url=original_url, defaults={'shortened_url': shortened_url})
        
        if scheme:
            url.shortened_url = f"{scheme}://{shortened_url}"
        
        return Response(URLSerializer(url).data, status=status.HTTP_201_CREATED)


class OriginalURLView(generics.RetrieveAPIView):
    queryset = URL.objects.all()
    serializer_class = URLSerializer
    lookup_field = 'shortened_url'

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)