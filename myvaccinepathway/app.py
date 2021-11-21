import streamlit as st
import pandas as pd
from datetime import date, timedelta
import plotly.express as px

from functions import get_immunity_level
from vaccine_data import *
from html_snippets import *

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
# TODO: remove? st_centre.markdown("<h4 style='text-align: center;'>Enter your information:</h4>", unsafe_allow_html=True)

number_of_doses = st_centre.number_input("How many jabs have you had?", value=2)

# Use form with submit button so page doesn't recalculate every time, only on submit
with st_centre.form(key='user_info_form'):
    st.write("Input your vaccination details")
    vaccine = st.radio("Vaccine type", options=[PFIZER, AZ, MODERNA])
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

# Print current immunity levels
current_symptomatic_immunity_level = df_symptomatic_immunity.set_index("dates").loc[date.today()]["immunity_level"]
# TODO: remove this: st.subheader(f"Your current immunity to symptomatic covid is: {current_symptomatic_immunity_level*100}%")
st_centre.markdown(f"<hr><h4 style='text-align: center;'>Your current immunity to symptomatic covid is: {current_symptomatic_immunity_level*100:.1f}%</h1><hr>", unsafe_allow_html=True)

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
fig_timeline.update_xaxes(range=[start_date, end_date], showgrid=False, title="", fixedrange=True)
fig_timeline.update_yaxes(range=[-0.2, 1], showgrid=False, title="", showticklabels=False, fixedrange=True)
fig_timeline.update_traces(marker={"symbol": "triangle-down"}, marker_size=20, textposition="top center")
fig_timeline.update_layout(hovermode=False, plot_bgcolor="rgba(0,0,0,0)")

st_centre.plotly_chart(fig_timeline, use_container_width=True)

# Symptomatic immunity plot
fig_symptomatic_immunity = px.line(df_symptomatic_immunity, x="dates", y="immunity_level",
                                   labels={"dates": "Date", "immunity_level": "Immunity Level"},
                                   title="Immunity from Symptomatic infection")
fig_symptomatic_immunity.update_xaxes(showspikes=True, spikecolor="white", spikethickness=0.5, spikesnap="cursor", spikemode="across", fixedrange=True)
fig_symptomatic_immunity.update_yaxes(tickformat=".1%", range=[0, 1], fixedrange=True)
fig_symptomatic_immunity.update_layout(spikedistance=1000, hovermode="x")
fig_symptomatic_immunity.update_traces(mode="lines", hovertemplate=None)

st_centre.plotly_chart(fig_symptomatic_immunity, use_container_width=True)
