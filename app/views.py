from django.shortcuts import render
from .tasks import send_emails

# Create your views here.
def send_test_email(request):
    send_emails.delay()
    return render(request,"test.html",{} ) 