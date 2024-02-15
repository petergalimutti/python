def is_palindrome(t):
# - Iterates over each character in the input string 't'.
# - Checks if the character is alphanumeric (a letter or a digit).
# - Converts each character to lowercase.
# - Joins the filtered characters into a single string, removing non-alphanumeric characters and ensuring uniformity in case.
# - 'cleanse_t' contains the cleaned string without spaces, punctuation, and with all letters converted to lowercase.

    cleanse_t = ''.join(text.lower() for text in t if text.isalnum())
    return(print(cleanse_t == cleanse_t[::-1]))

is_palindrome("A man, a plan, a canal, Panama")
