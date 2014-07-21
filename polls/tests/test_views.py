from django.utils import timezone
from django.core.urlresolvers import reverse
from django.test import TestCase

from ..models import Poll


class IndexViewTest(TestCase):
    def test_success(self):
        rv = self.client.get('/polls/')
        self.assertEqual(rv.status_code, 200)

    def test_poll_display(self):
        poll = Poll(question="Favorite animal?", pub_date=timezone.now())
        poll.save()
        rv = self.client.get('/polls/')
        self.assertContains(rv, poll.question)
        self.assertTemplateUsed(rv, 'polls/poll_list.html')


class ResultsViewTest(TestCase):
    def test_succes(self):
        rv = self.client.get('polls/results/')
        self.assertEqual(rv.status_code, 200)

    def test_template_used(self):
        pass

    def test_vote_count(self):
        pass
