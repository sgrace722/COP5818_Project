# COP5818_Project
Host repository for our final project

The idea is to allow someone to be able to log into our site, and then type a whole dollar amount, like $50 or something. Then generate a special link that is tracked to their account via database. They can then give that link out to someone, and they don't have to log into our site to see the page. On the page they will see a pay now for $50 in this case. And will have a paypal button that uses paypal payments to perform the transaction.

It's an extremely simple webpage, but it covers every single requirement for the assignment, and it's something that we feel is do-able by us within the limited time frame.

## Installs Required:

### Super User
Setting up super admin
```bash
python manage.py createsuperuser
```

### Libraries
```bash
pip install python-decouple
pip install django-allauth
pip install django-crispy_forms
pip install crispy-bootstrap4
```

## Important Notes:

Below are some important notes to bear in mind...

### **Important Note 1**

* Homepage is accessible via: [http://localhost:8000](http://localhost:8000)

This is due to OAuth return URL reasons, 127.0.0.1 cannot be used for that purpose.

### **Important Note 2**

* The requirements.txt contains a list of self installed pip packages, most of them are just sub-libraries of the primary libraries specified as required for install. They're left as a part of the repo as a failsafe in case a library install was missed during development.

Updating the requirements file can be done via the command done within the root of the project:
```bash
pip freeze > requirements.txt
```

Source: [More Info](https://stackoverflow.com/questions/18966564/pip-freeze-vs-pip-list)