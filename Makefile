# Regaining Control — build. Everything under figures/, guide/01, 06–10, 17 and the PDF is generated.
PY ?= python3
PDF := Regaining-Control-Observability-for-OpenStack-Platforms-in-Difficulty.pdf

.PHONY: all figures cards pages pdf check clean

all: figures cards pages pdf

figures:            ## src/figures/NN-slug.html → figures/NN-slug.png (1600 × 1000)
	$(PY) src/render/render_figures.py

cards:              ## signals/NN-slug.yaml → figures/cards/NN-slug.png (1080 × 1350)
	$(PY) src/render/render_cards.py

pages:              ## signals + meta → guide/01, 06–10, 17 and guide/README.md
	$(PY) src/render/build_pages.py

pdf:                ## guide + signals + figures → $(PDF)
	$(PY) src/render/build_pdf.py

check:              ## the PDF has the expected number of pages
	@$(PY) -c "import pikepdf,yaml; n=len(pikepdf.open('$(PDF)').pages); m=yaml.safe_load(open('src/content/meta.yaml'))['pages']; print(f'{n} pages'); raise SystemExit(0 if n==m else f'expected {m}')"

clean:
	rm -rf build
