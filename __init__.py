from aqt import mw
from aqt import gui_hooks
from aqt.utils import showInfo

#import pyclip
from . import pyclip

def copy_to_clipboard(card):
    # Get the text of the top field of the current card
    top_field = card.note().fields[0]
    # Copy the text to the clipboard
    pyclip.copy(top_field)

gui_hooks.reviewer_did_show_answer.append(copy_to_clipboard)
