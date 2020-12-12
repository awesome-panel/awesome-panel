import panel as pn

STYLE = """
td.large-number {
    background: red;
    color: gray;
}
"""
pn.config.raw_css.append(STYLE)

html_pane = pn.pane.HTML(
    """
<h1>This is an Example Code</h1>
<table>
  <tbody>
<tr>
    <th>January</th>
    <th>February</th>
    <th>March</th>
  </tr>
  <tr>
    <td class="large-number">15</td>
    <td>10</td>
    <td>8</td>
  </tr>
  <tr>
    <td>2</td>
    <td>3</td>
    <td class="large-number">34</td>
  </tr>
</tbody>
</table>
"""
)

pn.Column(html_pane).servable()
