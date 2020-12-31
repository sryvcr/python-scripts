def get_reverse_text(text_original: str) -> str:
    """
        get the text backwards and in lowercase
    """
    text_reverse: str = text_original[::-1].lower()
    return text_reverse


if __name__ == "__main__":
    text_original = (input("please, enter the text you want to get backwards: "))
    reverse_text = get_reverse_text(text_original)
    print(reverse_text)
