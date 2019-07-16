from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('courses', views.CoursesView)
router.register('category', views.CategoryView)
router.register('contacts', views.ContactsView)
router.register('branches', views.BranchesView)

urlpatterns = [
    path('', include(router.urls))
]
