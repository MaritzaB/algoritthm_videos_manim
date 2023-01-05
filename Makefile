render: \
	GraphAnimation
#	SquareToCircle

SquareToCircle: src/test_manim.py
	manim render $< SquareToCircle

GraphAnimation: src/graph_animation.py
	manim render $< GraphCreation -ql

BFS: src/algorithms.py
	manim render $< BFS -ql

foo: src/foo.py
	manim render $< msn -ql

clean:
	rm --recursive --force media/
	rm --recursive --force src/__pycache__/

format:
	black --line-length 80 src/*.py

.PHONY: \
	clean \
	render
