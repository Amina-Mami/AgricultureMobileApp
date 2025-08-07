from rest_framework import viewsets
from .models import Language, Season, AudioPrompt, AudioTranslation
from .serializers import LanguageSerializer, SeasonSerializer, AudioPromptSerializer, AudioTranslationSerializer

class LanguageViewSet(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer

class SeasonViewSet(viewsets.ModelViewSet):
    queryset = Season.objects.all()
    serializer_class = SeasonSerializer

class AudioPromptViewSet(viewsets.ModelViewSet):
    queryset = AudioPrompt.objects.all()
    serializer_class = AudioPromptSerializer

class AudioTranslationViewSet(viewsets.ModelViewSet):
    queryset = AudioTranslation.objects.all()
    serializer_class = AudioTranslationSerializer
