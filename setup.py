from setuptools import setup, find_packages
setup(
    name='twspy',
    packages=find_packages(exclude=['twspy.ib.cfg']),
)
