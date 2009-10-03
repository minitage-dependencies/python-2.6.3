import os, sys
import re
#ef getpythonenv(options,buildout):
#   """Where python looks to get its cflags."""
#   if os.uname()[0] == 'Darwin':
#       # regenerating ./configure
#       cwd = os.getcwd()
#       os.chdir(options['compile-directory'])
#       os.system('autoconf -v -f')
#       os.chdir(cwd)
#    os.environ['OPT'] = os.environ['CFLAGS']
#
#   crypt=''
#   if os.uname()[0] != 'Darwin':
#       crypt=' -lcrypt ' 
#    darwin_cflags = ''
#   myfile = open(
#       os.path.join(
#           options['compile-directory'],
#           'Modules',
#           'Setup.local'),
#       'w'
#   )
#
#    myfile.write("""
##_socket socketmodule.c
##bz2 bz2module.c %(bzip2)s
##cPickle cPickle.c
##cStringIO cStringIO.c
##posix posixmodule.c %(posixmodule)s
##readline readline.c %(readline)s
##syslog syslogmodule.c
##zlib zlibmodule.c %(zlib)s
##_curses _cursesmodule.c       %(ncurses)s
##_curses_panel _curses_panel.c %(ncurses)s
##_ssl _ssl.c %(ssl)s
##crypt cryptmodule.c %(crypt)s
#pyexpat pyexpat.c -DHAVE_EXPAT_H %(expat)s
#""" % {
# 'posixmodule': '%(dc)s ' % {
#     'dc': darwin_cflags,
# },
# 'readline': '-I%(readline)s/include -L%(readline)s/lib -Wl,-rpath,%(readline)s/lib -lhistory -lreadline -ledit' % {
#     'readline': os.path.abspath(buildout['readline']['location'])
# },
# 'ssl': '-I%(openssl)s/include -I%(openssl)s/include/openssl -L%(openssl)s/lib -Wl,-rpath -Wl,%(openssl)s/lib -lcrypto -lssl' % {
#     'openssl': os.path.abspath(buildout['openssl']['location'])
# },
# 'bzip2': '-I%(bzip2)s/include -L%(bzip2)s/lib -Wl,-rpath,%(bzip2)s/lib -lbz2' % {
#     'bzip2': os.path.abspath(buildout['bzip2']['location'])
# },
# 'zlib': '-I%(zlib)s/include -L%(zlib)s/lib -Wl,-rpath,%(zlib)s/lib -lz' % {
#     'zlib': os.path.abspath(buildout['zlib']['location'])
# },
# 'ncurses': '-I%(ncurses)s/include/ncurses -I%(ncurses)s/include -L%(ncurses)s/lib -Wl,-rpath -Wl,%(ncurses)s/lib -lpanel -lform -lmenu -lncurses' % {
#     'ncurses': os.path.abspath(buildout['ncurses']['location'])
# },
# 'expat': '-I%(expat)s/include -L%(expat)s/lib -Wl,-rpath,%(expat)s/lib -lexpat ' % {
#     'expat': os.path.abspath(buildout['expat']['location'])
# },
# 'crypt': crypt,
#}
#)
#    myfile.write("""
##bsddb185 bsddbmodule.c $(db)s
#_bsddb _bsddb.c %(db)s
#                 """ % {
#                     'db': '%(dc)s -I%(db)s/include -L%(db)s/lib -Wl,-rpath,%(db)s/lib -ldb-%(dbv)s' % {
#                         'dc': darwin_cflags,
#                         'db': os.path.abspath(buildout['db']['location']),
#                         'dbv': buildout['db']['version']
#                     },
#
#                 }
#                )
#    myfile.close()


def patchincludes(options,buildout):
    """Where python looks to get its cflags."""
    u, v = os.uname()[0],os.uname()[3]
    if u == 'Darwin' and v == '9.8.0':
        cmyfile = [l for l in open(
                        os.path.join(
                                options['compile-directory'],
                                'pyconfig.h'),
                        'r'
                     ).readlines() if not 'SETPGRP_HAVE_ARG' in l]
        cmyfile = open(
                        os.path.join(
                                options['compile-directory'],
                                'pyconfig.h'),
                        'w'
                     ).writelines(cmyfile + ['\n#define SETPGRP_HAVE_ARG 1\n'])
# vim:set ts=4 sts=4 et  :
