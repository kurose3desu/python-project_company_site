# login_action
忘れたとき用の仕様
cd login_action
python manage.py migrate
python manage.py runserver

pip install "django-anymail[mailgun]"


#テストメール用↓

python manage.py shell

from django.core.mail import send_mail

send_mail("テスト", "テストメールです。", "送信者 <from@example.com>", ["shunshun.dev@gmail.com"])# login_action
