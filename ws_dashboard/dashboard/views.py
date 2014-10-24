from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
 
from dashboard.models import *

import json

def index(requesti):
    return HttpResponse("WalletSaver Hackathon Dashboard Project")

def company(request, company_id):
    try:
        response = {}
        c = Company.objects.get(pk=company_id)
        employees = Employee.objects.filter(company=c)
        calls = Call.objects.filter(owner__in=employees)
        messages = Message.objects.filter(owner__in=employees)
        data = Data.objects.filter(owner__in=employees)

        total_calls_incoming = sum([c.length for c in 
            calls if c.call_type == 1])
        total_calls_outgoing = sum([c.length for c in 
            calls if c.call_type == 2])
        
        total_messages_incoming = sum([1 for m in 
            messages if m.message_type == 1])
        total_messages_outgoing = sum([1 for m in 
            messages if m.message_type == 2])

        total_data_incoming =  sum([d.volume for d in 
            data if d.data_type == 1])
        total_data_outgoing = sum([d.volume for d in 
            data if d.data_type == 2])

        response['total_calls_incoming'] = total_calls_incoming 
        response['total_calls_outgoing'] = total_calls_outgoing

        response['total_messages_incoming'] = total_messages_incoming
        response['total_messages_outgoing'] = total_messages_outgoing
       
        response['total_data_incoming'] = total_data_incoming
        response['total_data_outgoing'] = total_data_outgoing
         
        return HttpResponse(json.dumps(response))
    except Company.DoesNotExist:
        return HttpResponseNotFound()

