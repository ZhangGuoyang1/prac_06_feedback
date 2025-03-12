"""
Word Occurrences
Estimate: 20 minutes
Actual:   24 minutes
"""

from programming_language import ProgrammingLanguage


def main():
    """
    Create several ProgrammingLanguage instances, print their details,
    and then filter and print the names of dynamically typed languages.
    """
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    # Put them in a list for convenience
    languages = [python, ruby, visual_basic]

    # Print each language (which calls __str__ from the class)
    for language in languages:
        print(language)

    # Use the is_dynamic() method to filter and print only dynamically typed languages
    print("\nThe dynamically typed languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.name)


# Standard idiom to ensure main() runs only when this file is executed directly
if __name__ == "__main__":
    main()
