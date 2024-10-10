from django.db import models

class User(models.Model):
    id = models.CharField(max_length=10, primary_key=True)  # You can adjust the max_length as needed
    profile_picture = models.ImageField(upload_to='profile_pics/')
    email = models.EmailField(max_length=100, default= None, null=True, blank=True)  # New field for email
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Car(models.Model):
    license_plate_number = models.CharField(max_length=20, default= None)
    kilometer = models.DecimalField(max_digits=10, decimal_places=2, default= None)
    car_name = models.CharField(max_length=100)
    car_year = models.CharField(max_length=100)
    car_color = models.CharField(max_length=50)
    car_picture = models.ImageField(upload_to='car_stock_pictures/', blank=True, null=True)

    def __str__(self):
        return f"{self.car_name} - {self.car_year} ({self.car_color})"



class Contract(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE, default=None, blank=True, null=True)
    contract_image = models.ImageField(upload_to='contract_images/', null=True, blank=True)
    invoice_image = models.ImageField(upload_to='invoice_images/', null=True, blank=True, default=None)
    pickup_date = models.DateField()
    return_date = models.DateField()
    hold_release_date = models.DateField(blank=True, null=True, default = None)
    is_active = models.BooleanField(default=True)
    deposit_status = models.BooleanField(default = True)
    car_exterior_image1 = models.ImageField(upload_to='car_exterior_images/', blank=True, null=True)
    car_exterior_image2 = models.ImageField(upload_to='car_exterior_images/', blank=True, null=True)
    car_exterior_image3 = models.ImageField(upload_to='car_exterior_images/', blank=True, null=True)
    car_exterior_image4 = models.ImageField(upload_to='car_exterior_images/', blank=True, null=True)
    car_exterior_image5 = models.ImageField(upload_to='car_exterior_images/', blank=True, null=True)

    car_interior_image1 = models.ImageField(upload_to='car_interior_images/', blank=True, null=True)
    car_interior_image2 = models.ImageField(upload_to='car_interior_images/', blank=True, null=True)
    car_interior_image3 = models.ImageField(upload_to='car_interior_images/', blank=True, null=True)
    car_interior_image4 = models.ImageField(upload_to='car_interior_images/', blank=True, null=True)
    car_interior_image5 = models.ImageField(upload_to='car_interior_images/', blank=True, null=True)


    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}'s Contract for {self.car.car_name} ({self.pickup_date})"


class Fine(models.Model):
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE)
    fine_picture = models.ImageField(upload_to='fine_images/', null=True, blank=True)
    fine_number = models.CharField(max_length=50, default= None)
    fine_type = models.CharField(max_length=100)
    fine_date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Fine for {self.contract.user.first_name} {self.contract.user.last_name} - Type: {self.fine_type}"

class Driver(models.Model):
    id = models.CharField(max_length=10, primary_key=True)  # You can adjust the max_length as needed
    profile_picture = models.ImageField(upload_to='profile_pics/')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"