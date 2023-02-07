---
# TRANSLATOR
---
#### Video Demo: https://youtu.be/rtPStr5DQ3Q
#### Description
---
* With the advent of globalization, nowadays everyone seems to consume content from different regions of the world, thus arises the need of always having to customize our the content in your own language for better and increased comprehension. Besides we tend to familiarize well with the language we reasonate with. Having considered the above challenge, my project is a command-line argument that takes a text input from any language and expects a destination language of your choice in the command line argument, together with the text. This program enables you to be able to translate any message with your visual studio code or command line without the need of installing translator on yoour computer, phone, browser or any other device. 
* The main challenge that I faced while developing this project is being able to find a free translator model or API that would assist me with real time translation, other than having having to have a pre-compiled program with a very distinct amount of words or letters. 
* The code works by passing a command-line argument, for instance `python project.py -l es "text"` and it will translate the provided text to spanish.
* It uses Microsoft Translator to translate the text, it first starts by importing several python libraries:
    - `os` is used to access environment libraries, which are values stoed outside the code
    - `requests` is used to make requests to the API
    - `json` is used to parse the API response
    - `argparse` is used to handle command-line arguments
    - `langdetect` is used to detect the language of the text to be translated.
    - The API key is stored in an environment variable called `MS_TRANSLATOR_KEY`
    - The `main` function takes the text to be translated and the destination language as input and calls tow other functions `source_language` and `translate_text`. The `source_language` function uses the `langdetect` library to detect the language of the input text. The `translate_text` function uses the `requests` library to send a request to the Microsoft Translator API with the input text and the source and destination languages. The API response is then returned as the translated text. 
    - The `command_parser` function sets up a command-line argument parser that allows the user to specify the destination language code and dthe text to be translated. 
    - Finally the code checks if the script is being run as the main program. If so, it calls the `command_parser` function to get the user-specified arguments, and then calls the `main` function with these arguments.
---
