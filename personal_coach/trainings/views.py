from django.shortcuts import render

from trainings.models import TrainingType

def display_type(request, type_id=None):
    ''' Diplay type or all types
    '''
    query = {}
    if type_id:
        query['pk'] = int(type_id)

    context = {
            'training_types': TrainingType.objects.filter(**query),
            }

    return render(request, 'trainings/type.html', context)
