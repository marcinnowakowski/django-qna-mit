from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, FormView
from django.views.generic import TemplateView
from .models import Patient, Survey
from .forms import PatientForm, SurveySelectForm

# Create view to register a patient for a survey
class PatientRegisterView(CreateView):
    model = Patient
    form_class = PatientForm
    template_name = 'qna/patient_register.html'

    def get_success_url(self):
        return reverse_lazy('survey_select', kwargs={'patient_number': self.object.patient_number})
      
# Create view to select survey
class SurveySelectView(FormView):
    template_name = 'qna/survey_select.html'
    form_class = SurveySelectForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Fetch the recently created or selected patient by patient_number
        patient_number = self.kwargs.get('patient_number')
        context['patient_selected_model'] = get_object_or_404(Patient, patient_number=patient_number)
        return context
    
    def form_valid(self, form):
        # Access form data
        survey_selected = form.cleaned_data['survey_selected']

        # Save survey or perform additional logic if needed
        self.object = survey_selected  # Save the selected survey for use in success_url
        return super().form_valid(form)

    def get_success_url(self):
        # Get patient_number from URL kwargs
        patient_number = self.kwargs.get('patient_number')

        return reverse_lazy('survey_submission_create', kwargs={
            'patient_number': patient_number,
            'survey_selected': self.object.slug,  # Use the primary key of the selected survey
        })

# Create view to dispaly survey submission create
class SurveySubmissionCreateView(TemplateView):
    template_name = 'qna/survey_submission_create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Fetch the recently created or selected patient by patient_number
        patient_number = self.kwargs.get('patient_number')
        context['patient_selected_model'] = get_object_or_404(Patient, patient_number=patient_number)
        
        # Fetch the recently created or selected patient by patient_number
        survey_selected_slug = self.kwargs.get('survey_selected')
        context['survey_selected_model'] = get_object_or_404(Survey, slug=survey_selected_slug)
        return context
