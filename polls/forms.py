from django import forms


class PollForm(forms.Form):

    def __init__(self, *args, **kwargs):
        choices = kwargs.pop('choices', None)
        super(PollForm, self).__init__(*args, **kwargs)
        self.fields['choices'] = forms.ModelChoiceField(queryset=choices, widget=forms.RadioSelect, empty_label=None)
