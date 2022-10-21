render: \
	SquareToCircle


SquareToCircle: src/test_manim.py
	manim render $< SquareToCircle

clean:
	rm --recursive --force media/
	rm --recursive --force src/__pycache__/

.PHONY: \
	clean \
	render
