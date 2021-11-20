import streamlit as st
import pandas as pd
from datetime import date, timedelta
import plotly.express as px
from typing import List
from vaccine_data import *

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


# User input and streamlit page order
st.set_page_config(layout="wide")

st.title("My Vaccine Pathway")

number_of_doses = st.number_input("How many jabs have you had?", value=2)

# Use form with submit button so page doesn't recalculate every time, only on submit
with st.form(key='user_info_form'):
    st.write("Input your vaccination details")
    vaccine = st.selectbox("Vaccine type", options=[PFIZER, AZ, MODERNA])
    dose_dates = []
    # Allow for variable numbers of doses
    for dose_number in range(1, number_of_doses + 1):
        dose_dates.append(st.date_input(f"Dose {dose_number} date",
                                        value=date.today() - timedelta(DEFAULT_JAB_DATE_OFFSET.get(dose_number, 0))))
    submit_button = st.form_submit_button(label='Submit')

# TODO: Remove this hardcoding
dose_1 = dose_dates[0]
dose_2 = dose_dates[1]

start_date = dose_1 - timedelta(10)
end_date = date.today() + timedelta(10)

# Calculations
data_symptomatic_immunity = get_immunity_level(vaccine, start_date, end_date, [dose_1, dose_2])
df_symptomatic_immunity = pd.DataFrame(data_symptomatic_immunity)


# Plotly
# Timeline plot
data_timeline = {
    "dates": dose_dates,
    "values": [0.2]*len(dose_dates),
    "text": [f"Dose {dose_number}" for dose_number in range(1, len(dose_dates) + 1)]
}
df_timeline = pd.DataFrame(data_timeline)
fig_timeline = px.scatter(df_timeline, x="dates", y="values",
                          text="text",
                          height=250,
                          title="My vaccine timeline")
fig_timeline.update_xaxes(range=[start_date, end_date], showgrid=False, title="")
fig_timeline.update_yaxes(range=[-0.2, 1], showgrid=False, title="", showticklabels=False)
fig_timeline.update_traces(marker={"symbol": "triangle-down"}, marker_size=20, textposition="top center")
fig_timeline.update_layout(hovermode=False, plot_bgcolor="rgba(0,0,0,0)")

st.plotly_chart(fig_timeline, use_container_width=True)

# Symptomatic immunity plot
fig_symptomatic_immunity = px.line(df_symptomatic_immunity, x="dates", y="immunity_level",
                                   labels={"dates": "Date", "immunity_level": "Immunity Level"},
                                   title="Immunity from Symptomatic infection")
fig_symptomatic_immunity.update_xaxes(showspikes=True, spikecolor="white", spikethickness=0.5, spikesnap="cursor", spikemode="across")
fig_symptomatic_immunity.update_yaxes(tickformat=".1%", range=[0, 1])
fig_symptomatic_immunity.update_layout(spikedistance=1000, hovermode="x")
fig_symptomatic_immunity.update_traces(mode="lines", hovertemplate=None)

st.plotly_chart(fig_symptomatic_immunity, use_container_width=True)
