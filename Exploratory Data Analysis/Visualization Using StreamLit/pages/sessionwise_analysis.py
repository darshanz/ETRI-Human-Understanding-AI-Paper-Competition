import streamlit as st
import pandas as pd
import altair as alt

st.set_page_config(
    page_title="Annotations - Sessions",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'About': "# App for data exploration"
    }
)

st.markdown('''

## Sessions
 
 The annotation was one in 40 sessions

''')

ANNOTATION_FILE = "../../preprocessed/labels.csv"
annot_df = pd.read_csv(ANNOTATION_FILE)

# Define a list of options for the dropdown
options = [f"Sess{session:02}" for session in range(1,41)]

# Use the selectbox function to create the dropdown
selected_option = st.selectbox('Select a session:', options)

# Display the selected option
st.write('Session:', selected_option)
session_df  = annot_df[annot_df['segment_id'].str.contains(selected_option)]


st.header("Arousal valence distribution")
c = alt.Chart(session_df).mark_circle().encode(
     x=alt.X('valence', scale=alt.Scale(domain=[1, 5])), y = alt.Y('arousal', scale=alt.Scale(domain=[1, 5])), color='emotion',  tooltip=['valence', 'arousal']).properties(
    width=800,
    height=500
)

# Set custom tick ranges on the x-axis and y-axis
c = c.configure_axis(
    domain=False,      # Remove axis line
    tickSize=10,        # Set tick size
    tickCount=4       # Set number of ticks
)
c = c.configure_axis(
    labelFontSize=20  # set the font size of the axis labels to 14
)
st.write(c)

st.write("7 Emotions")
agg_data = session_df.groupby('emotion').agg(count=('emotion', 'count')).reset_index()
# Create a bar chart of the value counts


st.markdown('''

# Number of samples for different emotions 

''')


chart = alt.Chart(agg_data).mark_bar().encode(
    x='emotion',
    y='count'
).properties(
    width=800,
    height=500)

chart = chart.configure_axis(
    labelFontSize=20  # set the font size of the axis labels to 14
)
st.write(chart)


st.write(agg_data)
