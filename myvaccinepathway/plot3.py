import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import date, timedelta
from data import *

INITIAL_IMMUNITY = 0
start_date = date(2021, 1, 1)
end_date = date(2022, 12, 31)

daterange_index = pd.date_range(start_date, end_date)

immunity_df = pd.DataFrame(0, columns=COLUMNS, index=daterange_index)
immunity_df.index.name = INDEX

print(immunity_df)


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


doses = [
    Dose(date(2021, 1, 15), ASTRAZENECA, DOSE_1),
    Dose(date(2021, 4, 15), ASTRAZENECA, DOSE_2),
    Dose(date(2022, 5, 14), ASTRAZENECA, DOSE_2),
]


for dose in doses:
    dose_date = str(dose.dose_date)

    # Real data
    # Just symptomatic for now
    vaccine_immunity = dose.get_immunity(SYMPTOMATIC).copy()
    vaccine_immunity.index = pd.date_range(dose.dose_date, dose.dose_date + timedelta(int(vaccine_immunity.index.max())))
    plateau_value = vaccine_immunity.iloc[-1]

    # Piecewise combine series by taking max of two values, and plateau_value for missing values
    immunity_df[dose_date:] = immunity_df[dose_date:].combine(vaccine_immunity[dose_date:], func=np.maximum, fill_value=plateau_value)

# immunity_series = immunity_series.rolling(XYZ).mean()

print(immunity_df)
immunity_df.plot()
plt.show()
