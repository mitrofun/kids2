from django.shortcuts import render_to_response
from django.template import RequestContext
from loader.forms import UploadFileForm
from loader.handler import loader
from django.conf import settings
from loader.validators import get_extension
import pyexcel
import os


def upload(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            on_date = form.cleaned_data['load_date']
            file_handle = request.FILES['file']
            tmp_name_file = 'tmp' + get_extension(file_handle)
            path = "{}/{}".format(settings.MEDIA_ROOT, tmp_name_file)
            data = pyexcel.get_array(file_name=path)
            loader(data[settings.EXCEL_START_STRING:], on_date)
            os.remove(path)
            return render_to_response(
                'loader/index.html',
                {
                    'message': 'Данные загруженны',
                    'message_type': 'success',
                    'form': form,
                },
                context_instance=RequestContext(request))
        else:
            return render_to_response(
                'loader/index.html',
                {
                    'message': 'Ошибка загрузки',
                    'message_type': 'danger',
                    'form': form,
                },
                context_instance=RequestContext(request))

    else:
        form = UploadFileForm()

    return render_to_response(
        'loader/index.html',
        {'form': form},
        context_instance=RequestContext(request))