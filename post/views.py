from django.shortcuts import render
from post.models import PostTable


def getPostsList(request):
    postList = PostTable.objects.all()
    context ={
        "postList" : postList
    }
    return render(request, template_name='post/post-list.html', context=context)


def getHome(request):
    cohort = {
        "current_cohort": "21.2",
        "cohort_name": "Romans"
    }

    return render(request, template_name='post/home.html', context=cohort)
