from django.shortcuts import render

# Create your views here.
def doctor_signup(request):
    doctorForm=forms.DoctorForm()
    mydict={'doctorForm':doctorForm}
    if request.method=='POST':
        doctorForm=forms.DoctorForm(request.POST,request.FILES)
        if  doctorForm.is_valid():
            doctor=doctorForm.save(commit=False)
            doctor.user=user
            doctor=doctor.save()
        return HttpResponseRedirect('login')
    return render(request,'.html',context=mydict)