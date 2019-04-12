#!/usr/bin/env python
import os
import public
import yaml

"""
https://docs.jsfiddle.net/github-integration/untitled-1 Display fiddle from Gist
https://docs.jsfiddle.net/github-integration/untitled   Display fiddle from a Github repository
"""


@public.add
class Build:
    """methods: `render()`, `save(path)`"""

    @property
    def css(self):
        for filename in ["demo.css", "fiddle.css"]:
            path = os.path.join(os.getcwd(), filename)
            if os.path.exists(path):
                return open(path).read().strip()
        return ""

    @property
    def yaml(self):
        for filename in ["demo.details", "fiddle.manifest"]:
            path = os.path.join(os.getcwd(), filename)
            if os.path.exists(path):
                with open(path, 'r') as stream:
                    return yaml.load(stream)
        return {}

    @property
    def name(self):
        return self.yaml.get("name", os.path.basename(os.getcwd()))

    @property
    def resources(self):
        return self.yaml.get("resources", [])

    @property
    def js(self):
        for filename in ["demo.js", "fiddle.js"]:
            path = os.path.join(os.getcwd(), filename)
            if os.path.exists(path):
                return open(path).read().strip()
        return ""

    @property
    def html(self):
        for filename in ["demo.html", "fiddle.html"]:
            path = os.path.join(os.getcwd(), filename)
            if os.path.exists(path):
                return open(path).read().strip()
        return ""

    @property
    def head(self):
        lines = []
        for r in self.resources:
            if os.path.splitext(r)[1] == ".css" or ".css" in r:
                lines.append('<link rel="stylesheet" type="text/css" href="%s">' % r)
            if os.path.splitext(r)[1] == ".js" or ".js" in r:
                lines.append('<script type="text/javascript" src="%s"></script>' % r)
        if self.css:
            lines.append("""<style type="text/css">
%s
</style>""" % self.css)
        if self.js:
            lines.append("""<script type="text/javascript">
window.onload=function(){{
%s
}};
</script>""" % self.js)
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
