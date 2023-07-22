from setuptools import setup
import os

version_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 
                            "freecad", "part_centroid", "version.py")
with open(version_path) as fp:
    exec(fp.read())

setup(name='freecad.part_centroid',
      version=str(__version__),
      packages=['freecad',
                'freecad.part_centroid'],
      maintainer="Jonathan Railsback",
      maintainer_email="jonbitzen@hotmail.com",
      url="",
      description="workbench to change centroid of imported geometry",
      install_requires=[], # should be satisfied by FreeCAD's system dependencies already
      include_package_data=True)
