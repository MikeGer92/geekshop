from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from authapp.models import User
from adminapp.forms import UserAdminRegisterForm, UserAdminProfileForm

# Create your views here.
def index(request):
    return render(request, 'adminapp/admin.html')


def admin_users_read(request):
    context = {'header': 'Пользователи', 'users': User.objects.all()}
    return render(request, 'adminapp/admin-users-read.html', context)


def admin_users_create(request):
    if request.method == 'POST':
        form = UserAdminRegisterForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            # messages.success(request, 'Вы успешно зарегистрировались!')
            return HttpResponseRedirect(reverse('admin_staff:admin_users_read'))
        else:
            print(form.errors)
    else:
        form = UserAdminRegisterForm()
    context = {'header': 'Создание пользователя', 'form': form}
    return render(request, 'adminapp/admin-users-create.html', context)

def admin_users_update(request, user_id):
    selected_user = User.objects.get(id=user_id)
    if request.method == 'POST':
        form = UserAdminProfileForm(data=request.POST, files=request.FILES, instance=selected_user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admin_staff:admin_users_read'))
    else:
        form = UserAdminProfileForm(instance=selected_user)
    context = {'header': 'Редактирование пользователя','form': form, 'selected_user': selected_user}
    return render(request, 'adminapp/admin-users-update-delete.html', context)

def admin_users_remove(request, user_id):
    user = User.objects.get(id=user_id)
    user.delete()
    return HttpResponseRedirect(reverse('admin_staff:admin_users_read'))


