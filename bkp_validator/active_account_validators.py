from rest_framework import serializers


def inactive_account_if_closure_date_validate(closure_date, active_account: bool) -> bool:
    '''There can only be a closure date if the account is inactive'''
    if active_account and closure_date != None:
        return False
    else:
        return True


def closure_date_if_inactive_account_validate(closure_date, active_account: bool) -> bool:
    '''It's required to inform a closure date if the account is inactive'''
    if not active_account and closure_date == None:
        return False
    else:
        return True


def inactive_account_if_balance_zero(active_account: bool) -> bool:
    '''It's only possible to inactivate an account if the current balance is equal to 0'''
    balance = serializers.ReadOnlyField(source='balance.balance')
    if not active_account and balance != 0:
        return False
    else:
        return True
