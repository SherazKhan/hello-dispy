all:
	virtualenv venv
	venv/bin/pip install -r requirements.txt
	ln -s -f venv/bin/python .

clean:
	rm -rf python
	rm -rf venv
