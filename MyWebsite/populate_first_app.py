import os
import asyncio
import logging
os.environ.setdefault('DJANGO_SETTINGS_MODULE','MyWebsite.settings')
logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')

import django
django.setup()
import random
from first_app.models import Topic,AccessRecords,Webpage

from faker import Faker
fakegen=Faker()
topics=['Science', 'Social', 'News', 'Search','Games']

def add_topic():
    t=Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t

def populate(N=10):

    for i in range(N):
        try:
            top=add_topic()

            fake_url=fakegen.url()
            fake_date=fakegen.date()
            fake_name=fakegen.company()

            webpg=Webpage.objects.get_or_create(topic=top,url=fake_url,name=fake_name)[0]

            accrec=AccessRecords.objects.get_or_create(name=webpg,date=fake_date)[0]

        except Exception as e:

            print("Exception handled and logged")
            x='{"name":fake_name, "url":fake_url, "exception":str(e)}'
            y=json.loads(x)
            logging.error(fake_name+', '+fake_url+', '+str(e))
            continue

if(__name__=='__main__'):
    n=int(input("Enter number of data to populate using faker: "))
    print('Populating ',n,' data')
    populate(n)
    print("completed")
