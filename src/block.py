from enum import Enum

class BlockType(Enum):
    CODE = "code"
    HEADING = "heading"
    O_LIST = "ordered list"
    PARAGRAPH = "paragraph"
    QUOTE = "quote"
    U_LIST = "unordered list"

def block_to_block_type(markdown):
    if markdown.startswith("```") and markdown.endswith("```"):
        return BlockType.CODE
    if is_heading(markdown):
        return BlockType.HEADING
    if is_ordered_list(markdown):
        return BlockType.O_LIST
    if is_quote_block(markdown):
        return BlockType.QUOTE
    if markdown.startswith("- ") and filter(lambda l: l.startswith("-"), markdown):
        return BlockType.U_LIST
    return BlockType.PARAGRAPH

def is_heading(markdown):
    if not markdown.startswith("#"):
        return False
    
    prefix = markdown.split(maxsplit=1)[0]
    if len(prefix) > 7 or prefix.strip("#") != "":
        return False
    return True

def is_ordered_list(markdown):
    previous_number = 0
    for line in markdown.splitlines():
        if not (line[0].isnumeric() and line[1:3] == ". " and int(line[0]) == previous_number + 1):
            return False
        else:
            previous_number = int(line[0])
    return True

def is_quote_block(markdown):
    for line in markdown.splitlines():
        if line[0] != ">":
            return False