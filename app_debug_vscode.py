"""Use this module for development with VS Code and the integrated debugger"""
import panel as pn
import ptvsd

# pylint: disable=invalid-name
print("Ready to attach the VS Code debugger")

ptvsd.enable_attach(address=("localhost", 5678,))
ptvsd.wait_for_attach()

# START YOUR CODE HERE
app = pn.Column(pn.pane.Markdown("Hello Panel"))
app.servable()

app.append(pn.pane.Markdown("Step 2"))
