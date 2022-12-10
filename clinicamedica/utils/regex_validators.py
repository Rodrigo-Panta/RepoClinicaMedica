from django.core.validators import RegexValidator

    
phone_regex = RegexValidator(regex=r'^\d{11}$', message="Número de telefone deve conter 11 dígitos: '(XX) XXXXX XXXX'.")
cep_regex = RegexValidator(regex=r'^\d{8}$', message="CEP deve conter 8 dígitos: 'XX-XXX.XXX'.")
crm_regex = RegexValidator(regex=r'^CRM\/[A-Z][A-Z] d{6}$', message="CRM deve estar no formato: 'CRM/UF XXXXXX'.")
    