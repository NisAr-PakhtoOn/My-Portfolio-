import streamlit as st
from PIL import Image

with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

#####################
# Header 
st.write('''
# Nisar Ahmad
##### *Resume* 
''')

image = Image.open('nisar.jpeg')
st.image(image, width=200)

st.markdown('## Summary', unsafe_allow_html=True)
st.info('''
- Experienced data scientist having more than three years of professional expereience. Worked on some major projects in the recent Omdena Local Chapters.
- Strong knowledge of machine learning and deep learning
- Having experience in data analysis and data analytics
- Expertise in Natural language processing and reinforcement learning
- Strong verbal and written communication skills.
''')

#####################
# Navigation

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #16A2CB;">
  <a class="navbar-brand" href="https://www.linkedin.com/in/nisar-ahmad-%E2%9C%AA-838479219/" target="_blank">Nisar Ahmad</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="/">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#education">Education</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#work-experience">Work Experience</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#bioinformatics-tools">Projects</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#social-media">Social Media</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)

#####################
# Custom function for printing text
def txt(a, b):
  col1, col2 = st.columns([4,1])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)

def txt2(a, b):
  col1, col2 = st.columns([1,4])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)

def txt3(a, b):
  col1, col2 = st.columns([1,2])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)
  
def txt4(a, b, c):
  col1, col2, col3 = st.columns([1.5,2,2])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)
  with col3:
    st.markdown(c)

#####################
st.markdown('''
## Education
''')


txt('**Master of Data Science**, *Institute of management sciences*, Pakistan',
'2017-2020')
st.markdown('''
- GPA: `3.7`
- Research thesis entitled `Load Demand prediction under **LESCO** and **PESCO** plus another Research on Galls detection in the leaves of **Alistona Scholaris Tree**, I also worked on disease detection in Tomato and Potato leaves using deep learning`.
- Leading a team of 10 data scientist on Omdena. 
''')

#####################
st.markdown('''
## Work Experience
''')

txt('**Lead Data Scientist**, Omdena',
'2022-2022')
st.markdown('''
- Leading more than `10` data scientist on a project focused on `Road Severity Prediction` under the government of the `United Kingdom`. 
- Successfully accomplished a recent project on Omdena which was related to see the `Flood impacting the prices in Pakistan`.
- Invloved in `5` major final year projects for master level. 
''')


#####################
st.markdown('''
## Glance of some projects
''')
txt4('Tomato', 'A web application which detect disease in `Tomato leaves`', '')
txt4('AutoWeka', 'An automated data mining software based on Weka', 'https://nisar-pakhtoon-disease-detection-in-tomato-leaves-us-app-kkqwwv.streamlitapp.com/')
txt4('Regression', 'A website which will perform machine learning regression','https://randomforestregressor.herokuapp.com/')
txt4('Classification', 'A website which will perform machine learning Classification', 'https://randomforestclassifier.herokuapp.com/')
txt4('CryoProtect', 'A web server for classifying antifreeze proteins from non-antifreeze proteins','http://codes.bio/cryoprotect/')
txt4('ERpred', 'A web server for the prediction of subtype-specific estrogen receptor antagonists', 'http://codes.bio/erpred')
txt4('HemoPred', 'A web server for predicting the hemolytic activity of peptides', 'http://codes.bio/hemopred/')
txt4('iQSP', 'A sequence-based tool for the prediction and analysis of quorum sensing peptides', 'http://codes.bio/iqsp/')
txt4('THPep', 'A web server for predicting tumor homing peptides','http://codes.bio/thpep/')


#####################
st.markdown('''
## Skills
''')
txt3('Programming', '`Python`, `R`, `Linux`')
txt3('Data processing/wrangling', '`SQL`, `pandas`, `numpy`')
txt3('Data visualization', '`matplotlib`, `seaborn`, `plotly`, `altair`, `ggplot2`')
txt3('Machine Learning', '`scikit-learn`')
txt3('Deep Learning', '`TensorFlow`')
txt3('Web development', '`Flask`, `HTML`, `CSS`')
txt3('Model deployment', '`streamlit`, `gradio`, `R Shiny`, `Heroku`, `AWS`, `Digital Ocean`')

#####################
st.markdown('''
## Social Media
''')
txt2('LinkedIn', 'https://www.linkedin.com/in/nisar-ahmad-%E2%9C%AA-838479219/')
txt2('GitHub', 'https://github.com/NisAr-PakhtoOn')
txt2('Facebook', 'https://www.facebook.com/profile.php?id=100006846330389')
txt2('Email', 'nisar0998906@gmail.com, nisarmasid@gmail.com')
txt2('WhatsApp', '+923480998906')
