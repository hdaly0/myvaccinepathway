from vaccine_data import *
from typing import List
from datetime import date, timedelta


def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)


def _convert_dates_to_relative_days(start_date, end_date, dose_dates):
    start_day = 0
    end_day = (end_date - start_date).days
    dose_days = [(dose_date - start_date).days for dose_date in dose_dates]
    return start_day, end_day, dose_days


def _linear_plot(start_day, end_day, start_value, end_value):
    """ Inclusive of start day, exclusive of end day """
    day_range = end_day - start_day
    value_change = end_value - start_value
    gradient = value_change/day_range
    linear_values = [start_value + gradient*step for step in range(day_range)]
    return linear_values


def _linear_plot_rate(start_day, end_day, start_value, rate, min_value=0):
    """ Inclusive of start day, exclusive of end day """
    day_range = end_day - start_day
    linear_values = [start_value + rate*step for step in range(day_range)]
    linear_values = [val if val > min_value else min_value for val in linear_values]
    return linear_values


def _calculate_immunity_levels(vaccine, start_day, end_day, dose_days):
    immunity_levels = []

    # If no doses given
    if not dose_days:
        return _linear_plot(start_day, end_day, INITIAL_IMMUNITY_LEVEL, INITIAL_IMMUNITY_LEVEL)

    immunity_levels += _linear_plot(start_day, dose_days[0], INITIAL_IMMUNITY_LEVEL, INITIAL_IMMUNITY_LEVEL)
    immunity_levels += _linear_plot(dose_days[0],
                                    dose_days[0] + DOSE_1_PEAK_IMMUNITY_DAY[vaccine],
                                    INITIAL_IMMUNITY_LEVEL,
                                    DOSE_1_PEAK_IMMUNITY_LEVEL[vaccine])
    immunity_levels += _linear_plot_rate(dose_days[0] + DOSE_1_PEAK_IMMUNITY_DAY[vaccine],
                                         dose_days[1],
                                         DOSE_1_PEAK_IMMUNITY_LEVEL[vaccine],
                                         DOSE_1_IMMUNITY_WANING_RATE[vaccine])
    immunity_levels += _linear_plot(dose_days[1],
                                    dose_days[1] + DOSE_2_PEAK_IMMUNITY_DAY[vaccine],
                                    immunity_levels[-1],
                                    DOSE_2_PEAK_IMMUNITY_LEVEL[vaccine])
    immunity_levels += _linear_plot_rate(dose_days[1] + DOSE_2_PEAK_IMMUNITY_DAY[vaccine],
                                         end_day,
                                         DOSE_2_PEAK_IMMUNITY_LEVEL[vaccine],
                                         DOSE_2_IMMUNITY_WANING_RATE[vaccine])

    return immunity_levels


def get_immunity_level(vaccine: str, start_date: date, end_date: date=date.today(), dose_dates: List[date] = None):
    if not dose_dates:
        dose_dates = []
    assert start_date < end_date, "Start date cannot be after end date"
    assert all([(start_date < dose_date) and (dose_date < end_date) for dose_date in dose_dates]), "Dose dates must be between start and end dates"

    start_day, end_day, dose_days = _convert_dates_to_relative_days(start_date, end_date, dose_dates)
    dates = list(daterange(start_date, end_date))
    immunity_level = _calculate_immunity_levels(vaccine, start_day, end_day, dose_days)

    data = {
        "dates": dates,
        "immunity_level": immunity_level
    }

    return data

