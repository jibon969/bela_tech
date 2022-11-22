# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.contrib import messages
# from django.urls import reverse
# from django.views.generic import FormView, DetailView, View, UpdateView
# from django.views.generic.edit import FormMixin
# from django.shortcuts import render, redirect, get_object_or_404
# from django.utils.safestring import mark_safe
# from .forms import LoginForm, RegisterForm, ReactivateEmailForm, UserDetailChangeForm
# from .models import EmailActivation, Buyer
# from easy_pdf.views import PDFTemplateResponseMixin
# from django.core.mail import send_mail
# from django.conf import settings
# from htmlmin.decorators import minified_response
# from .models import User
# from django.http.response import HttpResponse
# from django.contrib.auth.decorators import login_required, user_passes_test
# import csv
# from django.db.models import Q
# from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
#
#
# class AccountEmailActivateView(FormMixin, View):
#     """
#     E-mail Activation for register user. default
#     """
#     success_url = '/login/'
#     form_class = ReactivateEmailForm
#     key = None
#
#     def get(self, request, key=None, *args, **kwargs):
#         self.key = key
#         if key is not None:
#             qs = EmailActivation.objects.filter(key__iexact=key)
#             confirm_qs = qs.confirmable()
#             if confirm_qs.count() == 1:
#                 obj = confirm_qs.first()
#                 obj.activate()
#                 messages.success(request, "Your email has been confirmed. Please login.")
#                 print("Your email has been confirmed. Please login.")
#                 return redirect("account:login")
#             else:
#                 activated_qs = qs.filter(activated=True)
#                 if activated_qs.exists():
#                     reset_link = reverse("password_reset")
#                     msg = """Your email has already been confirmed
#                     Do you need to <a href="{link}">reset your password</a>?
#                     """.format(link=reset_link)
#                     messages.success(request, mark_safe(msg))
#                     return redirect("account:login")
#         context = {'form': self.get_form(), 'key': key}
#         return render(request, 'registration/activation-error.html', context)
#
#     def post(self, request, *args, **kwargs):
#         # create form to receive an email
#         form = self.get_form()
#         if form.is_valid():
#             return self.form_valid(form)
#         else:
#             return self.form_invalid(form)
#
#     def form_valid(self, form):
#         msg = """Activation link sent, please check your email."""
#         # print("Activation link sent, please check your email.")
#         request = self.request
#         messages.success(request, msg)
#         email = form.cleaned_data.get("email")
#         obj = EmailActivation.objects.email_exists(email).first()
#         user = obj.user
#         new_activation = EmailActivation.objects.create(user=user, email=email)
#         new_activation.send_activation()
#         return super(AccountEmailActivateView, self).form_valid(form)
#
#     def form_invalid(self, form):
#         context = {'form': form, "key": self.key}
#         return render(self.request, 'registration/activation-error.html', context)
#
#
# class LoginView(NextUrlMixin, RequestFormAttachMixin, FormView):
#     """
#     Retail Login urls: http://127.0.0.1:8000/login/
#     """
#     form_class = LoginForm
#     success_url = '/'
#     template_name = 'accounts/login.html'
#     default_next = '/'
#
#     def form_valid(self, form):
#         # print('working')
#         next_path = self.get_next_url()
#         return redirect(next_path)
#
#
# class RegisterView(FormView):
#     """
#     Retail Register urls : http://127.0.0.1:8000/register/ (not work)
#     """
#     form_class = RegisterForm
#     template_name = 'accounts/register.html'
#     success_url = '/login/'
#
#
# @minified_response
# def signup(request):
#     """
#     This is work for signup
#     Retail Register urls : http://127.0.0.1:8000/register/
#     """
#     if request.method == 'POST':
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.add_message(request, messages.SUCCESS,
#                                  'Registration Successfully Completed,''Check Your Email To Activate Your Account')
#             return redirect('account:login')
#     else:
#         form = RegisterForm()
#     return render(request, 'accounts/register.html', {'form': form})
#
#
# @minified_response
# def buyer_signup(request):
#     """
#     Wholesales register urls
#     http://127.0.0.1:8000/wholesale/register/
#     """
#     if request.method == 'POST':
#         # print('Buyer Registering')
#         form = RegisterForm(request.POST)
#
#         if form.is_valid():
#             user = form.save()
#             # user.is_buyer = True
#             # user.save()
#             messages.success(request, 'Sign Up Successful! Please Verify Your Email.')
#             Buyer.objects.create(user=user)
#             from_email = settings.DEFAULT_FROM_EMAIL
#             send_mail(
#                 'Wholesale User Sign Up',
#                 '{} is recently sign up for wholesale account. Contact: {}'.format(user, user.contact_number),
#                 settings.DEFAULT_FROM_EMAIL,
#                 ['mohibul.delphi@gmail.com', 'help.belasea@gmail.com'],
#
#                 fail_silently=False,
#             )
#             return redirect('wholesale-login')
#     else:
#         form = RegisterForm()
#     return render(request, 'accounts/register.html', {'form': form, 'buyer': 'Mohinur Wholesale'})
#
#
# class BuyerLoginView(NextUrlMixin, RequestFormAttachMixin, FormView):
#     """
#     Wholesales Login : http://127.0.0.1:8000/wholesale/login/?next=/wholesale/
#     """
#     form_class = LoginForm
#     success_url = '/wholesale/'
#     template_name = 'accounts/login.html'
#
#     def get_context_data(self, *args, **kwargs):
#         context = super(BuyerLoginView, self).get_context_data(*args, **kwargs)
#         context['buyer'] = 'Mohinur Wholesale'
#         return context
#
#
# class UserDetailUpdateView(LoginRequiredMixin, UpdateView):
#     """
#     Retail user profile update urls
#     http://127.0.0.1:8000/account/details/
#     """
#     form_class = UserDetailChangeForm
#     template_name = 'accounts/detail-update-view.html'
#
#     def get_object(self):
#         return self.request.user
#
#     def get_context_data(self, *args, **kwargs):
#         context = super(UserDetailUpdateView, self).get_context_data(*args, **kwargs)
#         context['title'] = 'Change Your Account Details'
#         return context
#
#     def get_success_url(self):
#         return reverse("user-profile")
#
#
# @minified_response
# def user_invoice_list(request):
#     """
#     Retails user order invoice list urls
#     http://127.0.0.1:8000/invoice-list/
#     """
#     queryset = Invoice.objects.filter(user=request.user).order_by('-timestamp')
#
#     return render(request, 'accounts/invoice_list.html', {'object_list': queryset})
#
#
# class UserInvoicePDF(LoginRequiredMixin, PDFTemplateResponseMixin, DetailView):
#     """
#     Authenticated user invoice object pdf views urls
#     http://127.0.0.1:8000/invoice-list/
#     """
#     template_name = 'accounts/invoice_detail.html'
#
#     def get_object(self, *args, **kwargs):
#         slug = self.kwargs.get('slug')
#         obj = get_object_or_404(Invoice, slug=slug, user=self.request.user)
#         return obj
#
#
# def app_user(request):
#     if request.user.is_superuser:
#         queryset = User.objects.filter(platform_type="Mobile").order_by('-date_joined')
#         query = request.GET.get('q')
#         if query:
#             # Using strip method to remove extra white space
#             query = query.strip()
#             queryset = User.objects.filter(
#                 Q(contact_number__icontains=query) |
#                 Q(contact_number__startswith=query) |
#                 Q(contact_number__endswith=query)
#
#             ).distinct()
#         page = request.GET.get('page', 1)
#         paginator = Paginator(queryset, 100)
#         try:
#             posts = paginator.page(page)
#         except PageNotAnInteger:
#             posts = paginator.page(1)
#         except EmptyPage:
#             posts = paginator.page(paginator.num_pages)
#
#         context = {
#             'object_list': posts,
#             'page': page,
#             'queryset': queryset.count()
#         }
#         return render(request, "accounts/app_user.html", context)
#
#     else:
#         messages.add_message(request, messages.SUCCESS, "Oops you have no access.")
#         return redirect('account:app-user')
#
#
# def app_user_csv(request):
#     try:
#         if request.user.is_superuser:
#             queryset = User.objects.filter(platform_type="Mobile").order_by('-date_joined')
#             response = HttpResponse(content_type="text/csv")
#             writer = csv.writer(response)
#             writer.writerow([
#                 'ID', 'Contact Number'
#             ])
#             for user in queryset:
#                 row = []
#                 row.extend([
#                     user.id, user.contact_number
#                 ])
#                 writer.writerow(row[:])
#             response['Content-Disposition'] = 'attachment; filename="app_user_csv.csv"'
#             return response
#     except:
#         messages.add_message(request, messages.SUCCESS, "Oops you have no access")
#         return redirect('account:app-user')
