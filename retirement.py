def _validate_age_month(month):
    month = int(month)

    if month < 0 or month > 11:
        raise ValueError(f'Age month "{month}" must be between 0 and 11')

    return month


def _validate_age_year(year):
    year = int(year)

    if year < 65 or year > 67:
        raise ValueError(f'Age year "{year}" must be between 65 and 67')

    return year


def _validate_birth_month(month):
    month = int(month)

    if month < 1 or month > 12:
        raise ValueError(f'Birth month "{month}" must be between 1 and 12')

    return month


def _validate_birth_year(year):
    year = int(year)

    if year < 1900:
        raise ValueError(f'Birth year "{year}" must be no earlier than 1900')
    elif year >= 3000:
        raise ValueError(f'Birth year "{year}" must be earlier than 3000')

    return year