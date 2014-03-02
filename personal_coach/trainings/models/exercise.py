from django.db import models
from datetime import datetime
from pytz import utc


class Exercise(models.Model):
    '''Excercise that someone has performed
    '''
    plan = models.ForeignKey('trainings.ExercisePlan',
            null=True,
            blank=False,
            )
    type = models.ForeignKey('trainings.TrainingType',
            null=False,
            blank=False,
            on_delete=models.PROTECT,
            )
    times = models.FloatField(
            null=False,
            blank=False,
            default=.0,
            )
    breaks = models.IntegerField(
            null=False,
            blank=False,
            default=0,
            )

    class Meta:
        app_label = 'trainings'

    def __unicode__(self):
        return u'{} from {} performed with {}/{}'.format(
                self.type.name,
                self.plan,
                self.times,
                self.breaks,
                )

    def add_approach(self, times):
        total = self.breaks * self.times + times
        self.breaks += 1
        self.times = total / self.breaks
        self.save()


from django.contrib import admin
admin.site.register(Exercise)
