# COP5818_Project
This is the primary repository for our final project

The idea is to allow someone to be able to log into our site, and then type a whole dollar amount, like $50 or something. Then generate a special link that is tracked to their account via database. They can then give that link out to someone, and they don't have to log into our site to see the page. On the page they will see a pay now for $50 in this case. And will have a paypal page that will process the payment if the user wishes to complete perform the transaction.

It's an extremely simple site, but it covers every single requirement for the assignment, and it's something that we feel is do-able by us within the limited time frame.

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

[More Info](https://stackoverflow.com/questions/18966564/pip-freeze-vs-pip-list)


### **Important Note 3**

The API key is for currency conversion is left within the repo, this was done on purpose. It's free and limited to 10k / month.
In the real world, the API key would be hooked via an .env file.

In fact, we easily could using the `python-decouple` library ([More Info](https://pypi.org/project/python-decouple/#usage))

For the sake of ease, and clarity of what exactly the code is doing and to avoid any confusion regarding where the API key came from, and adding extra steps to setting up the project, it was left hardcoded in.
