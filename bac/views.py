from django.shortcuts import render, redirect
from .forms import BacRegistrationForm
from .models import BacRegistration
from django.shortcuts import render, get_object_or_404, redirect
from .models import BacRegistration
from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponse
from django.template.loader import render_to_string
from .models import BacRegistration
from .forms import UsernameSearchForm
import weasyprint
def register_bac(request):
    if request.method == 'POST':
        # if request.session.get('registered', False):
        #     return render(request, 'success.html', {'username': request.session.get('username')})

        form = BacRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            instance = BacRegistration.objects.get(id=form.instance.id)
            if instance.username is None:
                base_numbers = {
                    'sc': 300000,
                    'math': 400000,
                    'mt': 200000,
                    'lit': 500000,
                }
                base = base_numbers.get(instance.speciality, 600000)
                
                count = BacRegistration.objects.filter(speciality=instance.speciality).count()
                instance.username = base + count + 1
                instance.save()

            # Store registration status and username in session
            request.session['registered'] = True
            request.session['username'] = instance.username

            return render(request, 'success.html', {'username': instance.username})
    else:
        form = BacRegistrationForm()

    return render(request, 'register_bac.html', {'form': form})

@staff_member_required
def admin_dashboard(request):
    registrations = BacRegistration.objects.all()
    return render(request, 'admin_dashboard.html', {'registrations': registrations})

@staff_member_required
def update_status(request, reg_id, new_status):
    registration = get_object_or_404(BacRegistration, id=reg_id)
    if new_status in ['accepted', 'rejected']:
        registration.status = new_status
        registration.save()
    return redirect('admin_dashboard')

def download_admit_card(request):
    if request.method == 'POST':
        form = UsernameSearchForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            try:
                student = BacRegistration.objects.get(username=username, status='accepted')
                html = render_to_string('admit_card.html', {'student': student})
                pdf_file = weasyprint.HTML(string=html).write_pdf()

                response = HttpResponse(pdf_file, content_type='application/pdf')
                response['Content-Disposition'] = f'attachment; filename="استدعاء_{student.username}.pdf"'
                return response
            except BacRegistration.DoesNotExist:
                form.add_error('username', 'رقم التسجيل غير موجود أو لم يتم قبوله بعد.')
    else:
        form = UsernameSearchForm()

    return render(request, 'search_admit_card.html', {'form': form})