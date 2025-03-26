import json  # Add this import at the top of your file

# Mock function to simulate the response from analyze_with_genai
def generate_demo_response(entity_name):
    # Simulated OpenCorporates data
    oc_data = {
        "company": {
            "name": "Wells Fargo & Company",
            "jurisdiction_code": "us",
            "company_number": "123456789",
            "status": "Active",
            "industry_codes": ["Finance", "Banking"],
            "officers": [
                {"name": "John Doe", "role": "CEO"},
                {"name": "Jane Smith", "role": "CFO"}
            ]
        }
    }

    # Simulated Wikidata data
    wd_data = {
        "entity": {
            "label": "Wells Fargo",
            "description": "An American multinational financial services company.",
            "aliases": ["Wells Fargo Bank", "Wells Fargo & Co"],
            "founded": "1852",
            "headquarters": "San Francisco, California, USA"
        }
    }

    # Simulated risk assessment
    risk_assessment = {
        "Risk Score": 0.7,
        "Justification": "The entity operates in the financial sector, which is prone to risks such as money laundering and fraud. Additionally, past controversies and regulatory fines have been associated with the company.",
        "Confidence Level": 0.85,
        "Extracted Entity Details": {
            "Sanctioning Bodies": ["None identified"],
            "Reason for Risk": "High exposure to financial transactions and regulatory scrutiny.",
            "Additional Insights": [
                "The company has been fined for unethical practices in the past.",
                "Strong presence in the banking sector with global operations."
            ]
        }
    }

    # Combine all data into a single response
    response = {
        "Entity Name": entity_name,
        "OpenCorporates Data": oc_data,
        "Wikidata Data": wd_data,
        "Risk Assessment": risk_assessment
    }

    return response


# Example usage
if __name__ == "__main__":
    entity_name = "WellsFargo"
    demo_response = generate_demo_response(entity_name)
    print(json.dumps(demo_response, indent=2))