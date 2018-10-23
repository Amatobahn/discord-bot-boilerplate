from distutils.core import setup

setup(
    name='DiscordBot',
    version='0.1dev',

    description='Python 3.4+ Discord Bot boilerplate project',

    # The project's main homepage.
    url='https://www.IamGregAmato.com',

    # Author details.
    author='Greg Amato',
    author_email='amatobahn@gmail.com',

    # License
    license='MIT',

    # Classifiers
    classifiers=[
        # Project Stage:
        'Development Status :: 3 - Alpha',

        # Intended for:
        'Intended Audience :: Developers, Artists',
        'Topic :: Software Development :: Tools',

        # License:
        'License :: MIT',

        # Supported Python versions:
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'
    ],

    # Keywords
    keywords='development tools chat bot',

    # Required dependencies. Will be installed by pip
    # when the project is installed.
    install_requires=['discord.py', 'requests'],
)