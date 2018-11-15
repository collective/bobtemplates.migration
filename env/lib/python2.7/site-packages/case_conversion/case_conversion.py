import sys

PYTHON = sys.version_info[0]

if 3 == PYTHON:
    # Python 3 and ST3
    from . import case_parse
else:
    # Python 2 and ST2
    import case_parse


def camelcase(text, detect_acronyms=False, acronyms=[]):
    """Return text in camelCase style.

    Args:
        text: input string to convert case
        detect_acronyms: should attempt to detect acronyms
        acronyms: a list of acronyms to detect

    >>> camelcase("hello world")
    'helloWorld'
    >>> camelcase("HELLO_HTML_WORLD", True, ["HTML"])
    'helloHTMLWorld'
    """
    words, case, sep = case_parse.parse_case(text, detect_acronyms, acronyms)
    if words:
        words[0] = words[0].lower()
    return ''.join(words)


def pascalcase(text, detect_acronyms=False, acronyms=[]):
    """Return text in PascalCase style (aka MixedCase).

    Args:
        text: input string to convert case
        detect_acronyms: should attempt to detect acronyms
        acronyms: a list of acronyms to detect

    >>> pascalcase("hello world")
    'HelloWorld'
    >>> pascalcase("HELLO_HTML_WORLD", True, ["HTML"])
    'HelloHTMLWorld'
    """
    words, case, sep = case_parse.parse_case(text, detect_acronyms, acronyms)
    return ''.join(words)


def snakecase(text, detect_acronyms=False, acronyms=[]):
    """Return text in snake_case style.

    Args:
        text: input string to convert case
        detect_acronyms: should attempt to detect acronyms
        acronyms: a list of acronyms to detect

    >>> snakecase("hello world")
    'hello_world'
    >>> snakecase("HelloHTMLWorld", True, ["HTML"])
    'hello_html_world'
    """
    words, case, sep = case_parse.parse_case(text, detect_acronyms, acronyms)
    return '_'.join([w.lower() for w in words])


def dashcase(text, detect_acronyms=False, acronyms=[]):
    """Return text in dash-case style (aka kebab-case, spinal-case).

    Args:
        text: input string to convert case
        detect_acronyms: should attempt to detect acronyms
        acronyms: a list of acronyms to detect

    >>> dashcase("hello world")
    'hello-world'
    >>> dashcase("HelloHTMLWorld", True, ["HTML"])
    'hello-html-world'
    """
    words, case, sep = case_parse.parse_case(text, detect_acronyms, acronyms)
    return '-'.join([w.lower() for w in words])


def kebabcase(text, detect_acronyms=False, acronyms=[]):
    """Return text in kebab-case style (aka snake-case, spinal-case).

    Args:
        text: input string to convert case
        detect_acronyms: should attempt to detect acronyms
        acronyms: a list of acronyms to detect

    >>> kebabcase("hello world")
    'hello-world'
    >>> kebabcase("HelloHTMLWorld", True, ["HTML"])
    'hello-html-world'
    """
    return dashcase(text, detect_acronyms, acronyms)


def spinalcase(text, detect_acronyms=False, acronyms=[]):
    """Return text in spinal-case style (aka snake-case, kebab-case).

    Args:
        text: input string to convert case
        detect_acronyms: should attempt to detect acronyms
        acronyms: a list of acronyms to detect

    >>> spinalcase("hello world")
    'hello-world'
    >>> spinalcase("HELLO_HTML_WORLD", True, ["HTML"])
    'hello-html-world'
    """
    return dashcase(text, detect_acronyms, acronyms)


def constcase(text, detect_acronyms=False, acronyms=[]):
    """Return text in CONST_CASE style (aka SCREAMING_SNAKE_CASE).

    Args:
        text: input string to convert case
        detect_acronyms: should attempt to detect acronyms
        acronyms: a list of acronyms to detect

    >>> constcase("hello world")
    'HELLO_WORLD'
    >>> constcase("helloHTMLWorld", True, ["HTML"])
    'HELLO_HTML_WORLD'
    """
    words, case, sep = case_parse.parse_case(text, detect_acronyms, acronyms)
    return '_'.join([w.upper() for w in words])


def screaming_snakecase(text, detect_acronyms=False, acronyms=[]):
    """Return text in SCREAMING_SNAKE_CASE style (aka CONST_CASE).

    Args:
        text: input string to convert case
        detect_acronyms: should attempt to detect acronyms
        acronyms: a list of acronyms to detect

    >>> screaming_snakecase("hello world")
    'HELLO_WORLD'
    >>> screaming_snakecase("helloHTMLWorld", True, ["HTML"])
    'HELLO_HTML_WORLD'
    """
    return constcase(text, detect_acronyms, acronyms)


def dotcase(text, detect_acronyms=False, acronyms=[]):
    """Return text in dot.case style.

    Args:
        text: input string to convert case
        detect_acronyms: should attempt to detect acronyms
        acronyms: a list of acronyms to detect

    >>> dotcase("hello world")
    'hello.world'
    >>> dotcase("helloHTMLWorld", True, ["HTML"])
    'hello.html.world'
    """
    words, case, sep = case_parse.parse_case(text, detect_acronyms, acronyms)
    return '.'.join([w.lower() for w in words])


def separate_words(text, detect_acronyms=False, acronyms=[]):
    """Return text in "seperate words" style.

    Args:
        text: input string to convert case
        detect_acronyms: should attempt to detect acronyms
        acronyms: a list of acronyms to detect

    >>> separate_words("HELLO_WORLD")
    'HELLO WORLD'
    >>> separate_words("helloHTMLWorld", True, ["HTML"])
    'hello HTML World'
    """
    words, case, sep = case_parse.parse_case(
        text, detect_acronyms, acronyms, preserve_case=True)
    return ' '.join(words)


def slashcase(text, detect_acronyms=False, acronyms=[]):
    """Return text in slash/case style.

    Args:
        text: input string to convert case
        detect_acronyms: should attempt to detect acronyms
        acronyms: a list of acronyms to detect

    >>> slashcase("HELLO_WORLD")
    'HELLO/WORLD'
    >>> slashcase("helloHTMLWorld", True, ["HTML"])
    'hello/HTML/World'
    """
    words, case, sep = case_parse.parse_case(
        text, detect_acronyms, acronyms, preserve_case=True)
    return '/'.join(words)


def backslashcase(text, detect_acronyms=False, acronyms=[]):
    """Return text in backslash\case style.

    Args:
        text: input string to convert case
        detect_acronyms: should attempt to detect acronyms
        acronyms: a list of acronyms to detect

    >>> backslashcase("HELLO_WORLD") == r'HELLO\WORLD'
    True
    >>> backslashcase("helloHTMLWorld", True, ["HTML"]) == r'hello\HTML\World'
    True
    """
    words, case, sep = case_parse.parse_case(
        text, detect_acronyms, acronyms, preserve_case=True)
    return '\\'.join(words)
