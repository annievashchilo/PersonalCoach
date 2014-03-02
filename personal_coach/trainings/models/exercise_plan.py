from django.db import models


class ExercisePlan(models.Model):
    '''Plan for scheduling exercises
    '''
    member = models.ForeignKey('core.Member',
            null = False,
            blank = False,
            )
    is_finished = models.BooleanField(
            null = False,
            blank = False,
            default = False,
            )
    was_scheduled = models.DateTimeField(
            null=False,
            blank=False,
            )
    was_started = models.DateTimeField(
            null = True,
            blank = True,
            )
    was_stopped = models.DateTimeField(
            null = True,
            blank = True,
            )

    class Meta:
        app_label = 'trainings'

    def __unicode__(self):
        return u'Plan created for {} to {}'.format(
                self.member,
                self.was_scheduled,
                )


from django.contrib import admin
admin.site.register(ExercisePlan)
