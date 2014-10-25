from django.core.management.base import BaseCommand, CommandError
from dashboard.models import *

from faker import Factory

import random

class Command(BaseCommand):

    def handle(self, *args, **options):

        def create_company(name):
            faker = Factory.create()
            c = Company(name=name, country="IT")
            c.save()
            for e_i in range(2,10):
                e = Employee(name=faker.name(), role=1, company=c, 
                            phone_number=faker.phone_number())
                e.save()
    
        def fill_company(name):
            faker = Factory.create()
            c = Company.objects.get(name=name)
            emps = Employee.objects.filter(company=c)

            # Generate Outgoing Call/Msg
            for e in emps:
                # Generate Outoing Call/MSG
                for _ in range(20, random.randint(21,40)):
                    c = Call(owner=e, 
                            caller=e.phone_number, 
                            receiver=faker.phone_number(),
                            length = random.randint(20,360),
                            start_time = faker.date_time_this_year(),
                            call_type = 2)
                    c.save()
                for _ in range(10, random.randint(11,30)):
                    m = Message(owner=e,
                                sender=e.phone_number,
                                receiver=faker.phone_number(),
                                sent_time = faker.date_time_this_year(),
                                message_type = 2)
                    m.save()
                for _ in range(50, random.randint(51,100)):
                    d = Data(owner=e,
                                volume = random.randint(1024,1024*1024),
                                start_time = faker.date_time_this_year(),
                                data_type = 2)
                    d.save()
                
                # Generate Incoming Call/Msg/Data
                for _ in range(20, random.randint(21,40)):
                    c = Call(owner=e, 
                            caller=faker.phone_number(), 
                            receiver=e.phone_number,
                            length = random.randint(20,360),
                            start_time = faker.date_time_this_year(),
                            call_type = 1)
                    c.save()
                for _ in range(10, random.randint(11,30)):
                    m = Message(owner=e,
                                sender=faker.phone_number(),
                                receiver=e.phone_number,
                                sent_time = faker.date_time_this_year(),
                                message_type = 1)
                    m.save()
                for _ in range(50, random.randint(51,100)):
                    d = Data(owner=e,
                                volume = random.randint(1024,1024*1024),
                                start_time = faker.date_time_this_year(),
                                data_type = 1)
                    d.save()
                
        for c in range(5):
            faker = Factory.create()
            company_name = faker.company()
            create_company(name=company_name)
            fill_company(name=company_name)

