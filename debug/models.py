from django.db import models

# Create your models here.
class TestCase(models.Model):
   test_id = models.IntegerField()
   test_name = models.CharField(max_length = 100)
   test_condition = models.CharField(max_length = 500)
   test_process = models.CharField(max_length = 1000)
   test_expected = models.CharField(max_length = 1000)

class Group(models.Model):
   group_id = models.IntegerField()
   group_name = models.CharField(max_length = 20)

class User(models.Model):
   user_name = models.CharField(max_length = 20)
   password = models.CharField(max_length = 50)
   user_fullname = models.CharField(max_length = 10)
   group = models.ForeignKey(Group)
   create_time = models.DateTimeField(null = True)
   last_login_time = models.DateTimeField(null = True)

class Operation(models.Model):
   operate_id = models.IntegerField()
   operate_name = models.CharField(max_length = 10)

class GroupOperation(models.Model):
   group_id = models.ForeignKey(Group)
   operate_id = models.ForeignKey(Operation)

class Bug(models.Model):
   bug_id = models.IntegerField()
   bug_name = models.CharField(max_length = 50)
   bug_description = models.CharField(max_length = 1000)
   bug_test_case = models.ForeignKey(TestCase)
   bug_response = models.ForeignKey(User)


class BugOperations(models.Model):
   bug_id = models.ForeignKey(Bug)
   operate_id =models.ForeignKey(Operation)
   operater =  models.ForeignKey(User)
   operate_time = models.DateTimeField()
   operation_description = models.CharField(max_length = 500)
