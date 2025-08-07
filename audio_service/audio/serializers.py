from rest_framework import serializers
from .models import Language, Season, AudioPrompt, AudioTranslation

class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = '__all__'

class SeasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Season
        fields = '__all__'

class AudioTranslationSerializer(serializers.ModelSerializer):
    language = LanguageSerializer(read_only=True)
    language_id = serializers.PrimaryKeyRelatedField(
        queryset=Language.objects.all(), source='language', write_only=True)

    class Meta:
        model = AudioTranslation
        fields = ['id', 'audio_url', 'language', 'language_id']

class AudioPromptSerializer(serializers.ModelSerializer):
    translations = AudioTranslationSerializer(many=True, read_only=True)
    season = SeasonSerializer(read_only=True)
    season_id = serializers.PrimaryKeyRelatedField(
        queryset=Season.objects.all(), source='season', write_only=True, allow_null=True, required=False)

    class Meta:
        model = AudioPrompt
        fields = ['id', 'key', 'description', 'metadata', 'season', 'season_id', 'translations']
