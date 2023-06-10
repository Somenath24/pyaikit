<h1>PyAIKit</h1>

<p>

The `PyAIKit` package provides various functionalities for AI-based text analysis and processing.

Sub-packages
------------

sentiment_analysis:
    Provides functionality for performing sentiment analysis on text data.

    Feature:
    - generate_basic_sentiment: Provides basic sentiment analysis functionality, allowing the classification of text into positive, negative, or neutral sentiment.
    - generate_advanced_sentiment: Provides advanced sentiment analysis functionality, allowing the classification of text into specific emotions such as happy, sad, anger, irritated, or surprise.
    - generate_sentiment_score: Provides functionality to generate sentiment scores between -1 and +1 for text data.

text_summarization:
    Provides functionality for generating summaries of text data.

    Features:
    - summarize_text: Generates a summary of a given text with a specified number of words.
    - summarize_pdf: Generates a summary of a given PDF file, considering the specified number of pages.
  
text_generation:
    Provides functionality for generating text/blogs about any topic.

    Features:
    - generate_text: Generates a blogs/summary for a given topic.

translation:
    Provides functionality for translating any text.

    Features:
    - translator: Translate any text to any language
</p>

<h2>Features</h2>

<ul>
  <li>Easy-to-use functions and classes for various tasks related to OpenAI's API.</li>
  <li>Streamlined text generation, language processing, and other AI-powered functionalities.</li>
  <li>Support for both synchronous and asynchronous API calls.</li>
  <li>Flexibility to work with different models and configurations offered by OpenAI.</li>
</ul>

<h2>Installation</h2>



<p>You can install PyAIKit using pip:</p>

<pre><code>pip install pyaikit
or
pip install pyaikit@git+https://github.com/Somenath24/pyaikit
</code></pre>

<h2>Getting Started</h2>

<p>To get started with PyAIKit, you need to have an OpenAI API key. If you don't have one, visit the <a href="https://openai.com">OpenAI website</a> to obtain your API key.</p>

<p>Once you have your API key, you can set it as an environment variable in your project or provide it directly when using PyAIKit.</p>

<p>Here's a simple example that demonstrates how to generate text using PyAIKit:</p>

<pre><code>from pyaikit.text_summerization.text_summerizer import text_summerizer

openai1=auth.setup(api_key,org_id)
# Instantiate the text_summerizer with your OpenAI API key
generator = text_summerizer()

# Generate text summerization from pdf using the default model
response = generator.summarize_pdf(openai1, no_of_words, file_path, start_page, end_page)

print(response)
</code></pre>
For more code help please check the <a href="https://github.com/Somenath24/pyaikit/blob/main/example.py">example</a>

<h3>Future Extension Plans for PyAIKit: Enhancing the Power of NLP</h3>
<p>
        PyAIKit is an evolving project with a roadmap of more future extensions and enhancements.
        Here are some of the plans that are being considered to further empower the package:
</p>
<p>
       <b> Model Customization:</b>
        One of the key areas of focus for PyAIKit future development is enabling model customization. This means allowing users to fine-tune the underlying ChatGPT model according to their specific domain or application requirements. Customization options would enable users to train the model on their own data, resulting in more tailored and accurate text generation.
</p>
<p>
        <b> Advanced Text Analysis:</b>
        It aims to provide more advanced text analysis functionalities in the future. This includes features such as named entity recognition, part-of-speech tagging, and sentiment analysis. These enhancements would allow users to extract valuable insights from text data, enabling more sophisticated NLP applications and empowering data-driven decision-making.
</p>
<p>
        <b>Integration with Other AI Models:</b>
        This expansion would enable users to combine the power of ChatGPT with other state-of-the-art models, such as image recognition or speech processing models. This integration would enhance the package's versatility and enable the development of more comprehensive AI solutions.</p>
<h2>License</h2>

<p>PyAIKit is distributed under the <a href="https://github.com/somenath24/pyaikit/blob/main/LICENSE">MIT License</a>. See the <code>LICENSE</code> file for more information.
</p>
<p>
This package is using OpenAI API, no connection with openai organization
<hr>

<p>We hope that PyAIKit simplifies your integration with OpenAI's API and empowers you to leverage the potential of artificial intelligence in your Python projects. If you have any questions or need support, please don't hesitate to reach out to me at somenath.bhu.2010@gmail.com.</p>

<p>Happy coding!</p>


