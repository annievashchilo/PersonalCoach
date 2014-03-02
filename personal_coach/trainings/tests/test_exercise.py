from __future__ import division
from core.models import Member
from trainings.models import TrainingType
from trainings.models import Exercise
from trainings.models import ExercisePlan

from django.test import TestCase

from datetime import datetime


class ExerciseTest(TestCase):
    def setUp(self):
        self.exercise = Exercise.objects.create(
                plan = ExercisePlan.objects.create(
                    member = Member.objects.create(
                        first_name='Test',
                        last_name='User',
                        ),
                    was_scheduled = datetime.utcnow(),
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
