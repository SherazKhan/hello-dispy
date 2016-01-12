all:
	virtualenv venv
	venv/bin/pip install -r requirements.txt
	ln -s -f venv/bin/python .
	ln -s -f venv/bin/dispynode.py .

clean:
	rm -rf dispynode.py
	rm -rf python
	rm -rf venv
