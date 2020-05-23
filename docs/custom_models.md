# Bokeh Extensions

In this document I will describe how I got **prebuilt bokeh extensions** setup
as a part of the awesome-panel package. I needed it temporarily while waiting for the `WebComponent` PR to be reviewed and released by Panel.

Setting up prebuilt extensions using `Bokeh init --interactive` is briefly described in the Bokeh Docs. See [Bokeh Pre-built extensions](https://docs.bokeh.org/en/latest/docs/user_guide/extensions.html).

I hope this description can help others who would like to create custom bokeh models for Bokeh or Panel.

## Steps

I navigated to the root of the awesome-panel package

```bash
cd awesome-panel/package
```

ran `bokeh init --interactive`

```bash
$ bokeh init --interactive
Working directory: C:\repos\private\awesome-panel\package\awesome_panel
Wrote C:\repos\private\awesome-panel\package\awesome_panel\bokeh.ext.json
Create package.json? This will allow you to specify external dependencies. [y/n] y
  What's the extension's name? [awesome_panel]
  What's the extension's version? [0.0.1]
  What's the extension's description? []
Wrote C:\repos\private\awesome-panel\package\awesome_panel\package.json
Create tsconfig.json? This will allow for customized configuration and improved IDE experience. [y/n] y
Wrote C:\repos\private\awesome-panel\package\awesome_panel\tsconfig.json
Created empty index.ts. This is the entry point of your extension.
You can build your extension with bokeh build
All done.
```

In the `package.json` I had to replace

```ts
"dependencies": {
    "bokehjs": "^2.0.2"
  },
```

with

```ts
"dependencies": {
    "@bokeh/bokehjs": "^2.0.2"
  },
```

See [bokeh init issue](https://github.com/bokeh/bokeh/issues/10055).

For convenience I also added

```ts
"paths": {
      "@bokehjs/*": [
        "./node_modules/@bokeh/bokehjs/build/js/lib/*",
        "./node_modules/@bokeh/bokehjs/build/js/types/*"
      ]
    }
```

to `tsconfig.json` in order in order to use import `{ div, label } from "@bokehjs/core/dom"` like @philippjfr does in Panel.