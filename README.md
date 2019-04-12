<!--
https://pypi.org/project/readme-generator/
https://pypi.org/project/python-readme-generator/
-->

[![](https://img.shields.io/pypi/pyversions/jsfiddle-build.svg?longCache=True)](https://pypi.org/project/jsfiddle-build/)
[![](https://img.shields.io/pypi/v/jsfiddle-build.svg?maxAge=3600)](https://pypi.org/project/jsfiddle-build/)
[![Travis](https://api.travis-ci.org/looking-for-a-job/jsfiddle-build.py.svg?branch=master)](https://travis-ci.org/looking-for-a-job/jsfiddle-build.py/)

#### Installation
```bash
$ [sudo] pip install jsfiddle-build
```

#### How it works
[jsfiddle github repo](https://docs.jsfiddle.net/github-integration/untitled-1):
```
.
├── build.html          generated
├── demo.html           required
├── demo.css            optional
├── demo.js             optional
├── demo.details        optional
```

[jsfiddle github gist](https://docs.jsfiddle.net/github-integration/untitled):
```
.
├── build.html          generated
├── fiddle.html         required
├── fiddle.css          optional
├── fiddle.js           optional
├── fiddle.manifest     optional
```


`build.html`:
```html
<html>
<head>
<title>{title}</title>
{resources}
<style type="text/css">
    {css}
</style>
<script type="text/javascript">
window.onload=function(){
    {js}
}
</script>
</head>
<body>
    {html}
</body>
</html>
```

#### Classes
class|`__doc__`
-|-
`jsfiddle_build.Build` |methods: `render()`, `save(path)`

#### Executable modules
usage|`__doc__`
-|-
`python -m jsfiddle_build path ...` |build `build.html` from jsfiddle files (`demo.css`, `demo.details`,`demo.js`,`demo.html`)

#### Examples
```bash
$ find . -name "*.html" ! -name "build.*" | xargs python -m jsfiddle_build
```

---
paths with spaces:

OS|speed|command
-|-|-
any|slow|`find . -name "*.html" ! -name "build.*" -exec python -m jsfiddle_build {} \;`
Linux|fast|`find . -name "*.html" ! -name "build.*" -print0 \| xargs -d '\n' python -m jsfiddle_build`
macOS|fast|`find . -name "*.html" ! -name "build.*" -print0 \| xargs -0 python -m jsfiddle_build`

#### Related projects
+   [`jsfiddle-build.py` - build `build.html` file from jsfiddle files](https://pypi.org/project/jsfiddle-build/)
+   [`jsfiddle-factory.py` - jsfiddles mass production](https://pypi.org/project/jsfiddle-build/)
+   [`jsfiddle-generator.py` - jsfiddle files generator](https://pypi.org/project/jsfiddle-generator/)
+   [`jsfiddle-github.py` - jsfiddle github integration helper](https://pypi.org/project/jsfiddle-github/)
+   [`jsfiddle-readme-generator.py` - generate jsfiddle `README.md`](https://pypi.org/project/jsfiddle-readme-generator/)

#### Links
+   [Display fiddle from a Github repository](https://docs.jsfiddle.net/github-integration/untitled-1)
+   [Display fiddle from Gist](https://docs.jsfiddle.net/github-integration/untitled)

<p align="center">
    <a href="https://pypi.org/project/python-readme-generator/">python-readme-generator</a>
</p>