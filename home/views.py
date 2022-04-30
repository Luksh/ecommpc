from django.shortcuts import render
from .models import *
from .models import Contact
from django.views.generic import View
from django.contrib import messages
from django.contrib.auth.models import User

app_name = "home"

# Create your views here.

class BaseView(View):
    view = {}
    view['categories'] = Category.objects.all()

class HomeView(BaseView):
    def get(self, request):
        self.view['categories'] = Category.objects.all()
        self.view['subcategories'] = SubCategory.objects.all()
        self.view['sliders'] = Slider.objects.all()
        self.view['ads'] = Ad.objects.all()
        self.view['products'] = Product.objects.filter(status = 'active')
        self.view['hots'] = Product.objects.filter(labels= 'hot', status= 'active')
        self.view['sales'] = Product.objects.filter(labels= 'sale', status= 'active')
        self.view['news'] = Product.objects.filter(labels= 'new', status= 'active')

        return render(request, 'shop-index.html', self.view)

class ProductDetailView(BaseView):
    def get(self, request, slug):
        self.view['product_detail'] = Product.objects.filter(slug = slug)
        return render(request, 'shop-item.html', self.view)

class CategoryView(BaseView):
    def get(self, request, slug):
        cat_id = Category.objects.get(slug= slug).id
        cat_name = Category.objects.get(slug= slug).name
        self.view['cat_products'] = Product.objects.filter(category_id = cat_id)
        self.view['subcats'] = SubCategory.objects.filter(category_id = cat_id)
        self.view['category_name'] = cat_name
        return render(request, 'category.html', self.view)

class SubCategoryView(BaseView):
    def get(self, request, slug):
        subcat_id = SubCategory.objects.get(slug= slug).id
        subcat_name = SubCategory.objects.get(slug= slug).name
        cat_id = SubCategory.objects.get(slug= slug).category_id
        self.view['subcategory'] = SubCategory.objects.filter(category_id = cat_id)
        self.view['subcat_products'] = Product.objects.filter(subcategory_id = subcat_id)
        self.view['subcategory_name'] = subcat_name
        return render(request, 'subcategory.html', self.view)

class SearchView(BaseView):
    def get(self, request):
        if request.method == 'GET':
            query = request.GET['query']
            self.view['search_query'] = query
            self.view['search_product'] = Product.objects.filter(name__icontains = query)

        return render(request, 'shop-search-result.html', self.view)

def signup(request):
    if request.method == "POST":
        first_name = request.POST['fname']
        last_name = request.POST['lname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        if password == cpassword:
            if User.objects.filter(username = username).exists():
                messages.error(request, 'The username is already taken')
                return render(request, 'shop-standard-forms.html')

            elif User.objects.filter(email = email).exists():
                messages.error(request, 'The email is already taken')
                return render(request, 'shop-standard-forms.html')

            else:
                user = User.objects.create_user(
                    first_name = first_name,
                    last_name = last_name,
                    username = username,
                    email = email,
                    password = password
                )
                user.save()
        else:
            messages.error(request, 'The password does not match')
            return render(request, 'shop-standard-forms.html')

    return render(request, 'shop-standard-forms.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        subject = request.POST['subject']
        message = request.POST['message']

        data = Contact.objects.create(
            name = name,
            email = email,
            phone = phone,
            subject = subject,
            message = message
        )
        data.save()

    return render(request, 'shop-contacts.html')