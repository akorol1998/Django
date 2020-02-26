from polls.models import Question, Choice

from django.template import loader
from django.shortcuts import render, reverse, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.db.models import F
from django.views import generic

# Create your views here.
class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = 'question_list'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]
    

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get(self, request, pk=None, abc=None):
        print("It was GET")
        print(request)
        return render(request, self.template_name, {"question": get_object_or_404(Question, pk=pk)})
    
    def post(self,request, pk=None):
        print("It was Post")
        return render(request, self.template_name, {"question": get_object_or_404(Question, pk=pk)})
    
    def get_context_data(self, **kwargs):
        print("Context")
        context = super().get_context_data(kwargs)
        print(context)
        return context


class ResultView(generic.DetailView):
    model = Question
    template_name = 'polls/result.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist) as e:
        context = {"question": question,
                    "error_message": "No choice made"}
        return render(request, 'polls/detail.html', context)
    choice.votes = F('votes') + 1
    choice.save()
    choice.refresh_from_db()
#   If query, can use update()
    # choice.update(votes=F('votes') + 1)
    
    return HttpResponseRedirect(reverse('polls:result', args=({question.id})))