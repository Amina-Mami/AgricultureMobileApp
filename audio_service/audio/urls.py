from django.urls import include, path
from rest_framework import routers
from .views import LanguageViewSet, SeasonViewSet, AudioPromptViewSet, AudioTranslationViewSet

router = routers.DefaultRouter()
router.register(r'languages', LanguageViewSet)
router.register(r'seasons', SeasonViewSet)
router.register(r'prompts', AudioPromptViewSet)
router.register(r'translations', AudioTranslationViewSet)

urlpatterns = [
    path('', include(router.urls)),
   path('', include('chatbot.urls')), # <--- ici tu inclus ton app chatbot
]
