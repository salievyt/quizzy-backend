from rest_framework import generics
from .models import Question, Category
from .serializers import QuestionSerializer, CategorySerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class QuestionList(generics.ListAPIView):
    serializer_class = QuestionSerializer

    def get_queryset(self):
        queryset = Question.objects.all()
        category_id = self.request.query_params.get('category_id')
        if category_id is not None:
            queryset = queryset.filter(category_id=category_id)
        return queryset

@api_view(['GET'])
def check_health(request):
    return Response({"status": "ok"})
