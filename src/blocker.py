def markdown_to_blocks(markdown):
    return list(map(lambda b: b.strip(), list(filter(None, markdown.split("\n\n")))))