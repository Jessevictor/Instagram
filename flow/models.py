from django.db import models

# Create your models here.
class instagram(models.Model):
    image = models.ImageField(upload_to ='images')
    imageName = models.CharField(max_length=200)
    imageCaption = models.CharField( max_length=50);


    @classmethod
    def all_images(cls):
        my_image = cls.objects.all()
        return my_image

    @classmethod
    def search_by_category(cls, search_term):
        my_image = cls.objects.filter(imageName__icontains=search_term)
        return my_image

    def __str__(self):
        return self.imageName

    def save_gallery(self):
        self.save()
    
    def delete(self):
        self.delete()


class Caption(models.Model):
    caption_name= models.CharField(max_length=200)

    def __str__(self):
        return self.location_name

    def save_location(self):
        self.save()
    def delete(self):
        self.delete()
    
    


class Name(models.Model):
    name_name = models.CharField(max_length=200)

    def __str__(self):
        return self.category_name

    def save_Category(self):
        self.save()
    def delete(self):
        self.delete()