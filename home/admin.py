from django.contrib import admin
from home.models import Product,User,Recommendation
# Register your models here.

admin.site.register([Product,User,Recommendation])