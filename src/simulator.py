import income


def is_end_of_year(month):
    return month % 12 == 0


def run_simulation(length_in_months):
    income_entries = income.load_income_entries_from_file()

    income_for_year = 0
    total_income = 0

    for month in range(1, length_in_months + 1):
        income_for_month = income.calculate_income_for_month(income_entries,
                                                             month)
        income_for_year += income_for_month
        total_income += income_for_month

        if is_end_of_year(month):
            income_for_year = 0
