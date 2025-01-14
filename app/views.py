from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework import status


@api_view(['GET'])
def add(request):
    try:
        a = float(request.GET.get('a', 0))
        b = float(request.GET.get('b', 0))
        result = a + b
        return JsonResponse({'operation': 'add', 'result': result})
    except ValueError:
        return JsonResponse({'error': 'Invalid input  for a or b'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def subtract(request):
    try:
        a = float(request.GET.get('a', 0))
        b = float(request.GET.get('b', 0))
        result = a - b
        return JsonResponse({'operation': 'subtract', 'result': result})
    except ValueError:
        return JsonResponse({'error': 'Invalid input for a or b'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def multiply(request):
    try:
        a = float(request.GET.get('a', 0))
        b = float(request.GET.get('b', 0))
        result = a * b
        return JsonResponse({'operation': 'multiply', 'result': result})
    except ValueError:
        return JsonResponse({'error': 'Invalid input for a or b'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def divide(request):
    try:
        a = float(request.GET.get('a', 0))
        b = float(request.GET.get('b', 0))
        if b == 0:
            return JsonResponse({'error': 'Cannot divide by zero'}, status=status.HTTP_400_BAD_REQUEST)
        result = a / b
        return JsonResponse({'operation': 'divide', 'result': result})
    except ValueError:
        return JsonResponse({'error': 'Invalid input for a or b'}, status=status.HTTP_400_BAD_REQUEST)
