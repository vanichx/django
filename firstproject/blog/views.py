from django.shortcuts import render

posts = [
	{
		'author' : 'Vanich',
		'title' : 'Blog Post 1',
		'content' : 'Ivan post content',
		'date_posted' : 'August 27, 2024'
	},
	{
		'author' : 'Rostik',
		'title' : 'Blog Post 2',
		'content' : 'Rostik post content',
		'date_posted' : 'August 28, 2024'
	}
]

# Create your views here.
def home(request):
	context = {
		'posts' : posts
	}
	return render(request, 'blog/home.html', context)

def about(request):
	return render(request, 'blog/about.html', {'title':'About'})

