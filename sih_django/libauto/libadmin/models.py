from django.db import models

class student_info(models.Model):
	email = models.CharField(max_length = 200)
	password = models.CharField(max_length = 200)
	first_name = models.CharField(max_length = 20)
	last_name = models.CharField(max_length = 20)
class faculty_info(models.Model):
	email = models.CharField(max_length = 200)
	password = models.CharField(max_length = 200)
	first_name = models.CharField(max_length = 20)
	last_name = models.CharField(max_length = 20)
	
