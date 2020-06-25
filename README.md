# assignment
Creation of Customer and policy using django rest framework

Steps:
1- Clone repository
2- Create virtualenv
3- pip install -r requirements
4- python manage.py migrate
5- python manage.py runserver

Create Customer Request
-----------------------------------
POST /api/v1/create_customer/
    {
        "id":1,
        "first_name":"XXX",
        "last_name":"YYY",
        "dob":"Y-m-d"
    }

Response
    [{
        "id":1,
        "first_name":"Ans",
        "last_name":"Bilal",
        "dob":"1989-02-19"
    }]


Create Policy Request
-----------------------------------
POST /api/v1/create_policy/
    {
        "type":"text",
        "premium":200000,
        "cover":200,
        "customer":customer_id
    }

Response
    [{
        "type":"personal",
        "premium":200000,
        "cover":200,
        "customer":1
    }]