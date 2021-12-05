import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import date, timedelta
from data import DOSE_1, DOSE_2, BOOSTER, ASTRAZENECA, PFIZER, MODERNA, SYMPTOMATIC, HOSPITALISATION, DEATH, get_immunity_specific_immunity_type

INITIAL_IMMUNITY = 0
start_date = date(2021, 1, 1)
end_date = date(2022, 12, 31)

daterange_index = pd.date_range(start_date, end_date)

immunity_series = pd.Series(0, index=daterange_index)

print(immunity_series)


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


doses = [
    Dose(date(2021, 1, 15), PFIZER, DOSE_1),
    Dose(date(2021, 4, 15), PFIZER, DOSE_2),
    Dose(date(2022, 5, 14), PFIZER, DOSE_2),
]


for dose in doses:
    # Just symptomatic for now
    immunity = dose.get_immunity(SYMPTOMATIC)

    # Pre immunity
    immunity_delay = int(immunity.dropna().index[0])
    dose_date = str(dose.dose_date)
    peak_immunity_date = str(dose.dose_date + timedelta(immunity_delay-1))
    peak_immunity_level = immunity[immunity_delay]

    immunity_series[dose_date: peak_immunity_date] = np.linspace(immunity_series[dose_date], peak_immunity_level, immunity_delay)

    # Post immunity, real data
    vaccine_immunity = immunity.copy()
    vaccine_immunity.index = pd.date_range(dose.dose_date, dose.dose_date + timedelta(int(vaccine_immunity.index.max())))
    plateau_value = vaccine_immunity.iloc[-1]

    # Piecewise combine series by taking max of two values, and plateau_value for missing values
    immunity_series[dose_date:] = immunity_series[dose_date:].combine(vaccine_immunity[dose_date:], max, plateau_value)

print(immunity_series)
immunity_series.plot()
plt.show()
