**<h1>Text To SQL Converter</h1>**<br />
Utilized Gemini Pro Model that convert the entered text to SQL Query and fetch the data from SQLLite DB.<br /><br />

**Implementation Steps:**<br />
Step 1: Implements python code which read the csv file and stores the data to database (SQLLite).<br />
Step 2: Configure Genai Key, and create function that load the Gemini model which convert text to SQL Query<br />
Step 3: Create function which takes the Query generated by Gemini model and fetched the data.<br />
Step 4: Implement prompt template<br />
Step 5: Initialize streamlit to take input text from user and disply the data which is fetched by Gemini generated SQL Query.<br /><br />

**Ouput:**<br />

![Alt text](https://github.com/pneel27/SQLGen/blob/main/Screenshot%20(159).png?raw=true "SampleOutput1") <br />
![Alt text](https://github.com/pneel27/SQLGen/blob/main/Screenshot%20(160).png?raw=true "SampleOutput2")
