from anthropic import HUMAN_PROMPT, AI_PROMPT

def get_prompt(user_input):
    prompt_template = "You are now an expert in the Book of Change and a helpful expert in the field of the [situation]. To help me coming up a solution or a way to handle the [situation], I'd like you to interpret my [situation] according to the Book of Change, then speak from my perspective. You should be telling me which hexagram that the [situation] is related to, then give me a thorough explanation. Eventually, give me some insights so that I could learn from the [situation]. Your insights should be professional, specific, feasible, step-by-step, and realistic."
    user_inquiry = "[situation]:" + user_input
    end_prompt = f"{HUMAN_PROMPT}" + prompt_template + user_inquiry + f"{AI_PROMPT}"
    return end_prompt