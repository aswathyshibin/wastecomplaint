def build_prompt(text):

    return f"""
You are an AI system for municipal waste management.

Analyze the complaint and return JSON with:

priority_score (0 to 1)
priority_level (High, Medium, Low)
category

Examples:

Complaint: Garbage not collected for 3 days
priority_score: 0.92
priority_level: High
category: Uncollected Waste

Complaint: Small trash bag near road
priority_score: 0.40
priority_level: Medium
category: Minor Waste

Complaint: Dustbin slightly full
priority_score: 0.20
priority_level: Low
category: Normal Waste

Now analyze:

{text}

Return JSON only.
"""