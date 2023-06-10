from setuptools import setup

setup(
    name='pyaikit',
    version='1.0.4',
    author='Somenath Sit',
    author_email='somenath.bhu.2010@gmail.com',
    description='PyAIKit is a user-friendly Python package that simplifies the integration and usage of OpenAIs powerful ChatGPT API for natural language processing tasks',
    long_description=open("README.md").read(),
    long_description_content_type='text/markdown',
    url='https://github.com/somenath24/pyaikit',
    packages=['pyaikit','pyaikit/sentiment_analysis','pyaikit/text_summerization','pyaikit/translation','pyaikit/text_generation'],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
    ],
    project_urls={
        'GitHub' :  'https://github.com/somenath24/pyaikit',
        'Changelog' : 'https://github.com/Somenath24/pyaikit/blob/main/CHANGELOG.md'
    },
    python_requires='>=3.6',
    install_requires=[
        'openai',
        'pandas',
        'requests',
        'PyPDF2',
        'PySimpleGUI'
    ],
)