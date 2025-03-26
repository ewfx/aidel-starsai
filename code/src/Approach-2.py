import json
import google.generativeai as genai

def risk_analysis_llm(ofac_response, open_sanctions_response, model_name="gemini-1.5-pro", max_tokens=1000, temperature=0.7):
    # Combine both responses into a single JSON structure
    combined_data = {
        "OFAC Screening Results": ofac_response,
        "OpenSanctions Screening Results": open_sanctions_response
    }

    # Convert JSON to formatted string
    json_output_str = json.dumps(combined_data, indent=2)

    prompt = f"""You are a risk analysis expert specializing in identifying potential financial, legal, and security risks based on sanctions data that I will be providing you. You will carefully analyze the following raw JSON response, which contains details about various entities from multiple sources (OFAC and OpenSanctions). Your task is to determine whether the entities involved are risky and, if so, provide a well-reasoned justification with supporting evidences. You be like an Explainable AI.
A possbile response format can be something like:
Sanction Analysis:

Entity Name
- Risk Score: (0-1)?
- Justification and Evidence: (should include List of sanctioning bodies and any other details available, Reason for sanctions such as Terrorism, money laundering, fraud, etc., and any Additional insights like alias details, past violations, associated organizations, if any)

... (if more entities involved, use the same format)

Overall Risk Score (Sanction based) for the transaction:
- Final Risk Level: (in 0-1)
- Confidence Level: (in 0-1;  how much confidence do you have on the Final Risk Level)
- Justification: Justify everything, be as much detailed as possible, consideration of all individual entity risk levels, explanation of why this transaction should be flagged or cleared, Any patterns or red flags in the provided data, or anything. Think out of the box and think like an expert

Here is the JSON output from the sanctions screening:
{json_output_str}
"""

    # Configure the Gemini API
    genai.configure(api_key="")

    # Select the Gemini model
    model = genai.GenerativeModel(model_name)

    # Generate the response
    response = model.generate_content(prompt, generation_config={"temperature": temperature, "max_output_tokens": max_tokens})

    return response.text if response else "Error: No response from the model"