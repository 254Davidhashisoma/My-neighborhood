from django.db import models

# Create your models here.
class Neighborhood(models.Model):
    name = models.CharField(blank=True, max_length=120)
    location = models.CharField(blank=True, max_length=120)
    admin = models.ForeignKey('Profile', on_delete=models.CASCADE, related_name='hood')
    hood_logo = CloudinaryField('gallery/')
    occupants_count = models.PositiveIntegerField(default = '0')
    description = models.TextField()
    health_department = models.IntegerField(null=True, blank=True)
    police_number = models.IntegerField(null=True, blank=True) 

    @classmethod
    def find_neighborhood(cls, neighborhood_id):
        return cls.objects.filter(id=neighborhood_id)

    def save_post(self):
        self.save()

    @classmethod
    def update_post(cls,old,new):
        cap = Neighborhood.objects.filter(description=old).update(description=new)
        return cap

    def delete_post(self):
        self.delete()

    @classmethod
    def search_business(cls, name):
        return cls.objects.filter(name__icontains=name).all()

    def __str__(self):
        return f'{self.name} hood'
