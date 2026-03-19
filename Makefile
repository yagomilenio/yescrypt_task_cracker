START  ?= 1
END    ?= 10
BLEND  ?= $(shell ls *.blend 2>/dev/null | head -1)
OUTPUT ?= outputs/frames_$(START)_$(END).tar.gz

.PHONY: help setup run test clean

help:
	@echo ""
	@echo "  make setup                    instala Blender"
	@echo "  make run START=1 END=50       renderiza frames 1-50"
	@echo "  make test                     prueba rápida (frames 1-3)"
	@echo "  make clean                    borra outputs"
	@echo ""

setup:
	git clone https://github.com/openwall/john.git
	cd john/src && ./configure && make -s clean && make -sj$(nproc)

run:
	john/run/john hashes.txt --wordlist=wordlist.txt


clean:
	rm -rf john/run/john.pot
