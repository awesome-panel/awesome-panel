import panel as pn
import asyncio

pn.extension(sizing_mode="stretch_width", design="material")

MODEL = "sentiment-analysis"

@pn.cache
async def _get_pipeline_pyodide(model=MODEL):
    from transformers_js_py import import_transformers_js
    transformers = await import_transformers_js()
    return await transformers.pipeline(model)

@pn.cache
async def _get_pipeline_server(model=MODEL):
    from transformers import pipeline
    
    sync_version = await asyncio.to_thread(pipeline, model)
    
    async def async_version(text):
        return await asyncio.to_thread(sync_version, text)
    
    return async_version

async def _get_pipeline(model=MODEL):
    if pn.state._is_pyodide:
        return await _get_pipeline_pyodide(model)
    return await _get_pipeline_server(model)

examples = ["I'm so happy", "I'm so sad"]
examples_input = pn.widgets.RadioButtonGroup(options=examples)
text_input = pn.widgets.TextInput(placeholder="Send a message", name="Message")
button = pn.widgets.Button(name="Send", icon="send", align="end", button_type="primary")

@pn.depends(examples_input)
def update_text_input(text):
    text_input.value = text

@pn.depends(text_input, button)
async def _response(text, event):
    if not text:
        return {}
    pipe = await _get_pipeline()
    return await pipe(text)

pn.Column(
    examples_input, text_input, button, pn.pane.JSON(_response, depth=2)
).servable()