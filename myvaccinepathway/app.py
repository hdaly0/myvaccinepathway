import streamlit as st
import pandas as pd
from datetime import date, timedelta
from constants import DEFAULT_JAB_DATE, ALLOWED_VACCINE_TYPES, ALLWED_IMMUNITY_TYPES, SYMPTOMATIC, HOSPITALISATION, \
    DEATH, ALLOWED_VARIANT_TYPES, OMICRON, MODERNA, DELTA

from computation_functions import get_immunity, create_doses, get_start_and_end_dates
from plotting_functions import get_plotly_timeline, get_plotly_figure, get_plotly_figure_error_bars
from html_snippets import CURRENT_PRODUCT_STAGE, ASSUMPTIONS_DELTA_DATA, DISCLAIMER, PRODUCT_STAGES, \
    ASSUMPTIONS_OMICRON_DATA, MODERNA_OMICRON_DATA_WARNING, MODERNA_DELTA_DATA_WARNING, WHAT_IMMUNITY_LEVEL_MEANS, \
    FAQ, ROADMAP, CURRENT_IMMUNITY_TEXT_LAYOUT_3, CURRENT_IMMUNITY_TEXT_LAYOUT_2, CURRENT_IMMUNITY_TEXT_LAYOUT_1

# User input and streamlit page order
st.set_page_config(layout="wide")
st_left, st_centre, st_right = st.columns((1, 4, 1))

# Header
st_centre.markdown(CURRENT_PRODUCT_STAGE, unsafe_allow_html=True)

# Product stage - alpha, beta, gamma
st_centre.markdown(PRODUCT_STAGES, unsafe_allow_html=True)

# Disclaimer
st_centre.markdown(DISCLAIMER, unsafe_allow_html=True)

# Gather information
st_centre.subheader("Enter your information:")

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
        if (dose_number == 2) and (number_of_doses > 2):
            st.markdown("<p>Note: Jabs 3 and onward are assumed to be Pfizer. See Assumptions</p>",
                               unsafe_allow_html=True)

    variant_type = st.radio("Covid variant", options=ALLOWED_VARIANT_TYPES, index=1)

    submit_button = st.form_submit_button(label='Submit')


# Only load the plots after submit button has been clicked
if submit_button:
    # Present any data warnings for incomplete data
    # Moderna
    if (vaccine_type == MODERNA) and (variant_type == OMICRON):
        st_centre.markdown(MODERNA_OMICRON_DATA_WARNING, unsafe_allow_html=True)

    if (vaccine_type == MODERNA) and (variant_type == DELTA):
        st_centre.markdown(MODERNA_DELTA_DATA_WARNING, unsafe_allow_html=True)

    # Get doses and related details
    doses = create_doses(dose_dates, vaccine_type)
    start_date, end_date = get_start_and_end_dates(doses)

    # Get current immunity
    immunity_dfs = {immunity_type: get_immunity(variant_type, doses, start_date, end_date, immunity_type) for immunity_type in ALLWED_IMMUNITY_TYPES}

    # Print current immunity levels
    current_symptomatic_immunity_level_lower = immunity_dfs[SYMPTOMATIC].loc[str(date.today()), "lower"]
    # current_symptomatic_immunity_level_average = immunity_dfs[SYMPTOMATIC].loc[str(date.today()), "average"]
    current_symptomatic_immunity_level_upper = immunity_dfs[SYMPTOMATIC].loc[str(date.today()), "upper"]

    current_hospitalisation_immunity_level_lower = immunity_dfs[HOSPITALISATION].loc[str(date.today()), "lower"]
    # current_hospitalisation_immunity_level_average = immunity_dfs[HOSPITALISATION].loc[str(date.today()), "average"]
    current_hospitalisation_immunity_level_upper = immunity_dfs[HOSPITALISATION].loc[str(date.today()), "upper"]

    current_death_immunity_level_lower = immunity_dfs[DEATH].loc[str(date.today()), "lower"]
    # current_death_immunity_level_average = immunity_dfs[DEATH].loc[str(date.today()), "average"]
    current_death_immunity_level_upper = immunity_dfs[DEATH].loc[str(date.today()), "upper"]


    # Display information on what immunity levels actually mean
    st_centre.markdown(WHAT_IMMUNITY_LEVEL_MEANS, unsafe_allow_html=True)

    st_centre.markdown(
        CURRENT_IMMUNITY_TEXT_LAYOUT_3.format(
            symptomatic_lower=current_symptomatic_immunity_level_lower,
            symptomatic_upper=current_symptomatic_immunity_level_upper,
            hospitalisation_lower=current_hospitalisation_immunity_level_lower,
            hospitalisation_upper=current_hospitalisation_immunity_level_upper,
            death_lower=current_death_immunity_level_lower,
            death_upper=current_death_immunity_level_upper
        ), unsafe_allow_html=True
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
    fig_symptomatic_immunity = get_plotly_figure(immunity_dfs[SYMPTOMATIC], "Symptomatic infection")
    st_centre.plotly_chart(fig_symptomatic_immunity, use_container_width=True)

    # Hospitalisation plot
    fig_symptomatic_immunity = get_plotly_figure(immunity_dfs[HOSPITALISATION], "Hospitalisation")
    st_centre.plotly_chart(fig_symptomatic_immunity, use_container_width=True)

    # Death plot
    fig_symptomatic_immunity = get_plotly_figure(immunity_dfs[DEATH], "Death")
    st_centre.plotly_chart(fig_symptomatic_immunity, use_container_width=True)

    # Assumptions
    if variant_type == DELTA:
        st_centre.markdown(ASSUMPTIONS_DELTA_DATA, unsafe_allow_html=True)
    if variant_type == OMICRON:
        st_centre.markdown(ASSUMPTIONS_OMICRON_DATA, unsafe_allow_html=True)

    # FAQ
    st_centre.markdown(FAQ, unsafe_allow_html=True)

    # Roadmap
    st_centre.markdown(ROADMAP, unsafe_allow_html=True)
