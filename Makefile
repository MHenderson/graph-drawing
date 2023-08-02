all: img/petersen-circular.png\
     img/petersen-circular-black.png\
	 img/petersen-circular-options.png\
	 img/petersen-various.png\
	 img/dodecahedral.png

img/petersen-circular.png: src/petersen-circular.py
	poetry run python $<

img/petersen-circular-black.png: src/petersen-circular-black.py
	poetry run python $<

img/petersen-circular-options.png: src/petersen-circular-options.py
	poetry run python $<

img/petersen-various.png: src/petersen-various.py
	poetry run python $<

img/dodecahedral.png: src/dodecahedral.py
	poetry run python $<
