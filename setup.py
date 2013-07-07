from distutils.core import setup
setup(name='widukind',
	version='0.1',
	description='A tool for building real-time economic database',
	author='Michaël Malter',
	author_email='dev@michaelmalter.fr',
	package_dir=['':'src'],
	packages=[''],
	install_requires=[
		'pandas>=0.11'
		]
	)
