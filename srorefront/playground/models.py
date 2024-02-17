from django.db import models

# Create your models here.
class Promotion(models.Model):

    description = models.CharField(max_length = 255)

    discount = models.FloatField()



class Collection(models.Model):

    title = models.CharField(max_length = 255)
    featured_product = models.ForeignKey('Product', on_delete = models.SET_NULL ,null = True , related_name = "+")

class Product(models.Model):

    # cosidering django's default id system

    title = models.CharField(max_length = 255)
    description = models.TextField()
    price = models.DecimalField(max_digits = 6 , decimal_places = 2)
    inventory = models.IntegerField()
    last_update = models.DateField(auto_now = True)
    colelctiom =  models.ForeignKey(Collection, on_delete = models.CASCADE)
    promotions = models.ManyToManyField(Promotion)




class Customer(models.Model):

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length = 255)
    email = models.EmailField(max_length = 255)
    phone = models.CharField(max_length= 255)
    birth_date = models.DateField(null = True)




class Order(models.Model):
    PAYMENT_STATUS_Pending = 'P'
    PAYMENT_STATUS_Complete = 'C'
    PAYMENT_STATUS_Failed = 'F'
    PAYMENT_STATUS = [
        (PAYMENT_STATUS_Pending , 'Pending'),
        (PAYMENT_STATUS_Complete  , 'Complete'),
        (PAYMENT_STATUS_Failed , 'Failed')

    ]
    placed_at = models.DateField(auto_now_add= True)
    payment_status = models.CharField(max_length = 1 , choices = PAYMENT_STATUS, default = PAYMENT_STATUS_Pending)
    customer = models.ForeignKey(Customer , on_delete = models.PROTECT)



# crerating one to one relationship
    
class Address(models.Model):
    street = models.CharField(max_length = 255)
    city = models.CharField(max_length = 255)
    # set the address a prinmary key to prevent one to many relationship between customer and the address otherwise django would nake unique id for each of the addresses
    customer =  models.OneToOneField(Customer, on_delete = models.CASCADE, primary_key = True)
    # we could have used model.set_null to set null value on deletion of customer 
    # we could have used model.protected to set protect the value from deletion 




class OrderItem(models.Model):

    order = models.ForeignKey(Order,  on_delete = models.PROTECT)
    product = models.ForeignKey(Product, on_delete = models.PROTECT)
    unit_price = models.DecimalField(max_digits = 6 , decimal_places = 2)
    quantity = models.PositiveSmallIntegerField()



class Cart(models.Model):

    created_at = models.DateTimeField(auto_now_add = True)
    item  =  models.ForeignKey(OrderItem , on_delete = models.CASCADE)




class CartItem(models.Model):
    cart = models.ForeignKey( Cart, on_delete= models.CASCADE)    
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    quantity = models.PositiveSmallIntegerField()







