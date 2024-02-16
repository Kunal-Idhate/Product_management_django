# Product Managemenet App

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/Kunal-Idhate/Product_management_django.git
$ cd Product_management_django
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ virtualenv2 --no-site-packages env
$ source env/bin/activate
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```
Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv2`.

Once `pip` has finished downloading the dependencies:
```sh
(env)$ cd project
(env)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/`.



## Tests

To run the tests, `cd` into the directory where `manage.py` is:
```sh
(env)$ python manage.py test gc_app
```
## Screenshots

![1](https://github.com/Kunal-Idhate/Product_management_django/assets/104858057/310fb496-ef72-4b92-b5db-233ab3ea32aa)
![2](https://github.com/Kunal-Idhate/Product_management_django/assets/104858057/6638a65e-7fd4-45b0-9723-aa9445ff2cee)
![3](https://github.com/Kunal-Idhate/Product_management_django/assets/104858057/699d5eff-9b9e-4cc4-a785-35d5aeeb17bd)
![edit](https://github.com/Kunal-Idhate/Product_management_django/assets/104858057/f1fc780b-4746-49db-8dd1-980af85cfe3a)
![delete](https://github.com/Kunal-Idhate/Product_management_django/assets/104858057/5e3d29ee-3bb0-42f6-99b3-cfd5e4d55369)
![5](https://github.com/Kunal-Idhate/Product_management_django/assets/104858057/591af661-b757-4525-adda-e06f2153de88)
![4](https://github.com/Kunal-Idhate/Product_management_django/assets/104858057/a971c927-714a-4b0b-97fa-ad9066a8414c)


