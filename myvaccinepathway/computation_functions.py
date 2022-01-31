import pandas as pd
import numpy as np
from datetime import date, timedelta

from constants import COLUMNS, INDEX, PFIZER, DOSE_2, DOSE_1, BOOSTER_TYPE_FROM_VACCINE_MAP
from data import get_immunity_raw


class Dose:
    def __init__(self, date, vaccine_type, dose_number):
        self.dose_date = date
        self.dose_number = dose_number
        self.vaccine_type = vaccine_type

        self.immunity = get_immunity_raw(self.dose_number, self.vaccine_type)

    def get_immunity(self, variant_type, immunity_type):
        return self.immunity[variant_type][immunity_type]

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


def get_immunity(variant_type, doses, start_date, end_date, immunity_type):
    daterange_index = pd.date_range(start_date, end_date)

    immunity_df = pd.DataFrame(0, columns=COLUMNS, index=daterange_index)
    immunity_df.index.name = INDEX

    for dose in doses:
        dose_date = str(dose.dose_date)

        # Real data
        vaccine_immunity = dose.get_immunity(variant_type, immunity_type).copy()
        vaccine_immunity.index = pd.date_range(dose.dose_date, dose.dose_date + timedelta(int(vaccine_immunity.index.max())))
        plateau_values = vaccine_immunity.iloc[-1]

        # Piecewise combine series by taking max of two values, and plateau_value for missing values
        for col in immunity_df.columns:
            immunity_df.loc[dose_date:, col] = immunity_df.loc[dose_date:, col].combine(vaccine_immunity.loc[dose_date:, col], func=np.fmax, fill_value=plateau_values[col])

    # immunity_df = immunity_df.rolling(30).mean()

    return immunity_df


def create_doses(dose_dates, primary_vaccine_type, secondary_vaccine_type):
    if (len(dose_dates) > 2) and (secondary_vaccine_type is None):
        raise ValueError(
            "Have more than two doses but no secondary vaccine type. Internal logic error must have caused this."
        )

    doses = []
    for dose_number, dose_date in enumerate(dose_dates, start=1):
        if dose_number == 1:
            dose_number_reference = DOSE_1
        elif dose_number == 2:
            dose_number_reference = DOSE_2
        else:
            dose_number_reference = BOOSTER_TYPE_FROM_VACCINE_MAP[secondary_vaccine_type]
        dose = Dose(dose_date, primary_vaccine_type, dose_number_reference)
        doses.append(dose)

    return doses
