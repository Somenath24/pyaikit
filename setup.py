from setuptools import setup

setup(
    name='pyaikit',
    version='1.0.0',
    author='Somenath Sit',
    author_email='somenath.bhu.2010@gmail.com',
   description='PyAIKit is a user-friendly Python package that simplifies the integration and usage of OpenAIs powerful ChatGPT API for natural language processing tasks',
    long_description='''
        PyAIKit is a Python package designed to enhance the usability and accessibility of AI models, currently OpenAI's ChatGPT API for natural language processing (NLP) tasks. With PyAIKit, developers can seamlessly integrate ChatGPT's advanced text generation capabilities into their applications, simplifying the process of generating high-quality text based on given prompts or conversations.
        Key Features:
        Streamlined Integration: PyAIKit abstracts away the complexities of directly accessing the ChatGPT API, providing user-friendly functions and classes for authentication, API calls, and error handling.
        Text Summarization: Built-in functionality for extracting key insights from lengthy documents or articles, facilitating news aggregation, research analysis, and content curation.
        Sentiment Analysis: Seamlessly integrates with popular sentiment analysis libraries, allowing developers to analyze the sentiment of generated text and gain valuable insights into the emotional tone.
        Language Translation: Convenient translation capabilities that support various languages, enabling real-time multilingual applications.
        Text Generation: Generate any summary/text for a given topic.

        Future Extension Plans for PyAIKit: Enhancing the Power of NLP
        PyAIKit is an evolving project with a roadmap of more future extensions and enhancements. Here are some of the plans that are being considered to further empower the package:

        Model Customization:
        One of the key areas of focus for PyAIKit future development is enabling model customization. This means allowing users to fine-tune the underlying ChatGPT model according to their specific domain or application requirements. Customization options would enable users to train the model on their own data, resulting in more tailored and accurate text generation.

        Advanced Text Analysis:
        It aims to provide more advanced text analysis functionalities in the future. This includes features such as named entity recognition, part-of-speech tagging, and sentiment analysis. These enhancements would allow users to extract valuable insights from text data, enabling more sophisticated NLP applications and empowering data-driven decision-making.
        Integration with Other AI Models:
        This expansion would enable users to combine the power of ChatGPT with other state-of-the-art models, such as image recognition or speech processing models. This integration would enhance the package's versatility and enable the development of more comprehensive AI solutions.

    ''',
    long_description_content_type='text/markdown',
    url='https://github.com/somenath24/pyaikit',
    packages=['pyaikit','sentiment_analysis','text_summerization','translator','text_generation'],
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