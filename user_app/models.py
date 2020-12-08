from django.db import models
from passlib.hash import pbkdf2_sha256
from destination_app.models import DestinationModel
from multiselectfield import MultiSelectField

# Create your models here.
class LanguageModel(models.Model):
    language = models.CharField(max_length=20)

    def __str__(self):
        return(self.language)

class GuideRegisterModel(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    bio_desc = models.TextField(max_length=225)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    GENDER_MALE = 0
    GENDER_FEMALE = 1
    GENDER_OTHERS = 2
    GENDER_CHOICES = [
        (GENDER_MALE, 'Male'),
        (GENDER_FEMALE, 'Female'),
        (GENDER_OTHERS, 'Others'),
    ]
    gender = models.IntegerField(choices=GENDER_CHOICES)
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    user_img = models.ImageField(upload_to='UserImg', blank=True, null=True)
    citizenship_img = models.ImageField(upload_to='Citizenship')
    Liscence_img = models.ImageField(upload_to='LiscenceImg')

    LANGUAGES = (
        ('Nepali', 'Nepali'),
        ('English', 'English'),
        ('Spanish', 'Spanish'),
        ('Hindi', 'Hindi')
    )
    languages = MultiSelectField(choices=LANGUAGES)
    
    # languages = models.ManyToManyField(LanguageModel)
    DESTINATIONS = (
        ('kathmandu', 'Kathmandu'),
        ('Bhaktapur', 'Bhaktapur'),
        ('Everest Base Camp', 'Everest Base Camp'),
        ('Annapurna Base Camp', 'Annapurna Base Camp'),
    )
    locations = MultiSelectField(choices=DESTINATIONS)
    is_guide = models.BooleanField(default=1)

    def __str__(self):
        return(self.username)

    def verify_password(raw_password):
        return pbkdf2_sha256.verify(raw_password, self.password)
    
class TouristRegisterModel(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    GENDER_MALE = 0
    GENDER_FEMALE = 1
    GENDER_OTHERS = 2
    GENDER_CHOICES = [
        (GENDER_MALE, 'Male'),
        (GENDER_FEMALE, 'Female'),
        (GENDER_OTHERS, 'Others'),
    ]
    gender = models.IntegerField(choices=GENDER_CHOICES)
    is_tourist = models.BooleanField(default=True)

    def __str__(self):
        return(self.username)

    def verify_password(raw_password):
        return pbkdf2_sha256.verify(raw_password, self.password)



