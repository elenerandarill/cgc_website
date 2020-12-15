from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail


def home(request):
    if request.method == "POST":
        sender_name = request.POST['sender-name']
        print(sender_name)
        sender_email = request.POST['sender-email']
        print(sender_email)
        sender_message = request.POST['message']
        print(sender_message)

        # Sending an email.
        send_mail(
            f"Wiadomość od {sender_name}",
            sender_message,
            sender_email,
            ['contact@cg-consulting.pl'],

        )

        return render(request, "landing_page/home.html", {'status': "Success"})
    else:
        return render(request, "landing_page/home.html")
