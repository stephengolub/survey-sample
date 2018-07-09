from collections import defaultdict
from decimal import Decimal
from random import randint

from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import get_object_or_404, redirect, render

from .models import Answer, Question
from .forms import NewQuestionForm, SurveyForm



@login_required
def index(request):
    if request.method == 'POST':
        form = SurveyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'surveys/submitted.html', locals())
    else:
        current_user = request.user
        available_surveys = Question.objects.exclude(answer__in=Answer.objects.filter(responder=current_user))
        available_survey_count = len(available_surveys)
        random_survey = None if not available_survey_count else available_surveys[randint(0, available_survey_count - 1)]
        form = SurveyForm(question=random_survey, responder=current_user)
    return render(request, 'surveys/index.html', locals())


@staff_member_required
def survey_responses(request, question_id=None):
    if question_id is not None:
        question = get_object_or_404(Question, pk=question_id)
        answers = question.answer_set.all()
        answer_counts = {c.id: dict(count=0, item=c, percent=0.0) for c in question.available_options.all()}
        total_answers = len(answers)
        for answer in answers:
            answer_counts[answer.answer.id]['count'] += 1
            answer_counts[answer.answer.id]['percent'] = (Decimal(answer_counts[answer.answer.id]['count']) / Decimal(total_answers)) * 100
        return render(request, 'surveys/answers.html', locals())
    else:
        questions = Question.objects.all()
        return render(request, 'surveys/questions.html', locals())

@staff_member_required
def new_question(request):
    if request.method == 'POST':
        form = NewQuestionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('new_question')
    else:
        form = NewQuestionForm()
    return render(request, 'surveys/new.html', locals())
