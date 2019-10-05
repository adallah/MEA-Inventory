from rest_framework import serializers
from .models import portal

class portalSerializer(serializers.ModelSerializer):
    class Meta:
        model = portal
        fields = ('id',
                  # 'user',
                  'name', 'product','duration','did','cid','country')