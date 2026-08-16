AI Cold Email Generator

A Python tool that reads business information from a CSV file and uses the Claude AI API to automatically generate personalized cold emails — built for web design agency outreach.

What It Does
Reads a CSV file containing business details (name, address, description, website issues)
Sends each business's information to the Claude API with a structured prompt
Generates a personalised cold email for each business following a consistent format
Saves all generated emails to a new CSV file, ready to send

Why I Built This?
I run a web design agency targeting restaurants and renovation businesses. Writing personalized cold emails manually is time-consuming. This tool automates the process while keeping emails relevant and tailored to each business — combining the consistency of a template with the personalization of AI.

Project Structure
cold-email-generator/
├── main.py            # Main script
├── businesses.csv     # Input file with business data
├── output.csv         # Generated emails (created when script runs)
└── README.md
Input CSV Format

Your input CSV should have the following columns:

name	address	description	website_issues
Joe's Pizza	123 Main St	Family-run Italian restaurant	No website, only a Facebook page
How to Use
Clone this repository
Install the required library:
   pip install anthropic
Add your Anthropic API key as an environment variable:
   export ANTHROPIC_API_KEY=your_key_here
Fill in businesses.csv with your business data
Run the script:
   python main.py
Check output.csv for your generated emails
Tech Stack
Python 3
Claude API (Anthropic)
csv module (built-in)
Author

Maaz Mirza
Web design agency owner | CS student | Building at the intersection of AI and business automation.
