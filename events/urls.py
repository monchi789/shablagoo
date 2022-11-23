from django.urls import path
from . import views
from rest_framework import routers
from .api import *

router = routers.DefaultRouter()

router.register('api/roles', RoleViewSet, 'roles')
router.register('api/users', UserViewSet, 'users')
router.register('api/eventPlanners', EventPlannerViewSet, 'eventPlanners')
router.register('api/categorys', CategoryViewSet, 'categorys')
router.register('api/events', EventViewSet, 'events')

urlpatterns = router.urls