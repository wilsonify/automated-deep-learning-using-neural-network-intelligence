
build/version.txt:
	mkdir -p build && echo "1.0.0" > $@

build/adl-nni-base.txt:
	docker build -t adl-nni-base:latest -f Dockerfile-base . && touch $@

build/adl-nni-builder.txt: build/adl-nni-base.txt
	docker build -t adl-nni-builder:latest -f Dockerfile-builder . && touch $@

build/adl-nni.txt: build/adl-nni-builder.txt
	docker build -t adl-nni:latest -f Dockerfile . && touch $@

docker-run: build/adl-nni.txt
	docker run --rm --name adl-nni  -v $(shell pwd):/root -w /root/c01_Intro/bbf -P adl-nni:latest embedded_nni.py