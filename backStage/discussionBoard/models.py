import datetime

from django.db import models
from django.utils import timezone

# python3 manage.py makemigrations polls
#By running makemigrations, you’re telling Django that you’ve made some changes to your models
# (in this case, you’ve made new ones) and that you’d like the changes to be stored as a migration.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    #When Question.objects.all()--> displays all the questions in database
    #it only returns <QuerySet [<Question: Question object (1)>]>
    # TO MAKE IT MORE HELPFUL:
    def __str__(self):
        return self.question_text

#    def was_published_recently(self):
#        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


#Change your models (in models.py).
#Run python manage.py makemigrations to create migrations for those changes
#Run python manage.py migrate to apply those changes to the database