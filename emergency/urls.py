"""
URL configuration for EMERGENCE_RESPONSE_SYSTEM project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import Health_FacilitiesViewSet
from emergency import views

router = DefaultRouter()
router.register(
    prefix = 'api/v1/healthfacilities',
    viewset = Health_FacilitiesViewSet,
    basename = "healthfacilities"
)
# from emergency.views import index,report_emergency

urlpatterns = router.urls  

urlpatterns = [
    path("",views.index,name='index'),
    path("accounts/", include("django.contrib.auth.urls")),
    path('report_emergency/',views.report_emergency,name='report_emergency'),
    path('emergency_list/',views.emergency_list,name = 'emergency_list'),
    path('',include(router.urls),name='health_api'),
    path('get_closest_health_facility/',views.closest_health_facility),
    path('save-location/',views.save_location,name='update_location')
    # path("signup/", authView, name='authView')
] #static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

