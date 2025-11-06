from num2words import num2words


def basic_examples():
    print("=== BASIC EXAMPLES ===")
    print(num2words(0))
    print(num2words(5))
    print(num2words(42))
    print(num2words(123456))
    print()


def ordinal_examples():
    print("=== ORDINALS ===")
    for n in [1, 2, 3, 21, 42, 100]:
        print(f"{n} → {num2words(n, to='ordinal')}")
    print()


def ordinal_num_examples():
    print("=== ORDINAL NUMERIC STYLE ===")
    for n in [1, 2, 3, 21, 42, 100]:
        print(f"{n} → {num2words(n, to='ordinal_num')}")
    print()


def year_examples():
    print("=== YEAR STYLE ===")
    for y in [1999, 2000, 2010, 2024]:
        print(f"{y} → {num2words(y, to='year')}")
    print()


def currency_examples():
    print("=== CURRENCY STYLE ===")
    amounts = [12, 1200.45, 24_120.10]
    for amt in amounts:
        print(f"{amt} → {num2words(amt, to='currency', lang='en')}")
    print()


def multilingual_examples():
    print("=== MULTILINGUAL ===")
    langs = ["en", "fr", "es", "de", "hi"]
    for lang in langs:
        try:
            print(f"42 in {lang}: {num2words(42, lang=lang)}")
        except NotImplementedError:
            print(f"Language '{lang}' not supported.")
    print()


def mixed_examples():
    print("=== MIXED EXAMPLES ===")
    tests = [5, 15, 102, 1234]
    for n in tests:
        print(f"{n} → {num2words(n)}")
        print(f"{n} (ordinal) → {num2words(n, to='ordinal')}")
        print(f"{n} (year) → {num2words(n, to='year')}")
        print()
    print()


def indian_examples():
    print("=== INDIAN ENGLISH ===")
    try:
        print(num2words(1_23_456, lang='en_IN'))
        print(num2words(1_23_456.78, lang='en_IN', to='currency'))
    except NotImplementedError:
        print("Indian English locale not supported in your version.")
    print()


def error_handling_example():
    print("=== ERROR HANDLING ===")
    try:
        print(num2words(42, lang="xx"))
    except NotImplementedError:
        print("Unsupported language code → Falling back to English:")
        print(num2words(42, lang="en"))
    print()


def real_world_invoice_example(amount: float, lang: str = 'en_IN'):
    """Convert amount to words for an invoice."""
    try:
        words = num2words(amount, lang=lang, to='currency')
    except NotImplementedError:
        words = num2words(amount, lang='en', to='currency')
    return words.capitalize()


def invoice_demo():
    print("=== REAL-WORLD INVOICE EXAMPLE ===")
    amt = 15467.89
    print("In English (India):", real_world_invoice_example(amt, 'en_IN'))
    print("In Hindi:", real_world_invoice_example(amt, 'hi'))
    print()


def main():
    basic_examples()
    ordinal_examples()
    ordinal_num_examples()
    year_examples()
    currency_examples()
    multilingual_examples()
    mixed_examples()
    indian_examples()
    error_handling_example()
    invoice_demo()


if __name__ == "__main__":
    main()

