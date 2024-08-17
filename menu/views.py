from django.shortcuts import render, redirect
import pandas as pd
from .models import DailyMenu
from django.contrib.auth import login
from .tasks import send_daily_menu_email
from django.contrib.auth.models import User
from django.http import HttpResponse


def process_excel_data():
    file_path = 'C:/Users/bosun.HšSNABOSUN/Downloads/Haziran Ayı Akşam Yemeği Menüsü.xlsx'
    df = pd.read_excel(file_path)

    for index, row in df.iterrows():
        df['Date'] = pd.to_datetime(df['Date'], format='%d.%m.%y')
        DailyMenu.objects.update_or_create(
            Date=row['Date'],
            defaults={
                'soup': row['soup'],
                'main_course1_opt1': row['main_course1_opt1'],
                'main_course1_opt2': row['main_course1_opt2'],
                'main_course2': row['main_course2'],
                'sides': row['sides']
            }
        )


def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        if User.objects.filter(username=username).exists():
            return HttpResponse("Username already exists")
        password = request.POST.get('password')
        email = request.POST.get('email')
        user = User.objects.create_user(
            username=username,
            password=password,
            email=email
        )

        login(request, user)
        process_excel_data()
        send_daily_menu_email.delay()
        return redirect('success')

    return render(request, "signup.html")


def success_view(request):
    return render(request, 'success.html')
