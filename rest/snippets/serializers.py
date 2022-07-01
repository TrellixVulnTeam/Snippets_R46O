from django.core import serializers
from dataclasses import fields
from email.policy import default
from rest_framework import serializers
from .models import Snippet

# from pygments.lexers import get_all_lexers
# from pygments.styles import get_all_styles

# Create your models here.
# LEXERS=[item for item in get_all_lexers()if item[1]]
# LANGUAGE_CHOICES=sorted([(item[1][0],item[0]) for item in LEXERS])
# STYLE_CHOICES=sorted([(item,item) for item in get_all_styles()])

class SnippetSerializer(serializers.ModelSerializer):
        class Meta:
            model= Snippet
            fields = ['id','title','code','linenos','language','style']

# create an instance for snippet from the given validated data
def create(self,validated_data):
    return Snippet.objects.create(**validated_data)
# update and return instance of snippet from the given data
def update(self,instance,validated_data):
    instance.title=validated_data.get("title",instance.title)
    instance.code=validated_data.get("code",instance.code)
    instance.linenos=validated_data.get("linenos",instance.linenos)
    instance.language=validated_data.get("language",instance.language)
    instance.style=validated_data.get("style",instance.style)
    instance.save()
    return instance
   
    
