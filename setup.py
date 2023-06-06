from setuptools import setup

setup(
    name='pyaikit',
    version='1.0.0',
    author='Somenath Sit',
    author_email='somenath.bhu.2010@gmail.com',
    description='A short description of your package',
    long_description='A longer description of your package',
    long_description_content_type='text/markdown',
    url='https://github.com/somenath24/pyaikit',
    packages=['pyaikit'],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
    ],
    python_requires='>=3.6',
    install_requires=[
        'openai',
        'pandas',
        'requests',
        'PyPDF2',
        'PySimpleGUI'
    ],
)