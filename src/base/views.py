from django.shortcuts import render, redirect
from .models import Question, Option
from .forms import NumberForm, QuestionForm, AllForm, OptionForm


# Create your views here.

def question_list(request):
    questions = Question.objects.all()
    context = {
        "questions": questions
    }
    return render(request, "question.html", context)


def question_detail(request, question_id):
    ques = Question.objects.get(id=question_id)
    options = Option.objects.filter(question=ques)
    context = {
        "question": ques,
        "options": options
    }
    return render(request, 'detail.html', context)


def question_vote(request, question_id):
    option_id = request.GET.get('option')
    option = Option.objects.get(id=int(option_id))
    option.votes += 1
    option.save()
    return redirect('result', question_id)


def question_result(request, question_id):
    ques = Question.objects.get(id=question_id)
    options = Option.objects.filter(question=ques)
    context = {
        "question": ques,
        "options": options
    }
    return render(request, 'result.html', context)


def form_example(request):
    form = NumberForm


def create_polls(request):
    form = QuestionForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        "forms": form
    }

    return render(request, 'create.html', context)


def all_form(request):
    form = AllForm()
    context = {
        "form": form
    }
    return render(request, "allform.html", context)


def create_option(request):
    form = OptionForm(request.POST or None)
    if form.is_valid():
        print(form, form.is_valid())
        form.save()
    context = {
        "forms": form
    }

    return render(request, "option.html", context)
