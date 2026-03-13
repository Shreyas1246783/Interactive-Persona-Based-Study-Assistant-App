import os
from google import genai
from google.genai import types
import gradio as gr

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

personalities = {
    "Friendly": "You are a friendly study assistant who explains concepts simply with examples.",
    "Academic": "You are a professional professor giving detailed structured explanations."
}

def study_assistant(question, persona):

    system_prompt = personalities[persona]

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        config=types.GenerateContentConfig(
            system_instruction=system_prompt,
            temperature=0.4,
            max_output_tokens=2000
        ),
        contents=question
    )

    return response.text


demo = gr.Interface(
    fn=study_assistant,
    inputs=[
        gr.Textbox(lines=4, label="Question"),
        gr.Radio(choices=list(personalities.keys()), value="Friendly")
    ],
    outputs=gr.Textbox(lines=10),
    title="Study Assistant"
)

demo.launch()
