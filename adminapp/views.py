from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from authapp.models import User
from adminapp.forms import UserAdminRegisterForm

# Create your views here.
def index(request):
    return render(request, 'adminapp/admin.html')


def admin_users_read(request):
    context = {'users':User.objects.all()}
    return render(request, 'adminapp/admin-users-read.html', context)


def admin_users_create(request):
    if request.method == 'POST':
        form = UserAdminRegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            # messages.success(request, 'Вы успешно зарегистрировались!')
            return HttpResponseRedirect(reverse('admin_staff:admin_users_read'))
        else:
            print(form.errors)
    else:
        form = UserAdminRegisterForm()
    context = {'form': form}
    return render(request, 'adminapp/admin-users-create.html', context)



