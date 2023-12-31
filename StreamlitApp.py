import os
import json
import traceback
import pandas as pd
from dotenv import load_dotenv

from src.mcqgenerator.utils import read_file, get_table_data
from src.mcqgenerator.logger import logging
from src.mcqgenerator.MCQGenerator import generator_evaluate_chain
#from src.mcqgenerator.MCQGenerator import evaluate_quiz_sequence
import streamlit as st 



#Importing from Langchain
from langchain.callbacks import get_openai_callback


#load environment veriable from .env
load_dotenv()

try:
    KEY = os.getenv("OPENAI_API_KEY")
    if not KEY:
        raise ValueError("OpenAI API not found in environment variable")
except Exception as e:
    logging.error (f"Error loading OpenAI API key: {e}")
    raise

#loading json file
with open('Response.json', 'r') as file:
    RESPONSE_JSON = json.load(file)
    
#creating a title for the app
st.title("MCQ Mastermind Application with LangChain 🦜⛓️ ")

#create a form using st.form
with st.form("user_inputs"):
    #file upload
    uploaded_file = st.file_uploader("Upload a PDF or txt File")
    
    #input fields
    mcq_count = st.number_input("No. of MCQs", min_value=3, max_value=50)
    
    #subject
    subject = st.text_input("Insert Subject", max_chars=20)
    
    #Quiz tone
    tone = st.text_input("Complexity Level of Questions", max_chars=20, placeholder='Simple')
    
    #Add Button
    button = st.form_submit_button("Create MCQs")
    
    
    #check if button is clicked and all fields have input
    
    if button and uploaded_file is not None and mcq_count and subject and tone:
        with st.spinner("lodding..."):
            try:
                text = read_file(uploaded_file)
                #count tokens and cost of API call
                with get_openai_callback() as cb:
                    response = generator_evaluate_chain(KEY)(
                        {
                            "text": text,
                            "number": mcq_count,
                            "subject": subject,
                            "tone": tone,
                            "response_json" : json.dumps(RESPONSE_JSON)
                        }
                    )
            
            
            except Exception as e:
                traceback.print_exception(type(e), e, e.__traceback__)
                st.error("Error")
                
            else:
                print(f"Total Tokens: {cb.total_tokens}")
                print(f"Prompt Tokens: {cb.prompt_tokens}")
                print(f"Completion Tokens: {cb.completion_tokens}")
                print(f"Total cost: {cb.total_cost}")
                if isinstance(response, dict):
                    #Extract the quiz data from the response
                    quiz = response.get("quiz", None)
                    if quiz is not None:
                        table_data = get_table_data(quiz)
                        if table_data is not None:
                            df=pd.DataFrame(table_data)
                            df.index = df.index+1
                            st.table(df)
                            #Display the review in a text box as well
                            st.text_area(label="Review", value=response['review'])
                        else:
                            st.error("Error in the table data")
                
                else:
                    st.write(response)
                            

    
