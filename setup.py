from setuptools import setup

setup(name='tux_mixer',
      version='1.0',
      description='PulseAudio control with potentiometers',
      long_description=open('README.md').read(),
      long_description_content_type='text/markdown',
      keywords='mixer pulse audio tux volume control linux',
      classifiers=[
          'License :: OSI Approved :: MIT License',
          'Operating System :: POSIX :: Linux',
          'Programming Language :: Python :: 3.8',
          'Topic :: Multimedia :: Sound/Audio :: Mixers',
          ],
      url='http://github.com/dogonso/tux_mixer',
      author='Dogukan Meral',
      author_email='dogukan.meral@yahoo.com',
      license='MIT',
      include_package_data=True,
      packages=['tux_mixer'],
      entry_points = {
          'console_scripts': ['tux_mixer=tux_mixer.command_line:main'],
          },
      install_requires=[
          'notify2',
          'pystray',
          'pyfirmata',
          'pulsectl==21.3.4',
          'testresources',
          ],
      zip_safe=False)
