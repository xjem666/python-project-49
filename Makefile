install:
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

brain-games:
	poetry run brain-games

package-install:
	python3 -m pip install --user dist/*.whl

brain-even:
	poetry run brain-even

brain-calc:
	poetry run brain-calc

brain-nod:
	poetry run brain-nod

brain-progression:
	poetry run brain-progression

brain-prime:
	poetry run brain-prime

lint:
	poetry run flake8 brain_games
