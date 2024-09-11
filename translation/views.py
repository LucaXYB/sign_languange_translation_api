from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
@csrf_exempt
def translate_text(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            input_text = data.get('text')

            # Check if the text input is provided
            if not input_text:
                return JsonResponse({"error": "No text provided"}, status=400)
            
            # Simulate translation process
            translated_text = f"{input_text} (translated)"

            return JsonResponse({
                "input_text": input_text,
                "translated_text": translated_text,
                "message": "Translation successful"
            }, status=200)
        
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)
    
    return JsonResponse({"error": "Invalid method"}, status=405)
