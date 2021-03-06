from django.db import models

# Article Model
class Article(models.Model):

	title = models.CharField(max_length=200)
	preview = models.TextField(max_length=500)
	content = models.TextField(max_length=5000)
	posted = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title


class Researchpaper(models.Model):
	title = models.CharField(max_length=200)
	author = models.CharField(max_length=200)
	abstract = models.TextField(max_length=1000)
	pdf_url = models.CharField(max_length=100)
	pub_date = models.CharField(max_length=100)
	subject = models.CharField(max_length=100)

	def __str__(self):
		return self.title


class Subscription(models.Model):
	email = models.EmailField(null=False, blank=True, max_length=200, unique=True)
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.email


class Contact(models.Model):
	email = models.CharField(max_length=100)
	subject = models.CharField(max_length=100)
	message = models.TextField(max_length=500)
	contacted_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.email