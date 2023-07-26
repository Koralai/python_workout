def generate_xml(tag, content, *attributes):
    
    attr_formatted = ''
    for attribute in attributes:
        attribute = attribute.replace(',','')
        attr_formatted += attribute
        
    return f'<{tag} {attr_formatted}>{content}</{tag}>'

print(generate_xml('emphasis', 'emphasized text', 'italic="yes", underscore="yes"'))
