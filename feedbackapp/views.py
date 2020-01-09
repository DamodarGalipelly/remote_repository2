from django.shortcuts import render

# Create your views here.
from feedbackapp.models import FeedbackData
from feedbackapp.forms import FeedbackForm
from django.http.response import HttpResponse
import datetime as dt
date1 = dt.datetime.now()

def feedbackview(request):
    if request.method=="POST":
        fforms=FeedbackForm(request.POST)
        if fforms.is_valid():
            name1=request.POST.get('name')
            rating1=request.POST.get('rating')
            feedback1=request.POST.get('feedback')
            data=FeedbackData(
                name=name1,
                rating=rating1,
                date=date1,
                feedback=feedback1
            )
            data.save()
            fforms=FeedbackForm()
            feedbacks=FeedbackData.objects.all()
            return render(request,'feedbackform.html',{'fforms':fforms,'feedbacks':feedbacks})
        else:
            return HttpResponse('User Missed Some Values')
    else:
        fforms=FeedbackForm()
        feedbacks =FeedbackData.objects.all()
        return render(request,'feedbackform.html',{'fforms':fforms,'feedbacks':feedbacks})
