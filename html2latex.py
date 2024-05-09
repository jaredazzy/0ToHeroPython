#This part of the code is so we can ask the user for their html text so we can later input it into the function
user_html = input('Please enter a HTML string: ')
#This part of the code is so we can create a function that define the replacement rules for converting the html to latex
#Here we are replacing the html string with their latex replacements
def convert_html_to_latex(html):
    html = html.replace('&ldquo;', '``')
    html = html.replace('&rdquo;', '"')
    html = html.replace('&apos;', "'")
    html = html.replace('&amp;', '&')
    html = html.replace('&lt;', '<')
    html = html.replace('&gt;', '>')
    html = html.replace('{', '\\{')
    html = html.replace('}', '\\}')
    html = html.replace('%', '\\%')

    return html
#This part of the code we are printing the result of the converted html to latex string back to the user
print(convert_html_to_latex(user_html))