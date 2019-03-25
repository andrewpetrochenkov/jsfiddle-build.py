#!/usr/bin/env python
import jsfiddle
import os
import public


@public.add
class Build:
    """methods: `render()`, `save(path)`"""

    @property
    def css(self):
        path = os.path.join(os.getcwd(), "demo.css")
        return open(path).read() if os.path.exists(path) else ""

    @property
    def details(self):
        return jsfiddle.details.load()

    @property
    def name(self):
        return self.details.get("name", os.path.basename(os.getcwd()))

    @property
    def resources(self):
        return self.details.get("resources", [])

    @property
    def js(self):
        path = os.path.join(os.getcwd(), "demo.js")
        return open(path).read() if os.path.exists(path) else ""

    @property
    def html(self):
        path = os.path.join(os.getcwd(), "demo.html")
        return open(path).read()

    @property
    def head(self):
        lines = []
        for r in self.resources:
            if os.path.splitext(r)[1] == ".css" or ".css" in r:
                lines.append('<link rel="stylesheet" type="text/css" href="%s">' % r)
            if os.path.splitext(r)[1] == ".js" or ".js" in r:
                lines.append('<script type="text/javascript" src="%s"></script>' % r)
        return "\n".join(lines)

    def render(self):
        kwargs = dict(
            css=self.css,
            head=self.head,
            html=self.html,
            js=self.js,
            name=self.name,
        )
        return """<html>
<head>
<title>{name}</title>
{head}
<style type="text/css">
    {css}
</style>
<script type="text/javascript">
window.onload=function(){{
    {js}
}}
</script>
</head>
<body>
    {html}
</body>
</html>
""".format(**kwargs)

    def save(self, path):
        dirname = os.path.dirname(path)
        if dirname and not os.path.exists(dirname):
            os.makedirs(dirname)
        open(path, "w").write(str(self))

    def __str__(self):
        return self.render()

