%.pdf : %.Rmd
	Rscript -e "library(rmarkdown);  library(utils); render('$<', 'pdf_document')"

%.pdf : %.tex
	pdflatex $<
