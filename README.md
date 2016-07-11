# What is Vaquero?

<div align="center">
    <img src="logo.png" alt="Vaquero logo" />
    <!-- art by https://www.fiverr.com/calum_mcghee -->
</div>

## TL;DR

It's a library for iterative and interactive data wrangling at laptop-scale. 
If you spend a lot of time in a [Jupyter notebook](http://jupyter.org/), 
trying to clean dirty, raw data, it's probably useful. 

It would be nice if it were possible to write data cleaning code correctly. 
But, the people who pay you to do data analysis don't do data analysis 
and don't understand how dangerous dirty data are, so you rarely get the 
luxury of feeling secure with what you extract. Vaquero tries to find a 
balance between "business" demands and good hygiene. Borrowing from Larry 
Page, it tries "to make the easy things easy, and the hard things possible." 
In this context, "hard things" refers to those wonderfully fun situations 
where, you write some code that you know will break in the future but you have 
no time to fix it; then, three months later, it breaks and you have no idea 
what your code does.

## Modules as Pipelines

> Namespaces are one honking great idea -- let's do more of those!

Programmers use namespaces everywhere to organize their code. Yet, when writing data cleaning code, everything ends up in a big file with lots of poorly-named functions. Think: `from hellishlib import *`. The perfectionist in me says, "this is awful, and I should write it properly, as a full library with lots of unit tests!" But, for "perfectionists with deadlines," that's not possible. 

Furthermore, the single-file-of-functions pattern emerges not only because of time constraints; it's a reflection of the problem! ELT code is **inherently** tightly-coupled. Code that extracts this variable probably depends on that one which in term also depends on some other one. This leads to a tree of transformations, encapsulated by function calls. 

Recognizing this, `vaquero` doesn't try to move you away from collecting all your ELT code in a single file. It's going to happen anyway. Instead, it makes it safer with some conventions. 

1. A module represents a single encapsulated pipeline. It should process a well-defined document. 
2. The function definition order is meaningful. Functions at the top of the file execute before those above them. Again, it's a pipeline. 
3. As per pythonic convention, functions prefixed with `_` are private. Here, that means, the pipeline constructor ignores it when compiling the pipeline. This gives you nice helper functions.
4. You're probably not going to use unit tests -- you don't have time. But, since it's a module, pepper it with assertions. And, using the `_`-prefix, you can actually write namespaced tests (e.g. `_my_test()`), and immediately call them in the module. (I actually write a lot of my code with `unittest` in the pipeline module and it gets called right before the module fully imports.) Then, when you break something, you can't even start pipeline processing. It fails fast. 
(You can deviate from this pattern -- but, in general, don't.)

## Expecting Exceptions

The fragile tree. 

Make, Drake, etc. 

Rather than fighting this single-file-of-functions-pattern, I'll just make it safer. 




## Installation

```sh
pip install vaquero
```

## Disclaimer

I have this big monstrous library called Vaquero on my computer. It's a 
collection of lots of functions I've written over (entirely too) many data 
munging projects. I use it often, and keep telling myself "once I find the 
time, I'll release it!" And, that never happens. It's too big to clean up in 
a way that makes me comfortable. Instead, I'll be releasing little bits of 
code in a ad-hoc, just-in-time fashion. When I absolutely need some feature 
of the big library going forward, I'll extract it and put it here. 

Still, library-user beware. This means things will break.

## Tips

Use '_name' fields for intermediary results in a document. 
Delete them at the end of the pipeline. 
On failure, you get to see hidden fields.
