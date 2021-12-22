from datetime import date

# Variant type
DELTA = "Delta"
OMICRON = "Omicron"
ALLOWED_VARIANT_TYPES = [DELTA, OMICRON]

# Dose number
DOSE_1 = "dose_1"
DOSE_2 = "dose_2"
# DOSE_3_PLUS = DOSE_2  # Use immunity data from dose 2 for all future doses
BOOSTER = "booster"
ALLOWED_DOSE_NUMBERS = [DOSE_1, DOSE_2, BOOSTER]

# Vaccine type
ASTRAZENECA = "AstraZeneca"
PFIZER = "Pfizer"
MODERNA = "Moderna"
ALLOWED_VACCINE_TYPES = [ASTRAZENECA, PFIZER, MODERNA]

# Immunity type
SYMPTOMATIC = "symptomatic"
HOSPITALISATION = "hospitalisation"
DEATH = "death"
ALLWED_IMMUNITY_TYPES = [SYMPTOMATIC, HOSPITALISATION, DEATH]

INDEX = "delay"
LOWER, AVERAGE, UPPER = "lower", "average", "upper"
COLUMNS = [LOWER, AVERAGE, UPPER]

# Streamlit
DEFAULT_JAB_DATE = {
    1: date(2021, 4, 1),
    2: date(2021, 6, 1),
    3: date(2021, 12, 14),
}
