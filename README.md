# stats101

These are my notes on statistical analysis and quantitative methods for social science researchers.
They're available here in case they're of any use to anyone, but I offer no guarantee or warranty as to their accuracy.
You're welcome to use or adapt them, for example to share with colleagues, but you cannot sell them.


## Generating documentation

This project used [Jupyter notebooks](https://jupyter.org/) to write functionality and run code.
You can edit the notebooks by opening a terminal, navigating to the `stats101` folder, and running:

```j
upyter notebook
```

This should open the notebooks in your browser to edit.

[`nbsphinx`](https://nbsphinx.readthedocs.io/) is then used to generate documentation webpages from the notebooks.
To generate the docs, run:

```
python3 -m sphinx source/ docs/
```


## License

&copy; 2018--19 Phil Mike Jones.

![CC BY-NC](cc-by-nc.png)

- Content and text: [CC BY-NC](https://creativecommons.org/licenses/by-nc/4.0/)
- Code: MIT

You are welcome to use or share these notes, but you must provide an attribution or reference, and you cannot sell them or make money from them.
