from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from .models import Menu, Booking

class MenuSerializer(ModelSerializer):
    class Meta:
        model = Menu
        fields = ['id','Title', 'Price', 'Inventory']

class BookingSerializer(ModelSerializer):
    class Meta:
        model = Booking
        # fields = ['Name', 'No_of_guests', 'BookingDate']
        fields = "__all__"

class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']