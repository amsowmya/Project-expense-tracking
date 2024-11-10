from backend import db_helper

import os
import sys


def test_fetch_expenses_for_date_aug_15():
    expences = db_helper.fetch_expenses_for_date("2024-8-15")
    print(expences)
    
    assert len(expences) == 1
    assert expences[0]['amount'] == 10
    assert expences[0]['category'] == "Shopping"
    assert expences[0]['notes'] == "Bought potatoes"
    
def test_fetch_expenses_for_date_invalid_date():
    expenses = db_helper.fetch_expenses_for_date("9999-09-18")
    
    assert len(expenses) == 0
    
def test_fetch_expense_summary_summary_invalid_range():
    summary = db_helper.fetch_expense_summary("2099-02-2", "2099-02-22")
    assert len(summary) == 0