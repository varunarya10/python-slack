from setuptools import setup, find_packages

with open('requirements.txt') as f:
    install_requires = f.read().splitlines()

setup(
    name='python-slackmon',
    version='0.1',
    description='Generates report for consul-alerts',
    author='Amar Krishna',
    author_email='Amar.Krishna@ril.com',
    url='http://github.com/JioCloud/python-slack',
    packages=find_packages(),
    include_package_data=True,
    license='Apache 2.0',
    keywords='slack consul',
    install_requires=install_requires,
)
