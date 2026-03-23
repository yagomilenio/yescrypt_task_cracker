.PHONY: help setup run clean

help:
	@echo ""
	@echo "  make setup                    instala john"
	@echo "  make run WORDS='1234 holamunod passwd'"
	@echo "  make clean                    borra outputs"
	@echo ""

setup:
	git clone https://github.com/openwall/john.git
	cd john/src && ./configure && make -s clean && make -sj$(nproc)

run:
	echo $$WORDS | tr ' ' '\n' |  john/run/john hashes.txt --stdin


clean:
	rm -rf john/run/john.pot
