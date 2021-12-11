import streamlit as st
import pandas as pd
from datetime import date, timedelta
from constants import DEFAULT_JAB_DATE, ALLOWED_VACCINE_TYPES

from computation_functions import get_symptomatic_immunity, create_doses, get_start_and_end_dates
from plotting_functions import get_plotly_timeline, get_plotly_figure
from html_snippets import CURRENT_PRODUCT_STAGE, ASSUMPTIONS, DISCLAIMER, PRODUCT_STAGES

# User input and streamlit page order
st.set_page_config(layout="wide")
st_left, st_centre, st_right = st.columns((1, 4, 1))

# Header
st_centre.markdown(CURRENT_PRODUCT_STAGE, unsafe_allow_html=True)

# Product stage - alpha, beta, gamma
st_centre.markdown(PRODUCT_STAGES, unsafe_allow_html=True)

# Disclaimer
st_centre.markdown(DISCLAIMER, unsafe_allow_html=True)

# Assumptions
st_centre.markdown(ASSUMPTIONS, unsafe_allow_html=True)

# Gather information
st_centre.subheader("Enter your information:")
# TODO: remove? st_centre.markdown("<h4 style='text-align: center;'>Enter your information:</h4>", unsafe_allow_html=True)

number_of_doses = st_centre.number_input("How many jabs have you had?", value=2)

# Use form with submit button so page doesn't recalculate every time, only on submit
with st_centre.form(key='user_info_form'):
    st.write("Input your vaccination details")
    vaccine_type = st.radio("Vaccine type", options=ALLOWED_VACCINE_TYPES)

    dose_dates = []
    # Allow for variable numbers of doses
    for dose_number in range(1, number_of_doses + 1):
        dose_dates.append(
            st.date_input(f"Dose {dose_number} date",
                          value=DEFAULT_JAB_DATE.get(dose_number, date.today() - timedelta(180)))
        )

    submit_button = st.form_submit_button(label='Submit')


# Only load the plots after submit button has been clicked
if submit_button:
    # Get doses and related details
    doses = create_doses(dose_dates, vaccine_type)
    start_date, end_date = get_start_and_end_dates(doses)

    # Get current immunity
    df_symptomatic_immunity = get_symptomatic_immunity(doses, start_date, end_date)

    # Print current immunity levels
    current_symptomatic_immunity_level_lower = df_symptomatic_immunity.loc[str(date.today()), "lower"]
    # current_symptomatic_immunity_level_average = df_symptomatic_immunity.loc[str(date.today()), "average"]
    current_symptomatic_immunity_level_upper = df_symptomatic_immunity.loc[str(date.today()), "upper"]
    # TODO: remove this: st.subheader(f"Your current immunity to symptomatic covid is: {current_symptomatic_immunity_level*100}%")
    st_centre.markdown(f"<hr><h4 style='text-align: center;'>Your current immunity to covid is:</h4>", unsafe_allow_html=True)
    # TODO: Clean this up/create a function for this html
    st_centre.markdown(
        f"<div><h5 style='text-align: center; box-sizing: border-box; float: left; width: 33.33%; padding: 10px;'>"
        f"{current_symptomatic_immunity_level_lower:.0f}-{current_symptomatic_immunity_level_upper:.0f}%"
        f"<br>against getting symptomatic covid</h5>"
        f"<h4 style='text-align: center; box-sizing: border-box; float: left; width: 33.33%; padding: 10px;'>"
        # f"{current_symptomatic_immunity_level_lower:.0f}-{current_symptomatic_immunity_level_upper:.0f}%"
        f"<br>against hospitalisation</h4>"
        f"<h5 style='text-align: center; box-sizing: border-box; float: left; width: 33.33%; padding: 10px;'>"
        # f"{current_symptomatic_immunity_level_lower:.0f}-{current_symptomatic_immunity_level_upper:.0f}%"
        f"<br>against death</h5></div><hr>", unsafe_allow_html=True
    )

    # Plotly
    # Timeline plot
    data_timeline = {
        "dates": dose_dates,
        "values": [0.2]*len(dose_dates),
        "text": [f"Dose {dose_number}" for dose_number in range(1, len(dose_dates) + 1)]
    }
    df_timeline = pd.DataFrame(data_timeline)
    fig_timeline = get_plotly_timeline(df_timeline, start_date, end_date)
    st_centre.plotly_chart(fig_timeline, use_container_width=True)

    # Symptomatic immunity plot
    fig_symptomatic_immunity = get_plotly_figure(df_symptomatic_immunity)
    st_centre.plotly_chart(fig_symptomatic_immunity, use_container_width=True)
