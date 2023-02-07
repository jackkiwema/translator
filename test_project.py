import pytest
import os
from project import source_language
from project import translate_text
from project import command_parser
from project import main 


# https://learn.microsoft.com/en-us/azure/cognitive-services/translator/reference/v3-0-translate


# Test source_language valid input
def test_valid_input_sl():
    text = "Hola, ¿cómo estás?"
    assert source_language(text) == "es"

# Test source_language long input
def test_long_input_sl():
    text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
    assert source_language(text) == "ca"

def test_valid_input_tt():
    text = "Hello"
    source_language = "en"
    dest_language = "es"
    expected_result = "Hola"
    result = translate_text(text, source_language, dest_language)
    assert result == expected_result


# Test Translate_Text Missing key
def test_missing_key_tt():
    with pytest.raises(RuntimeError):
        del os.environ["MS_TRANSLATOR_KEY"]
        translate_text("Hello", "en", "es")

# Test Translate_text no output
def test_no_output_tt():
    text = None
    source_language = "en"
    dest_language = "es"
    with pytest.raises(RuntimeError):
        translate_text(text, source_language, dest_language)

# Test translate_text empty output
def test_empty_output_tt():
    text = ""
    source_language = "en"
    dest_language = "es"
    with pytest.raises(RuntimeError):
        translate_text(text, source_language, dest_language)

# Test main invalid input
def test_invalid_input_main():
    text = "Hello"
    dest_language = ""
    with pytest.raises(RuntimeError):
        main(text, dest_language)

# Test command_parser with no argument
def test_command_parser_no_arg():
    with pytest.raises(SystemExit):
        command_parser()

