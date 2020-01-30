# Tips and Tricks + Best Practices for creating performant panel apps

Slow Panel apps can have different causes

- The Bokeh Layout Engine can slow your application down. See [Issue 9515](https://github.com/bokeh/bokeh/issues/9515).

My tips+tricks to mitigate this is.

- Use the Template system whenever you can.
- Don’t do lots of nested Columns and Rows in Panel. Use pn.Param if you have a model with a lot of parameters.
- Don’t configure layout settings like width, height, margin etc. of Panel Columns and Rows via Css. Use Column and Row attributes in Panel for that.
- Use FireFox instead of Chrome. It's much faster.
