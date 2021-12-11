import pandas as pd
import numpy as np
from datetime import date, timedelta

from constants import COLUMNS, INDEX, SYMPTOMATIC, PFIZER, DOSE_2, DOSE_1
from data import get_immunity_specific_immunity_type


class Dose:
    def __init__(self, date, vaccine_type, dose_number):
        self.dose_date = date
        self.dose_number = dose_number
        self.vaccine_type = vaccine_type

        # TODO: reintroduce this when all data present
        # self.immunity = get_immunity(self.dose_number, self.vaccine_type)

    # TODO: replace this with call in constructor once all data present
    def get_immunity(self, immunity_type):
        return get_immunity_specific_immunity_type(self.dose_number, self.vaccine_type, immunity_type)

    @staticmethod
    def create_doses(dose_type_pairs):
        doses = []
        for dose_type_pair in dose_type_pairs:
            dose_date, dose_type = dose_type_pair
            doses.append(Dose(dose_date, dose_type, len(doses) + 1))
        return doses

    def __str__(self):
        return f"{self.vaccine_type} {self.dose_number}: {self.dose_date}"

    def __repr__(self):
        return self.__str__()


def get_start_and_end_dates(doses):
    if not doses:
        min_date = max_date = date.today()
    else:
        min_date = min(doses[0].dose_date, date.today())
        max_date = max(doses[-1].dose_date, date.today())

    start_date = min_date - timedelta(30)
    end_date = max_date + timedelta(30)

    return start_date, end_date


def get_symptomatic_immunity(doses, start_date, end_date):
    daterange_index = pd.date_range(start_date, end_date)

    immunity_df = pd.DataFrame(0, columns=COLUMNS, index=daterange_index)
    immunity_df.index.name = INDEX

    for dose in doses:
        dose_date = str(dose.dose_date)

        # Real data
        # Just symptomatic for now
        vaccine_immunity = dose.get_immunity(SYMPTOMATIC).copy()
        vaccine_immunity.index = pd.date_range(dose.dose_date, dose.dose_date + timedelta(int(vaccine_immunity.index.max())))
        plateau_values = vaccine_immunity.iloc[-1]

        # Piecewise combine series by taking max of two values, and plateau_value for missing values
        for col in immunity_df.columns:
            immunity_df.loc[dose_date:, col] = immunity_df.loc[dose_date:, col].combine(vaccine_immunity.loc[dose_date:, col], func=np.fmax, fill_value=plateau_values[col])

    # immunity_df = immunity_df.rolling(30).mean()

    return immunity_df


def create_doses(dose_dates, vaccine_type):
    doses = []
    for dose_number, dose_date in enumerate(dose_dates, start=1):
        if dose_number == 1:
            current_vaccine_type = vaccine_type
            dose_number_reference = DOSE_1
        elif dose_number == 2:
            current_vaccine_type = vaccine_type
            dose_number_reference = DOSE_2
        else:
            # Booster jabs are Pfizer
            current_vaccine_type = PFIZER
            dose_number_reference = DOSE_2
        dose = Dose(dose_date, current_vaccine_type, dose_number_reference)
        doses.append(dose)

    return doses
