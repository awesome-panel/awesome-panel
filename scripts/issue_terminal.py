import panel as pn

SCRIPT = """
<script src="https://www.unpkg.com/terminal@0.1.4/lib/terminal.js" type="text/javascript"></script>
"""
script_panel = pn.pane.HTML(SCRIPT, width=0, height=0, margin=0, sizing_mode="fixed")


HTML = """
<div id="terminal-1"></div>
<script>
	var t1 = new Terminal()
	t1.setHeight("100%")
	t1.setWidth('100%')

    el = document.getElementById("terminal-1")
    el.appendChild(t1.html)

	t1.print('Hello, world!')
	t1.input('Whats your name?', function (input) {
		t1.print('Welcome, ' + input)
	})
</script>
"""

terminal = pn.pane.HTML(HTML, height=200, width=200)

pn.Column(terminal).servable()

