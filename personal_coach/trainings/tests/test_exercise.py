from __future__ import division
from core.models import Member
from trainings.models import TrainingType
from trainings.models import Exercise

from django.test import TestCase

from datetime import datetime
from time import sleep
from pytz import utc


class ExerciseTest(TestCase):
    def setUp(self):
        self.exercise = Exercise.objects.create(
                member = Member.objects.create(
                    first_name='Test',
                    last_name='User',
                    ),
                type = TrainingType.objects.create(
                    name='Test training',
                    load='C',
                    ),
                )

    def test_approaches(self):
        times = (10, 10, 9, 7, 3)
        mean = sum(times) / len(times)

        for t in times:
            self.exercise.add_approach(t)

        e = Exercise.objects.get(pk=self.exercise.pk)

        self.assertEqual(e.times, mean)
        self.assertEqual(e.breaks, len(times))

        self.exercise.save(True)
        e = Exercise.objects.get(pk=self.exercise.pk)
        d = datetime.utcnow().replace(tzinfo=utc) - e.was_stopped
        self.assertEqual(0, d.seconds)

        # second save() should not affect was_stopped time
        sleep(1)
        self.exercise.save(True)
        e = Exercise.objects.get(pk=self.exercise.pk)
        d = datetime.utcnow().replace(tzinfo=utc) - e.was_stopped
        self.assertGreater(d.seconds, 0)

