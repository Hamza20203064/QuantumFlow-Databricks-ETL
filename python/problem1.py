# Replace |Name| and |Date| in the fallowing string


letter = '''Dear <|Name|>,
You are Sellected!!
<|Date|>'''
# /Impotant Sintax
# chaining function
print (letter.replace('<|Name|>' , 'HAMZA AHMAD' ).replace('<|Date|>' , '26 jun 2024')) 
