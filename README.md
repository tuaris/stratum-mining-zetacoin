#Vardiff Branch Notes
This branch is in *active development* and *will* be broken. Do *not* run this in production yet.

#Description
Stratum-mining is a pooled mining protocol. It is a replacement for *getwork* based pooling servers by allowing clients to generate work. The stratum protocol is described [here](http://mining.bitcoin.cz/stratum-mining) in full detail.

This is an implementation of stratum-mining for SHA-256 based coins; specifically built and tested for Zetacoin. It is compatible with *mmcfe-ng* as well as *mmcfe*, as it complies with the standards of *pushpool*.

Rather than forking from the GeneralFault stratum-mining repository, which most people are using for ZetaCoin, I wanted to ensure that the latest improvements and fixes were incorporated. To do this I forked from the moopless stratum-mining-litecoin repository and removed scrypt. This should ensure that this is the most up to date stratum-mining code that has been tested for ZetaCoin from day one.

The goal is to make a reliable stratum mining server for Zetacoin based pools. Over time any stability or security issues will be patched as discovered.

**NOTE:** This fork is in active development. Features may be broken, or may become broken with an update in the future. Please report any broken features or issues.

#Donors
A special thanks to everyone that has donated to this project. 

* Nobody yet...

Zetacoin Donations are welcome: ZUnvK9Uj8AGbvPXyGsmU9QiNUnxz6THCNf

#Features

* Stratum Mining Pool 
* Solved Block Confirmation
* Zetacoin network compatible
* Should be SHA-256 coin compatible
* DYNAMIC Vardiff support [The server will automatically determine difficulty for miner. Doesn't accept user choice.]
* Log Rotation
* Initial low difficulty share confirmation
* Multiple *zetacoind* wallets
* On the fly addition of new *zetacoind* wallets
* MySQL database support
* Adjustable database commit parameters
* Bypass password check for workers
* Automatically create workers on first connect


#Requirements
*stratum-mining-zetacoin* is built in python. I have been testing it with 2.7.4, but it should work with other versions. The requirements for running the software are below.

* Python 2.7+
* python-twisted
* stratum
* MySQL Server 
* Zetacoind

#Installation

1. Clone.

2. Copy conf/config_sample.py to conf/config.py

3. Edit config.py appropriately

4. Test, test, test.

#Contact
I try to stay in #ZetaCoin on freenode.

#Credits

* Original version by Slush0
* Modified version by GeneralFault
* Modified version Wade Womersley (Media Skunk Works)
* Scrypt conversion from work done by viperaus
* Modified version by moopless
* ZetaCoin converted version by IainKay (Donations welcome: ZUnvK9Uj8AGbvPXyGsmU9QiNUnxz6THCNf)


#License
This software is provides AS-IS without any warranties of any kind. Please use at your own risk. 
