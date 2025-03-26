import requests
import json
import numpy as np
from sklearn.ensemble import IsolationForest
from fastapi import FastAPI, Query
import google.generativeai as genai

try:
    import ssl
except ModuleNotFoundError:
    print("Warning: SSL module is not available. Secure HTTP requests may fail.")

# Configure the Google Generative AI API
genai.configure(api_key="")  # Replace with your actual API key

# Initialize FastAPI app
app = FastAPI()

# Entity analysis API endpoint
@app.get("/analyze-entity")
def analyze_entity(entity_name: str = Query(..., description="WellsFargo")):
    oc_data = fetch_open_corporates(entity_name)
    wd_data = fetch_wikidata(entity_name)
    genai_analysis = analyze_with_genai(entity_name, oc_data, wd_data)
    
    return genai_analysis

# Function to fetch data from OpenCorporates API
def fetch_open_corporates(entity_name):
    try:
        url = f"https://api.opencorporates.com/v0.4/companies/search?q={"wellsfargo"}"
        response = requests.get(url)
        print(response)
        if response.status_code == 200:
            return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching OpenCorporates data: {e}")
    return {}

# Function to fetch data from Wikidata
def fetch_wikidata(entity_name):
    try:
        query = f"SELECT ?item ?itemLabel WHERE {{ ?item rdfs:label '{"wellsfargo"}'@en . }} LIMIT 1"
        url = f"https://query.wikidata.org/sparql"
        headers = {"Accept": "application/json"}
        response = requests.get(url, headers=headers, params={"query": query, "format": "json"})
        print(response)
        if response.status_code == 200:
            return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching Wikidata: {e}")
    return {}

# Function to analyze entity using Google Generative AI
def analyze_with_genai(entity_name, oc_data, wd_data):
    combined_data = {
        "Entity Name": entity_name,
        "OpenCorporates Data": oc_data,
        "Wikidata Data": wd_data
    }
    json_output_str = json.dumps(combined_data, indent=2)

    prompt = f"""You are an AI risk analysis expert. Analyze the following data for potential risks:
    {json_output_str}
    Provide a detailed risk assessment, including risk score (0-1), justification, confidence level, and extracted entity details."""
    
    model = genai.GenerativeModel("gemini-1.5-pro")  # Replace with the appropriate model name
    response = model.generate_content(prompt, generation_config={"temperature": 0.7, "max_output_tokens": 1000})
    return json.loads(response.text) if response else {"error": "No response from the model"}


