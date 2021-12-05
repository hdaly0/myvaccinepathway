import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import date, timedelta
from data import az_immunity_series

INITIAL_IMMUNITY = 0
start_date = date(2021, 1, 1)
end_date = date(2022, 12, 31)

daterange_index = pd.date_range(start_date, end_date)

immunity_series = pd.Series(0, index=daterange_index)

print(immunity_series)


class Dose:
    def __init__(self, date, type, dose_number):
        self.dose_date = date
        self.type = type
        self.dose_number = dose_number
        self.peak_immunity_level = Dose.get_peak_immunity_level(self.type, self.dose_number)
        self.peak_immunity_date = Dose.get_peak_immunity_date(self.type, self.dose_number, self.dose_date)

    @staticmethod
    def get_peak_immunity_level(type, dose_number):
        # AZ
        if dose_number <= 0:
            return 0
        if dose_number == 1:
            return 0.45
        return 0.65

    @staticmethod
    def get_peak_immunity_date(type, dose_number, dose_date):
        # AZ
        if dose_number <= 0:
            return dose_date
        if dose_number == 1:
            return dose_date + timedelta(7)
        return dose_date + timedelta(14)

    @staticmethod
    def create_doses(dose_type_pairs):
        doses = []
        for dose_type_pair in dose_type_pairs:
            dose_date, dose_type = dose_type_pair
            doses.append(Dose(dose_date, dose_type, len(doses) + 1))
        return doses


doses = Dose.create_doses([
    (date(2021, 1, 15), "az"),
    (date(2021, 6, 15), "az"),
    (date(2022, 4, 14), "az"),
    (date(2022, 7, 22), "pf"),
])


for dose in doses:
    # Pre immunity
    immunity_delay = int(az_immunity_series.dropna().index[0])
    dose_date = str(dose.dose_date)
    peak_immunity_date = str(dose.dose_date + timedelta(immunity_delay-1))
    peak_immunity_level = az_immunity_series[immunity_delay]

    immunity_series[dose_date: peak_immunity_date] = np.linspace(immunity_series[dose_date], peak_immunity_level, immunity_delay)

    # Post immunity, real data
    vaccine_immunity = az_immunity_series.copy()
    vaccine_immunity.index = pd.date_range(dose.dose_date, dose.dose_date + timedelta(int(vaccine_immunity.index.max())))
    vaccine_immunity = vaccine_immunity.dropna()

    # Could be that immunity_series or vaccine_immunity have a longer end date than the other
    # Avoid errors by choosing the lower of the two
    start_date_to_set = str(vaccine_immunity.index.min())
    max_date_to_set = str(min(max(vaccine_immunity.index), max(immunity_series.index)))
    immunity_series[start_date_to_set: max_date_to_set] = vaccine_immunity[start_date_to_set: max_date_to_set]

    # Plateau data
    immunity_plateau_value = vaccine_immunity.iloc[-1]
    plateau_start_date = max_date_to_set
    plateau_end_date = str(max(immunity_series.index))
    immunity_series[plateau_start_date: plateau_end_date] = immunity_plateau_value

print(immunity_series)
immunity_series.plot()
plt.show()
