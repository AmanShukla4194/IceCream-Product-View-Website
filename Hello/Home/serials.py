from rest_framework import serializers
from Home.models import LogIns

class serials(serializers.ModelSerializer):
    class Meta:
        model = LogIns
        fields = "__all__" 
        