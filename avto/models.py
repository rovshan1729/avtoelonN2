from django.db import models
from utils.models import BaseModel

REGIONS = [
       ('Andijan Region', 'Andijan Region'),
       ('Bukhara Region', 'Bukhara Region'),
       ('Fergana Region', 'Fergana Region'),
       ('Jizzakh Region', 'Jizzakh Region'),
       ('Karakalpakstan', 'Karakalpakstan (Autonomous Republic)'),
       ('Namangan Region', 'Namangan Region'),
       ('Navoiy Region', 'Navoiy Region'),
       ('Qashqadaryo Region', 'Qashqadaryo Region'),
       ('Samarkand Region', 'Samarkand Region'),
       ('Sirdaryo Region', 'Sirdaryo Region'),
       ('Surxondaryo Region', 'Surxondaryo Region'),
       ('Tashkent Region', 'Tashkent Region'),
   ]
   


class Region(BaseModel):
    title = models.CharField(max_length=256)

    def __str__(self):
        return self.title


class District(BaseModel):
    title = models.CharField(max_length=256)
    region = models.ForeignKey(
        Region, on_delete=models.CASCADE, related_name="districts"
    )

    is_filter = models.BooleanField(default=False)

    def __str__(self):
        return self.title


# Create your models here.
class Category(BaseModel):
    title = models.CharField(max_length=256)

    def __str__(self):
        return self.title


class SubCategory(BaseModel):
    title = models.CharField(max_length=256)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="subcategories"
    )
    has_price = models.BooleanField(default=True)
    options = models.ManyToManyField(
        "option.Option",
    )

    def __str__(self):
        return self.title


class Post(BaseModel):
    subcategory = models.ForeignKey(
        SubCategory, on_delete=models.CASCADE, related_name="posts"
    )

    published_at = models.DateTimeField(auto_now_add=True)
    info = models.TextField(blank=True, null=True)
    price = models.IntegerField(default=0, null=True, blank=True)
    views = models.IntegerField(default=0, editable=False)

    district = models.ForeignKey(
        District, on_delete=models.CASCADE, related_name="posts"
    )

    is_salon = models.BooleanField(default=False)
    is_bargain = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.info

class SaveAndNote(BaseModel):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='saveandnote')
    is_saved = models.BooleanField(default=False)
    add_note = models.TextField(null=True, blank=True)

class Photo(BaseModel):
    image = models.ImageField(upload_to="photos")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="photos")
    is_main = models.BooleanField(default=False)

class RentToOwn(BaseModel):
    is_rent = models.BooleanField(default=False)

    pre_payment = models.IntegerField()
    rent_period = models.IntegerField()
    payment_for_month = models.IntegerField()


class ContactInfo(BaseModel):
    region = models.CharField(max_length=128, choices=REGIONS)
    district = models.ForeignKey(District, on_delete=models.CASCADE)

    phone_number = models.IntegerField()

    is_agree = models.BooleanField(default=False)



