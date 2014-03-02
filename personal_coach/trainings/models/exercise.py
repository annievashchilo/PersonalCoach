from django.db import models
from datetime import datetime
from pytz import utc


class Exercise(models.Model):
    '''Excercise that someone has performed
    '''
    member = models.ForeignKey('core.Member',
            null=False,
            blank=False,
            on_delete=models.CASCADE,
            )
    type = models.ForeignKey('trainings.TrainingType',
            null=False,
            blank=False,
            on_delete=models.PROTECT,
            )
    was_started = models.DateTimeField(
            null=False,
            blank=False,
            auto_now_add=True,
            )
    was_stopped = models.DateTimeField(
            null=True,
            blank=True,
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
    is_finished = models.BooleanField(
            null=False,
            blank=False,
            default=False,
            )

    class Meta:
        app_label = 'trainings'

    def __unicode__(self):
        return u'{} performed {} with {}/{} from {} till {}'.format(
                self.member,
                self.type.name,
                self.times,
                self.breaks,
                self.was_started,
                self.was_stopped,
                )

    def add_approach(self, times):
        if not self.is_finished:
            total = self.breaks * self.times + times
            self.breaks += 1
            self.times = total / self.breaks
            self.save()

    def save(self, last=False, *args, **kwargs):
        if last and not self.is_finished:
            self.was_stopped = datetime.utcnow().replace(tzinfo=utc)
            self.is_finished = True
        
        super(Exercise, self).save(*args, **kwargs)


from django.contrib import admin
admin.site.register(Exercise)
