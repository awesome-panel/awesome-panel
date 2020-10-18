import panel as pn
pn.config.js_files["dropzonejs"]="https://rawgit.com/enyo/dropzone/master/dist/dropzone.js"
pn.config.css_files.append("https://rawgit.com/enyo/dropzone/master/dist/dropzone.css")
pn.config.css_files.append("https://www.dropzonejs.com/css/style.css?v=1595510599")
pn.extension()
html = """
    <p> Text </p>

    <!-- Change /upload-target to your upload address -->
    <form action="/upload" class="dropzone" id="demo-upload">

    <div class="dz-message needsclick">
      <button type="button" class="dz-button">Drop files here or click to upload.</button><br>
      <span class="note needsclick">(This is just a demo dropzone. Selected files are <strong>not</strong> actually uploaded.)</span>
    </div>
    <script>var myDropzone = new Dropzone("form#demo-upload", { url: "/file/post"});</script>
"""
pn.pane.HTML(html).servable()