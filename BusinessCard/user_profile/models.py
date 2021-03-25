from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #age = models.IntegerField()
    #birthday = models.CharField(max_length=10)
    #jobtitle = models.CharField(max_length=100)
    #employer = models.CharField(max_length=100)
    #location = models.CharField(max_length=100)
    #phone = models.CharField(max_length=15)
    image = models.CharField(max_length=1000)


    def longFormat(self):
        return {#'last_name':self.last_name,
                #'age':self.age,
                #'birthday':self.birthday,
                #'jobtitle':self.jobtitle,
                #'employer':self.employer,
                #'location':self.location,
                #'email':self.email,
                #'phone':self.phone,
                'image':self.image,
                'user_id':self.user.id,
                'username':self.user.username
            } 

    def delete(self):
        self.user.delete()


    @receiver(post_save,sender=User)
    def create_user_profile(sender,instance,created,**kwargs):
        if created:
            Profile.objects.create(user=instance)


    @receiver(post_save,sender=User)
    def save_user_profile(sender,instance,**kwargs):
        instance.profile.save()

