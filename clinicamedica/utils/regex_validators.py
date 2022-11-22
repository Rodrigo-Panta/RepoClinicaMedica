from django.core.validators import RegexValidator

    
phone_regex = RegexValidator(regex=r'^\d{11}$', message="Número de telefone deve conter 11 dígitos: '(99) 99999 9999'.")
cep_regex = RegexValidator(regex=r'^\d{8}$', message="CEP deve conter 8 dígitos: '30-444.222'.")
    