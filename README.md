# COP5818_Project
Host repository for our final project
Currently working on stage 1
idea is to allow someone to be able to log into our site, and then type a whole dollar amount, like $50 or something. Then generate a special link that is tracked to their account via database. They can then give that link out to someone, and they don't have to log into our site to see the page. On the page they will see a pay now for $50 in this case. And will have a paypal button that uses paypal payments to perform the transaction.
It's an extremely simple webpage, but it covers every single requirement for the assignment, and it's something that I feel is do-able by us within the limited time frame.

## Installs Required:

Setting up super admin
```bash
python manage.py createsuperuser
```

```bash
pip install python-decouple
pip install django-allauth
pip install django-crispy_forms
pip install crispy-bootstrap4
pip install Pillow
```
