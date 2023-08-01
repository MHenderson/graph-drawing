all: img/petersen-circular.png\
     img/petersen-circular-black.png\
	 img/petersen-circular-options.png\
	 img/petersen-shell.png

img/petersen-circular.png: src/petersen-circular.py
	poetry run python $<

img/petersen-circular-black.png: src/petersen-circular-black.py
	poetry run python $<

img/petersen-circular-options.png: src/petersen-circular-options.py
	poetry run python $<

img/petersen-shell.png: src/petersen-shell.py
	poetry run python $<
