def test_find_packages_exclude():
    import os
    from setuptools import find_packages
    packages = find_packages(os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
                             exclude=['twspy.ib.cfg'])
    for package in packages:
        assert 'cfg' not in package
