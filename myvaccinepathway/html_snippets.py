DISCLAIMER = """
<h4 style="text-align: center;">Disclaimer</h4>
Whilst we endeavour to display the most accurate information available, and have taken our data from reliable scientific studies,
you should not use the provided data to make any healthcare or life decisions. Always follow the scientific guidance,
wear a mask, wash your hands, and social distance. The information provided is intended to more easily present information
in the scientific literature to give people an idea of how covid immunity levels vary by vaccine, time, and covid variant. 
We do not guarantee we have copied across the data correctly, or interpreted the data correctly. We hold
no responsibility or liability for any of the information displayed or consequences resulting from this website.
<hr>
"""

HEAD_TITLE = """
<div style="text-align: center;">
    <h1 style="display:inline;">My Vaccine Pathway</h1>
    <br>
    <br>
    <h3 style="display:inline;">What is my current covid immunity?</h3>
    <br>
    <br>
    <h5 style="display:inline; color: green">Updated 31 Jan. 2022 - Latest Omicron immunity data</h3>
</div>
<hr>
"""

PRODUCT_STAGES = """
<h4 style="text-align: center;">Current product stage: <h4 style="color: blue; display: inline;">βeta</h4></h4>
<p style="color: red; display: inline;">αlpha</p>: \tProduct not complete and still under development. Data not correct or referenced.<br>
<p style="color: blue; display: inline;">βeta</p>: \tProduction stage: Minimum viable product complete. Real data sourced from academic literature used. Not all features implemented.<br>
<p style="color: gold; display: inline;">γamma</p>: \tFinal offering: All desired features are implemented.<br>
<hr>
"""

REFERENCE_DELTA_DATA = """
<h4 style="text-align: center;">References: Delta variant data</h4>
<p>
    The data presented is from <a href="https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/1029794/S1411_VEEP_Vaccine_Effectiveness_Table_.pdf" target="_blank">this paper by SAGE</a>, the UK Government's Scientific Advisory group, 
    <a href="https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/1017309/S1362_PHE_duration_of_protection_of_COVID-19_vaccines_against_clinical_disease.pdf" target="_blank">this paper by Public Health England</a>, 
    and <a href="https://www.health.gov.au/initiatives-and-programs/covid-19-vaccines/is-it-true/is-it-true-how-long-does-it-take-to-have-immunity-after-vaccination" target="_blank">this site</a> by the Australian Government's Department of Health.
</p>
"""

ASSUMPTIONS_DELTA_DATA = """
<hr>
<h4 style="text-align: center;">Assumptions: Delta variant data</h4>
<ul>
  <li>Doses 1 and 2 were of the same type. I.e. either both doses 1 and 2 were AstraZeneca, Pfizer, or Moderna, but not a combination of the three.</li>
  <li>Booster/dose 3 vaccine data currently presented is a copy of dose 2 levels as this is a reasonable estimate until the real booster data can be inserted.</li>
  <li>Moderna data is less available than Astrazeneca and Pfizer due to it's later approval in the UK. Currently, Moderna data for hospitalisation and deaths isn't included. Where Moderna data is missing, the corresponding Pfizer data is used instead since the vaccine types are most similar and the trend seems to be Moderna having greater immunity levels, so using Pfizer will provide a lower bound.</li>
</ul>
<hr>
"""

REFERENCE_OMICRON_DATA = """
<h4 style="text-align: center;">References: Omicron variant data</h4>
<p>
    Omicron data presented is from <a href="https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/1050721/Vaccine-surveillance-report-week-4.pdf"> this survey by the UKHSA</a>.
    The survey is an aggregation of several international efforts to analyse the limited omicron data becoming available, including data from the UK.
</p>
"""

ASSUMPTIONS_OMICRON_DATA = """
<hr>
<h4 style="text-align: center;">Assumptions: Omicron variant data</h4>
<ul>
  <li>Dose 1 immunity data is unavailable so Dose 1 immunity levels were assumed to be 1/2 dose 2 immunity levels. This value was chosen as it was the assumption made in the <a href="https://www.imperial.ac.uk/mrc-global-infectious-disease-analysis/covid-19/report-48-global-omicron/">Imperial College London/WHO paper</a> that modelled Omicron immunity.</li>
  <li>Fatality from Covid-19 data for Omicron Covid-19 is only currently available as an average value for Astrazeneca, Pfizer, and Moderna vaccinated individuals, so this average value is presented as the hospitalisation value of all three vaccine types.</li>
  <li>Fatality from Covid-19 data for Omicron Covid-19 is currently extremely limited, with only 2 datapoints at 3 months post dose 2, and 2 weeks post dose 3. There is not currently data on immunity from fatal Covid-19 shortly after dose 2, or long after dose 3, which is why the fatality graphs do no show a decrease in immunity with time at the moment.</li>
  <li>There is no Moderna immunity data for hospitalisation from Covid-19 so Pfizer data is used in its place. Moderna jabs are likely to have similar, if not higher, immunity values to Pfizer, so the Pfizer data provides a realistic lower bound for Moderna vaccinated individuals.</li>
  <li>There is no AstraZeneca immunity data for hospitalisation from Covid-19 before 154 days after dose 2, so the values at 154 days are used as a lower bound for earlier dates. This is the reason the AstraZeneca hospitalisation from Covid-19 graph does not show a decrease in immunity after dose 2 at the moment.</li>
</ul>
<hr>
"""

OMICRON_DATA_WARNING = """
<p style="color: orange; text-align: center;">
    <b>Note:</b> Some Omicron data is still limited, especially for immunity from fatal Covid-19 and some vaccine types - see Assumptions.
</p>
"""

MODERNA_DELTA_DATA_WARNING = """
<p style="color: orange; text-align: center;">Warning: Moderna data for hospitalisation and death has not yet been extracted so Pfizer data has been used in its place here. See Assumptions</p>
"""

WHAT_IMMUNITY_LEVEL_MEANS = """
<hr>
<p style="font-size: 25px; text-align: center;">
    <b>Immunity</b> is how much 
    <b>less</b> likely you are to catch covid, require hospital treatment, or die 
    <b>compared to being unvaccinated</b>.
</p>
<hr>
"""

WHAT_IMMUNITY_LEVEL_MEANS_2 = """
<hr>
<p style="font-size: 25px; text-align: center;">
    <b>Immunity</b> is how much your chance of getting symptoms, requiring hospital treatment, or dying from covid
    is <b>reduced</b> by being vaccinated.
</p>
"""

FAQ = """
<h4 style="text-align: center;">FAQ</h4>
<h6>Why is there a range in my immunity?</h6>
<p>
    The value of "immunity" is actually a measurement of how well the vaccine has worked in the wider population 
    ("vaccine effectiveness"). 
    As with all measurements, there are always uncertainties associated with the measurement. For vaccine data, these
    uncertainties arise because of limited amounts of data, limited data quality, and how the vaccine affects different 
    people differently (i.e. dependent of their age, health, gender, ethnicity, etc.), among other things. The ranges 
    present the uncertainty present due to multiple factors. 
    For more information see <a href="https://www.who.int/news-room/feature-stories/detail/vaccine-efficacy-effectiveness-and-protection" target="_blank">this World Health Organisation article</a>.
</p>
<h6>Why is there a large range of possible values for some Omicron immunity values?</h6>
<p>
    Data for immunity from the Omicron variant of Covid-19 is still coming to light. When there is less data available
    it makes the results of that data more uncertain, which is another way of saying the ranges of possible values
    are larger. As more data becomes available we can expect the ranges of the values to decrease as we better
    understand different immune reactions to Omicron.
</p>
<hr>
"""

ROADMAP = """
<h4 style="text-align: center;">MyVaccinePathway roadmap</h4>
<p>
    MyVaccinePathway is a personal project. Development happens in our spare time so we do no have a timeline 
    for future features, but the following are on our list to implement:
</p>
<ul>
  <li>Immunity provided by prior covid infection</li>
  <li>Age-based immunity data</li>
  <li>Immunity data for immunocompromised individuals</li>
  <li>Data for more vaccine types</li>
</ul>
<hr>
"""

CURRENT_IMMUNITY_TEXT_LAYOUT_1 = """
<h4 style='text-align: center;'>Your current immunity levels:</h4>
<div>
    <h5 style='text-align: center; box-sizing: border-box; float: left; width: 33.33%; padding: 10px;'>
        {symptomatic_lower:.0f}-{symptomatic_upper:.0f}%
        <br>against getting symptomatic covid
    </h5>
    <h4 style='text-align: center; box-sizing: border-box; float: left; width: 33.33%; padding: 10px;'>
        {hospitalisation_lower:.0f}-{hospitalisation_upper:.0f}%
        <br>against hospitalisation
    </h4>
    <h5 style='text-align: center; box-sizing: border-box; float: left; width: 33.33%; padding: 10px;'>
        {death_lower:.0f}-{death_upper:.0f}%
        <br>against death
    </h5>
</div>
<hr>
"""

CURRENT_IMMUNITY_TEXT_LAYOUT_2 = """
<div>
    <h5 style='text-align: center; box-sizing: border-box; float: left; width: 33.33%; padding: 10px;'>
        You are<br>
        {symptomatic_lower:.0f}-{symptomatic_upper:.0f}%
        <br>less likely to get symptomatic covid than before you were vaccinated
    </h5>
    <h4 style='text-align: center; box-sizing: border-box; float: left; width: 33.33%; padding: 10px;'>
        You are<br>
        {hospitalisation_lower:.0f}-{hospitalisation_upper:.0f}%
        <br>less likely to require hospital treatment for covid than before you were vaccinated
    </h4>
    <h5 style='text-align: center; box-sizing: border-box; float: left; width: 33.33%; padding: 10px;'>
        You are<br>
        {death_lower:.0f}-{death_upper:.0f}%
        <br>less likely to die from covid than before you were vaccinated
    </h5>
</div>
<hr>
"""

CURRENT_IMMUNITY_TEXT_LAYOUT_3 = """
<h4 style='text-align: center;'>
    Your current immunity levels:<br><br>You are:
</h4>
<div style='text-align: center; box-sizing: border-box; float: left; width: 33.33%; padding: 10px;'>
    <h4>{symptomatic_lower:.0f}-{symptomatic_upper:.0f}%</h4>
    <p><b>less likely</b> to get <b>symptomatic covid</b> than before you were vaccinated</p>
</div>
<div style='text-align: center; box-sizing: border-box; float: left; width: 33.33%; padding: 10px;'>
    <h4>{hospitalisation_lower:.0f}-{hospitalisation_upper:.0f}%</h4>
    <p><b>less likely</b> to require <b>hospital treatment</b> for covid than before you were vaccinated</p>
</div>
<div style='text-align: center; box-sizing: border-box; float: left; width: 33.33%; padding: 10px;'>
    <h4>{death_lower:.0f}-{death_upper:.0f}%</h4>
    <p><b>less likely to die</b> from covid than before you were vaccinated</p>
</div>
<hr>
"""

ABOUT_US = """
<h4 style="text-align: center;">About</h4>
<p>
    This app is a personal project that came about because of a desire to know our current immunity levels. We couldn't 
    find a simple application to tell us this information, so we decided to build one. The code for this app is open source
    and can be found on <a href="https://github.com/hdaly0/myvaccinepathway" target="_blank">github</a>.
</p>
<p>
    Feedback and suggestions can be emailed to myvaccinepathway [at] gmail [dot] com
</p>
<hr>
"""
