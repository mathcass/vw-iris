
all: clean test

env:
	pipenv install

iris.vw: iris_to_vw.py
	pipenv run python $< | shuf > $@

train.vw: iris.vw
	head -125 $< > $@

test.vw: iris.vw
	tail -25 $< > $@

model: train.vw
	pipenv run python -m vw \
		--passes 10 --oaa 3 --loss_function logistic -q LW LP LI WP WI PI \
		-f $@ -d $< --cache_file train.cache

test: test.vw model
	pipenv run python -m vw -t -i model -d test.vw -p test
	paste test test.vw

clean:
	rm -f test.vw train.vw iris.vw model test train.cache
