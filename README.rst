django-jabber
=============

Send Jabber notifications from Django

Usage
-----

.. code-block:: python

    from django_jabber import send_message

    recipients = ['user1', 'user2', ] # without @domain.com part
    send_message(u'Hello there', recipients)

    # You can also pass this job to your Celery instance
    send_message.delay(u'Async message', recipients)


Installation
------------

Install the package via Pypi: `pip install django-jabber`

Add some lines to your settings.py:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'django_jabber',
        ...
    )

    JABBER = {
        'HOST': 'jabber.domain.com',
        'USER': 'robot@domain.com',
        'PASSWORD': 'someStr0ngOne!1',
        'USE_TLS': True,
        'USE_SSL': False,
    }

Requirements
^^^^^^^^^^^^

- sleekxmpp
- celery
- django

Compatibility
-------------

We use this package on Python 2.7 and Django 1.7+.

License
-------

GPLv3

Authors
-------

`django-jabber` was written by `Alex Morozov <inductor2000@mail.ru>`_.
