all:
	virtualenv venv
	venv/bin/pip install -r requirements.txt
	ln -s -f venv/bin/python .
	ln -s -f venv/bin/dispynode.py .

clean:
	rm -rf dispynode.py
	rm -rf python
	rm -rf venv

deploy_runit:
	mkdir -p /etc/sv/dispynode
	cp dispynode.runit /etc/sv/dispynode/run
	chmod +x /etc/sv/dispynode/run
	ln -sf /etc/sv/dispynode /etc/service/dispynode

remove_runit:
	rm -rf /etc/sv/dispynode
	rm -rf /etc/service/dispynode
