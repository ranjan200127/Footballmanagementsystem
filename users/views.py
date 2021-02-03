from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.views.generic import DetailView
from .forms import UserRegisterForm,UserUpdateForm,ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from users.models import player
from django.contrib.auth.models import User
from blog.models import team,goal
@login_required
def profile(request):
	if request.method=='POST':
		u_form=UserUpdateForm(request.POST,instance=request.user)
		p_form=ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
		if u_form.is_valid() and p_form.is_valid():
			u_form.save()
			p_form.save()
			messages.success(request,f'Your account has been updated!')
			return redirect('profile')
	else:
		u_form=UserUpdateForm(instance=request.user)
		p_form=ProfileUpdateForm(instance=request.user.profile)
	context={
	'u_form':u_form,
	'p_form':p_form
		}
	return render(request,'users/profile.html',context)
# Create your views here.
class PlayerDetailView(DetailView):
	model=player
	template_name="users/player_detail.html"
	def get_context_data(self,**kwargs):
		context=super(PlayerDetailView,self).get_context_data(**kwargs)
		context.update({
			'object':self.get_object(),
			'goal':len(goal.objects.filter(player_id=self.get_object().user))
			})
		return context