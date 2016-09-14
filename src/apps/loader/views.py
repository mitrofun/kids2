from django.shortcuts import render_to_response
from django.template import RequestContext
from loader.forms import UploadFileForm
from loader.handler import loader
from django.conf import settings


def upload(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            on_date = form.cleaned_data['load_date']
            file_handle = request.FILES['file']
            data = file_handle.get_array()

            loader(data[settings.EXCEL_START_STRING:], on_date)

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
