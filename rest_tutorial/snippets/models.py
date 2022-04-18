from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LANGUAGE_CHOICES = [("py", "python"), ("c", "ANSI_C")]                                  # when "py" is given in POST querry django translate it to python
STYLE_CHOICES = [("f", "friendly"), ("h", "hostile")]                                   # when POST querry is not same as choice the error will be given


class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, max_length=100)               # Apply choices from line 5
    style = models.CharField(choices=STYLE_CHOICES, max_length=100)                     # Apply choices for style from line 6

    class Meta:
        ordering = ['created']
