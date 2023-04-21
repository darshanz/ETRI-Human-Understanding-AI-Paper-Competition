import streamlit as st
import pandas as pd
import altair as alt



st.set_page_config(
    page_title="Annotations All",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'About': "# App for data exploration"
    }
)




st.markdown('''

 # test annotations
 ## Train
''')




ANNOTATION_FILE = "../../KEMDy20ERC/train_labels.csv"
annot_df = pd.read_csv(ANNOTATION_FILE)

st.header("Annotations")

st.write(annot_df)

st.write(f"Annotation file has : {annot_df.shape[0]} samples")


st.header("Arousal valence distribution")
c = alt.Chart(annot_df).mark_circle().encode(
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

st.write(c)

st.markdown('''

## In the Plot
- The center part is all green: most of the samples are neutral
- Blue(Angry) one on the right bottom corner indicates, there is something wrong with the dataset annotation.
    - Anngry should be considered as a negative emotion and it is more reasonable to have those samples on either HALV or LALV quadrants.
    - Fear usually has higher arousal and it is also an emotion with low valence. But it does not appear to be the case in this dataset.
    - Happy on the top right quadrant makes sense. 
''')


st.write("7 Emotions")
agg_data = annot_df.groupby('emotion').agg(count=('emotion', 'count')).reset_index()
# Create a bar chart of the value counts
st.write(agg_data)


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
