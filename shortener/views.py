from rest_framework import generics, status
from rest_framework.response import Response
from .models import URL
from .serializers import URLSerializer
import string, random

class URLShortenerView(generics.CreateAPIView):
    queryset = URL.objects.all()
    serializer_class = URLSerializer

    def create(self, request, *args, **kwargs):
        original_url = request.data.get('original_url')
        shortened_url = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
        
        url, created = URL.objects.get_or_create(original_url=original_url, defaults={'shortened_url': shortened_url})
        
        return Response(URLSerializer(url).data, status=status.HTTP_201_CREATED)
