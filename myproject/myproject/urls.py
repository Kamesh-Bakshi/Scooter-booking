"""myproject URL Configuration

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
from rideapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('scooters/', views.scooterList.as_view()),
]


    #path('scooters?radius=20&lat=20.3&long=36.3',views.NearByScooter.as_view())
    #path('book?uniqueid=20&source_address=(lat,long)&destination_address=(lat,long)',views.BookScooter.as_view())
    # a URL which will accept request like "https//sitename.com/scooters?radius=10&lat=23.32&long=63.32"

    #a POST URL type also which will be responsible for making reservation/BOOKING: It will contain
    # Unique_ID of the scooter to be booked.

