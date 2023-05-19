from django.forms import ModelForm
from .models import *

class PostForm(ModelForm):
	def __init__(self, *args, **kwargs):
	    super(ModuleForm, self).__init__(*args, **kwargs)
	    for visible in self.visible_fields():
	        visible.field.widget.attrs['class'] = 'form-control'

	class Meta:
		model=Post
		fields='__all__'


class ProfileForm(ModelForm):

	class Meta:
		model=Profile
		fields='__all__'