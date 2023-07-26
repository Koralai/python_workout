def generate_xml(tag, content):
    return f'<{tag}>{content}</{tag}>'

print(generate_xml('emphasis', 'emphasized text'))
