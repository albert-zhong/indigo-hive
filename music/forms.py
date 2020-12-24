import urllib.parse as urlparse

from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from .models import Song, Album, Genre


YOUTUBE_LINK = 'youtube_link'
YOUTUBE_ID = 'youtube_id'


class SongCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(SongCreateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'songCreateForm'
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit'))

    class Meta:
        model = Song
        fields = [
            'title',
            'description',
            'genre',
            'album',
        ]

    def clean(self):
        cleaned_data = super().clean()
        youtube_link = cleaned_data.get(YOUTUBE_LINK)
        if not youtube_link:
            raise ValidationError('YouTube link was not found.')

        url_data = urlparse.urlparse(youtube_link)
        query = urlparse.parse_qs(url_data.query)
        if 'v' not in query or not query['v']:
            print(query)
            raise ValidationError('Invalid YouTube link.')
        youtube_id = query['v'][0]
        self.cleaned_data['youtube_id'] = youtube_id

    youtube_link = forms.CharField()


class AlbumCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AlbumCreateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'albumCreateForm'
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit'))

    class Meta:
        model = Album
        fields = [
            'title',
            'description',
            'genre',
        ]


class ArtistUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ArtistUpdateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'artistUpdateForm'
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit'))

    class Meta:
        model = get_user_model()
        fields = ('description', 'image')

    description = forms.CharField(widget=forms.Textarea)
