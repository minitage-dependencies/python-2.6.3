import os
import zc.buildout


os_ldflags=''
uname=os.uname()[0]
if uname == 'Darwin':
    os_ldflags=' -mmacosx-version-min=10.5.0'


def append_env_var(env,var,sep=":",before=True):
    """ append text to a environnement variable
    @param env String variable to set
    @param before append before or after the variable"""
    for path in var:
    	if before:os.environ[env] = "%s%s%s" % (path,sep,os.environ.get(env,''))
	else:os.environ[env] = "%s%s%s" % (os.environ.get(env,''),sep,path)


def getpythonenv(options,buildout):
    """ add needed submodules to the Setup.local as python cannot see shared libraries in non standard places """
    for var in ['zlib','db', 'readline', 'bzip2', 'ncurses','openssl','expat']:
        append_env_var('LD_RUN_PATH',  ["%(lib)s/lib"%{'lib':buildout[var]['location']}],sep=':',before=False)
        append_env_var('LDFLAGS',   [ os_ldflags ],sep=' ',before=False)
        append_env_var('CFLAGS',   ["-I%s/include "%(buildout[var]['location'])],sep=' ',before=False)
        append_env_var('CPPFLAGS', ["-I%s/include "%(buildout[var]['location'])],sep=' ',before=False)
        append_env_var('CXXFLAGS', ["-I%s/include "%(buildout[var]['location'])],sep=' ',before=False)

    if uname == 'Darwin':
        append_env_var('CFLAGS',   [" -D__DARWIN_UNIX03 "],sep=' ',before=False)
        append_env_var('OPT',      [" -D__DARWIN_UNIX03 "],sep=' ',before=False)
        append_env_var('CPPFLAGS', [" -D__DARWIN_UNIX03 "],sep=' ',before=False)
        append_env_var('CXXFLAGS', [" -D__DARWIN_UNIX03 "],sep=' ',before=False)

    compile_dir=options['compile-directory']
    if os.path.isdir(compile_dir):
        contents = os.listdir(compile_dir)
        if len(contents) == 1:
            os.chdir('%s/%s'%(compile_dir,contents[0]))

    myfile = open('%s/%s/%s' %(os.getcwd(),'Modules','Setup.local'),'w')
    crypt=''
    if uname != 'Darwin': crypt=' -lcrypt '
    # Nevermind toutpt, it 's pasted from the PythonSRCFOLDER/Modules/Setup.dist
    myfile.write( """
zlib zlibmodule.c %(zlib)s
crypt cryptmodule.c %(crypt)s
bz2 bz2module.c %(bzip2)s
_curses _cursesmodule.c       %(ncurses)s
_curses_panel _curses_panel.c %(ncurses)s
readline readline.c %(readline)s
_socket socketmodule.c
_ssl _ssl.c  -DUSE_SSL %(openssl)s
syslog syslogmodule.c
cStringIO cStringIO.c
cPickle cPickle.c
pyexpat pyexpat.c -DHAVE_EXPAT_H %(expat)s
_bsddb _bsddb.c %(db)s
                 """ %{
                     'db':"-I%(db)s/include -L%(db)s/lib -Wl,-rpath,%(db)s/lib -ldb-4.4"%{'db':buildout['db']['location'] },
                     'readline':"-I%(readline)s/include -L%(readline)s/lib -Wl,-rpath,%(readline)s/lib -lhistory -lreadline"%{'readline':buildout['readline']['location'] },
                     'openssl':"-I%(openssl)s/include -L%(openssl)s/lib -Wl,-rpath,%(openssl)s/lib -lcrypto -lssl"%{'openssl':buildout['openssl']['location'] },
                     'bzip2':"-I%(bzip2)s/include -L%(bzip2)s/lib -Wl,-rpath,%(bzip2)s/lib -lbz2"%{'bzip2':buildout['bzip2']['location'] },
                     'zlib':"-I%(zlib)s/include -L%(zlib)s/lib -Wl,-rpath,%(zlib)s/lib -lz"%{'zlib':buildout['zlib']['location'] },
                     'ncurses':"-I%(ncurses)s/include/ncurses -I%(ncurses)s/include -L%(ncurses)s/lib -Wl,-rpath,%(ncurses)s/lib -lpanel -lform -lmenu -lncurses"%{'ncurses':buildout['ncurses']['location'] },
                     'expat':"-I%(expat)s/include -L%(expat)s/lib -Wl,-rpath,%(expat)s/lib -lexpat"%{'expat':buildout['expat']['location'] },
                     'openssl-prefix':buildout['openssl']['location'],
                     'crypt':crypt,
                 }
                )
    myfile.close()

# vim:set ts=4 sts=4 et  :
