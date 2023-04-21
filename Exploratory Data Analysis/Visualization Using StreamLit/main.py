import streamlit as st

st.set_page_config(
    page_title="ETRI Data Exploration",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'About': "# App for data exploration"
    }
)


st.markdown('''### Data Information

- KEMDy20 is a multimodal emotion dataset:
- speech data
- Text data transcribed from the speech
- electrodermal activity (EDA),
- Inter-Beat-Interval (IBI),
- Wrist skin temperature ''')

st.markdown(
'''
### Data Characteristics

| Characteristics  |  Description |  
|---|---| 
|Number of Participants | 80   |  
|Age of participants| 19-30  |  
| Language  | Korean  |  
| Device  | Empatica E4  |  
| Stimulus  |  6 videos (~5-minute length) + conversation   |  
| Annotation  |  10 External annotators (??)
| Labels  | 7 Emotions(“angry”, “sad”, “happy”, “disgust”, “fear”, “surprise”, “neutral”))
Arousal & Valence (1-5 scale)  |  


''')


st.markdown('''

### Initial Observation

- Data was collected during conversation
- The videos watched before the conversation can be considered the stimulus videos, however the conversation is the primary stimulus.
- (Role of the videos is not clear, the emotion during the conversation not only depends on the videos but also on the conversational context)
- The video was labeled by external annotators.
- Based on majority vote of the external annotators.
- Video was recorded during the conversation. 
- The external annotators tagged the speech segments while listening to the recorded utternaces.
- It is not clear whether the evaluators had access to the facial expressions.


''')


st.markdown('''
### Questions to be explored
- What is the size of the data, is there any data excluded/missing?
- What is the distribution of different labels. Are there any outliers?
- Is there any special consideration needed before building a classification/prediction model?


''')