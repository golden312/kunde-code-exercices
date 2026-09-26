from week3.Part_3_Prompt.prompt_test import get_answer
from pathlib import Path


user_question = "Where can I get free mental health support in Ottawa?"
mental_health_resources = [
    {
        "name": "Ottawa Community Wellness Centre",
        "service": "Counselling and mental health support",
        "address": "150 King Edward Avenue, Ottawa, ON",
        "phone": "613-555-0150",
        "hours": "Monday–Friday, 9:00 AM–5:00 PM",
        "languages": ["English", "French", "Arabic"],
        "eligibility": "Services are available to Ottawa residents. Intake may be required.",
        "cost": "Free."
    },
    {
        "name": "Newcomer Wellness Program",
        "service": "Mental health counselling and newcomer support groups",
        "address": "325 Dalhousie Street, Ottawa, ON",
        "phone": "613-555-0177",
        "hours": "Tuesday–Saturday, 10:00 AM–6:00 PM",
        "languages": ["English", "French", "Arabic"],
        "eligibility": "For newcomers experiencing stress, isolation, or adjustment difficulties.",
        "cost": "Free."
    },
    {
        "name": "Youth Counselling Services",
        "service": "Short-term counselling for youth",
        "address": "80 Elgin Street, Ottawa, ON",
        "phone": "613-555-0137",
        "hours": "Monday–Friday, 10:00 AM–7:00 PM",
        "languages": ["English", "French"],
        "eligibility": "For youth ages 13–24.",
        "cost": "Free."
    }
]

prompt = f"""
            Here is the needed information for the system prompt: {mental_health_resources}. The question the user asked was: {user_question}
          """

# ^ If your team decides to write a system prompt do so here, if not leave it empty

system_prompt =  """
You are a legal advisor assistant helping sudanese newcomers and
refugees through their legal process into Canada. You must give
accurate and factual information by using the information given to you and format it in a user-friendly way where it
clearly displays the information in the form of a list in order from most important to least important (name, service, ). Then, write a clear description
that serves as an introduction to the given places where it will give them all the necessary information they need to know.
"""

#! Don't change anything below

answer = get_answer(prompt, system_prompt)

output_path = Path(__file__).parent / "ai_output.md"
output_path.write_text(answer, encoding="utf-8")