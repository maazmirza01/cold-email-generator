from main import email_receiver
from main import system_instructor
from main import prompt_engineer
from main import dict_creator

businesses = dict_creator()
prompts = prompt_engineer(businesses)

emails = email_receiver(system_instructor(), prompts)

for email in emails:
    print (email)