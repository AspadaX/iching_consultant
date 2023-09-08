import gradio as gr
from commons.llms_calling import claude_chat_completion,claude_api,local_api,local_chat_completion,openai_api,openai_chat_completion
from commons.claude_prompts import get_prompt
from commons.file_handling import save_response_to_file

a_models = ["claude-1", "claude-1-100k", "claude-2", "claude-instant-1", "claude-instant-1-100k"]
o_models = ["gpt-3.5-turbo-4k","gpt-3.5-turbo-16k","gpt-4-16k","gpt-4-32k"]
l_models = ["local_large_language_model"]
models = a_models + o_models + l_models

def iching(query,model):
    a_models = ["claude-1", "claude-1-100k", "claude-2", "claude-instant-1", "claude-instant-1-100k"]
    o_models = ["gpt-3.5-turbo-4k","gpt-3.5-turbo-16k","gpt-4-16k","gpt-4-32k"]
    l_models = ["local_large_language_model"]

    end_prompt = get_prompt(query)

    if model in a_models:
        claude = claude_api()
        response = claude_chat_completion(prompt=end_prompt, model_input=model, api=claude).completion
        save_response_to_file(response,"claude_response.txt")
        return response
    elif model in o_models:
        openai_api()
        response = openai_chat_completion(prompt=end_prompt, model=model)
        save_response_to_file(response,"gpt_response.txt")
        return response
    elif model in l_models:
        local_api()
        response = local_chat_completion(prompt=end_prompt)
        save_response_to_file(response, "local_response.txt")
        return response

demo = gr.Interface(
    fn=iching,
    inputs=[gr.Textbox(label="Query"),gr.Radio(models)],
    outputs=gr.Textbox(label="Response"),
)

demo.launch()