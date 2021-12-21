DISCLAIMER = """
<h4 style="text-align: center;">Disclaimer</h4>
Whilst we endeavour to display the most accurate information available, and have taken our data from reliable scientific studies,
you should not use the provided data to make any healthcare or life decisions. Always follow the scientific guidance,
wear a mask, wash your hands, and social distance. The information provided is intended to more easily present information
in the scientific literature to give people an idea of how covid immunity levels vary by vaccine, time, age, and health
of individuals. We do not guarantee we have copied across the data correctly, or interpreted the data correctly. We hold
no responsibility or liability for any of the information displayed or consequences resulting from this website.
<hr>
"""

CURRENT_PRODUCT_STAGE = """
<div style="text-align: center;">
    <h1 style="display:inline;">My vaccine pathway: </h1><h1 style="color: blue; display: inline;">βeta</h1>
</div>
<hr>
"""

PRODUCT_STAGES = """
<h4 style="text-align: center;">Product stages</h4>
<p style="color: red; display: inline;">αlpha</p>: \tproduct not complete and still under development. Data not correct or referenced.<br>
<p style="color: blue; display: inline;">βeta</p>: \tproduction stage:Minimum viable product complete. Real data sourced from academic literature used. Not all features implemented.<br>
<p style="color: gold; display: inline;">γamma</p>: \tfinal offering: All features required are offered.<br>
<hr>
"""

ASSUMPTIONS_DELTA_DATA = """
<hr>
<h4 style="text-align: center;">Assumptions: Delta variant data</h4>
<p>The data presented is from <a href="https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/1029794/S1411_VEEP_Vaccine_Effectiveness_Table_.pdf" target="_blank">this paper by SAGE</a>, the UK Government's Scientific Advisory group,
 <a href="https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/1017309/S1362_PHE_duration_of_protection_of_COVID-19_vaccines_against_clinical_disease.pdf" target="_blank">this paper by Public Health England</a>,
 and <a href="https://www.health.gov.au/initiatives-and-programs/covid-19-vaccines/is-it-true/is-it-true-how-long-does-it-take-to-have-immunity-after-vaccination" target="_blank">this site</a> by the Australian Government's Department of Health.</p>
<ul>
  <li>Doses 1 and 2 were of the same type. I.e. either both doses 1 and 2 were AstraZeneca, Pfizer, or Moderna, but not a combination of the three.</li>
  <li>Doses 3 and onwards are assumed to be Pfizer jabs since these are generally the boosters and 3rd jabs on offer in the UK.</li>
  <li>Moderna data is less available than Astrazeneca and Pfizer due to it's later approval in the UK. Currently, Moderna data for hospitalisation and deaths isn't included. Where Moderna data is missing, the corresponding Pfizer data is used instead since the vaccine types are most similar and the trend seems to be Moderna having greater immunity levels, so using Pfizer will provide a lower bound.</li>
</ul>
<hr>
"""

ASSUMPTIONS_OMICRON_DATA = """
<hr>
<h4 style="text-align: center;">Assumptions: Omicron variant data</h4>
<p>Data is only available for primary doses of Astrazeneca and Pfizer, coupled with a Pfizer booster. The data presented
is also only a <b>model</b> of expected behaviour from the limited omicron data available and previous covid behaviours seen. The data
will be updated with real-world data as and when it becomes available.</p>
<p>The data presented is from <a href="https://www.imperial.ac.uk/mrc-global-infectious-disease-analysis/covid-19/report-48-global-omicron/" target="_blank">this paper by Imperial College London</a>.</p>
<ul>
  <li>Dose 1 immunity levels were assumed to be 1/2 dose 2 immunity levels as dose 1 immunity data was unavailable</li>
  <li>Some dose 2 data, and some booster jab data, was extrapolated based on patterns in the data that were available. For full details see comments in the code on <a href="https://github.com/hdaly0/myvaccinepathway" target="_blank">github</a>.</li>
  <li>Dose 3 onwards are assumed to be Pfizer. Moderna jabs (primary and booster) are likely to have similar, if not higher, immunity values to Pfizer, so the Pfizer data provides a realistic lower bound for Moderna vaccinated individuals</li>
  <li>Moderna data for the Omincron variant is not currently published so Pfizer data is used in its place. As above, this is should be a reasonable lower bound for Moderna vaccinated individuals.</li>
</ul>
<hr>
"""

MODERNA_OMICRON_DATA_WARNING = """
<p style="color: orange; text-align: center;">Warning: Moderna data is limited so Pfizer data has been used in its place here. See Assumptions</p>
"""

MODERNA_DELTA_DATA_WARNING = """
<p style="color: orange; text-align: center;">Warning: Moderna data for hospitalisation and death is limited so Pfizer data has been used in its place here. See Assumptions</p>
"""
