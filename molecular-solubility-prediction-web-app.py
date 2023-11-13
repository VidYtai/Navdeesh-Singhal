from PIL import Image
import streamlit as st

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

st.write("# **Molecular Solubility Prediction Web App**")
st.write("""
[Explore the Molecular Solubility Prediction Web App here](https://molecular-solubility-prediction-web-app.onrender.com/)

## Project Overview:
The Molecular Solubility Prediction Web App is a data-driven application designed to predict the solubility values (LogS) of molecules. This web-based tool leverages molecular descriptors calculated from chemical structures to provide insightful predictions, making it a valuable resource for researchers and professionals in the field.

## Features:
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

## Data Source:
The molecular solubility prediction model is trained on data from the research article "ESOL: Estimating Aqueous Solubility Directly from Molecular Structure" by John S. Delaney, published in the Journal of Chemical Information and Computer Sciences in 2004.

[Link to the Article](https://pubs.acs.org/doi/10.1021/ci034243x)

## Technologies Used:
- **Python:** The backend of the application is developed using Python.
- **Streamlit:** The user interface is created using the Streamlit library, making it easy to deploy and share.

## Future Enhancements:
Future enhancements may include expanding the model's training data, incorporating more advanced machine learning techniques, and improving the user interface for a seamless experience.

## Conclusion:
The Molecular Solubility Prediction Web App combines scientific rigor with user-friendly design, contributing to the advancement of research in molecular solubility prediction. This project showcases your skills in data science, machine learning, and web development, making it a valuable addition to your portfolio.
""")
