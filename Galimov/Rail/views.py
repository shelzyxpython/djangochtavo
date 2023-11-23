from django.shortcuts import render


def home(request):
    kwargs = {
        'fio': 'Галимов Раиль Расимович',
        'age': '16 годиков',
        'interests': 'Поспать'
    }
    return render(request, 'home.html', kwargs)


def about(request):
    kwargs = {
        'origin': 'г. Азнакаево',
        'performance': 'Почти не тупой',
        'study': 'Ну вроде люблю учебу, а вроде и нет'
    }
    return render(request, 'about.html', kwargs)


def contacts(request):
    kwargs = {
        'github': 'https://github.com/shelzyxpython/djangochtavo',
        'contact_info': 'Отсутствуют'
    }
    return render(request, 'contacts.html', kwargs)
