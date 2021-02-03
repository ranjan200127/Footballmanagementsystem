from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image
# Create your models here.
class post(models.Model):
	title=models.CharField(max_length=100)
	content=models.TextField()
	date_posted=models.DateTimeField(default=timezone.now)
	author=models.ForeignKey(User,on_delete=models.CASCADE)
	def __str__(self):
		return self.title
	def get_absolute_url(self):
		return reverse('post-detail',kwargs={'pk':self.pk})
class team(models.Model):
	team_id = models.IntegerField(primary_key=True)
	team_name= models.CharField(max_length=50,unique=True)
	team_country=models.CharField(max_length=60,unique=True)
	team_content=models.TextField(default="International Football Team")
	team_image=models.ImageField(default="django1.jpg",upload_to='team_images/')
	def __str__(self):
		return self.team_name
	def save(self):
		super().save()
		img=Image.open(self.team_image.path)
		img=img.convert("RGB")
		if img.height>300 or img.width>300:
			output_size=(300,300)
			img.thumbnail(output_size)
		img.save(self.team_image.path)
class point_table(models.Model):
	team_id = models.OneToOneField(team,primary_key=True,on_delete=models.CASCADE)
	win = models.IntegerField()
	loss= models.IntegerField()
	draw= models.IntegerField()
	played = models.IntegerField()
	def __str__(self):
		return self.team_id.team_name
class match(models.Model):
	match_id =models.AutoField(primary_key=True)
	match_date= models.DateField()
	match_time=models.TimeField(default='5:30:30')
	teama_id=models.ForeignKey(team,to_field="team_id",on_delete=models.CASCADE,related_name="sample1")
	teamb_id=models.ForeignKey(team,to_field="team_id",on_delete=models.CASCADE,related_name="sample2")
	def __str__(self):
		return str(self.match_id)
				
class goal(models.Model):
	goal_id = models.AutoField(primary_key=True)
	goal_time =models.TimeField()
	goal_date=models.DateField(default="2020-12-12")
	match_id=models.ForeignKey(match,on_delete=models.CASCADE)
	team_id=models.ForeignKey(team,on_delete=models.CASCADE,default=1)
	player_id=models.ForeignKey(User,on_delete=models.CASCADE)
	def __str__(self):
		return "goal"+" "+str(self.goal_id)