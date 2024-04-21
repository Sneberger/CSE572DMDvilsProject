import csv
import re

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
    test_list_from_csv = csv_to_list('Mixed_Pairs_FINAL_Result_wGPT.csv') #('example_input_test.csv') # for 1,924 URL input

    #header = ['URL', 'Compare']
    header = ['URL', 'Result', 'Deep URL', 'Text', 'Text cont', 'C-Result', 'C-Deep URL', 'C-Text', 'C-Text cont', 'GPT', 'CAGPT', 'Q1', 'Q2', 'Q3', 'Q4', 'Q5']


    #print(*test_list_from_csv, sep = '\n')
    with open('Heuristic_Mixed_Output.csv', 'w', encoding='utf-8', newline='', errors='ignore') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(header)

        for line in test_list_from_csv:
            nonCA_counter_1 = line[9].count('1.')
            CA_counter_1 = line[10].count('1.')
            nonCA_counter_2 = line[9].count('2.')
            CA_counter_2 = line[10].count('2.')
            nonCA_counter_3 = line[9].count('3.')
            CA_counter_3 = line[10].count('3.')
            nonCA_counter_4 = line[9].count('4.')
            CA_counter_4 = line[10].count('4.')
            nonCA_counter_5 = line[9].count('5.')
            CA_counter_5 = line[10].count('5.')
            Q1 = CA_counter_1 - nonCA_counter_1
            Q2 = CA_counter_2 - nonCA_counter_2
            Q3 = CA_counter_3 - nonCA_counter_3
            Q4 = CA_counter_4 - nonCA_counter_4
            Q5 = CA_counter_5 - nonCA_counter_5

            #print(nonCA_counter_1, nonCA_counter_2, nonCA_counter_3, nonCA_counter_4, nonCA_counter_5)
            #print(CA_counter_1, CA_counter_2, CA_counter_3, CA_counter_4, CA_counter_5)

            writer.writerow([line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7], line[8], line[9], line[10], Q1, Q2, Q3, Q4, Q5])         


def main():
    #scrape_base
    chat_data()

if __name__ == "__main__":
    main()