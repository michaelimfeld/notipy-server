test:
	./run.sh

coverage: test
	wkhtmltopdf cover/index.html notipyservercoverage.pdf

clean:
	rm -rf cover
	rm -f notipyservercoverage.pdf
