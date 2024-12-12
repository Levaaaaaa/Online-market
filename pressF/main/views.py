from django.shortcuts import render

from goods.models import Categories
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
def index(request):
    categories = Categories.objects.all()
    context = {
        'categories' : categories
    }
    return render(request, "main/index.html", context)

def about(request):
    return render(request, 'main/about.html')

def index_rest(request):
    catalog = [obj.__dict__() for obj in Categories.objects.all()]
    json_renderer = renderers.JSONRenderer()
    return json_renderer.render(catalog)

class ExampleAPI(APIView):
    def get(self, request):
        return Response({"message": "Hello from Django!"})
