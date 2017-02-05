## Introduction

MIT OpenCourseWare (OCW) is great, but when you want to download their files,
their website basically just dumps their whole course page on you. Problems
with that include

1. Many useless web-related files (html, xml and the like).
2. Long prefixes like MIT18_06SCF11_ on almost every single pdf file.
3. MIT terms and conditions page at the back of every pdf.
 
So these scripts help you sort all that out, although you'll have to drag and drop a few files around to make it look really nice.


All scripts are recursively descending and will start at folder it is in. Make sure the subdirectories don't lead to anywhere you don't want it to lead.  

### Courses supported

These are the courses I have done/am doing and so the rename and remove scripts will work especially well for these. To extend the capabilities to other courses you will need you to modify the scripts a bit, like changing the prefixes. See details below.

* [18.02 (Multivarable Calculus)](http://ocw.mit.edu/courses/mathematics/18-02-multivariable-calculus-fall-2007/ "Multivarable Calculus")
* [18.03 (Differential Equations)](http://ocw.mit.edu/courses/mathematics/18-03-differential-equations-spring-2010/ "Differential Equations")]
* [18.06 (Linear Algebra)](http://ocw.mit.edu/courses/mathematics/18-06-linear-algebra-spring-2010/ "Linear Algebra")
* [6.041 (Probabilistic Systems Analysis and Applied Probability)](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-041-probabilistic-systems-analysis-and-applied-probability-fall-2010/ "Probabilistic Systems Analysis and Applied Probability") - pypdf encounters some errors with this course, more under bugs
* [18.100b (Analysis I)](http://ocw.mit.edu/courses/mathematics/18-100b-analysis-i-fall-2010/index.htm  "Analysis I")
* [18.100c (Real Analysis)](http://ocw.mit.edu/courses/mathematics/18-100c-real-analysis-fall-2012/ "Real Analysis")


### Remove Last Page
Removes the last page of every pdf, useful for getting rid of terms and conditions page, so you don't waste paper and ink while printing. 


In order for remove_last_page.py to work, you will need PyPDF2. You can use pip to install it
> pip install PyPDF2. 

If you have a PDF whose last page you **don't** want to remove you can append SKIP to its name. You can change the escape sequence in the file itself, from SKIP to maybe ^&, which might be easier to type. MIT is pretty good at attaching its terms and conditions to every PDF though.


To run
> python remove_last_page.py

You don't want to run this script more than once in any particular folder. Note that sometimes PYPDF would have trouble processing a pdf file. See bugs for more.

### Rename
Removes prefix of all files 
You must **first edit the file itself** to get it to remove what prefix you want.
> fi_prefix = 'whatever-prefix-you-want'

> di_prefix = 'whatever-prefix-you-want'

Remember to uncomment the 
> remove_prefix(di_prefix, "directory")

If you intent to change any directory names.


To run
> python rename.py

### Remove

Removes useless files like html and xml files. It will prompt with the file extensions it will remove, or you can read the file. It removes the recitation files for 18.02.


> ./remove

### Remove 18.03

Same as remove, but also includes additional files specific to 18.03, see prompt or read file.

### Bugs

PyPDF has trouble processing the following files in 6.041

* MIT6_041SCF13_L13.pdf or 6-041sc-fall-2013/contents/unit-iii/lecture-13/MIT6_041SCF13_L13.pdf 
* MIT6_041SCF13_L17.pdf or 6-041sc-fall-2013/contents/unit-iii/lecture-17/MIT6_041SCF13_L17.pdf 
* MIT6_041SCF13_L18.pdf or 6-041sc-fall-2013/contents/unit-iii/lecture-18/MIT6_041SCF13_L18.pdf 
* MIT6_041SCF13_L22.pdf or 6-041sc-fall-2013/contents/unit-iv/lecture-22/MIT6_041SCF13_L22.pdf  

### Disclaimer
Only tested on OSX. Python scripts should be platform independent. Bash scripts should work on any *nix machine.
