from django.db import models
import datetime
from django.utils import timezone
# Create your models here.

class Task(models.Model):
	task_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('Created On')

	def __str__(self):
		return self.task_text
	def recent(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Completed(models.Model):
	status = models.ForeignKey(Task, on_delete = models.CASCADE)
	def __str__(self):
		return self.status
