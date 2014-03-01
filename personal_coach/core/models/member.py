from django.db import models

class Member(models.Model):
    '''Member who uses the system
    '''
    user = models.ForeignKey('auth.User',
            null=True,
            blank=True,
            on_delete=models.PROTECT,
            )
    first_name = models.CharField(
            null=False,
            blank=False,
            max_length=50,
            )
    last_name = models.CharField(
            null=False,
            blank=False,
            max_length=50,
            )

    class Meta:
        app_label = 'core'

    def __unicode__(self):
        return u'{} {}{}'.format(
                self.first_name,
                self.last_name,
                u' ({})'.format(self.user.email) if self.user else u'',
                )


from django.contrib import admin
admin.site.register(Member)
