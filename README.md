
 


# The 2nd ETRI Human Understanding Artificial Intelligence Paper Competition

Disseminating human understanding artificial intelligence technology research by utilizing datasets constructed to enable the study of technologies that understand human behavior and emotions.

https://aifactory.space/competition/detail/2234

### Data Information

- KEMDy20 is a multimodal emotion dataset:
- Speech data (Audio)
- Text data transcribed from the speech
- Electrodermal Activity (EDA)
- Inter-Beat-Interval (IBI)
- Wrist skin temperature


### Data Characteristics

| Characteristics  |  Description |  
|---|---| 
|Number of Participants | 80   |  
|Age of participants| 19-30  |  
| Language  | Korean  |  
| Device  | Empatica E4  |  
| Stimulus  |  6 videos (~5-minute length) + conversation   |  
| Annotation  |  10 External annotators
| Labels  | 7 Emotions(“angry”, “sad”, “happy”, “disgust”, “fear”, “surprise”, “neutral”)) Arousal & Valence (1-5 scale)  |  


### Emotion Recognition Technology Field Utilizing Multi-modal Emotion Datasets

The emotion recognition research field aiming to recognize or predict the emotions of participants in a dialogue process involving two or more participants.


### Multi-modal Fusion Attention Network (MMFAN)

In emotion recognition, the multi-modal approach is based on the assumption that the information from each modality is complementary. Therefore, it is necessary to effectively integrate and fuse information from multiple modalities. Accordingly, this paper proposes a Multi-modal Fusion Attention Network (MMFAN) that fuses features extracted from each modality and focuses on the interactive parts through an attention mechanism for emotion classification.



### Source Files Description

- Exploratory Data Analysis : Perform exploratory data analysis using various data analysis techniques
- Preprocessing and Training : Preprocessing for each modality and execution code for the proposed model (MMFAN)
- requirements.txt : List of configuration environments for running the code



### visualization using streamlit App

StreamLit app is included in ```/Exploratory Data Analysis/Visualization Using StreamLit```

- Run using and open streamlit on browser using the URL in the output

```
streamlit run main.py

```


 ![Streamlit Screenshot](https://github.com/darshanz/EtriChallenge/blob/main/Exploratory%20Data%20Analysis/Visualization%20Using%20StreamLit/streamlit_screenshots/streamlit1.png) 





 

- SKEZ@901-v.10

 


