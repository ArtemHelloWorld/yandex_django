import django.core.mail


def send_feedback_mail(text, email):
    message = (f'Спасибо за ваш отзыв!\n'
               f'Мы получили выше обращение '
               f'через форму обратной связи '
               f'со следующим сообщением\n'
               f'{text}\n'
               f'В ближайшее время мы рассмотрим '
               f'ваше обращение и отправим письмо '
               f'с ответом')
    django.core.mail.send_mail(
        subject='Subject',
        message=message,
        from_email=None,
        recipient_list=[email]
    )