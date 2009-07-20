import os
def getpythonenv(options,buildout):
    """Where python looks to get its cflags."""
    crypt=''
    if os.uname()[0] != 'Darwin':
        crypt=' -lcrypt '
    myfile = open(
        os.path.join(
            options['compile-directory'],
            'Modules',
            'Setup.local'),
        'w'
    )
    myfile.write("""
zlib zlibmodule.c %(zlib)s
crypt cryptmodule.c %(crypt)s
bz2 bz2module.c %(bzip2)s
_curses _cursesmodule.c       %(ncurses)s
_curses_panel _curses_panel.c %(ncurses)s
readline readline.c %(readline)s
_socket socketmodule.c
syslog syslogmodule.c
_ssl _ssl.c %(ssl)s
cStringIO cStringIO.c
cPickle cPickle.c
pyexpat pyexpat.c -DHAVE_EXPAT_H %(expat)s
_bsddb _bsddb.c %(db)s
""" % {
 'db': '-I%(db)s/include -L%(db)s/lib -Wl,-rpath,%(db)s/lib -ldb-%(dbv)s' % {
     'db': os.path.abspath(buildout['db']['location']),
     'dbv': buildout['db']['version']
 },
 'readline': '-I%(readline)s/include -L%(readline)s/lib -Wl,-rpath,%(readline)s/lib -lhistory -lreadline' % {
     'readline': os.path.abspath(buildout['readline']['location'])
 },
 'ssl': '-I%(openssl)s/include -I%(openssl)s/include/openssl -L%(openssl)s/lib -Wl,-rpath -Wl,%(openssl)s/lib -lcrypto -lssl' % {
     'openssl': os.path.abspath(buildout['openssl']['location'])
 },
 'bzip2': '-I%(bzip2)s/include -L%(bzip2)s/lib -Wl,-rpath,%(bzip2)s/lib -lbz2' % {
     'bzip2': os.path.abspath(buildout['bzip2']['location'])
 },
 'zlib': '-I%(zlib)s/include -L%(zlib)s/lib -Wl,-rpath,%(zlib)s/lib -lz' % {
     'zlib': os.path.abspath(buildout['zlib']['location'])
 },
 'ncurses': '-I%(ncurses)s/include/ncurses -I%(ncurses)s/include -L%(ncurses)s/lib -Wl,-rpath -Wl,%(ncurses)s/lib -lpanel -lform -lmenu -lncurses' % {
     'ncurses': os.path.abspath(buildout['ncurses']['location'])
 },
 'expat': '-I%(expat)s/include -L%(expat)s/lib -Wl,-rpath,%(expat)s/lib -lexpat ' % {
     'expat': os.path.abspath(buildout['expat']['location'])
 },
 'crypt': crypt,
}
)
    myfile.close()
    os.environ['OPT'] = os.environ['CFLAGS']
# vim:set ts=4 sts=4 et  :
