hello-dispy
===========

Installation
------------

Run make:

   make


Local run
----------

Run on each server node:

   ./python ./dispynode.py

Run on the client:

   ./python test.py node1 node2 node3

where node* are your server nodes.


EC2 cluster run
---------------

Create EC2 configuration file:

   cp ec2.conf.in ec2.conf
   vi ec2.conf

Launch the cluster:

   ./python launch-ec2.py

