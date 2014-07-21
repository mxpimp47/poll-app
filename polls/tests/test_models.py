from datetime import timedelta
from django.test import TestCase
from django.utils import timezone

from ..models import Poll


class PollModelTest(TestCase):
    def test_was_published_recently(self):
        recent = timezone.now()
        poll = Poll(question='whats your favorite color?',
                    pub_date=recent)
        poll.save()
        self.assertTrue(poll.was_published_recently())

    def test_was_publish_recently_fail(self):
        not_recent = timezone.now() - timedelta(days=5)
        poll = Poll(question='whats your favorite color?',
                    pub_date=not_recent)
        poll.save()
        self.assertFalse(poll.was_published_recently())
