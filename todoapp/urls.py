from django.urls import path,include
from todoapp import views
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register("vtodos",views.TodoViewSets,basename="vtodos")
router.register("mvtodos",views.TodoModelViewset,basename="mvtodos")
router.register("accounts/signup",views.UserViewSets,basename="usersviewset")

urlpatterns = [
    path("todos", views.TodoCreateView.as_view()),
    path('todos/<int:id>', views.TodoDetail.as_view()),
    path("mtodos", views.TodoMixinList.as_view()),
    path("mtodos/<int:id>", views.TodoMixinDetails.as_view()),
    path("accounts/login",views.SignInView.as_view())
]+router.urls


