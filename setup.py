from setuptools import setup, find_packages


def read_requirements():
    with open('requirements.txt') as req:
        content = req.read()
        requirements = content.split('\n')
    
    return requirements


setup(
    name="pycli",
    version="0.0.1",
    description="Python CLI",
    author="Hojung",
    include_package_data=True,
    install_requires=read_requirements(),
    packages=find_packages(),
    entry_points='''
        [console_scripts]
        pycli=pycli.cli:cli
    '''
)