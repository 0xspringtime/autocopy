from aqt import mw
#from aqt.reviewer import Reviewer
from aqt import gui_hooks
from aqt.utils import showInfo
import pyclip

def copy_to_clipboard(card):
    # Get the text of the top field of the current card
    top_field = card.note().fields[0]
    # Copy the text to the clipboard
    pyclip.copy(top_field)
    # Show a notification to confirm that the text has been copied

# Add the copy_to_clipboard function to the post_answer method of the Reviewer class
#Reviewer._postAnswer = copy_to_clipboard
gui_hooks.reviewer_did_show_answer.append(copy_to_clipboard)
