from  rest_framework.serializers import ValidationError
SCAM_WORDS = ['крипта', 'биржа', 'продам']


def validator_words(value):

    if set(value.lower().split()) & set(SCAM_WORDS):
        raise ValidationError('Недопустимое слово')




