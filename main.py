import streamlit as st
from PIL import Image
import pandas as pd
import requests

st.set_page_config(
    page_title="Ds. Navdeesh",
    page_icon="dp.png"  # You can replace this with the path to your favicon file
)

with open("style.css") as f:
  st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

#####################
# Header
st.write('''
# Navdeesh, Data Scientist
##### *Resume* 
''')

image = Image.open('dp.png')
st.image(image, width=150)

st.markdown('## Summary', unsafe_allow_html=True)
st.info('''
- Committed to ongoing professional development, regularly participating in workshops, conferences, and online courses to stay updated with the latest advancements in the field.
- Driven by a strong ambition to leverage advanced data analytics techniques in a dynamic environment, aiming to contribute to Google's cutting-edge projects.
- Possess extensive expertise in coding and development, with a keen understanding of various programming languages and development tools, proficiency in designing, implementing, and optimizing software solutions to address complex challenges.
''')

#####################
# Navigation

st.markdown(
    '<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">',
    unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #16A2CB;">
  <a class="navbar-brand" href="/">Ds. Navdeesh</a>
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
        <a class="nav-link" href="#skills">Skills</a>
      </li>
    </ul>
  </div>
</nav>
""",
            unsafe_allow_html=True)


#####################
# Custom function for printing text
def txt(a, b):
  col1, col2 = st.columns([4, 1])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)


def txt2(a, b):
  col1, col2 = st.columns([1, 4])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)


def txt3(a, b):
  col1, col2 = st.columns([1, 2])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)


def txt4(a, b, c):
  col1, col2, col3 = st.columns([1.5, 2, 2])
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

txt(
    '**Data Science Course** (Complete Data Science Technology), *Odin School*, India',
    '2028-2028')
st.markdown('''
- Relevant Coursework: Covered advanced topics in Machine Learning, Data Analysis, and Statistical Modeling.
- Completed projects utilizing Python, R, and SQL for data manipulation and analysis, demonstrating proficiency in these programming languages.
- Attended workshops and seminars on cutting-edge data science technologies and methodologies.
- Actively participated in group projects, honing teamwork and collaboration skills in a professional setting.
''')

txt('**School** (Class 7), *Tagore International School*, India', '2015-2023')
st.markdown('''
- Relevant Coursework: Included subjects like Machine Learning, Data Analysis, and Statistical Modeling.
- Completed projects in Python, R, and SQL, demonstrating proficiency in data manipulation and analysis.
- Participated in workshops and seminars on topics related to data science and programming.
- Contributed to group projects, showcasing strong teamwork and collaboration skills.
''')

#####################
st.markdown('''
## Work Experience
''')

txt('**Data Scientist**, Google, Germany', '2038-Present')
st.markdown('''
- Spearheading data-driven decision-making processes by analyzing large datasets and extracting valuable insights.
- Designing and implementing machine learning models to optimize various aspects of user experience and business operations.
- Collaborating with cross-functional teams to define and address complex problems using data science methodologies.
- Contributing to the development of scalable and efficient data processing pipelines.

- **Key Achievements:**
  - Successfully implemented a predictive modeling solution that improved user engagement by 20%.
  - Led a team of data scientists in developing a recommendation system resulting in a 15% increase in click-through rates.

''')

txt('**Senior Data Analyst**, Amazon, San Francisco, CA, USA', '2032-2038')
st.markdown('''
- Conducting thorough data analysis to identify trends, patterns, and anomalies, providing actionable insights for business strategies.
- Building and maintaining robust dashboards and reports to visualize and communicate data findings to stakeholders.
- Collaborating with business leaders to understand requirements and translate them into effective data-driven solutions.
- Utilizing statistical methods and machine learning algorithms to enhance predictive analytics.

- **Key Achievements:**
  - Implemented a data quality improvement initiative, reducing errors in reporting by 30%.
  - Developed and deployed a fraud detection model, resulting in a 25% reduction in fraudulent activities.

''')

txt(
    '**Data Science Researcher**, ISB Institute of Data Science, Hyderabad, India',
    '2028-2032')
st.markdown('''
- Engaged in cutting-edge research at the intersection of data science and computational biology, focusing on understanding the role of genetic variations in complex diseases.
- Applied advanced machine learning techniques, including deep learning and ensemble methods, to analyze large-scale genomic datasets and identify potential biomarkers for disease susceptibility.
- Collaborated with a diverse team of bioinformaticians, geneticists, and statisticians to integrate multi-omics data and enhance the accuracy of predictive models.

- **Key Achievements:**
  - Published research papers in esteemed conferences such as the International Conference on Bioinformatics (ICB) and the Annual Conference on Computational Biology (ACCB).
  - Recognized with the **ISB Institute of Data Science Research Society Outstanding Researcher Award** for contributions to unraveling the genetic basis of Cancer.
''')

#####################
st.markdown('''
## Skills
''')
txt3('Programming', '`Python`, `R`, `Linux`')
txt3('Data processing/wrangling', '`SQL`, `pandas`, `numpy`')
txt3('Data visualization',
     '`matplotlib`, `seaborn`, `plotly`, `altair`, `ggplot2`')
txt3('Machine Learning', '`scikit-learn`')
txt3('Deep Learning', '`TensorFlow`')
txt3('Web development', '`Flask`, `HTML`, `CSS`, `Django`')
txt3('Model deployment',
     '`streamlit`, `gradio`, `R Shiny`, `Heroku`, `AWS`, `Digital Ocean`')

#####################


def save_to_markdown(data, markdown_file):
  with open(markdown_file, 'w') as file:
    file.write(data.to_markdown(index=False))


st.markdown('''
## Contact Form
''')

name = st.text_input("Name")
email = st.text_input("Email")
message = st.text_area("Message")
submitted = st.button("Submit")

if submitted:
    # Create a DataFrame with the form data
    data = {"Name": [name], "Email": [email], "Message": [message]}
    df = pd.DataFrame(data)

    # Send POST request to a server
    api_url = "https://contact-1.navdeeshsingha2.repl.co/api/contact"
    headers = {"Content-Type": "application/json"}
    payload = df.to_json(orient="records")

    response = requests.post(api_url, data=payload, headers=headers)

    if response.status_code == 200:
            st.success("Form sent successfully.")
    else:
            st.error(f"Failed to send data. Status code: {response.status_code}")
