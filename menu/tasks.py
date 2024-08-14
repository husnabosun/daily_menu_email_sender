from celery import shared_task
from django.core.mail import send_mail
import pytz
from datetime import datetime
from django.conf import settings
from menu.models import DailyMenu
from django.contrib.auth.models import User


@shared_task
def send_daily_menu_email():
    utc_now = datetime.utcnow().replace(tzinfo=pytz.utc)
    local_tz = pytz.timezone('Europe/Istanbul')
    local_time = utc_now.astimezone(local_tz)
    today = local_time.date()
    menu = DailyMenu.objects.filter(Date=today).first()
    if menu:
        subject = f"Today's KYK Dinner Menu {menu.Date}"
        message = (
            f"Soup: {menu.soup}\n"
            f"Main Course 1 : {menu.main_course1_opt1}\n"
            f"Main Course 1 Vegetarian Option: {menu.main_course1_opt2}\n"
            f"Main Course 2: {menu.main_course2}\n"
            f"Sides/Desserts : {menu.sides}\n\n"
            f"Enjoy Your Meal!\n\n"
        )
        send_email_to_all_users(subject, message)
        return "Email sent successfully"
    return "No menu found for today"


def send_email_to_all_users(subject, message):
    users = User.objects.all()
    sender_email = settings.EMAIL_HOST_USER
    for user in users:
        send_mail(subject, message, sender_email, [user.email])