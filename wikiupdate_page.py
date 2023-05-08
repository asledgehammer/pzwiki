#!/usr/bin/env python

import sys
from wiki import Wiki

if __name__ == '__main__':
	Wiki().update_event(sys.argv[1])
