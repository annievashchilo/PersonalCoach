from django.db import models

class TrainingType(models.Model):
    ''' Type of training
    '''
    LOAD_TYPES = (
            ('C', 'cardio',),
            ('P', 'power',),
            ('M', 'mixed',),
            )

    name = models.CharField('Training name',
            null=False,
            blank=False,
            unique=True,
            max_length=50,
            )
    description = models.TextField('Training description',
            null=True,
            blank=True,
            )
    load = models.CharField(
            null=False,
            blank=False,
            choices=LOAD_TYPES,
            max_length=1,
            )

    class Meta:
        app_label='trainings'

    def __unicode__(self):
        return u'{} ({})'.format(
                self.name,
                self.get_load_display(),
                )


from django.contrib import admin
admin.site.register(TrainingType)
