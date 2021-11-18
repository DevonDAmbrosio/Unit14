import pytest
from pytest_bdd import scenarios, parsers, given, when, then

from retirement import _validate_birth_year

scenarios('../features/retirement.feature')

EXTRA_TYPES = {'Number': int}
CONVERTERS = {'year': int}


@when(parsers.cfparse('user gives "{year: Number}"', extra_types=EXTRA_TYPES), target_fixture='given_year')
@when('user gives "<year>"')
def given_year(year):
    return _validate_birth_year(year)


@then(parsers.cfparse('"{year: Number}" will be returned', extra_types=EXTRA_TYPES))
@then('"<year>" will be returned')
def valid(given_year, year):
    assert given_year == year


@when(parsers.cfparse('user gives "{year: Number}"', extra_types=EXTRA_TYPES), target_fixture='year_given')
@when('user give "<year>"')
def year_given(year):
    return _validate_birth_year(year)


@then(parsers.cfparse('"{year: Number}" will be returned', extra_types=EXTRA_TYPES))
@then("ValueError will be returned")
def invalid(year_given):
    with pytest.raises(ValueError):
        assert _validate_birth_year(year_given)
