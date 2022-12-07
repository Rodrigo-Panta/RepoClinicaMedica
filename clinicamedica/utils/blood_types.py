from enum import Enum

class BloodTypeEnum(Enum):
    A_NEG = 'A-'
    A_POS = 'A+'
    B_NEG = 'B-'
    B_POS = 'B+'
    O_NEG = 'O-'
    O_POS = 'O+'
    AB_NEG = 'AB-'
    AB_POS = 'AB+'

blood_types = [
   (bt.value,bt.value) for bt in BloodTypeEnum
]