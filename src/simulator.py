import income
import expense
import graphing
import pandas as pd


def run_simulation(length_in_months):
    income_entries = income.load_entries_from_file()
    expense_entries = expense.load_entries_from_file()

    months = pd.DataFrame(columns=["month", "income", "expenses", "net"])
    months["month"] = months["month"].astype(int)
    months["income"] = months["income"].astype(float)
    months["expenses"] = months["expenses"].astype(float)
    months["net"] = months["net"].astype(float)

    for month in range(1, length_in_months + 1):
        income_for_month = income.calculate_income_for_month(income_entries,
                                                             month)
        expenses_for_month = expense.calculate_expenses_for_month(
            expense_entries)

        months = months.append(pd.DataFrame({
            "month": [month],
            "income": [income_for_month],
            "expenses": [expenses_for_month],
            "net": [income_for_month - expenses_for_month]
        }), ignore_index=True)



    graphing.graph(months)
