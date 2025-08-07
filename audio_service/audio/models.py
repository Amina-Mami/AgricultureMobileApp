from django.db import models

class Language(models.Model):
    code = models.CharField(max_length=10, unique=True) 
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Season(models.Model):
    name = models.CharField(max_length=50)  
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.name

class AudioPrompt(models.Model):
    key = models.CharField(max_length=100, unique=True)  
    description = models.TextField(blank=True, null=True)

   
    metadata = models.JSONField(blank=True, null=True)

   
    season = models.ForeignKey(Season, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.key

class AudioTranslation(models.Model):
    audio_prompt = models.ForeignKey(AudioPrompt, related_name='translations', on_delete=models.CASCADE)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    audio_url = models.URLField()

    class Meta:
        unique_together = ('audio_prompt', 'language')

    def __str__(self):
        return f'{self.audio_prompt.key} - {self.language.code}'
