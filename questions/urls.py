from django.urls import path
from .views import QuestionList, CategoryList, check_health

urlpatterns = [
    path('categories/', CategoryList.as_view(), name='category_list'),
    path('list/', QuestionList.as_view(), name='question_list'),
    path('health/', check_health, name='health_check'),
]
