from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from .models import Poll
from .forms import PollForm


class IndexView(generic.ListView):
    def get_queryset(self):
        return Poll.objects.order_by('-pub_date')[:5]


class ResultsView(generic.DetailView):
    model = Poll
    template_name = 'polls/poll_results.html'


def detail(request, pk):
    poll = get_object_or_404(Poll, pk=pk)
    choices = poll.choice_set.all()
    form = PollForm(request.POST or None, choices=choices)

    if request.method == "POST" and form.is_valid():
            choice = form.cleaned_data['choices']
            choice.votes += 1
            choice.save()
            return HttpResponseRedirect(reverse('polls-results', args=(poll.id,)))
    return render(request, 'polls/poll_detail.html', {'poll': poll, 'form': form})



# def detail(request, poll_id):
#     poll = get_object_or_404(Poll, pk=poll_id)

#     try:
#         selected_choice = poll.choice_set.get(pk=request.POST['choice'])
#     except (KeyError, Choice.DoesNotExist):
#         # Redisplay the poll voting form.
#         return render(request, 'polls/poll_detail.html', {
#             'poll': poll,
#             'error_message': "You didn't select a choice.",
#         })
#     else:
#         selected_choice.votes += 1
#         selected_choice.save()
#         # Always return an HttpResponseRedirect after successfully dealing
#         # with POST data. This prevents data from being posted twice if a
#         # user hits the Back button.
#         return HttpResponseRedirect(reverse('polls-results', args=(poll.id,)))
