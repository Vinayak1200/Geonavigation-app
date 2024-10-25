from rest_framework.serializers import ModelSerializer
from .models import Reviews

class ReviewsSerializer(ModelSerializer):
    class Meta:
        model = Reviews
        fields = ['body']
    

