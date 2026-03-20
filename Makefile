.PHONY: help setup run clean

help:
	@echo ""
	@echo "  make setup                    instala john"
	@echo "  make run WORD='1234'"
	@echo "  make clean                    borra outputs"
	@echo ""

setup:
	git clone https://github.com/openwall/john.git
	cd john/src && ./configure && make -s clean && make -sj$(nproc)
	wget https://weakpass.com/download/90/rockyou.txt.gz
	wget https://crackstation.net/files/crackstation.txt.gz
	gunzip rockyou.txt.gz
	gunzip crackstation.txt.gz
	rm -f *.gz
	cat rockyou.txt.gz >> crackstation.txt
	rm rockyou.txt
	mv crackstation.txt wordlist.txt

run:
	echo $$WORD |  john/run/john hashes.txt --stdin


clean:
	rm -rf john/run/john.pot
