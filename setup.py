import setuptools

setuptools.setup(
    name='jsfiddle-build',
    install_requires=open('requirements.txt').read().splitlines(),
    packages=setuptools.find_packages()
)
