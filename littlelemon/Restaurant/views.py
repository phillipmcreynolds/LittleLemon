from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import permission_classes
from rest_framework import viewsets
from django.contrib.auth.models import User
from .models import Menu, Booking
from .serializers import MenuSerializer, BookingSerializer, UserSerializer

# Open views.py. Does it contain the code for viewset classes of for the Menu 
class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all().order_by('id')
    serializer_class = MenuSerializer
# and Booking models?
class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all().order_by('id')
    serializer_class = BookingSerializer

class MenuItemsView(ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class UserView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class SingleMenuItemView(RetrieveUpdateDestroyAPIView, CreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
            return self.create(request, *args, **kwargs)
        
    def put(self, request, *args, **kwargs):
            return self.update(request, *args, **kwargs)
        
    def patch(self, request, *args, **kwargs):
            return self.update(request, *args, **kwargs)
    def delete(self, request, *args, **kwargs):
            return self.destroy(request, *args, **kwargs)
        
@permission_classes([IsAuthenticated])
class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

def authenticated(Request):
    permission_classes = [IsAuthenticated]
    return True

def home(request):
    return render(request, 'index.html')