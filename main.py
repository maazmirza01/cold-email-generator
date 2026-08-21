import csv
from google import generativeai
from dotenv import load_dotenv
import os



def mainfunc(): # main function where everything happens ......
    businesses = dict_creator()
    prompts = prompt_engineer(businesses)

    emails = email_receiver(system_instructor(), prompts)

    csv_creator(businesses, emails)
    
    

def dict_creator(): # creates dictionary from the csv input file containing information of businesses with same fields as in the csv
    businesses = []
    with open("businesses.csv", "r") as file:
        reader = csv.DictReader(file)
        for business in reader:
            businesses.append(business)
    return businesses

def prompt_engineer(businesses): # returns a "prompts" list containing prompts for each business using "businesses" dictionary as parameter
    prompts = []
    for business in businesses:
        prompt = f"""

            Write a cold email for the following business:

            Business Name: {business['name']}
            About the Business: {business['description']}
            Compliment to open with: {business['compliment']}
            Website Problems: {business['issues']}

            """
        prompts.append(prompt)
    return prompts


def system_instructor(): # reads "history.txt" and returns a variable containing all of that information
    with open("history.txt", "r") as file:
        instructions = file.read()
    return instructions

def email_receiver(instructions, prompts): # Submits the prompt while passing system instructions to fill a list of emails; "results" which is returned

    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY") # api key is called here

    results = []

    generativeai.configure(api_key=api_key)
    model = generativeai.GenerativeModel("gemini-3.5-flash-lite", system_instruction=instructions)
    chat = model.start_chat()

    for prompt in prompts:
        response = chat.send_message(prompt)
        results.append(response.text)
    return results

def csv_creator(businesses, emails): # creates csv with emails and email copies
    final_list = []
    count = 0
    for business in businesses:
        final_dict = {}
        final_dict["name"] = business["name"]
        final_dict["address"] = business["address"]
        final_dict["email_address"] = business["email"]
        final_dict["email_copy"] = emails[count]
        count += 1
        final_list.append(final_dict)

    with open("email_list.csv", "a") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=["name", "address", "email_address", "email_copy"])
        for dict in final_list:
            writer.writerow(dict)



if __name__ == "__main__":
    mainfunc()