from django.http import JsonResponse
from rest_framework.decorators import api_view
from .serializers import CalculationSerializer
from .models import Calculation

@api_view(['GET'])
def add(request):
    a = float(request.GET.get('a', 0))
    b = float(request.GET.get('b', 0))
    result = a + b
    
    # Serialize and save the data
    serializer = CalculationSerializer(data={'first_value': a, 'second_value': b, 'result': result})
    if serializer.is_valid():
        serializer.save()  # Save to the database
        return JsonResponse({'operation': 'add', 'result': result})
    return JsonResponse(serializer.errors, status=400)

@api_view(['GET'])
def subtract(request):
    a = float(request.GET.get('a', 0))
    b = float(request.GET.get('b', 0))
    result = a - b
    
    # Serialize and save the data
    serializer = CalculationSerializer(data={'first_value': a, 'second_value': b, 'result': result})
    if serializer.is_valid():
        serializer.save()  # Save to the database
        return JsonResponse({'operation': 'subtract', 'result': result})
    return JsonResponse(serializer.errors, status=400)

@api_view(['GET'])
def multiply(request):
    a = float(request.GET.get('a', 0))
    b = float(request.GET.get('b', 0))
    result = a * b
    
    # Serialize and save the data
    serializer = CalculationSerializer(data={'first_value': a, 'second_value': b, 'result': result})
    if serializer.is_valid():
        serializer.save()  # Save to the database
        return JsonResponse({'operation': 'multiply', 'result': result})
    return JsonResponse(serializer.errors, status=400)

@api_view(['GET'])
def divide(request):
    a = float(request.GET.get('a', 0))
    b = float(request.GET.get('b', 1))  # Default to 1 to avoid division by zero
    result = a / b if b != 0 else None  # Handle division by zero
    
    # Serialize and save the data
    serializer = CalculationSerializer(data={'first_value': a, 'second_value': b, 'result': result})
    if serializer.is_valid():
        serializer.save()  # Save to the database
        return JsonResponse({'operation': 'divide', 'result': result})
    return JsonResponse(serializer.errors, status=400)
