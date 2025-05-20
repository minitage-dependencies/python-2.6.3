#!parts/part/bin/python

# Copyright (C) 2009, Makina Corpus <freesoftware@makina-corpus.com>
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice,
#    this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
# 3. Neither the name of the <ORGANIZATION> nor the names of its
#    contributors may be used to endorse or promote products derived from
#    this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

__docformat__ = 'restructuredtext en'


import sys
print "testing %s" % sys.executable

import urllib2
imports = ['ctypes',
           'asyncore',
           '_ssl',
           'zlib',
           'zipfile',
           'tarfile',
           'readline',
           'setuptools',
           'sqlite3',
           'itertools',
           '_elementtree',
           'pyexpat',
           'bz2',
           'gestalt',
           'curses',
           'bsddb']

def msg(m):
    print "-" * 79
    if not isinstance(m, str):
        for i in m:
            print i
    else:
        print m
    print "-" * 79

for i in imports:
    try:
        exec 'import %s' % i
        print "Imported %s" % i
    except Exception, e:
        msg(["ERROR on %s" % i,"%s" % e])

if not ('Minitage' in urllib2.urlopen('https://www.minitage.org').read()):
    msg("Problem with ssl layer")



if sys.platform == 'darwin':

    import platform
    print platform.mac_ver()

