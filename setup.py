from distutils.core import setup

setup(
    name='HamBot',
    version='0.1dev',

    description='A basic discord bot',

    # The project's main homepage.
    url='https://www.IamGregAmato.com',

    # Author details.
    author='Greg Amato',
    author_email='amatobahn@gmail.com',

    # License
    license='Proprietary License',

    # Classifiers
    classifiers=[
        # Project Stage:
        'Development Status :: 3 - Alpha',

        # Intended for:
        'Intended Audience :: Developers, Artists',
        'Topic :: Software Development :: Tools',

        # License:
        'License :: Proprietary License',

        # Supported Python versions:
        'Programming Language :: Python :: 3.4.4',
    ],

    # Keywords
    keywords='development tools chat bot',

    # Required dependencies. Will be installed by pip
    # when the project is installed.
    install_requires=['discord', 'bot', 'requests'],
)