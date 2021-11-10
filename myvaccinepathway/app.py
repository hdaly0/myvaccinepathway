import streamlit as st
import pandas as pd
from datetime import date, timedelta
import plotly.express as px
from typing import List


def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)


INITIAL_IMMUNITY_LEVEL = 0

PFIZER = "pfizer"
AZ = "astrazeneca"
MODERNA = "moderna"


DOSE_1_PEAK_IMMUNITY_LEVEL = {
    PFIZER: 0.3,
    AZ: 0.33,  # Dummy value
    MODERNA: 0.3,  # Dummy value
}
DOSE_2_PEAK_IMMUNITY_LEVEL = {
    PFIZER: 0.95,
    AZ: 0.7,  # Dummy value
    MODERNA: 0.95,  # Dummy value
}
DOSE_PEAK_IMMUNITY_LEVEL = [DOSE_1_PEAK_IMMUNITY_LEVEL, DOSE_2_PEAK_IMMUNITY_LEVEL]


DOSE_1_PEAK_IMMUNITY_DAY = {
    PFIZER: 12,
    AZ: 12,  # Dummy value
    MODERNA: 12,  # Dummy value
}
DOSE_2_PEAK_IMMUNITY_DAY = {
    PFIZER: 7,
    AZ: 7,  # Dummy value
    MODERNA: 7,  # Dummy value
}
DOSE_PEAK_IMMUNITY_DAY = [DOSE_1_PEAK_IMMUNITY_DAY, DOSE_2_PEAK_IMMUNITY_DAY]


DOSE_1_IMMUNITY_WANING_RATE = {
    PFIZER: -0.001,  # Dummy value
    AZ: -0.001,  # Dummy value
    MODERNA: -0.001,  # Dummy value
}
DOSE_2_IMMUNITY_WANING_RATE = {
    PFIZER: -0.001,  # Dummy value
    AZ: -0.001,  # Dummy value
    MODERNA: -0.001,  # Dummy value
}
DOSE_IMMUNITY_WANING_RATE = [DOSE_1_IMMUNITY_WANING_RATE, DOSE_2_IMMUNITY_WANING_RATE]


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


# User input and streamlit page order
st.title("My Vaccine Pathway")

# Use form with submit button so page doesn't recalculate every time, only on submit
with st.form(key='user_info_form'):
    st.write("Input your vaccination details")
    vaccine = st.selectbox("Vaccine type", options=[PFIZER, AZ, MODERNA])
    dose_1 = st.date_input("Dose 1 date", value=date.today() - timedelta(120))
    dose_2 = st.date_input("Dose 2 date", value=date.today() - timedelta(30))
    submit_button = st.form_submit_button(label='Submit')

start_date = dose_1 - timedelta(10)
end_date = date.today() + timedelta(10)

# Calculations
data = get_immunity_level(vaccine, start_date, end_date, [dose_1, dose_2])
df = pd.DataFrame(data)

df["immunity_level_percentage"] = df["immunity_level"]*100

# st.line_chart(df[["immunity_level_percentage", "dates"]].set_index("dates"))

# Plotly
fig = px.line(df, x="dates", y="immunity_level_percentage",
              range_y=[0, 100],
              labels={"dates": "Date", "immunity_level_percentage": "Immunity Level %"})
# fig.update_yaxes(showspikes=True, spikecolor="white", spikethickness=0.5, spikesnap="cursor", spikemode="across")
fig.update_xaxes(showspikes=True, spikecolor="white", spikethickness=0.5, spikesnap="cursor", spikemode="across")
fig.update_layout(spikedistance=1000, hoverdistance=100)
st.plotly_chart(fig)

