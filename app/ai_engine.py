import requests
import json
import re
from app.prompt import build_prompt
from app.config import API_KEY, API_URL, MODEL_NAME


def analyze_complaint(text):
    prompt = build_prompt(text)

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": MODEL_NAME,
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "temperature": 0
    }

    try:
        response = requests.post(API_URL, headers=headers, json=data, timeout=10)
        response.raise_for_status()
        
        result_json = response.json()
        content = result_json['choices'][0]['message']['content']
        
        # Robustly extract JSON from the response content
        json_match = re.search(r'\{.*\}', content, re.DOTALL)
        if json_match:
            return json.loads(json_match.group(0))
        else:
            return {
                "priority_score": 0.5,
                "priority_level": "Medium",
                "category": "Uncategorized",
                "error": "Could not parse AI response"
            }
            
    except Exception as e:
        print(f"Error in AI analysis: {e}")
        return {
            "priority_score": 0.0,
            "priority_level": "Low",
            "category": "Error",
            "error": str(e)
        }