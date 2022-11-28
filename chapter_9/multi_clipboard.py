#! python3

# multi_clipboard.py delete - Deletes all keywords
# multi_clipboard.py delete <keyword> - Deletes keyword
# multi_clipboard.py save <keyword> - Saves clipboard to keyword
# multi_clipboard.py <keyword> - Loads keyword to clipboard
# multi_clipboard.py list - Loads all keywords to clipboard

# Extend the multi-clipboard program in this chapter so that it
# has a delete <keyword> command line argument that will delete a
# keyword from the shelf. Then add a delete command line argument 
# that will delete all keywords.


import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')

# Save clipboard content.
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
    del mcbShelf[sys.argv[2]]
elif len(sys.argv) == 2:
    # List keywords and load content.
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    if sys.argv[1].lower() == 'delete':
        for keyword in list(mcbShelf.keys()):
            del mcbShelf[keyword]
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])

mcbShelf.close()