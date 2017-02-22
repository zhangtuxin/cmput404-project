from myapp.forms import ProfileForm
from myapp.models import Profile

def SaveProfile(request):
    save = false

    if request.method = "post":
        # Get the posted form
        MyProfileForm = ProfileForm(request.POST, request.FILES)

        if MyProfileForm.is_valid():
            profile = Profile()
            profile.name = MyProfileForm.cleaned_data["name"]
            profile.picture = MyProfileForm.cleaned_data["picture"]
            profile.save()
            save = true

        else:
            MyProfileForm = ProfileForm()

        return render(request, "save.html", locals())
