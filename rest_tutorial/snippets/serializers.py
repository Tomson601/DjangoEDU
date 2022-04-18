from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES


class SnippetSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Snippet
        fields = ['id', 'title', 'code', 'linenos', 'language', 'style']

    def to_representation(self, obj):                                               # Formtaing output data with to_representaion function
        return {
            "id": obj.id,                                                           
            "title": obj.title,
            "code": obj.code,
            "linenos": obj.linenos,
            "language": obj.get_language_display(),
            "style": obj.get_style_display()
        }
