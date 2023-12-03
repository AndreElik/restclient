from setuptools import setup
REQIRES = [
    'allure-pytest',
    'curlify',
    'requests',
    'structlog'
]
setup(
    name='restclient',
    version='0.0.1',
    packages=['restclient'],
    url='https://github.com/AndreElik/restclient.git',
    license='MIT',
    author='Andre',
    author_email='',
    install_requires=REQIRES,
    description='restclient'
)
