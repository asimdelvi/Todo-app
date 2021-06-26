from django.urls import path
from .views import index, update_task, delete_task


urlpatterns = [
  path('', index, name="homepage"),
  path('updatetask/<int:pk>/', update_task, name="update_task"),
  path("deletetask/<int:pk>/", delete_task, name="delete")
]
