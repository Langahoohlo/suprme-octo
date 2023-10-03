from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import SMSMessage

@csrf_exempt
def receive_sms(request):
    if request.method == 'POST':
        sender = request.POST.get('senderNumber', '')
        message_text = request.POST.get('messageText', '')

        # You can save the SMS to the database if needed
        sms = SMSMessage(sender=sender, message=message_text)
        sms.save()

        # Handle the SMS data as required
        # For now, let's return a simple response
        return JsonResponse({'status': 'SMS received and processed'})

    return JsonResponse({'error': 'Invalid request'}, status=400)
