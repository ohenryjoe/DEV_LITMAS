import os

import fake as fake

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "litmas.settings")

import django

django.setup()

from faker import factory, Faker


d = dict()
d['first_name_and_gender'] = first_name_and_gender
d['last_name'] = lambda: {'last_name': fake.last_name()}
d['personal_email'] = lambda: {'email': fake.email()}
d['ssn'] = lambda: {'ssn': fake.ssn()}
d['birth_and_start_date'] = birth_and_start_date
d['title_office_org_salary_bonus'] = title_office_org_salary_bonus
d['accrued_holidays'] = lambda: {'accrued_holiday': random.randint(0, 20)}


for _ in range(numRows):
    deep_list = [list(d[k]().values()) for k in d.keys()]
    row = [item for sublist in deep_list for item in sublist]
    print(row)
