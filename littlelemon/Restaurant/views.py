from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from django.contrib.auth.models import User
from .models import Menu, Booking
from .serializers import MenuSerializer, BookingSerializer, UserSerializer

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
        if IsAuthenticated():
            return self.create(request, *args, **kwargs)
        else:
            return Response({"message": "unauthorized"}, status.HTTP_403_FORBIDDEN)
    def put(self, request, *args, **kwargs):
        if IsAuthenticated():
            return self.update(request, *args, **kwargs)
        else:
            return Response({"message": "unauthorized"}, status.HTTP_403_FORBIDDEN)
        
    def patch(self, request, *args, **kwargs):
        if IsAuthenticated():
            return self.update(request, *args, **kwargs)
        else:
            return Response({"message": "unauthorized"}, status.HTTP_403_FORBIDDEN)
        
    def delete(self, request, *args, **kwargs):
        if IsAuthenticated():
            return self.destroy(request, *args, **kwargs)
        else:
            return Response({"message": "DELETE undefined for lists, but it's fine :)"}, status.HTTP_200_OK)

@permission_classes([IsAuthenticated])
class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

def authenticated(Request):
    permission_classes = [IsAuthenticated]
    return True