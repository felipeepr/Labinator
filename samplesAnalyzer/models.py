from django.db import models
from django.utils import timezone

class Samples(models.Model):
    sample_name = models.CharField(max_length=50)
    sample_pacient_name = models.CharField(max_length=50)
    sample_date = models.DateTimeField("Sample Date")
    sample_image = models.ImageField(upload_to="samples/", blank=True, null=True)
    
    def __str__(self):
        return self.sample_name
    
    def recentlyTested(self):
        return self.sample_indicator > 0
    
class Result(models.Model):
    POSITIVE = "POSITIVE"
    NEGATIVE = "NEGATIVE"
    MUST_REPEAT = "MUST REPEAT"
    
    RESULT_CHOICES = [
        (POSITIVE, "POSITIVE"),
        (NEGATIVE, "NEGATIVE"),
        (MUST_REPEAT, "MUST REPEAT"),
    ]
    
    samples = models.ForeignKey(Samples, on_delete=models.CASCADE)
    result_sample = models.CharField(max_length=50)
    result_result = models.CharField(max_length=20, default="NEGATIVE")
    result_date = models.DateTimeField("Result Date")
    
    def __str__(self):
        return self.result_sample
    