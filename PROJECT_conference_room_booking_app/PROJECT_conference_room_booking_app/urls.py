"""PROJECT_conference_room_booking_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from APP_conference_room_booking_app import views as booking_room

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', booking_room.StartPageView.as_view(), name='start_page'),
    path('room/new/', booking_room.AddNewRoomView.as_view(), name='add_room'),
    path('rooms/', booking_room.ListOfRoomsView.as_view(), name='list_of_rooms'),
    path('room/<int:id_room>/', booking_room.DetailsRoomView.as_view(), name='details_room'),
    path('room/modify/<int:id_room>/', booking_room.ModifyRoomView.as_view(), name='modify_room'),
    path('room/delete/<int:id_room>/', booking_room.DeleteRoomView.as_view(), name='delete_room'),
    path('room/reserve/<int:id_room>/', booking_room.ReserveRoomView.as_view(), name='reserve_room'),
    path('search/', booking_room.SearchRoomView.as_view(), name='search_room'),
]
