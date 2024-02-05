from django.shortcuts import render
from .models import Person
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

def Home(request):
    return render(request,"search.html")

@csrf_exempt
def Suggestions(request):
        query = request.GET.get('term', '')
        per = Person.objects.filter(name__icontains=query)[:10]
        results = [x.name for x in per]
        return JsonResponse(results, safe=False)