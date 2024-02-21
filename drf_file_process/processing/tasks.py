from time import sleep

from celery import shared_task
from django.core.exceptions import ObjectDoesNotExist

from .models import File


@shared_task
def process_file_task(file_id):
    try:
        print(f'Uploading file {file_id}')
        sleep(3)
        file = File.objects.get(id=file_id)
        file_format = str(file).split('.')[-1]
        if file_format in ('txt', 'doc'):
            print(f'Processing a {file_format} file')
        elif file_format in ('png', 'jpg', 'jpeg'):
            print(f'Processing a {file_format} file')
        elif file_format in ('pdf'):
            print(f'Processing a {file_format} file')
        else:
            print(f'Processing a {file_format} file')

        sleep(3)
        file.processed = True
        file.save()
        print(f'File {file_id} uploaded.')

    except ObjectDoesNotExist:
        print('Object does not exist')

    except Exception as e:
        print('An error occured')
        print(e)
