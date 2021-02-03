from django.shortcuts import render,get_object_or_404
from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from datetime import date,timedelta
# Create your views here.
from .models import post,team,point_table,match,goal
from django.http import HttpResponse
from datetime import date,datetime
from users.models import player
from statistics import mode
def home(request):
	context={
	'posts':post.objects.all()
	}
	return render(request,'blog/home.html',context)
def teams(request):
	context={
	'posts':team.objects.all()
	}
	return render(request,'blog/team_list.html',context)
def points(request):
	context={
	'posts':point_table.objects.all().order_by('-win','-draw','-played')
	}
	return render(request,'blog/team_points.html',context)
def calculate(obj):
	teama=[]
	teamb=[]
	for i in goal.objects.all():
		
		if i.goal_date==obj.match_date and obj.match_id==i.match_id_id:
			if i.team_id_id==obj.teama_id_id:
				teama.append(i)
			else:
				teamb.append(i)
	#print(i.goal_date==previous[1].first().match_date)
	team_a_goal=len(teama)
	team_b_goal=len(teamb)
	if team_a_goal>team_b_goal:
		winner=(obj.teama_id.team_name,team_a_goal,team_b_goal)
		#man_of_match=mode(todays.first().teama_id.values_list('player_id_id'))
	elif team_a_goal==team_b_goal:
		winner=("draw",team_a_goal,team_b_goal)
	else:
		winner=(obj.teamb_id.team_name,team_a_goal,team_b_goal)
	return winner
		#man_of_match=mode(teamb[0].values_list('player_id_id'))
def matches(request):
	todays=match.objects.filter(match_date=date.today())
	previous=[]
	for i in range(1,4):
		r=match.objects.filter(match_date=date.today()-timedelta(days=i))
		if len(r):
			previous.append(r)
	upcoming=[]
	for i in range(1,4):
		r=match.objects.filter(match_date=date.today()+timedelta(days=i))
		if len(r):
			upcoming.append(r)
	listprevious={}
	for i in previous:
		for j in i:
			listprevious[j]=calculate(j)
	listtoday={}
	for i in todays:
		listtoday[i]=calculate(i)
	context={
	'posts':todays,
	'postcount':len(todays),
	'post1':previous,
	'post1count':len(previous),
	'post2':upcoming,
	'post2count':len(upcoming),
	'listp':listprevious,
	'timenow':datetime.now(),
	'listt':listtoday
	#'man_of_matches':man_of_match,
	}
	print(context['post2count'])
	return render(request,'blog/match.html',context)
class PostListView(ListView):
	model=post
	template_name='blog/home.html'
	context_object_name='posts'
	ordering=['-date_posted']
	paginate_by=3
class UserPostListView(ListView):
	model=post
	template_name='blog/user_posts.html'
	context_object_name='posts'
	paginate_by=3
	def get_queryset(self):
		user=get_object_or_404(User,username=self.kwargs.get('username'))
		return post.objects.filter(author=user).order_by('-date_posted')
class TeamListView(ListView):
	model=team
	template_name="blog/team_list.html"
class TeamDetailView(DetailView):
	model=team
	template_name="blog/team_detail.html"
	def get_context_data(self,**kwargs):
		context=super(TeamDetailView,self).get_context_data(**kwargs)
		context.update({
			'object':self.get_object(),
			'players':player.objects.filter(team_id=self.get_object().team_id)
			})
		return context
class PostDetailView(DetailView):
	model=post
class PostCreateView(LoginRequiredMixin,CreateView):
	model=post
	fields=['title','content']
	def form_valid(self,form):
		form.instance.author=self.request.user
		return super().form_valid(form)
class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
	model=post
	fields=['title','content']
	def form_valid(self,form):
		form.instance.author=self.request.user
		return super().form_valid(form)
	def test_func(self):
		post=self.get_object()
		if self.request.user==post.author:
			return True
		return False
class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
	model=post
	success_url='/'
	fields=['title','content']
	def form_valid(self,form):
		form.instance.author=self.request.user
		return super().form_valid(form)
	def test_func(self):
		post=self.get_object()
		if self.request.user==post.author:
			return True
		return False
# Create your views here.
