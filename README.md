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
required: `demo.html`. optional: `demo.css`, `demo.js`, `demo.details`

`demo.details` (optional)
```yml
---
 name: Name of the Demo
 description: Some description, please keep it in one line
 resources:
   - http://some.url.com/some/file.js
   - http://other.url.com/other_filename.css
```

`build.html`:
```html
<html>
<head>
<title>Name of the Demo</title>
<script type="text/javascript" src="http://some.url.com/some/file.js"></script>
<link rel="stylesheet" type="text/css" href="http://other.url.com/other_filename.css">
<style type="text/css">
    demo.css ...
</style>
<script type="text/javascript">
window.onload=function(){
    demo.js ...
}
</script>
</head>
<body>
    demo.html ...
</body>
</html>

```

#### Classes
class|`__doc__`
-|-
`jsfiddle_build.Build` |methods: `render()`, `save(path)`

#### Examples
```bash
$ find . -name "demo.html" | xargs python -m jsfiddle_build
```

paths with spaces:

OS|speed|command
-|-|-
Linux|fast|`find . -name "demo.html" -print0 | xargs -d '\n' python -m jsfiddle_build`
macOS|fast|`find . -name "demo.html" -print0 | xargs -0 python -m jsfiddle_build`
any|slow|`find . -name "demo.html" -exec python -m jsfiddle_build {} \;`

#### Related projects
+   [`jsfiddle.py` - jsfiddle helper](https://pypi.org/project/jsfiddle/)
+   [`jsfiddle-build.py` - build html file from jsfiddle files](https://pypi.org/project/jsfiddle-build/)
+   [`jsfiddle-generator.py` - jsfiddle files generator](https://pypi.org/project/jsfiddle-generator/)
+   [`jsfiddle-readme.py` - generate jsfiddle `README.md`](https://pypi.org/project/jsfiddle-readme/)

#### Links
+   [Display fiddle from a Github repository](https://docs.jsfiddle.net/github-integration/untitled-1)

<p align="center">
    <a href="https://pypi.org/project/python-readme-generator/">python-readme-generator</a>
</p>