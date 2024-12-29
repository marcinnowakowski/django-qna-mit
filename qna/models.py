from django.db import models
from django.urls import reverse
  
class Question(models.Model):
  title = models.CharField(max_length=255)
  pub_date = models.DateTimeField('Date submitted',auto_now_add=True)
  slug = models.SlugField(unique=True)
  question = models.TextField()
  public = models.BooleanField(default=False)
  allow_comments = models.BooleanField(default=True)

  def __str__(self):
    return self.title
    
  def get_absolute_url(self):
    return reverse('question_detail', kwargs={'slug': self.slug})
    
  def save(self, *a, **kw):
    if not self.slug:
      from django.template.defaultfilters import slugify
      self.slug = slugify(self.title)[:50]
    super(Question, self).save(*a, **kw)

class SurveySubmission(models.Model):
  pesel = models.CharField(max_length=11)
  pub_date = models.DateTimeField('Date submitted',auto_now_add=True)

  def __str__(self):
    return self.pesel + ":" + str(self.pub_date)

class Answer(models.Model):
  survey_submission = models.ForeignKey(SurveySubmission, on_delete=models.CASCADE, related_name='answers')
  question = models.ForeignKey(Question, on_delete=models.DO_NOTHING)
  answer = models.TextField()

  def __str__(self):
    return str(self.survey_submission) + ":" + str(self.question)
