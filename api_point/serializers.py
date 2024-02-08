from rest_framework import serializers
from ecomapp.models import *

class Ser(serializers.ModelSerializer):
    class Meta:
        model= Post
        fields=['content','date_posted','author']