from django.contrib.auth import login
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect
from management.decorators import manager_required
from .models import Role, Department
from django.contrib import messages
from django.core.paginator import Paginator
from .models import CustomUser
from .forms import RoleForm, RegistrationForm
from django.contrib import messages, auth



def is_manager(user):
    return user.is_authenticated and user.role == 'manager'

@login_required
@manager_required
# @user_passes_test(is_manager)
def dashboard(request,):
    roles = Role.objects.all()
    dept = CustomUser.objects.filter(department=1)
    count_dept = dept.count()

    # Search functionality
    search_query = request.GET.get('search', '')
    if search_query:
        roles = roles.filter(name__icontains=search_query)

    paginator = Paginator(roles, 10)  # Paginate roles, 10 per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'roles/management_dashboard.html', {'page_obj': page_obj, 'search_query': search_query, 'count_dept':count_dept})


@login_required
@manager_required
def add_role(request):
    if request.method == 'POST':
        form = RoleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('role_list')
    else:
        form = RoleForm()
        return render(request, 'roles/add_role.html', context={'form': form})


def registerUser(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You are now register and can log in')
            return redirect('login')
            
    else:
        form = RegistrationForm()
    return render(request, 'roles/register.html', context={'form': form})
        

def loginUser(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('login')
    else:
        return render(request, 'roles/login.html')