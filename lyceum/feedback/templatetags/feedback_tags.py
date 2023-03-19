import cryptography.fernet
import django.conf
import django.template

register = django.template.Library()


@register.simple_tag(name="id_encode")
def id_encoder(feedback_id):
    f = cryptography.fernet.Fernet(django.conf.settings.KEY32.encode())
    encrypt = f.encrypt(str(feedback_id).encode())
    return encrypt.decode()
