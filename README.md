## Dependencies
- OS:Should work on Any Ubuntu and its derivatives
- grip
- wkhtmltopdf
- Should have internet connection to run the script

## Customization
This script is intended to convert .py files.
Can be Customized for other language files

### Instructions for Customization
- In `output_pdf = fileName.replace('.py','.pdf')` replace .py to 
Your file extension
- In below section replace `#` with comments of the language 
Ex :In Java and javascript it's `//`

```python  

    text_style = string.startswith('#')
    code_style = not string.startswith('#')
    start = string.startswith('# start')
    end = string.startswith('# end')

```
- In `return """```python"""` replace python with your own language
Ex java, javascript etc Refer git-hub markdown syntax 


### Convert any program file to PDF 
- This script will help to write tutorials for programming
- This script is intended for Python Progrms 
- Refer the examples to view the out put pdfs



#### Instructions while writing the program
- Follow the markdown syntax while writing comments 
- Write comment <space> start before the code block
- Write comment <space> end after code block

#### Usage 
- `py_to_md -i <file_name>`
- Out put will be saved as file_name.pdf

