## Remove Last Page
In order for remove_last_page.py to work, you will need PyPDF2. You can use pip to install it
> pip install PyPDF2. 

If you have a PDF whose last page you **don't** want to remove you can append SKIP to its name. You can change the escape sequence in the file itself, from SKIP to maybe ^&, which might be easier to type.

## Rename
You must edit the file itself to get it to remove what prefix you want.
> fi_prefix = 'whatever-prefix-you-want'

> di_prefix = 'whatever-prefix-you-want'

Remember to uncomment the 
> remove_prefix(di_prefix, "directory")

If you intent to change any directory names.

## Remove

Removes useless files like html and xml files. It will prompt with the file extensions it will remove, or you can read the file. It removes the recitation files for 18.02.


## Remove 18.03

Same as remove, but also includes additional files specific to 18.03, see prompt or read file.
