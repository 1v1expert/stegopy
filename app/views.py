from django.shortcuts import render, redirect
from app.forms import EncryptForm, DecryptForm
from app.models import Steganographic, MainLog
from app.decorators import a_decorator_passing_logs

header_text = 'StegoPy в качестве ЦВЗ использует QR-код с введёной Вами информацией и ' \
              'используя метод наименее значащего бита (LSB) скрывает его в пикселях RGB ' \
              'фрактального изображения, инициализируемого псевдо-случайными параметрами на ' \
              'множестве Жюлиа. Далее полученный секретный ключ(СК) встраивается в контейнер методом' \
              ' Дармстедтера-Делейгла-Квисквотера-Макка. Данная технология позволяет достичь высокий ' \
              'уровень визуального качества, а различия между оригинальным и заполненным ' \
              'контейнером не заметны человеческому глазу.'


@a_decorator_passing_logs
def index_view(request):
    return render(request, 'index.html',
                  {
                   'header_text': header_text
                  })


@a_decorator_passing_logs
def encrypt_view(request):
    if request.method == 'POST':
        encrypt_form = EncryptForm(request.POST, request.FILES)
        if encrypt_form.is_valid():
            encrypt_form.save()
            try:
                encrypt_form.instance.create_stegocontainer()
            except Exception as e:
                MainLog.objects.create(user=None if str(request.user) == 'AnonymousUser' else request.user,
                                       message=str(encrypt_form.instance.pk),
                                       has_errors=True,
                                       raw=str(e)
                                       )
                return render(request, 'encrypt.html',
                              {'form': encrypt_form,
                               'header_text': header_text,
                               'error': 'Произошла ошибка при формировании стегоконтейнера, обратитесь в поддержку'
                               }
                              )
            return redirect('app:encrypt', encrypt_form.instance.pk)

    encrypt_form = EncryptForm()
    return render(request, 'result.html', {"encrypt_form": encrypt_form})


@a_decorator_passing_logs
def decrypt_view(request, result_id=None):

    decrypt_form = DecryptForm()
    return render(request, 'decrypt.html', {'decrypt_form': decrypt_form})


@a_decorator_passing_logs
def result_view(request, result_id=None):
    if result_id is None:
        return redirect('app:index')
    
    return render(request, 'result.html', {'steganographic': Steganographic.objects.get(pk=result_id)})