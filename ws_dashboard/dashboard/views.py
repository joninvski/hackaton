from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
 
from dashboard.models import *

import json
import itertools

def index(requesti):
    return HttpResponse("WalletSaver Hackathon Dashboard Project")

def company(request, company_id):
    try:
        response_body = {}
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

        response_body['calls'] = list()
        response_body['calls'].append({'label': 'Incoming Calls',
                        'value': total_calls_incoming})       
        response_body['calls'].append({'label': 'Outgoing Calls',
                        'value': total_calls_outgoing}) 
        
        response_body['messages'] = list()
        response_body['messages'].append({'label': 'Incoming Messages',
                        'value': total_messages_incoming})       
        response_body['messages'].append({'label': 'Outgoing Messages',
                        'value': total_messages_outgoing}) 
 
        response_body['data'] = list()
        response_body['data'].append({'label': 'Incoming Data',
                        'value': total_data_incoming})       
        response_body['data'].append({'label': 'Outgoing Data',
                        'value': total_data_outgoing}) 
        golden_response = {'total_calls_incoming':total_calls_incoming,
                            'total_calls_outgoingg':total_calls_outgoing,
                            'total_messages_incoming':total_messages_incoming,
                            'total_messages_outgoing':total_messages_outgoing,
                            'total_data_incoming':total_data_incoming,
                            'total_data_outgoing':total_data_outgoing}

        response = HttpResponse(json.dumps(golden_response, sort_keys=True), 
                               content_type="application/json")
        return response
    except Company.DoesNotExist:
        return HttpResponseNotFound()

def company_calls(request, company_id, call_type, days):
    try:
        response_body = {}
        c = Company.objects.get(pk=company_id)
        employees = Employee.objects.filter(company=c)
        last_days = datetime.datetime.today() - datetime.timedelta(days)
        calls = Call.objects.filter(owner__in=employees, call_type=call_type)
        response = HttpResponse(json.dumps(response_body, sort_keys=True))
        return
    except Company.DoesNotExist:
        return HttpResponseNotFound()

