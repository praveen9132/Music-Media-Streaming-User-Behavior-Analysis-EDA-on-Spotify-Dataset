import streamlit as st
import pandas as pd

#dataset loading
df=pd.read_csv('spotify_churn_dataset.csv')
st.title("Exploratory Data Analysis on Spotify Churn Dataset")
st.sidebar.title("EDA Details")
st.sidebar.header('About The Table')
a=st.sidebar.selectbox("Table Overview",['Default','Sample','Details','Steps','Licence'])
if a=='Default':
    pass
elif a=='Sample':
    st.success('Displaying The Dataset')
    st.dataframe(df)
elif a=='Details':
    st.write('The column names are',list(df.columns))
    st.write('The information about dataset was',df.describe())
elif a=='Steps':
    st.success('Step-1')
    st.header('✅ Load The Dataset')
    st.success('step-2')
    st.header('🧹 Data Cleaning')
    st.write('viewing Dataset , Check Null values , if found Remove Null Values')
    st.write('Removing Duplicates')
    st.success('step-3')
    st.header(' 📊 Start Doing The Analysis')
    st.write('After Finding Insights Do Univariate Bivariate And multiVariate Analysis')
elif a == 'Licence':
    st.subheader("License Information")
    st.markdown("""
    This notebook and analysis are released under the [MIT License](https://opensource.org/licenses/MIT).  
    You are free to use, modify, and distribute this work with proper attribution.
    
    **Author:** praveen  
    **Dataset Source:** [Spotify Churn Dataset on Kaggle](https://www.kaggle.com/datasets/nabihazahid/spotify-dataset-for-churn-analysis)  
    """)
st.sidebar.write('----------')
st.sidebar.header('Univariate Analysis')
b=st.sidebar.radio('click to get Analysis',['Default','UA-Graphs','UA-Report'])
if b=='Default':
    pass
elif b=='UA-Graphs':
    st.image('univariate1.jpg')
    st.image('univariate2.png')
    st.image('univariate3.jpg')
elif b=='UA-Report':
    st.write('1. Age Distribution' \
    'The histogram shows the distribution of people by Age.' \
    'Most age groups are evenly distributed between 20 and 60 years.' \
    'A density curve shows slight fluctuations, but overall there is no extreme skewness.' \
    'The highest counts are around ages 25, 35, 45, and 55, where the bar heights peak.' \
    'This indicates that people of all age ranges are listening almost equally, with no specific dominance of a particular age group.')
    st.write('2. Gender Distribution' \
    'The horizontal bar chart shows the distribution of people by Gender.' \
    'The categories are Male, Female, and Other.' \
    'All three categories have almost equal counts (~2600 each).' \
    'This suggests that the dataset is balanced across genders, meaning there is no gender bias in listening habits.')
    st.write('3. Country Distribution' \
    'The horizontal bar chart shows the Country-wise count of people.' \
    'Countries included: CA, DE, AU, US, UK, IN, FR, PK.' \
    'All countries have similar counts (around 900–1050 people).' \
    'Slightly fewer people are from the UK and CA, while AU, DE, US, and IN have the highest counts.' \
    'The distribution is well-balanced across different countries, showing global representation.')
    st.success('Summary Insights' \
    'Age: People from ages 20–60 are evenly represented. Listening is not age-specific.' \
    'Gender: The dataset is well-balanced across Male, Female, and Other genders.' \
    'Country: Representation is fairly even across multiple countries, ensuring no regional dominance.')
st.sidebar.header('Bivariate and multivariate')
c=st.sidebar.radio('click to get Analysis',['Default','BA & UA - Graphs','BA & UA -Report'])
if c=='Default':
    pass
elif c=='BA & UA - Graphs':
    st.image('bmpic1.jpg')
    st.image('bmpic2.jpg')
    st.image('bmpic3.jpg')
    st.image('bmpic4.jpg')
    st.image('bmpic5.jpg')
    st.image('bmpic6.jpg')
    st.image('bmpic7.jpg')
    st.image('bmpic8.jpg')
    st.image('bmpic9.jpg')
elif c=='BA & UA -Report':
    st.write('User counts and age distribution are consistent across all 8 countries (CA-PK)')
    st.write('with the median age around 35-40.')
    st.write('Premium is the most common subscription type for all genders, followed by Free and Student.')
    st.write('Overall, average listening time (≈155) and songs played per day (≈50) show no significant difference by gender.')
    st.write('The overall skip rate is high, consistently around 30%, across all demographics.')
    st.write('Males generally exhibit the highest skip rate and play slightly more songs per day.')
    st.write('Females consistently listen to more ads per week compared to Males in most countries.')
    st.write('The number of ads listened per week shows the highest average in the UK for all genders.')
    st.write('Listening time and songs played per day are strongly and positively correlated.')
    st.success('Other numerical features (age, skip rate, ads) show no strong correlations with each other.')
    st.success('Overall Summary: The user base is stable demographically, with usage volume being gender-neutral. However, behavioral nuances exist: males skip more, females listen to more ads. The high 30% skip rate is the most critical metric for potential retention issues.')