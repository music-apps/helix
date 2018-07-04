from setuptools import setup

setup(name='funniest',
      version='0.1',
      description='Python Music Production',
      url='http://github.com/winzurk/helix',
      author='',
      author_email='zwinzurk@asu.edu',
      license='MIT',
      packages=['helix'],
      install_requires=[
          'numpy',
          'librosa',
          'matplotlib'
      ],
      zip_safe=False)

