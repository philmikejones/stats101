#! /bin/bash
jupyter nbconvert --to html notebooks/stats101.ipynb
mv notebooks/stats101.html docs/index.html
cp -r notebooks/images/ docs/

