#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import onp

if __name__ == "__main__":
    print onp.editdistance(sys.argv[1], sys.argv[2])

