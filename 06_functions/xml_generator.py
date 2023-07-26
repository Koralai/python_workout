def generate_xml(tag, content, *attributes):
    
    all_attributes = ''.join(*attributes)
    attrs_formatted = all_attributes.replace(",", "")
        
    return f'<{tag} {attrs_formatted}>{content}</{tag}>'

print(generate_xml('emphasis', 'emphasized text', 'italic="yes"'))
