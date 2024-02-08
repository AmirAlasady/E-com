from django.shortcuts import render
from .serializers import Ser
from ecomapp.models import *
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

# Create your views here.
class BookingView(ListCreateAPIView):
    model = Post
    queryset = model.objects.all()
    serializer_class = Ser

    def get(self, request):
        return 
