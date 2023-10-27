from django.shortcuts import render
from django.db import transaction
from django.http import HttpResponse,HttpRequest
from django.contrib.contenttypes.models import ContentType
from store.models import Product, OrderItem, Order, Customer, Collection
from tags.models import TaggedItem, TaggedItemManager



def say_hello(request):

    #####################################
    # #### Custome Manager
    # queryset = TaggedItem.objects.get_tags_for(Product, 1)

    #####################################
    # ### Database Query Caching
    # queryset = Product.objects.all()
    # queryset[0] 
    # list(queryset)

    #####################################
    # ### Inserting record in the database

    ##### Approach - 1: One line Shortcut to insert data, it uses keyword argument
    # Collection.objects.create(title= 'Video Games', featured_product_id=1)
    
    ##### Approach - 2: Traditional way to insert data 
    # collection = Collection()
    # collection.title = 'VR Box'
    # collection.featured_product = Product(pk=2)
    # collection.save()
    # result = collection.title

    #####################################
    # ### Updating record in the database

    ##### Approach - 1: One line Shortcut to update data, using update() method
    # Collection.objects.filter(pk=11).update(featured_product=None)

    ##### Approach - 2: Traditional way to insert data 
    # collection = Collection.objects.get(pk=14)
    # collection.title = 'RPG Games'
    # collection.featured_product = None
    # collection.save()
    # result = collection.title 

    #####################################
    # ### Deleting record/records in the database

    # ### Delete single object
    # collection = Collection(pk=13)
    # collection.delete()

    # ### Delete multiple object
    # collection = Collection()
    # Collection.objects.filter(pk__gt=10).delete()

    result = None 
     
    return render(request, 'hello.html', {'name': 'Moon', 'results': result})
 