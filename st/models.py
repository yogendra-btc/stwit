from django.db import models
from django.contrib.auth.models import User

# class User(AbstractUser):

#     first_name = models.CharField(max_length = 100)
#     last_name = models.CharField(max_length = 100)
#     email = models.EmailField(max_length=100,unique=True)
    
#     def __str__(self):
#         return str(self.first_name)

class Domain(models.Model):
    domain_name = models.CharField(max_length = 100)

    def __str__(self):
        return self.domain_name

class Keyword(models.Model):
    user_id = models.ForeignKey(User,on_delete = models.CASCADE)
    domain_id = models.ForeignKey(Domain,on_delete = models.CASCADE)
    keyword_string = models.CharField(max_length = 500)
    keyword_status = models.BooleanField(default = True)

class Results(models.Model):
    user_id = models.ForeignKey(User,on_delete = models.CASCADE)
    keyword_id = models.ForeignKey(Keyword,on_delete = models.CASCADE)
    domain_id = models.ForeignKey(Domain,on_delete = models.CASCADE)
    result_string = models.CharField(max_length = 1000)
    datetime = models.DateTimeField()

class Tweets(models.Model):
    user_id = models.ForeignKey(User,on_delete = models.CASCADE)
    tweet = models.CharField(max_length = 1000)
    datetime = models.DateTimeField()

class Irrelevant(models.Model):
    user_id = models.ForeignKey(User,on_delete = models.CASCADE)
    keyword_id = models.ForeignKey(Keyword,on_delete = models.CASCADE)
    irrelevant_keyword = models.CharField(max_length = 100,null = True, blank = True)
    domain_id = models.ManyToManyField(Domain)
    datetime = models.DateTimeField()

class Plan(models.Model):
    plan_name = models.CharField(max_length = 100)
    num_of_keywords = models.CharField(max_length = 50)

class My_Plan(models.Model):
    user_id = models.ForeignKey(User,on_delete = models.CASCADE)
    plan_id = models.ForeignKey(Plan,on_delete = models.CASCADE)