from django.test import TestCase, Client
from django.urls import reverse
from home.models import Product,User 

class IndexViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.product1 = Product.objects.create(shape="Square", location="Red")
        self.product2 = Product.objects.create(shape="Circle", location="Blue")

    def test_index_with_search_query(self):
        url = reverse('index')
        response = self.client.post(url, {'search': 'Squa'})
        
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.product1.shape)  
        self.assertNotContains(response, self.product2.shape)  

    def test_index_without_search_query(self):
        url = reverse('index')
        response = self.client.post(url)
        
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.product1.shape)  
        self.assertContains(response, self.product2.shape)

class ProductTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_add_product(self):
        url = reverse('add_product')
        data = {
            'shape': 'Square',
            'size': 'Large',
            'location': 'Warehouse A',
            'price': 10.00,
        }
        response = self.client.post(url, data)
        
    
        self.assertEqual(response.status_code, 302)  
        self.assertTrue(Product.objects.filter(shape='Square', size='Large', location='Warehouse A', price=10.00).exists())

    def test_update_product(self):
        product = Product.objects.create(shape='Circle', size='Small', location='Warehouse B', price=5.00)
        url = reverse('update_product', args=[product.id])
        data = {
            'shape': 'Triangle',
            'size': 'Medium',
            'location': 'Warehouse C',
            'price': '7.50',
        }
        response = self.client.post(url, data)
        
        self.assertEqual(response.status_code, 302)
        updated_product = Product.objects.get(id=product.id)
        self.assertEqual(updated_product.shape, 'Triangle')
        self.assertEqual(updated_product.size, 'Medium')
        self.assertEqual(updated_product.location, 'Warehouse C')
        self.assertEqual(updated_product.price, 7.50)

    def test_delete_product(self):
        product = Product.objects.create(shape='Circle', size='Small', location='Warehouse B', price=5.00)
        url = reverse('delete_product', args=[product.id])
        response = self.client.post(url)
        
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Product.objects.filter(id=product.id).exists())


class UserTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_users(self):
        User.objects.create(name='Alice', age=25, address='123 Main St')
        User.objects.create(name='Bob', age=30, address='456 Elm St')

        url = reverse('users')
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Alice')
        self.assertContains(response, 'Bob')

    def test_add_user(self):
        url = reverse('add_user')
        data = {
            'name': 'Charlie',
            'age': 35,
            'address': '789 Oak St',
        }
        response = self.client.post(url, data)
        
        self.assertEqual(response.status_code, 302)  
        self.assertTrue(User.objects.filter(name='Charlie', age=35, address='789 Oak St').exists())

    def test_update_user(self):
        user = User.objects.create(name='David', age=40, address='987 Pine St')
        url = reverse('update_user', args=[user.id])
        data = {
            'name': 'Eve',
            'age': 45,
            'address': '654 Cedar St',
        }
        response = self.client.post(url, data)
        
        self.assertEqual(response.status_code, 302)
        updated_user = User.objects.get(id=user.id)
        self.assertEqual(updated_user.name, 'Eve')
        self.assertEqual(updated_user.age, 45)
        self.assertEqual(updated_user.address, '654 Cedar St')

    def test_delete_user(self):
        user = User.objects.create(name='Frank', age=50, address='321 Maple St')
        url = reverse('delete_user', args=[user.id])
        response = self.client.post(url)
        
        self.assertEqual(response.status_code, 302)
        self.assertFalse(User.objects.filter(id=user.id).exists())