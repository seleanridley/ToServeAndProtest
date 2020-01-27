from django import forms
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect

class MemberForm(forms.Form):
    f_name = forms.CharField(max_length=100, label='First Name')
    l_name = forms.CharField(max_length=100, label='Last Name')
    email = forms.CharField(max_length=255, label='Email')
    occupation = forms.CharField(max_length=100, label='Occupation')

def member(request):
    submitted = False
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            #assert False
            return HttpResponseRedirect('/member?submitted=True')
    else:
        form = MemberForm()
        if 'submitted' in request.GET:
            submitted = True

    return render(request, '../templates/member.html', {'form': form, 'submitted': submitted})
