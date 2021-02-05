from typing import Tuple, List

from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail

# Where emails from form will be send to.
from django.urls import reverse
from django.utils.translation import activate

from .ClientLogoSmallView import ClientLogoSmallView
from .models import TeamMember, TeamMemberTrans, ClientLogo, ServicesItem, ServicesItemTrans, WorkflowItem, WorkflowItemTrans, CommonText, CommonTextTrans
from .TeamMemberView import TeamMemberView
from .ServicesItemView import ServicesItemView
from .WorkflowItemView import WorkflowItemView
from .CommonTextView import CommonTextView

to_email = 'paulina@cg-consulting.pl'


def send_email(the_request):
    sender_name = the_request['sender-name']
    sender_email = the_request['sender-email']
    sender_message = the_request['sender-message']

    # Sending an email.
    send_mail(
        subject=f"Formularz kontaktowy CGC: od {sender_name}.",
        message=f"Sender name: {sender_name},\nSender email: {sender_email},\n\nMessage: {sender_message} ",
        from_email=to_email,
        recipient_list=[to_email, 'cgajda@cg-consulting.pl'],
    )


def home(request):
    current_language = request.LANGUAGE_CODE
    context = {"lang_code": current_language}

    # Pobierz aktualny język użytkownika
    if current_language == "pl":
        context['lang_next'] = "EN"
        activate("en")
        context['lang_href'] = reverse("home")
        activate("pl")
    else:
        context['lang_next'] = "PL"
        activate("pl")
        context['lang_href'] = reverse("home")
        activate("en")

    # Append data into 'context' dictionary.

    # ---Common text---
    texts_items = CommonText.objects.all()
    # list of objects in current lang.
    texts_list = CommonTextView.collect_lang_text_translations(current_language, texts_items)
    for t in texts_list:
        # print(context)
        # print(f"*******{t.id},{t.lang}, {t.translation}*******")
        context[t.id] = t

    # ---Services items---
    services_items = ServicesItem.objects.all()
    items_list = ServicesItemView.collect_lang_services_items(current_language, services_items)
    context['services_items'] = items_list

    # ---Workflow 'arrow' items---
    workflow_items = WorkflowItem.objects.all()
    workflow_list = WorkflowItemView.collect_lang_workflow_items(current_language, workflow_items)
    context['workflow_item01'] = workflow_list[0]
    context['workflow_item02'] = workflow_list[1]
    context['workflow_item03'] = workflow_list[2]

    # ---Team members---
    members = TeamMember.objects.all()
    # Collect only current language translations for each member.
    members_list = TeamMemberView.collect_lang_members(current_language, members)
    context['team_members'] = members_list

    # ---Logos---
    logos = ClientLogo.objects.all()
    context['clients_logos'] = logos

    # ---Logos for small screens--
    logos_small = []
    for i in range(0, len(logos), 2):
        logo2 = logos[i + 1] if i + 1 < len(logos) else None
        logos_small.append(ClientLogoSmallView(logos[i], logo2))
    context['clients_logos_small'] = logos_small


    if request.method == "POST":
        send_email(request.POST)

    return render(request, "landing_page/home.html", context=context)
