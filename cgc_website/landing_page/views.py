from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail

# Where emails from form will be send to.
to_email = 'contact@cg-consulting.pl'


def send_email(the_request):
    sender_name = the_request['sender-name']
    sender_email = the_request['sender-email']
    sender_message = the_request['message']

    # Sending an email.
    send_mail(
        f"Wiadomość od {sender_name}",
        sender_message,
        sender_email,
        [to_email],
    )


def home(request):
    if request.method == "POST":
        send_email(request.POST)
        return render(request, "landing_page/home.html", {'status': "Success"})
    else:
        return render(request, "landing_page/home.html")


# English version.
def en_home(request):
    if request.method == "POST":
        send_email(request.POST)
        return render(request, "landing_page/en/home.html", {})
    else:
        return render(request, "landing_page/en/home.html")
