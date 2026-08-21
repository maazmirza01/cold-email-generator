from main import prompt_engineer
from main import dict_creator
businesses = dict_creator()
prompts = prompt_engineer(businesses)
for prompt in prompts:
    print(prompt)