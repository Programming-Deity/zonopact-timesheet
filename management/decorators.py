from django.shortcuts import redirect, render

def manager_required(view_func):
    def wrapper_func(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        elif not request.user.is_manager:
            return render(request, 'roles/no_access.html')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func

