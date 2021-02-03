from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.core.validators import RegexValidator
from blog.models import team,goal
class Profile(models.Model):
	user=models.OneToOneField(User,on_delete=models.CASCADE)
	image=models.ImageField(default="django1.jpg",upload_to='profile_pics')
	def __str__(self):
		return f'{self.user.username} Profile'
	def save(self):
		super().save()
		img=Image.open(self.image.path)
		if img.height>300 or img.width>300:
			output_size=(300,300)
			img.thumbnail(output_size)
		img.save(self.image.path)

# Create your models here.
class player(models.Model):
	user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
	mobile_number=models.CharField(validators=[RegexValidator(regex=r'\d{10,15}',message="Phone number must be entered in the format: '9343526371")],max_length=13,blank=True)
	nationality=models.CharField(max_length=20,default="Indian")
	date_of_birth=models.DateField()
	team_id=models.ForeignKey(team,on_delete=models.CASCADE)
	content=models.TextField(default="football player")
	def __str__(self):
		return self.user.username