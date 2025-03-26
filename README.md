# 🚀 STARS AI

## 📌 Table of Contents
- [Introduction](#introduction)
- [Demo](#demo)
- [Inspiration](#inspiration)
- [What It Does](#what-it-does)
- [How We Built It](#how-we-built-it)
- [Challenges We Faced](#challenges-we-faced)
- [How to Run](#how-to-run)
- [Tech Stack](#tech-stack)
- [Team](#team)

---

## 🎯 Introduction
This project aims to develop an AI-powered system that can extract, analyze, classify, and risk-score entities such as companies and organizations using Generative AI and Machine Learning. By integrating open datasets and APIs (e.g., OpenCorporates, Wikidata), the system identifies potential risks, detects anomalies, and provides evidence-backed justifications.
Key Features:
Entity Data Extraction – Retrieves real-time information from open sources.
AI-Based Risk Analysis – Uses Google Generative AI to assess risk levels dynamically.
Anomaly Detection – Identifies shell or fraudulent companies.
Justification & Evidence – Generates structured reports with confidence scores.
API-Driven Implementation – Enables seamless integration with other systems.
This solution is designed for fraud detection, compliance monitoring, and financial risk assessment, ensuring transparency and efficiency in risk analysis using only free tools and open-source datasets.

## 🎥 Demo
🔗 [Video Demo](https://github.com/ewfx/aidel-starsai/blob/main/artifacts/demo/VID-20250326-WA0003.mp4)
📹  


## 💡 Inspiration
The inspiration for this project comes from the growing need for automated risk assessment and fraud detection in corporate and financial sectors. With increasing financial crimes, shell companies, and fraudulent transactions, businesses, regulators, and financial institutions struggle to verify and assess the credibility of entities efficiently..

## ⚙️ What It Does
🚨 AI-Based Risk Scoring & Anomaly Detection
🔎 Fraud & Shell Company Identification
📜 Evidence-Based Justification
⚡ API-Driven & Dynamic Reports

## 🛠️ How We Built It
🔹 Programming Language Python – For backend development, data processing, and AI/ML integration.
🔹 AI & Machine Learning - Google Generative AI (Gemini-1.5 Pro) – For NLP-based risk assessment, entity classification, and justification generation.
Scikit-learn (Isolation Forest) – For anomaly detection and fraud identification.
NumPy – For data manipulation and risk score calculations.
🔹 Web Frameworks & APIs - FastAPI – For building a high-performance REST API to analyze entities.
Requests – For fetching data from OpenCorporates API and Wikidata API.
🔹 Open Datasets & External APIs - OpenCorporates API – For retrieving corporate registration data.
Wikidata SPARQL API – For fetching entity-related information.
🔹 Deployment & Environment - JSON – For structured data representation and AI model input/output.
Open-source and free tools – Ensuring accessibility without paid dependencies.

## 🚧 Challenges We Faced
1️⃣ Handling Unstructured & Incomplete Data
2️⃣ Dynamic Risk Scoring & Anomaly Detection
3️⃣ API Rate Limits & Latency Issues
4️⃣ Generating Justifiable AI Outputs
5️⃣ Free Tool Constraints

## 🏃 How to Run
1. Clone the repository  
   ```sh
   git clone https://github.com/aidel-starsai.git
   ```
2. Install dependencies  
   ```sh
   pip install fastapi requests numpy scikit-learn google-generativeai uvicorn

   ```
3. Run the project  
   ```sh
   python app.py
   ```

## 🏗️ Tech Stack
Python – Backend logic, AI/ML integration, and API interactions.
Google Generative AI (Gemini-1.5 Pro) – NLP-based entity classification, risk assessment, and justification generation.
Scikit-learn (Isolation Forest) – Machine learning-based anomaly detection for fraud identification.
NumPy – Data manipulation and numerical computations for risk modeling.
OpenCorporates API – Fetch corporate registration and business entity details.
Wikidata SPARQL API – Extract entity-related information and relationships.

## 👥 Team
- Ravi Shankar Garlapati
- Alli Rajj
- Sudarshan Katepally
- Ravikanth Pal
- Anandeshi Siva
