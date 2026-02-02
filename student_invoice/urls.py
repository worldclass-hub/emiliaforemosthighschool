from django.urls import path
from django.conf.urls.i18n import set_language
from django.views.generic import RedirectView

from . import views  # Make sure to import views here

urlpatterns = [
  
    # Redirect default Django login URL to your custom login page
    path('accounts/login/', RedirectView.as_view(pattern_name='login_page', permanent=False)),
    
    # Authentication
    path('login/', views.login_view, name='login_page'),
    path('logout/', views.logout_view, name='logout'),
    
    # Main page (protected with login_required)
    path('general_exam_page/', views.general_exam_page, name="general_exam_page"),
    path('', views.dashboard_exam_page, name="dashboard_exam_page"),

    path('term_end_account/', views.term_end_account, name="term_end_account"),
    path('new_term_bill_payment/', views.new_term_bill_payment, name="new_term_bill_payment"),


    path('student_id_maker/', views.student_id_maker, name="student_id_maker"),


    path('student_report_card_maker/', views.student_report_card_maker, name="student_report_card_maker"),


    path('ss1_exam_result_view', views.ss1_exam_result_view, name='ss1_exam_result'),
    path('ss2_exam_result_view', views.ss2_exam_result_view, name='ss2_exam_result'),
    path('ss3_exam_result_view', views.ss3_exam_result_view, name='ss3_exam_result'),
    path('jss1_exam_result_view', views.jss1_exam_result_view, name='jss1_exam_result'),
    path('jss2_exam_result_view', views.jss2_exam_result_view, name='jss2_exam_result'),
    path('jss3_exam_result_view', views.jss3_exam_result_view, name='jss3_exam_result'),
    path('general/staff_broadsheet/', views.staff_broadsheet, name='staff_broadsheet'),

    path('student_result_search/', views.student_result_search, name="student_result_search"),
    
    # Core functions
    path('search/', views.search_result, name='search'),
    path('download/', views.download_pdf, name='download'),
    path('preview/', views.preview_pdf, name='preview'),
    
    # Session management
    path('get_sessions/', views.get_sessions, name='get_sessions'),
    path('generate_sessions/', views.generate_sessions, name='generate_sessions'),
    
    # Testing and debugging
    path('test/', views.test_folder_structure, name='test_folder_structure'),
    path('status/', views.system_status, name='status'),
    path('debug/', views.debug_search, name='debug'),
    path('batch_test/', views.batch_test, name='batch_test'),
    
    # API documentation/health check
    path('api/health/', views.system_status, name='api_health'),
    path('student_result_search/', views.student_result_search, name="student_result_search"),
    
    # Core functions
    path('search/', views.search_result, name='search'),
    path('download/', views.download_pdf, name='download'),
    path('preview/', views.preview_pdf, name='preview'),
    
    # Session management
    path('get_sessions/', views.get_sessions, name='get_sessions'),
    path('generate_sessions/', views.generate_sessions, name='generate_sessions'),
    
    # Testing and debugging
    path('test/', views.test_folder_structure, name='test_folder_structure'),
    path('status/', views.system_status, name='status'),
    path('debug/', views.debug_search, name='debug'),
    path('batch_test/', views.batch_test, name='batch_test'),
    
    # API documentation/health check
    path('api/health/', views.system_status, name='api_health'),

   
]



