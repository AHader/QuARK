# Basic Commands

## Setting Up Your Users

* To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.

* To create an **superuser account**, use this command

    $ python manage.py createsuperuser

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.

## Type checks


Running type checks with mypy:

   $ mypy apps

## Test coverage


To run the tests, check your test coverage, and generate an HTML coverage report:

    $ coverage run -m pytest
    $ coverage html
    $ open htmlcov/index.html

### Running tests with py.test

    $ pytest

# Live reloading and Sass CSS compilation


Moved to `Live reloading and SASS compilation`_.

.. _`Live reloading and SASS compilation`: http://cookiecutter-django.readthedocs.io/en/latest/live-reloading-and-sass-compilation.html



# Celery


This app comes with Celery.

To run a celery worker:

.. code-block:: bash

    cd apps
    celery -A config.celery_app worker -l info

Please note: For Celery's import magic to work, it is important *where* the celery commands are run. If you are in the same folder with *manage.py*, you should be right.




# Email Server


In development, it is often nice to be able to see emails that are being sent from your application. For that reason local SMTP server `MailHog`_ with a web interface is available as docker container.

Container mailhog will start automatically when you will run all docker containers.
Please check `cookiecutter-django Docker documentation`_ for more details how to start all containers.

With MailHog running, to view messages that are sent by your application, open your browser and go to ``http://127.0.0.1:8025``

.. _mailhog: https://github.com/mailhog/MailHog



# Deployment

The following details how to deploy this application.



## Docker


See detailed `cookiecutter-django Docker documentation`_.

.. _`cookiecutter-django Docker documentation`: http://cookiecutter-django.readthedocs.io/en/latest/deployment-with-docker.html



## Docker for Windows

Enable necessary Windows features (PS with admin privilegde):

    Enable-WindowsOptionalFeature -Online -FeatureName containers –All
    Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Hyper-V –All

Also make sure that virtualization is supported by your CPU and enabled in BIOS.

Follow installation guide:
https://docs.docker.com/docker-for-windows/install/


## Windows Subsystem for Linux

Install from Microsoft Store (e.g. Debian)
Add information about how to reach Docker from WSL into your ~/.bashrc:

    echo "export DOCKER_HOST=tcp://localhost:2375" >> ~/.bashrc
    source ~/.bashrc


## Getting everything to run

Checkout:

    git clone https://github.com/Brandl/QuARK.git
  
Switch to directory and start building Docker images:

    cd QuARK
    docker-compose -f local.yml build

Start them up:

    docker-compose -f local.yml up

Connect to your local instance via http://localhost:8000


Stop them via:

    docker-compose -f local.ymp stop