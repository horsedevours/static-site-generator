import blocker
from block import block_to_block_type

def markdown_to_html_node(markdown):
    blocks = blocker.markdown_to_blocks(markdown)

    for block in blocks:
        type = block_to_block_type(block)
        print(type)