.PHONY: help setup run clean

help:
	@echo ""
	@echo "  make setup                    instala john"
	@echo "  make run WORDS='1234 holamunod passwd'"
	@echo "  make clean                    borra outputs"
	@echo ""

setup:
	echo "Nada que instalar"

run:
	echo $$WORDS | tr ' ' '\n' |  john hashes.txt --stdin


clean:
	rm -rf ~/.john
