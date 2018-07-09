from django import forms

from . import models


class CustomRadio(forms.RadioSelect):
    option_template_name = "surveys/radio.html"


class SurveyForm(forms.ModelForm):
    def __init__(self, *args, question=None, responder=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['question'].initial = question
        self.fields['responder'].initial = responder
        if question is not None:
            self.fields['answer'].queryset = question.available_options.all()

    class Meta:
        model = models.Answer
        fields = ('question', 'answer', 'responder')
        labels = {
            'answer': ''
        }
        widgets = {
            'question': forms.HiddenInput(),
            'responder': forms.HiddenInput(),
            'answer': CustomRadio,
        }


class NewQuestionForm(forms.Form):
    question_text = forms.CharField(label="Question", max_length=200,
                                    widget=forms.TextInput(attrs={'size': "100%"}))
    option_entry = forms.CharField(label="Survey Answer Options",
                                   widget=forms.Textarea,
                                   help_text="Enter choices on separate lines.")

    @property
    def options(self):
        return self.data.get('option_entry', '').split("\r\n")

    def save(self):
        choices = [models.Choice(choice_text=c) for c in self.options]
        for c in choices:
            c.save()
        question = models.Question(question_text=self.data['question_text'])
        question.save()
        question.available_options.set(choices)
        return question
