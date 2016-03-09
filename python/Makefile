%.pdf : %.md src/*.py head.tex
	gpp -T $< | pandoc -o $@ -H head.tex --number-sections

%.tex : %.md head.tex
	gpp -T $< -o $*.tmp.md
	pandoc $*.tmp.md -s -R -o $@ -H head.tex --number-sections

all: README.pdf

tex: README.tex

clean:
	rm README.pdf
