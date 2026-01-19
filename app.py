import gradio as gr

def optimize_prompt(user_input, style):
    base_prompt =  f""" A{style.lower()} style interior design of {user_input}, proffessional interior photography, soft natural lighting, realistic textures, high detail, wide angle lens, 4k quality"""
    negative_prompt = """ low quality, blurry, distorted furniture, bad lightning, cluttered space, oversaturated colors, watermark"""
    return base_prompt.strip(), negative_prompt.strip()

styles = ["Modern", "Minimalist", "Bohemian", "Industrial", "Scandinavian", "Rustic"]

with gr.Blocks() as demo:
    gr.Markdown("# Interior Design Prompt Optimizer")
    gr.Markdown("Convert simple ideas into high quality AI image prompts")

    user_input = gr.Textbox(label = "Describe the room", placeholder = "Example:small living room with large windows")
    style = gr.Dropdown(choices=styles, label="Select Design Style", value="Modern")
    generate_button = gr.Button("Generate optimized Prompt")

    output_prompt = gr.Textbox(label="Optimized Prompt", lines=6, show_copy_button=True)
    negative_prompt = gr.Textbox(label="Negative Prompt", lines=4, show_copy_button=True)

    generate_button.click(fn = optimize_prompt, inputs=[user_input, style], outputs=[output_prompt, negative_prompt])

    demo.launch()