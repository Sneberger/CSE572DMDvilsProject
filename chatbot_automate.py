import csv

from dotenv import load_dotenv
load_dotenv()

import os
os.environ['OPENAI_API_KEY']

from openai import OpenAI
client = OpenAI()

#def chat_compare(nonCCPA, CCPA):    # dummy for testing
#    return 'non-CA: ' + nonCCPA[:10] + ' ... ' + nonCCPA[-10:] + ' CA: ' + CCPA[:10] + ' .. ' + CCPA[-10:]

def chat_review(nonCA, CA):    #PROMPT 1
    query = f"""Compare and contrast {nonCA} and {CA} in light of these questions:
    1) how is data described as being collected?
    2) what data is described as being collected?
    3) what data is described as being provided to third parties?
    4) how long is data described as being retained?
    5) how are a user's rights regarding their data described?
    
    Focus on how {nonCA} and {CA} differ in their descriptions of data usage and user rights.

    Format your answers to each question by heading your response for {nonCA} with 'a)' and 
    how your answer to the questions differs for {CA} from your answers for {nonCA} as 'b)'.
    """

    completion = client.chat.completions.create(
    model="gpt-4-0125-preview",
    messages=[
        {"role": "system", "content": "You are a data privacy attorney, skilled in parsing website privacy policies."},
        {"role": "user", "content": query}
    ]
    )

    return completion.choices[0].message

def chat_review(text):
    question1 = "Please describe how data is being collected below"
    question2 = "Please describe the data being collected below"
    question3 = "Please list the data being provided to third parties below"
    question4 = "Please describe how long data is retained below"
    question5 = "Please describe what are users' rights related to the data items found in your response to question2"

    query = f'''
    {question1}
    Please return in the following format:

    1) 
    1.1 Item 1 how collected
    1.2 Item 2 how collected
    1.3 Item 3 how collected
    ... 

    NOTE: Only include the response in the above format without ANY additional information.
    NOTE: Only include one piece of information per line. Do NOT include multiple pieces of information on the same line.

    {question2}
    Please return in the following format:

    2) 
    2.1 Item 1 being collected
    2.2 Item 2 being collected
    2.3 Item 3 being collected
    ... 

    NOTE: Only include the response in the above format without ANY additional information.
    NOTE: Only include one piece of information per line. Do NOT include multiple pieces of information on the same line.

    {question3}
    Please return in the following format:

    3) 
    3.1 Item 1 provided to third parties
    3.2 Item 2 provided to third parties
    3.3 Item 3 provided to third parties
    ... 

    NOTE: Only include the response in the above format without ANY additional information.
    NOTE: Only include one piece of information per line. Do NOT include multiple pieces of information on the same line.

    {question4}
    Please return in the following format:

    4) 
    4.1 Item 1 how long data found in question2 is retained
    4.2 Item 2 how long data found in question2 is retained
    4.3 Item 3 how long data found in question2 is retained
    ... 

    NOTE: Only include the response in the above format without ANY additional information.
    NOTE: Only include one piece of information per line. Do NOT include multiple pieces of information on the same line.

    {question5}
    Please return in the following format:

    5) 
    5.1 Item 1 user right
    5.2 Item 2 user right
    5.3. Item 3 user right
    ... 

    NOTE: Only include the response in the above format without ANY additional information.
    NOTE: Only include one piece of information per line. Do NOT include multiple pieces of information on the same line.

    Here is the text:

    {text}
    '''
    #"gpt-4-turbo"
    model_name = "gpt-4-0125-preview"

    completion = client.chat.completions.create(
      model=model_name,
      messages=[
        {"role": "system", "content":"You are an expert lawyer specializing in data privacy"},
        {"role": "user", "content": query}
      ]
    )

    return completion.choices[0].message

def csv_to_list(file_name):
    test_list_from_csv = []
    with open(file_name, mode ='r', encoding='utf-8', errors='ignore')as file:
   
        # reading the CSV file
        csvFile = csv.reader(file)
        next(csvFile)
    
        # move lines from csv file to test_list_from_csv
        for line in csvFile:
            test_list_from_csv.append(line)
    return test_list_from_csv

def chat_data():
    test_list_from_csv = csv_to_list('LEFTOVERS_nonCA_Output.csv') #('example_input_test.csv') # for 1,924 URL input

    #header = ['URL', 'Compare']
    header = ['URL', 'Result', 'Deep URL', 'Text', 'Text cont', 'C-Result', 'C-Deep URL', 'C-Text', 'C-Text cont', 'GPT', 'CAGPT']


    #print(*test_list_from_csv, sep = '\n')
    with open('LEFTOVERS_CA_Output.csv', 'w', encoding='utf-8', newline='', errors='ignore') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(header)
        counter = 0

        for line in test_list_from_csv:
            counter += 1
            #for nonCA
            #result = chat_review(line[3] + line[4])
            #for CA
            result = chat_review(line[7] + line[8])
            #for nonCA
            #writer.writerow([line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7], line[8], result])
            #for CA
            writer.writerow([line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7], line[8], line[9], result])
            
            #for LONG
            #for nonCA
            #result = chat_review(line[3] + line[4] + line[5])
            #for CA
            #result = chat_review(line[8] + line[9] + line[10])
            #for nonCA
            #writer.writerow([line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7], line[8], line[9], line[10], result])
            #for CA
            #writer.writerow([line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7], line[8], line[9], line[10], line[11], result])
            
            print(counter, line[0])


def main():
    #scrape_base
    chat_data()

if __name__ == "__main__":
    main()