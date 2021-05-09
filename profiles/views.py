from django.shortcuts import render, get_object_or_404

from .models import UserProfile
from .forms import UserProfileForm


def profile(request):
    """ To display client profile """
    print(request.user.id)
    profile = get_object_or_404(UserProfile, pk=request.user.id)

    if request.method == "POST":
        form = serProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully update Profile!")
        else:
            messages.error(request, "Something is wrong with your form!")
    else:
        form = UserProfileForm(instance=profile)


    form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    template = "profiles/profile.html"
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True
    }
    return render(request, template, context)
