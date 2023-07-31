all: img/petersen-circular.png img/petersen-circular-black.png

img/petersen-circular.png: src/petersen-circular.py
	poetry run python $<

img/petersen-circular-black.png: src/petersen-circular-black.py
	poetry run python $<
