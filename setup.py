from setuptools import find_packages, setup

exec(open('twspy/_version.py').read())

setup(
    name='twspy',
    version=__version__,

    description='Python API to Interactive Brokers TWS',
    long_description=open('README.rst').read(),
    author='Brian Kearns',
    author_email='bdkearns@gmail.com',
    url='https://github.com/bdkearns/twspy',
    license='MIT',

    packages=find_packages(exclude=['twspy.ib.cfg']),
)
