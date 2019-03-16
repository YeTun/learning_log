from django.shortcuts import render
from .models import Topic


def index(request):
    """The home page for Learning Log"""
    return render(request, 'index.html', {'title': 'Home'})


def about(request):
    """The about page for Learning Log"""
    return render(request, 'about.html', {'title': 'about'})

def topics(request):
    """Show all topics"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'topics.html', context)


def topic(request, topic_id):
    """Show a single topic and all its entries"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'topic.html', context)


