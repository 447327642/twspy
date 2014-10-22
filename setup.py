from setuptools import find_packages, setup

exec(open('twspy/_version.py').read())

long_description = '\n'.join([open('README.rst').read(),
                              open('NEWS.rst').read()])

setup(
    name='twspy',
    version=__version__,  # noqa

    description='Python API to Interactive Brokers TWS',
    long_description=long_description,
    author='Brian Kearns',
    author_email='bdkearns@gmail.com',
    url='https://github.com/bdkearns/twspy',
    license='MIT',

    packages=find_packages(exclude=['twspy.ib.cfg']),
)
