import streamlit as st
from PIL import Image
import pandas as pd
import requests

st.set_page_config(
    page_title="Ds. Navdeesh",
    page_icon="dp.png"  # You can replace this with the path to your favicon file
)

st.markdown(
    '''<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">''',
    unsafe_allow_html=True)

st.markdown("""
<div class="customnavv">
  <a href="#navdeesh-data-scientist">Home</a>
  <a href="#education">Education</a>
  <a href="#work-experience">Work Experience</a>
  <a href="#projects">Projects</a>
  <a href="#skills">Skills</a>
</div>
""",
            unsafe_allow_html=True)

with open("style.css") as f:
  st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

#####################
# Header
st.write('''
# Navdeesh, Data Scientist
##### *Resume* 
''')

st.markdown("""
<div class="text-center">
    <img src="https://raw.githubusercontent.com/VidYtai/Navdeesh-Singhal/main/dp.png" class="img-fluid" alt="Centered Image">
</div>
""", unsafe_allow_html=True)

st.markdown('## Summary', unsafe_allow_html=True)
st.info('''
- Committed to ongoing professional development, regularly participating in workshops, conferences, and online courses to stay updated with the latest advancements in the field.
- Driven by a strong ambition to leverage advanced data analytics techniques in a dynamic environment, aiming to contribute to Google's cutting-edge projects.
- Possess extensive expertise in coding and development, with a keen understanding of various programming languages and development tools, proficiency in designing, implementing, and optimizing software solutions to address complex challenges.
''')

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
## Projects
''')
st.write("### **1. Molecular Solubility Prediction Web App**")
st.write("""
[Explore the Molecular Solubility Prediction Web App here](https://molecular-solubility-prediction-web-app.onrender.com/)

#### Project Overview:
The Molecular Solubility Prediction Web App is a data-driven application designed to predict the solubility values (LogS) of molecules. This web-based tool leverages molecular descriptors calculated from chemical structures to provide insightful predictions, making it a valuable resource for researchers and professionals in the field.

#### Features:
1. **Molecular Descriptors Calculation:**
   - The app utilizes the RDKit library to calculate essential molecular descriptors, including Molecular LogP, Molecular Weight, Number of Rotatable Bonds, and Aromatic Proportion.

2. **User-Friendly Interface:**
   - The intuitive interface allows users to input molecular structures using Simplified Molecular Input Line Entry System (SMILES) notation.

3. **Predictive Analytics:**
   - A pre-built machine learning model, trained on data from John S. Delaney's work, is incorporated into the app. This model predicts LogS values based on the provided molecular descriptors.

4. **Results Display:**
   - The app displays predicted LogS values for the input molecules, providing users with valuable insights into the solubility characteristics of the compounds.

5. **Customization:**
   - Users can easily customize input molecules, allowing for flexibility in exploring the solubility predictions for different chemical structures.

#### Data Source:
The molecular solubility prediction model is trained on data from the research article "ESOL: Estimating Aqueous Solubility Directly from Molecular Structure" by John S. Delaney, published in the Journal of Chemical Information and Computer Sciences in 2004.

[Link to the Article](https://pubs.acs.org/doi/10.1021/ci034243x)

#### Technologies Used:
- **Python:** The backend of the application is developed using Python.
- **Streamlit:** The user interface is created using the Streamlit library, making it easy to deploy and share.

#### Future Enhancements:
Future enhancements may include expanding the model's training data, incorporating more advanced machine learning techniques, and improving the user interface for a seamless experience.

#### Conclusion:
The Molecular Solubility Prediction Web App combines scientific rigor with user-friendly design, contributing to the advancement of research in molecular solubility prediction. This project showcases your skills in data science, machine learning, and web development, making it a valuable addition to your portfolio.
""")

st.write("### **2. DNA Nucleotide Count Web App**")
st.write("""
[Explore the DNA Nucleotide Count Web App here](https://dna-nucleotide-count-web-app.onrender.com/)

This app counts the nucleotide composition of query DNA!

#### Overview:
The "DNA Nucleotide Count Web App" is a user-friendly tool designed to analyze the nucleotide composition of a given DNA sequence. The app provides a comprehensive breakdown of the count of each nucleotide (Adenine, Thymine, Guanine, and Cytosine) and visualizes the results using a bar chart. This project is implemented using the Streamlit library for the web interface, Altair for data visualization, and Pandas for data manipulation.

#### Features and Functionality:

1. **Input DNA Sequence:**
    - The app allows users to input a DNA sequence using a text area. The user can either use the default DNA sequence provided or replace it with their own. The input is then processed to extract the sequence for analysis.

2. **Nucleotide Count:**
    - The core functionality of the app is to count the occurrences of each nucleotide in the given DNA sequence. The counts are stored in a dictionary and displayed in both tabular and text formats. This information gives users a quick overview of the nucleotide distribution in the input DNA sequence.

3. **Display DataFrame:**
    - The app converts the nucleotide count dictionary into a Pandas DataFrame for a structured presentation. This DataFrame includes two columns: 'nucleotide' and 'count'. Users can easily interpret the nucleotide composition through this tabular format.

4. **Visual Representation with Bar Chart:**
    - To enhance data visualization, the app generates a bar chart using the Altair library. The chart visually represents the count of each nucleotide, providing a clear and intuitive way to understand the composition of the DNA sequence.

5. **User-Friendly Interface:**
    - The web interface is designed with a clean and simple layout. Users are guided through the steps with section headers and clear instructions. The input and output sections are well-organized, making it easy for users to understand the results.

#### Technologies Used:
- **Streamlit:** Used to create the interactive web interface.
- **Altair:** Employed for generating the bar chart for data visualization.
- **Pandas:** Utilized for data manipulation and organization.
- **PIL (Pillow):** Used for displaying the DNA logo image.

#### Future Improvements:
- Allow users to upload their DNA sequences as text files.
- Implement additional statistical analyses or visualizations for more in-depth insights into DNA composition.
- Enhance the user interface with additional customization options.

#### Conclusion:
The "DNA Nucleotide Count Web App" serves as a valuable tool for scientists, researchers, and students working with DNA sequences. It provides a quick and efficient way to analyze and visualize the nucleotide composition of DNA, contributing to a better understanding of genetic information.
""")

st.write("### **3. Simple Stock Price App**")
st.write("""
[Explore the Simple Stock Price App here](https://simple-stock-price-app.onrender.com/)

Welcome to the Simple Stock Price App! This app is designed to provide a straightforward analysis of the historical closing price and volume of Google's stock (GOOGL).

#### Overview:
The "Simple Stock Price App" is a user-friendly tool that allows users to visualize and analyze the historical data of Google's stock. The app leverages the Yahoo Finance API (yfinance) to fetch historical stock data and presents it in an easy-to-understand format. Developed using the Streamlit framework, this project offers insights into the closing prices and trading volumes over a specified time range.

#### Features and Functionality:

1. **Closing Price Analysis:**
    - Explore the historical closing prices of Google's stock through an interactive line chart. This visualization helps users identify trends and patterns in the stock's performance.

2. **Volume Analysis:**
    - Visualize the trading activity by examining the volume of trades over the selected time period. The dedicated line chart provides a clear representation of the stock's trading history.

3. **User-Friendly Interface:**
    - The app features a clean and intuitive interface, making it easy for users to navigate and interpret the displayed information. Streamlit's simplicity ensures a seamless user experience.

#### Customization:
The application is configured with a custom page title and favicon, providing a personalized touch to the user interface.

#### Future Enhancements:
- Incorporate additional technical indicators for a more comprehensive analysis.
- Implement real-time data updates to provide users with the latest stock information.

#### Conclusion:
The Simple Stock Price App showcases my skills in data retrieval, data visualization, and web application development. It serves as a practical example of creating a functional and aesthetically pleasing tool for analyzing stock market data.

Feel free to explore and gain valuable insights into the world of stock trading with this app!
""")


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
    data = {"Name": name, "Email": email, "Message": message}
    df = pd.DataFrame([data])  # Convert a single dictionary to a DataFrame with a list


    # Send POST request to a server
    api_url = "https://contact-1.navdeeshsingha2.repl.co/api/contact"
    headers = {"Content-Type": "application/json"}
    payload = df.to_json(orient="records")

    response = requests.post(api_url, data=payload, headers=headers)

    if response.status_code == 200:
        st.success("Form sent successfully.")
    else:
        st.error(f"Failed to send data. Status code: {response.status_code}")
        st.error(f"Error message from server: {response.json().get('error')}")
