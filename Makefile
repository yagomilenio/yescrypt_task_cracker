.PHONY: help setup run clean

help:
	@echo ""
	@echo "  make setup                    instala Blender"
	@echo "  make run HASH=$y$j9T$6EjPWvckfxRiWQIKFMmUF.$t8fMGSJnaI1iRjNIwXWTDSe7Pz9uVgMAp2WJVPI1k1D"
	@echo "  make clean                    borra outputs"
	@echo ""

setup:
	git clone https://github.com/openwall/john.git
	cd john/src && ./configure && make -s clean && make -sj$(nproc)

run:
	echo $HASH |  john/run/john --stdin --wordlist=wordlist.txt


clean:
	rm -rf john/run/john.pot
