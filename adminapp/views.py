from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import user_passes_test
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from authapp.models import User
from adminapp.forms import UserAdminRegisterForm, UserAdminProfileForm

# Create your views here.


@user_passes_test(lambda u: u.is_superuser)
def index(request):
    return render(request, 'adminapp/admin.html')


# @user_passes_test(lambda u: u.is_superuser)
# def admin_users_read(request):
#     context = {'header': 'Пользователи', 'users': User.objects.all()}
#     return render(request, 'adminapp/admin-users-read.html', context)

class UserListView(ListView):
    model = User
    template_name = 'adminapp/admin-users-read.html'



# @user_passes_test(lambda u: u.is_superuser)
# def admin_users_create(request):
#     if request.method == 'POST':
#         form = UserAdminRegisterForm(data=request.POST, files=request.FILES)
#         if form.is_valid():
#             form.save()
#             # messages.success(request, 'Вы успешно зарегистрировались!')
#             return HttpResponseRedirect(reverse('admin_staff:admin_users_read'))
#         else:
#             print(form.errors)
#     else:
#         form = UserAdminRegisterForm()
#     context = {'header': 'Создание пользователя', 'form': form}
#     return render(request, 'adminapp/admin-users-create.html', context)


class UserCreateView(CreateView):
    model = User
    template_name = 'adminapp/admin-users-create.html'
    form_class = UserAdminRegisterForm
    success_url = reverse_lazy('admin_staff:admin_users_read')




# @user_passes_test(lambda u: u.is_superuser)
# def admin_users_update(request, user_id):
#     selected_user = User.objects.get(id=user_id)
#     if request.method == 'POST':
#         form = UserAdminProfileForm(data=request.POST, files=request.FILES, instance=selected_user)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('admin_staff:admin_users_read'))
#     else:
#         form = UserAdminProfileForm(instance=selected_user)
#     context = {'header': 'Редактирование пользователя','form': form, 'selected_user': selected_user}
#     return render(request, 'adminapp/admin-users-update-delete.html', context)

class UserUpdateView(UpdateView):
    model = User
    template_name = 'adminapp/admin-users-update-delete.html'
    success_url = reverse_lazy('admin_staff:admin_users_read')
    form_class = UserAdminProfileForm


class UserDeleteView(DeleteView):
    model = User
    emplate_name = 'adminapp/admin-users-update-delete.html'
    success_url = reverse_lazy('admin_staff:admin_users_read')


@user_passes_test(lambda u: u.is_superuser)
def admin_users_remove(request, user_id):
    user = User.objects.get(id=user_id)
    if user.is_active:
        user.is_active = False
    else:
        user.is_active = True
    user.save()
    # user.delete() если нужно удалить
    return HttpResponseRedirect(reverse('admin_staff:admin_users_read'))



