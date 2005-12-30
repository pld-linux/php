# TODO:
# - think of including support for:
#    - mcve,
#    - ovrimos,
#    - pfpro,
#   These extensions BuildRequires proprietary libraries...
# - deal with modules removed from php and not moved to PECL
#   (existing only in php4):
#   db, hyperwave, java, mcal, overload, qtdom
#   and removed from php 5.1:
#   cpdf, fam, yp, oracle
# - mime_magic can't handle new "string/*" entries in magic.mime
# - make additional headers added by mail patch configurable
# - apply -hardened patch by default ?
# - modularize session, standard (output from pure php -m)?
# - package for pdo-firebird?
# warning: Installed (but unpackaged) file(s) found:
#   /etc/php/conf.d/pdo_firebird.ini
#   /usr/lib/php/pdo_firebird.so
#
# Conditional build:
%bcond_with	db3		# use db3 packages instead of db (4.x) for Berkeley DB support
%bcond_with	fdf		# with FDF (PDF forms) module		(BR: proprietary lib)
%bcond_with	hardening	# build with hardening patch applied (http://www.hardened-php.net/)
%bcond_with	hwapi		# with Hw API support			(BR: proprietary libs)
%bcond_with	interbase_inst	# use InterBase install., not Firebird	(BR: proprietary libs)
%bcond_with	oci8		# with Oracle oci8 extension module	(BR: proprietary libs)
%bcond_without	curl		# without CURL extension module
%bcond_without	imap		# without IMAP extension module
%bcond_without	interbase	# with InterBase extension module
%bcond_without	ldap		# without LDAP extension module
%bcond_without	mhash		# without mhash extension module
%bcond_without	ming		# without ming extension module
%bcond_without	mm		# without mm support for session storage
%bcond_without	msession	# without msession extension module
%bcond_without	mssql		# without MS SQL extension module
%bcond_without	mime_magic		# without mime-magic module
%bcond_without	odbc		# without ODBC extension module
%bcond_without	openssl		# without OpenSSL support and OpenSSL extension (module)
%bcond_without	pcre		# without PCRE extension module
%bcond_without	pgsql		# without PostgreSQL extension module
%bcond_without	pspell		# without pspell extension module
%bcond_without	recode		# without recode extension module
%bcond_without	snmp		# without SNMP extension module
%bcond_without	sqlite		# without SQLite extension module
%bcond_without	sybase		# without Sybase extension module
%bcond_without	sybase_ct	# without Sybase-CT extension module
%bcond_without	tidy		# without Tidy extension module
%bcond_without	wddx		# without WDDX extension module
%bcond_without	xmlrpc		# without XML-RPC extension module
%bcond_without	apache1		# disable building apache 1.3.x module
%bcond_without	apache2		# disable building apache 2.x module
%bcond_without	fcgi		# disable building FCGI SAPI
%bcond_without	zts		# disable experimental-zts
%bcond_without	mysqli		# with mysqli support (Requires mysql > 4.1)

%define apxs1		/usr/sbin/apxs1
%define	apxs2		/usr/sbin/apxs

# some problems with apache 2.x
%if %{with apache2}
%undefine	with_mm
%endif

%ifnarch %{ix86} %{x8664} sparc sparcv9 alpha ppc
%undefine	with_interbase
%endif

%if %{without apache1} && %{without apache2}
ERROR: You need to select at least one Apache SAPI to build shared modules.
%endif

# x86-only lib
%ifnarch %{ix86}
%undefine	with_msession
%endif

Summary:	The PHP HTML-embedded scripting language for use with Apache
Summary(fr):	Le langage de script embarque-HTML PHP pour Apache
Summary(pl):	JÍzyk skryptowy PHP - uøywany wraz z serwerem Apache
Summary(pt_BR):	A linguagem de script PHP
Summary(ru):	PHP ˜≈“”…… 5 - —⁄ŸÀ –“≈–“œ√≈””…“œ◊¡Œ…— HTML-∆¡ Ãœ◊, ◊Ÿ–œÃŒ—≈ÕŸ  Œ¡ ”≈“◊≈“≈
Summary(uk):	PHP ˜≈“”¶ß 5 - Õœ◊¡ –“≈–“œ√≈”’◊¡ŒŒ— HTML-∆¡ Ã¶◊, ◊…ÀœŒ’◊¡Œ¡ Œ¡ ”≈“◊≈“¶
Name:		php
Version:	5.1.1
%define	_rel 6
Release:	%{_rel}%{?with_hardening:hardened}
Epoch:		4
Group:		Libraries
License:	PHP
Source0:	http://www.php.net/distributions/%{name}-%{version}.tar.bz2
# Source0-md5:	70a7c90de182d1a1901c390b844153c7
Source1:	FAQ.%{name}
Source2:	zend.gif
Source3:	%{name}-module-install
Source4:	%{name}-mod_%{name}.conf
Source5:	%{name}-cgi-fcgi.ini
Source6:	%{name}-cgi.ini
Source7:	%{name}-apache.ini
Source8:	%{name}-cli.ini
Source9:	http://www.hardened-php.net/hardening-patch-5.0.4-0.3.0.patch.gz
# Source9-md5:	47a742fa9fab2826ad10c13a2376111a
Patch0:		%{name}-shared.patch
Patch1:		%{name}-pldlogo.patch
Patch2:		%{name}-mail.patch
Patch3:		%{name}-link-libs.patch
Patch4:		%{name}-libpq_fs_h_path.patch
Patch5:		%{name}-msession-shared-lib.patch
Patch6:		%{name}-build_modules.patch
Patch7:		%{name}-sapi-ini-file.patch
Patch8:		%{name}-no-metaccld.patch
Patch10:	%{name}-ini.patch
Patch11:	%{name}-acam.patch
Patch14:	%{name}-allow-db31.patch
Patch15:	%{name}-threads-acfix.patch
Patch16:	%{name}-tsrmlsfetchgcc2.patch
Patch17:	%{name}-no_pear_install.patch
Patch18:	%{name}-zlib.patch
Patch19:	%{name}-sybase-fix.patch
Patch20:	%{name}-readline.patch
Patch21:	%{name}-nohttpd.patch
Patch23:	%{name}-gd_imagerotate_enable.patch
Patch24:	%{name}-uint32_t.patch
Patch25:	%{name}-hwapi-link.patch
Patch26:	%{name}-dba-link.patch
Patch30:	%{name}-hardening-fix.patch
Patch31:	%{name}-both-apxs.patch
Patch32:	%{name}-builddir.patch
Icon:		php.gif
URL:		http://www.php.net/
%{?with_interbase:%{!?with_interbase_inst:BuildRequires:	Firebird-devel >= 1.0.2.908-2}}
%{?with_pspell:BuildRequires:	aspell-devel >= 2:0.50.0}
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake >= 1.4d
BuildRequires:	bison
BuildRequires:	bzip2-devel
%{?with_curl:BuildRequires:	curl-devel >= 7.12.0}
BuildRequires:	cyrus-sasl-devel
%{!?with_db3:BuildRequires:	db-devel >= 4.0}
%{?with_db3:BuildRequires:	db3-devel >= 3.1}
BuildRequires:	elfutils-devel
%if %{with xmlrpc}
BuildRequires:	expat-devel
%endif
%{?with_fcgi:BuildRequires:	fcgi-devel}
%{?with_fdf:BuildRequires:	fdftk-devel}
BuildRequires:	flex
%if %{with mssql} || %{with sybase} || %{with sybase_ct}
BuildRequires:	freetds-devel
%endif
BuildRequires:	freetype-devel >= 2.0
BuildRequires:	gd-devel >= 2.0.28-4
BuildRequires:	gdbm-devel
BuildRequires:	gmp-devel
%{?with_imap:BuildRequires:	imap-devel >= 1:2001-0.BETA.200107022325.2}
BuildRequires:	libjpeg-devel
BuildRequires:	libltdl-devel >= 1.4
BuildRequires:	libmcrypt-devel >= 2.4.4
BuildRequires:	libpng-devel >= 1.0.8
BuildRequires:	libtiff-devel
BuildRequires:	libtool >= 1.4.3
BuildRequires:	libwrap-devel
BuildRequires:	libxml2-devel >= 2.5.10
BuildRequires:	libxslt-devel >= 1.0.18
%{?with_mhash:BuildRequires:	mhash-devel}
%{?with_ming:BuildRequires:	ming-devel >= 0.1.0}
%{?with_mm:BuildRequires:	mm-devel >= 1.3.0}
BuildRequires:	mysql-devel >= 4.0.0
%{?with_mysqli:BuildRequires:	mysql-devel >= 4.1.0}
BuildRequires:	ncurses-ext-devel
%{?with_ldap:BuildRequires:	openldap-devel >= 2.0}
%if %{with openssl} || %{with ldap}
BuildRequires:	openssl-devel >= 0.9.7d
%endif
BuildRequires:	%{__perl}
%{?with_snmp:BuildRequires:	net-snmp-devel >= 5.0.7}
BuildRequires:	pam-devel
%{?with_pcre:BuildRequires:	pcre-devel}
%{?with_msession:BuildRequires:	phoenix-devel}
%{?with_pgsql:BuildRequires:	postgresql-backend-devel >= 7.2}
%{?with_pgsql:BuildRequires:	postgresql-devel}
BuildRequires:	readline-devel
%{?with_recode:BuildRequires:	recode-devel >= 3.5d-3}
BuildRequires:	rpm-build >= 4.4.0
BuildRequires:	rpmbuild(macros) >= 1.238
%{?with_sqlite:BuildRequires:	sqlite-devel}
BuildRequires:	t1lib-devel
%{?with_tidy:BuildRequires:	tidy-devel}
%{?with_odbc:BuildRequires:	unixODBC-devel}
%{?with_xmlrpc:BuildRequires:	xmlrpc-epi-devel}
BuildRequires:	zlib-devel >= 1.0.9
%if %{with apache1}
BuildRequires:	apache1-devel
%endif
%if %{with apache2}
BuildRequires:	apache-devel >= 2.0.52-2
BuildRequires:	apr-devel >= 1:1.0.0
BuildRequires:	apr-util-devel >= 1:1.0.0
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/php
%define		_phpsharedir	%{_datadir}/php
%define		extensionsdir	%{_libdir}/php

# must be in sync with source. extra check ensuring that it is so is done in %%build
%define		php_api_version		20041225
%define		zend_module_api		20050922
%define		zend_extension_api	220051025
%define		zend_zts			%{!?with_zts:0}%{?with_zts:1}
%define		php_debug			%{!?debug:0}%{?debug:1}

%description
PHP is an HTML-embedded scripting language. PHP attempts to make it
easy for developers to write dynamically generated web pages. PHP also
offers built-in database integration for several commercial and
non-commercial database management systems, so writing a
database-enabled web page with PHP is fairly simple. The most common
use of PHP coding is probably as a replacement for CGI scripts. The
mod_php module enables the Apache web server to understand and process
the embedded PHP language in web pages. This package contains php
version %{version}. If you use applications which specifically rely on
PHP/FI (PHP v2 and earlier), you should instead install the PHP/FI
module contained in the phpfi package. If you're just starting with
PHP, you should install this package. You'll also need to install the
Apache web server.

%description -l fr
PHP est un langage de script embarque dans le HTM. PHP essaye de
rendre simple aux developpeurs d'ecrire des pages web generees
dynamiquement. PHP incorpore egalement une integration avec plusieurs
systemes de gestion de bases de donnees commerciaux et
non-connerciaux, qui rent facile la creation de pages web liees avec
des bases de donnees. L'utilisation la plus commune de PHP est
probablement en remplacement de scripts CGI. Le module mod_php permet
au serveur web apache de comprendre et de traiter le langage PHP
integre dans des pages web. Ce package contient php version
%{version}. Si vous utilisez des applications qui utilisent
specifiquement PHP/FI, vous devrez installer le module PHP/FI inclus
dans le package mod_php. Si vous debutez avec PHP, vous devriez
installer ce package. Vous aurez egalement besoin dinstaller le
serveur web Apache.

%description -l pl
PHP jest jÍzykiem skryptowym, ktÛrego polecenia umieszcza siÍ w
plikach HTML. Pakiet ten zawiera modu≥ przeznaczony dla serwera HTTP
(jak np. Apache), ktÛry interpretuje te polecenia. Umoøliwia to
tworzenie dynamicznie stron WWW. Spora czÍ∂Ê sk≥adni PHP zapoøyczona
zosta≥a z jÍzykÛw: C, Java i Perl.

%description -l pt_BR
PHP: Preprocessador de Hipertexto vers„o 4 È uma linguagem script
embutida em HTML. Muito de sua sintaxe È emprestada de C, Java e Perl,
com algumas caracterÌsticas ˙nicas, especÌficas ao PHP. O objetivo da
linguagem È permitir que desenvolvedores web escrevam p·ginas
dinamicamente geradas de forma r·pida.

%description -l ru
PHP - ‹‘œ —⁄ŸÀ Œ¡–…”¡Œ…— ”À“…–‘œ◊, ◊”‘“¡…◊¡≈ÕŸ» ◊ HTML-Àœƒ. PHP
–“≈ƒÃ¡«¡≈‘ …Œ‘≈“«“¡√…¿ ” ÕŒœ÷≈”‘◊œÕ Ûı‚‰, –œ‹‘œÕ’ Œ¡–…”¡Œ…≈ ”À“…–‘œ◊
ƒÃ— “¡¬œ‘Ÿ ” ¬¡⁄¡Õ… ƒ¡ŒŒŸ» œ‘Œœ”…‘≈ÃÿŒœ –“œ”‘œ. Ó¡…¬œÃ≈≈ –œ–’Ã—“Œœ≈
…”–œÃÿ⁄œ◊¡Œ…≈ PHP - ⁄¡Õ≈Œ¡ ƒÃ— CGI ”À“…–‘œ◊.

¸‘œ‘ –¡À≈‘ ”œƒ≈“÷…‘ ”¡Õœƒœ”‘¡‘œﬁŒ’¿ (CGI) ◊≈“”…¿ …Œ‘≈“–“≈‘¡‘œ“¡ —⁄ŸÀ¡.
˜Ÿ ƒœÃ÷ŒŸ ‘¡À÷≈ ’”‘¡Œœ◊…‘ÿ –¡À≈‘ %{name}-common. Â”Ã… ◊¡Õ Œ’÷≈Œ
…Œ‘≈“–“≈‘¡‘œ“ PHP ◊ À¡ﬁ≈”‘◊≈ Õœƒ’Ã— apache, ’”‘¡Œœ◊…‘≈ –¡À≈‘
apache-php.

%description -l uk
PHP - √≈ Õœ◊¡ Œ¡–…”¡ŒŒ— ”À“…–‘¶◊, ›œ ◊¬’ƒœ◊’¿‘ÿ”— ◊ HTML-Àœƒ. PHP
–“œ–œŒ’§ ¶Œ‘≈«“¡√¶¿ ⁄ ¬¡«¡‘ÿÕ¡ Ûı‚‰, ‘œÕ’ Œ¡–…”¡ŒŒ— ”À“…–‘¶◊ ƒÃ—
“œ¬œ‘… ⁄ ¬¡⁄¡Õ… ƒ¡Œ…» § ƒœ◊œÃ¶ –“œ”‘…Õ. Ó¡ ¬¶Ãÿ€ –œ–’Ã—“Œ≈
◊…Àœ“…”‘¡ŒŒ— PHP - ⁄¡Õ¶Œ¡ ƒÃ— CGI ”À“…–‘¶◊.

„≈  –¡À≈‘ Õ¶”‘…‘ÿ ”¡Õœƒœ”‘¡‘Œ¿ (CGI) ◊≈“”¶¿ ¶Œ‘≈“–“≈‘¡‘œ“¡ Õœ◊…. ˜…
Õ¡§‘≈ ‘¡Àœ÷ ◊”‘¡Œœ◊…‘… –¡À≈‘ %{name}-common. ÒÀ›œ ◊¡Õ –œ‘“¶¬≈Œ
¶Œ‘≈“–“≈‘¡‘œ“ PHP ◊ —Àœ”‘¶ Õœƒ’Ã— apache, ◊”‘¡Œœ◊¶‘ÿ –¡À≈‘ apache-php.

%package -n apache1-mod_php
Summary:	PHP DSO module for apache 1.3.x
Summary(pl):	Modu≥ DSO (Dynamic Shared Object) php dla apache 1.3.x
Group:		Development/Languages/PHP
Requires(post,preun):	%{__perl}
Requires(post,preun):	%{apxs1}
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	apache1(EAPI) >= 1.3.33-2
Requires:	apache1-mod_mime
Provides:	php = %{epoch}:%{version}-%{release}
Obsoletes:	apache-mod_php < 1:4.1.1
Obsoletes:	phpfi

%description -n apache1-mod_php
PHP as DSO module for apache 1.3.x.

%description -n apache1-mod_php -l pl
php jako modu≥ DSO (Dynamic Shared Object) dla apache 1.3.x.

%package -n apache-mod_php
Summary:	PHP DSO module for apache 2.x
Summary(pl):	Modu≥ DSO (Dynamic Shared Object) php dla apache 2.x
Group:		Development/Languages/PHP
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	apache >= 2.2.0
Requires:	apache(modules-api) = %{apache_modules_api}
Provides:	php = %{epoch}:%{version}-%{release}
Obsoletes:	phpfi

%description -n apache-mod_php
PHP as DSO module for apache 2.x.

%description -n apache-mod_php -l pl
php jako modu≥ DSO (Dynamic Shared Object) dla apache 2.x.

%package fcgi
Summary:	php as FastCGI program
Summary(pl):	php jako program FastCGI
Group:		Development/Languages/PHP
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php = %{epoch}:%{version}-%{release}

%description fcgi
php as FastCGI program.

%description fcgi -l pl
php jako program FastCGI.

%package cgi
Summary:	php as CGI program
Summary(pl):	php jako program CGI
Group:		Development/Languages/PHP
Requires:	%{name}-common = %{epoch}:%{version}-%{release}

%description cgi
php as CGI program.

%description cgi -l pl
php jako program CGI.

%package cli
Summary:	php as CLI interpreter
Summary(pl):	php jako interpreter dzia≥aj±cy z linii poleceÒ
Group:		Development/Languages/PHP
Requires:	%{name}-common = %{epoch}:%{version}-%{release}

%description cli
php as CLI interpreter.

%description cli -l pl
php jako interpreter dzia≥aj±cy z linii poleceÒ.

%package program
Summary:	/usr/bin/php symlink
Summary(pl):	Dowi±zanie symboliczne /usr/bin/php
Group:		Development/Languages/PHP
Requires:	%{name}-cli = %{epoch}:%{version}-%{release}
Provides:	php(program)
Obsoletes:	php(program)

%description program
Package providing /usr/bin/php symlink to PHP CLI.

%description program -l pl
Pakiet dostarczaj±cy dowi±zanie symboliczne /usr/bin/php do PHP CLI.

%package common
Summary:	Common files needed by both apache module and CGI
Summary(pl):	WspÛlne pliki dla modu≥u apache'a i programu CGI
Summary(ru):	Ú¡⁄ƒ≈Ã—≈ÕŸ≈ ¬…¬Ã…œ‘≈À… ƒÃ— php
Summary(uk):	‚¶¬Ã¶œ‘≈À… ”–¶ÃÿŒœ«œ ◊…Àœ“…”‘¡ŒŒ— ƒÃ— php
Group:		Libraries
# because of dlclose() bugs in glibc <= 2.3.4 causing SEGVs on exit
Requires:	glibc >= 6:2.3.5
Requires:	sed >= 4.0
Provides:	%{name}-libxml = %{epoch}:%{version}-%{release}
Provides:	%{name}-session = %{epoch}:%{version}-%{release}
Provides:	%{name}-simplexml = %{epoch}:%{version}-%{release}
Provides:	%{name}-spl = %{epoch}:%{version}-%{release}
Provides:	%{name}-standard = %{epoch}:%{version}-%{release}
Provides:	php(modules_api) = %{php_api_version}
Provides:	php(zend_extension_api) = %{zend_extension_api}
Provides:	php(zend_module_api) = %{zend_module_api}
Provides:	php5(debug) = %{php_debug}
Provides:	php5(thread-safety) = %{zend_zts}
Obsoletes:	php-pecl-domxml
Obsoletes:	php-session < 3:4.2.1-2
# for the posttrans scriptlet, conflicts because in vserver enviroinment rpm package is not installed.
Conflicts:	rpm < 4.4.2-0.2

%description common
Common files needed by both apache module and CGI.

%description common -l pl
WspÛlne pliki dla modu≥u apacha i programu CGI.

%description common -l ru
¸‘œ‘ –¡À≈‘ ”œƒ≈“÷…‘ œ¬›…≈ ∆¡ ÃŸ ƒÃ— “¡⁄ŒŸ» ◊¡“…¡Œ‘œ◊ “≈¡Ã…⁄¡√…… PHP
(”¡Õœƒœ”‘¡‘œﬁŒœ  … ◊ À¡ﬁ≈”‘◊≈ Õœƒ’Ã— apache).

%description common -l uk
„≈  –¡À≈‘ Õ¶”‘…‘ÿ ”–¶ÃÿŒ¶ ∆¡ Ã… ƒÃ— “¶⁄Œ…» ◊¡“¶¡Œ‘¶◊ “≈¡Ã¶⁄¡√¶ß PHP
(”¡Õœƒœ”‘¡‘Œÿœß ‘¡ ◊ —Àœ”‘¶ Õœƒ’Ã— apache).

%package devel
Summary:	Files for PHP modules development
Summary(pl):	Pliki do kompilacji modu≥Ûw PHP
Summary(pt_BR):	Arquivos de desenvolvimento para PHP
Summary(ru):	¡À≈‘ “¡⁄“¡¬œ‘À… ƒÃ— –œ”‘“œ≈Œ…— “¡”€…“≈Œ…  PHP
Summary(uk):	¡À≈‘ “œ⁄“œ¬À… ƒÃ— –œ¬’ƒœ◊… “œ⁄€…“≈Œÿ PHP
Group:		Development/Languages/PHP
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	autoconf
Requires:	automake
Requires:	libtool
Requires:	shtool
Obsoletes:	php-pear-devel
Obsoletes:	php4-devel

%description devel
The php-devel package lets you compile dynamic extensions to PHP.
Included here is the source for the PHP extensions. Instead of
recompiling the whole php binary to add support for, say, oracle,
install this package and use the new self-contained extensions
support. For more information, read the file
README.SELF-CONTAINED-EXTENSIONS.

%description devel -l pl
Ten pakiet zawiera pliki potrzebne do kompilacji modu≥Ûw PHP. Zamiast
rekompilowaÊ ca≥e php aby dodaÊ obs≥ugÍ np. oracle, moøna przy uøyciu
tego pakietu skompilowaÊ samodzielne rozszerzenie. WiÍcej informacji o
samodzielnych rozszerzeniach moøna znaleºÊ w pliku
README.SELF-CONTAINED-EXTENSIONS.

%description devel -l pt_BR
Este pacote contÈm arquivos usados no desenvolvimento de programas ou
mÛdulos PHP.

%description devel -l ru
¡À≈‘ php-devel ƒ¡≈‘ ◊œ⁄Õœ÷Œœ”‘ÿ ÀœÕ–…Ã…“œ◊¡‘ÿ ƒ…Œ¡Õ…ﬁ≈”À…≈ “¡”€…“≈Œ…—
PHP. ¡À≈‘ ◊ÀÃ¿ﬁ¡≈‘ …”»œƒŒŸ  Àœƒ ‹‘…» “¡”€…“≈Œ… . ˜Õ≈”‘œ –œ◊‘œ“Œœ 
ÀœÕ–…Ã—√…… ¬…Œ¡“Œœ«œ ∆¡ Ã¡ php ƒÃ— ƒœ¬¡◊Ã≈Œ…—, Œ¡–“…Õ≈“, –œƒƒ≈“÷À…
oracle, ’”‘¡Œœ◊…‘≈ ‹‘œ‘ –¡À≈‘ ƒÃ— ÀœÕ–…Ã…“œ◊¡Œ…— œ‘ƒ≈ÃÿŒŸ» “¡”€…“≈Œ… .
œƒ“œ¬Œœ”‘… - ◊ ∆¡ Ã≈ README.SELF-CONTAINED-EXTENSIONS.

%description devel -l uk
¡À≈‘ php-devel ƒ¡§ Õœ÷Ã…◊¶”‘ÿ ÀœÕ–¶Ã¿◊¡‘… ƒ…Œ¡Õ¶ﬁŒ¶ “œ⁄€…“≈ŒŒ— PHP.
‰œ –¡À≈‘’ ◊ÀÃ¿ﬁ≈Œœ ◊…»¶ƒŒ…  Àœƒ ƒÃ— “œ⁄€…“≈Œÿ. ˙¡Õ¶”‘ÿ –œ◊‘œ“Œœß
ÀœÕ–¶Ã—√¶ß ¬¶Œ¡“Œœ«œ ∆¡ Ã’ php ƒÃ— ƒœƒ¡ŒŒ—, Œ¡–“…ÀÃ¡ƒ, –¶ƒ‘“…ÕÀ…
oracle, ◊”‘¡Œœ◊¶‘ÿ √≈  –¡À≈‘ ƒÃ— ÀœÕ–¶Ã—√¶ß œÀ“≈Õ…» “œ⁄€…“≈Œÿ.
‰≈‘¡ÃÿŒ¶€¡ ¶Œ∆œ“Õ¡√¶— - ◊ ∆¡ Ã¶ README.SELF-CONTAINED-EXTENSIONS.

%package bcmath
Summary:	bcmath extension module for PHP
Summary(pl):	Modu≥ bcmath dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-common = %{epoch}:%{version}-%{release}

%description bcmath
This is a dynamic shared object (DSO) for PHP that will add bc style
precision math functions support.

%description bcmath -l pl
Modu≥ PHP umoøliwiaj±cy korzystanie z dok≥adnych funkcji
matematycznych takich jak w programie bc.

%package bzip2
Summary:	Bzip2 extension module for PHP
Summary(pl):	Modu≥ bzip2 dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-common = %{epoch}:%{version}-%{release}

%description bzip2
This is a dynamic shared object (DSO) for PHP that will add bzip2
compression support to PHP.

%description bzip2 -l pl
Modu≥ PHP umoøliwiaj±cy uøywanie kompresji bzip2.

%package calendar
Summary:	Calendar extension module for PHP
Summary(pl):	Modu≥ funkcji kalendarza dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-common = %{epoch}:%{version}-%{release}

%description calendar
This is a dynamic shared object (DSO) for PHP that will add calendar
support.

%description calendar -l pl
Modu≥ PHP dodaj±cy wsparcie dla kalendarza.

%package ctype
Summary:	ctype extension module for PHP
Summary(pl):	Modu≥ ctype dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-common = %{epoch}:%{version}-%{release}

%description ctype
This is a dynamic shared object (DSO) for PHP that will add ctype
support.

%description ctype -l pl
Modu≥ PHP umoøliwiaj±cy korzystanie z funkcji ctype.

%package curl
Summary:	curl extension module for PHP
Summary(pl):	Modu≥ curl dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-common = %{epoch}:%{version}-%{release}

%description curl
This is a dynamic shared object (DSO) for PHP that will add curl
support.

%description curl -l pl
Modu≥ PHP umoøliwiaj±cy korzystanie z biblioteki curl.

%package dba
Summary:	DBA extension module for PHP
Summary(pl):	Modu≥ DBA dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-common = %{epoch}:%{version}-%{release}

%description dba
This is a dynamic shared object (DSO) for PHP that will add flat-file
databases (DBA) support.

%description dba -l pl
Modu≥ dla PHP dodaj±cy obs≥ugÍ dla baz danych opartych na plikach
(DBA).

%package dbase
Summary:	DBase extension module for PHP
Summary(pl):	Modu≥ DBase dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-common = %{epoch}:%{version}-%{release}

%description dbase
This is a dynamic shared object (DSO) for PHP that will add DBase
support.

%description dbase -l pl
Modu≥ PHP ze wsparciem dla DBase.

%package dom
Summary:	DOM extension module for PHP
Summary(pl):	Modu≥ DOM dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
# it has some compatibility functions
Provides:	php-domxml = %{epoch}:%{version}-%{release}
Obsoletes:	php-domxml <= 3:4.3.8-1

%description dom
This is a dynamic shared object (DSO) for PHP that will add new DOM
support.

%description dom -l pl
Modu≥ PHP dodaj±cy now± obs≥ugÍ DOM.

%package exif
Summary:	exif extension module for PHP
Summary(pl):	Modu≥ exif dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-common = %{epoch}:%{version}-%{release}

%description exif
This is a dynamic shared object (DSO) for PHP that will add EXIF tags
support in image files.

%description exif -l pl
Modu≥ PHP dodaj±cy obs≥ugÍ znacznikÛw EXIF w plikach obrazkÛw.

%package fdf
Summary:	FDF extension module for PHP
Summary(pl):	Modu≥ FDF dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-common = %{epoch}:%{version}-%{release}

%description fdf
This PHP module adds support for PDF Forms through Adobe FDFTK
library.

%description fdf -l pl
Modu≥ PHP dodaj±cy obs≥ugÍ formularzy PDF poprzez bibliotekÍ Adobe
FDFTK.

%package filepro
Summary:	filePro extension module for PHP
Summary(pl):	Modu≥ filePro dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-common = %{epoch}:%{version}-%{release}

%description filepro
This is a dynamic shared object (DSO) for PHP that will add support
for read-only access to filePro databases.

%description filepro -l pl
Modu≥ PHP dodaj±cy moøliwo∂Ê dostÍpu (tylko do odczytu) do baz danych
filePro.

%package ftp
Summary:	FTP extension module for PHP
Summary(pl):	Modu≥ FTP dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-common = %{epoch}:%{version}-%{release}

%description ftp
This is a dynamic shared object (DSO) for PHP that will add FTP
support.

%description ftp -l pl
Modu≥ PHP dodaj±cy obs≥ugÍ protoko≥u FTP.

%package gd
Summary:	GD extension module for PHP
Summary(pl):	Modu≥ GD dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	gd >= 2.0.28-4
Provides:	%{name}-gd(gif) = %{epoch}:%{version}-%{release}

%description gd
This is a dynamic shared object (DSO) for PHP that will add GD
support, allowing you to create and manipulate images with PHP.

%description gd -l pl
Modu≥ PHP umoøliwiaj±cy korzystanie z biblioteki GD, pozwalaj±cej na
tworzenie i obrÛbkÍ obrazkÛw.

%package gettext
Summary:	gettext extension module for PHP
Summary(pl):	Modu≥ gettext dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-common = %{epoch}:%{version}-%{release}

%description gettext
This is a dynamic shared object (DSO) for PHP that will add gettext
support.

%description gettext -l pl
Modu≥ PHP dodaj±cy obs≥ugÍ lokalizacji przez gettext.

%package gmp
Summary:	gmp extension module for PHP
Summary(pl):	Modu≥ gmp dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-common = %{epoch}:%{version}-%{release}

%description gmp
This is a dynamic shared object (DSO) for PHP that will add arbitrary
length number support with GNU MP library.

%description gmp -l pl
Modu≥ PHP umoøliwiaj±cy korzystanie z biblioteki gmp do obliczeÒ na
liczbach o dowolnej d≥ugo∂ci.

%package hwapi
Summary:	Hyperwave API extension module for PHP
Summary(pl):	Modu≥ API Hyperwave dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-common = %{epoch}:%{version}-%{release}

%description hwapi
This is a dynamic shared object (DSO) for PHP that will add official
Hyperwave API support.

%description hwapi -l pl
Modu≥ PHP dodaj±cy obs≥ugÍ Hyperwave.

%package iconv
Summary:	iconv extension module for PHP
Summary(pl):	Modu≥ iconv dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-common = %{epoch}:%{version}-%{release}

%description iconv
This is a dynamic shared object (DSO) for PHP that will add iconv
support.

%description iconv -l pl
Modu≥ PHP dodaj±cy obs≥ugÍ iconv.

%package imap
Summary:	IMAP extension module for PHP
Summary(pl):	Modu≥ IMAP dla PHP
Summary(pt_BR):	Um mÛdulo para aplicaÁıes PHP que usam IMAP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-common = %{epoch}:%{version}-%{release}

%description imap
This is a dynamic shared object (DSO) for PHP that will add IMAP
support.

%description imap -l pl
Modu≥ PHP dodaj±cy obs≥ugÍ skrzynek IMAP.

%description imap -l pt_BR
Um mÛdulo para aplicaÁıes PHP que usam IMAP.

%package interbase
Summary:	InterBase/Firebird database module for PHP
Summary(pl):	Modu≥ bazy danych InterBase/Firebird dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
%{?with_interbase_inst:Autoreq:	false}

%description interbase
This is a dynamic shared object (DSO) for PHP that will add InterBase
and Firebird database support.

%description interbase -l pl
Modu≥ PHP umoøliwiaj±cy dostÍp do baz danych InterBase i Firebird.

%package ldap
Summary:	LDAP extension module for PHP
Summary(pl):	Modu≥ LDAP dla PHP
Summary(pt_BR):	Um mÛdulo para aplicaÁıes PHP que usam LDAP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-common = %{epoch}:%{version}-%{release}

%description ldap
This is a dynamic shared object (DSO) for PHP that will add LDAP
support.

%description ldap -l pl
Modu≥ PHP dodaj±cy obs≥ugÍ LDAP.

%description ldap -l pt_BR
Um mÛdulo para aplicaÁıes PHP que usam LDAP.

%package mbstring
Summary:	mbstring extension module for PHP
Summary(pl):	Modu≥ mbstring dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-common = %{epoch}:%{version}-%{release}

%description mbstring
This is a dynamic shared object (DSO) for PHP that will add multibyte
string support.

%description mbstring -l pl
Modu≥ PHP dodaj±cy obs≥ugÍ ci±gÛw znakÛw wielobajtowych.

%package mcrypt
Summary:	mcrypt extension module for PHP
Summary(pl):	Modu≥ mcrypt dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-common = %{epoch}:%{version}-%{release}

%description mcrypt
This is a dynamic shared object (DSO) for PHP that will add mcrypt
support.

%description mcrypt -l pl
Modu≥ PHP dodaj±cy moøliwo∂Ê szyfrowania poprzez bibliotekÍ mcrypt.

%package mhash
Summary:	mhash extension module for PHP
Summary(pl):	Modu≥ mhash dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-common = %{epoch}:%{version}-%{release}

%description mhash
This is a dynamic shared object (DSO) for PHP that will add mhash
support.

%description mhash -l pl
Modu≥ PHP udostÍpniaj±cy funkcje mieszaj±ce z biblioteki mhash.

%package mime_magic
Summary:	mime_magic extension module for PHP
Summary(pl):	Modu≥ mime_magic dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	/usr/share/file/magic.mime

%description mime_magic
This PHP module adds support for MIME type lookup via file magic
numbers using magic.mime database.

%description mime_magic -l pl
Modu≥ PHP dodaj±cy obs≥ugÍ wyszukiwania typÛw MIME wed≥ug magicznych
znacznikÛw plikÛw z uøyciem bazy danych magic.mime.

%package ming
Summary:	ming extension module for PHP
Summary(pl):	Modu≥ ming dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-common = %{epoch}:%{version}-%{release}

%description ming
This is a dynamic shared object (DSO) for PHP that will add ming
(Flash - .swf files) support.

%description ming -l pl
Modu≥ PHP dodaj±cy obs≥ugÍ plikÛw Flash (.swf) poprzez bibliotekÍ
ming.

%package msession
Summary:	msession extension module for PHP
Summary(pl):	Modu≥ msession dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-common = %{epoch}:%{version}-%{release}

%description msession
This is a dynamic shared object (DSO) for PHP that will allow you to
use msession. msession is a high speed session daemon which can run
either locally or remotely. It is designed to provide consistent
session management for a PHP web farm.

%description msession -l pl
Modu≥ PHP dodaj±cy umoøliwiaj±cy korzystanie z demona msession. Jest
to demon szybkiej obs≥ugi sesji, ktÛry moøe dzia≥aÊ lokalnie lub na
innej maszynie. S≥uøy do zapewniania spÛjnej obs≥ugi sesji dla farmy
serwerÛw.

%package mssql
Summary:	MS SQL extension module for PHP
Summary(pl):	Modu≥ MS SQL dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-common = %{epoch}:%{version}-%{release}

%description mssql
This is a dynamic shared object (DSO) for PHP that will add MS SQL
databases support through FreeTDS library.

%description mssql -l pl
Modu≥ PHP dodaj±cy obs≥ugÍ baz danych MS SQL poprzez bibliotekÍ
FreeTDS.

%package mysql
Summary:	MySQL database module for PHP
Summary(pl):	Modu≥ bazy danych MySQL dla PHP
Summary(pt_BR):	Um mÛdulo para aplicaÁıes PHP que usam bancos de dados MySQL
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-common = %{epoch}:%{version}-%{release}

%description mysql
This is a dynamic shared object (DSO) for PHP that will add MySQL
database support.

%description mysql -l pl
Modu≥ PHP umoøliwiaj±cy dostÍp do bazy danych MySQL.

%description mysql -l pt_BR
Um mÛdulo para aplicaÁıes PHP que usam bancos de dados MySQL.

%package mysqli
Summary:	MySQLi module for PHP
Summary(pl):	Modu≥ MySQLi dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	mysql-libs >= 4.1.0

%description mysqli
This is a dynamic shared object (DSO) for PHP that will add MySQLi
(Improved MySQL) support. The difference between it and mysql module
is that it provides access to functionality of MySQL 4.1 and above.

%description mysqli -l pl
Modu≥ PHP umoøliwiaj±cy udoskonalony dostÍp do bazy danych MySQL.
RÛønic± miÍdzy nim a modu≥em mysql jest dostÍp do funkcjonalno∂ci
MySQL w wersji 4.1 i nowszych.

%package ncurses
Summary:	ncurses module for PHP
Summary(pl):	Modu≥ ncurses dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-cli = %{epoch}:%{version}-%{release}
Requires:	%{name}-cli = %{epoch}:%{version}-%{release}

%description ncurses
This PHP module adds support for ncurses functions (only for cli and
cgi SAPIs).

%description ncurses -l pl
Modu≥ PHP dodaj±cy obs≥ugÍ funkcji ncurses (tylko do SAPI cli i cgi).

%package oci8
Summary:	Oracle 8+ database module for PHP
Summary(pl):	Modu≥ bazy danych Oracle 8+ dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Autoreq:	false

%description oci8
This is a dynamic shared object (DSO) for PHP that will add Oracle 7,
8, 9 and 10 database support through Oracle8 Call-Interface (OCI8).

%description oci8 -l pl
Modu≥ PHP umoøliwiaj±cy dostÍp do bazy danych Oracle 7, 8, 9 i 10
poprzez interfejs Oracle8 Call-Interface (OCI8).

%package odbc
Summary:	ODBC extension module for PHP
Summary(pl):	Modu≥ ODBC dla PHP
Summary(pt_BR):	Um mÛdulo para aplicaÁıes PHP que usam bases de dados ODBC
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	unixODBC >= 2.1.1-3

%description odbc
This is a dynamic shared object (DSO) for PHP that will add ODBC
support.

%description odbc -l pl
Modu≥ PHP ze wsparciem dla ODBC.

%description odbc -l pt_BR
Um mÛdulo para aplicaÁıes PHP que usam ODBC.

%package openssl
Summary:	OpenSSL extension module for PHP
Summary(pl):	Modu≥ OpenSSL dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-common = %{epoch}:%{version}-%{release}

%description openssl
This is a dynamic shared object (DSO) for PHP that will add OpenSSL
support.

Warning: this is an experimental module.

%description openssl -l pl
Modu≥ PHP umoøliwiaj±cy korzystanie z biblioteki OpenSSL.

Uwaga: to jest modu≥ eksperymentalny.

%package pcntl
Summary:	Process Control extension module for PHP
Summary(pl):	Modu≥ Process Control dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-program = %{epoch}:%{version}-%{release}
Requires:	%{name}-program = %{epoch}:%{version}-%{release}

%description pcntl
This is a dynamic shared object (DSO) for PHP that will add process
spawning and control support. It supports functions like fork(),
waitpid(), signal() etc.

Warning: this is an experimental module. Also, don't use it in
webserver environment!

%description pcntl -l pl
Modu≥ PHP umoøliwiaj±cy tworzenie nowych procesÛw i kontrolÍ nad nimi.
Obs≥uguje funkcje takie jak fork(), waitpid(), signal() i podobne.

Uwaga: to jest modu≥ eksperymentalny. Ponadto nie jest przeznaczony do
uøywania z serwerem WWW - nie prÛbuj tego!

%package pcre
Summary:	PCRE extension module for PHP
Summary(pl):	Modu≥ PCRE dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-common = %{epoch}:%{version}-%{release}

%description pcre
This is a dynamic shared object (DSO) for PHP that will add Perl
Compatible Regular Expression support.

%description pcre -l pl
Modu≥ PHP umoøliwiaj±cy korzystanie z perlowych wyraøeÒ regularnych
(Perl Compatible Regular Expressions)

%package pdo
Summary:	PHP Data Objects (PDO)
Summary(pl):	Obs≥uga PHP Data Objects (PDO)
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-common = %{epoch}:%{version}-%{release}

%description pdo
This is a dynamic shared object (DSO) for PHP that will add PDO
support.

%description pdo -l pl
Modu≥ PHP dodaj±cy obs≥ugÍ PDO (PHP Data Objects).

%package pdo-dblib
Summary:	PHP Data Objects (PDO) FreeTDS support
Summary(pl):	Modu≥ PHP Data Objects (PDO) z obs≥ug± FreeTDS
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-pdo = %{epoch}:%{version}-%{release}

%description pdo-dblib
This is a dynamic shared object (DSO) for PHP that will add PDO
FreeTDS support.

%description pdo-dblib -l pl
Modu≥ dla PHP dodaj±cy obs≥ugÍ baz danych FreeTDS za po∂rednictwem
interfejsu PDO.

%package pdo-mysql
Summary:	PHP Data Objects (PDO) MySQL support
Summary(pl):	Modu≥ PHP Data Objects (PDO) z obs≥ug± MySQL-a
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-pdo = %{epoch}:%{version}-%{release}

%description pdo-mysql
This is a dynamic shared object (DSO) for PHP that will add PDO MySQL
support.

%description pdo-mysql -l pl
Modu≥ dla PHP dodaj±cy obs≥ugÍ baz danych MySQL za po∂rednictwem
interfejsu PDO.

%package pdo-oci
Summary:	PHP Data Objects (PDO) Oracle support
Summary(pl):	Modu≥ PHP Data Objects (PDO) z obs≥ug± Oracle'a
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-pdo = %{epoch}:%{version}-%{release}

%description pdo-oci
This is a dynamic shared object (DSO) for PHP that will add PDO Oracle
support.

%description pdo-oci -l pl
Modu≥ dla PHP dodaj±cy obs≥ugÍ baz danych Oracle za po∂rednictwem
interfejsu PDO.

%package pdo-odbc
Summary:	PHP Data Objects (PDO) ODBC support
Summary(pl):	Modu≥ PHP Data Objects (PDO) z obs≥ug± ODBC
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-pdo = %{epoch}:%{version}-%{release}

%description pdo-odbc
This is a dynamic shared object (DSO) for PHP that will add PDO ODBC
support.

%description pdo-odbc -l pl
Modu≥ dla PHP dodaj±cy obs≥ugÍ baz danych ODBC za po∂rednictwem
interfejsu PDO.

%package pdo-pgsql
Summary:	PHP Data Objects (PDO) PostgreSQL support
Summary(pl):	Modu≥ PHP Data Objects (PDO) z obs≥ug± PostgreSQL-a
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-pdo = %{epoch}:%{version}-%{release}

%description pdo-pgsql
This is a dynamic shared object (DSO) for PHP that will add PDO
PostgreSQL support.

%description pdo-pgsql -l pl
Modu≥ dla PHP dodaj±cy obs≥ugÍ baz danych PostgreSQL za po∂rednictwem
interfejsu PDO.

%package pdo-sqlite
Summary:	PHP Data Objects (PDO) SQLite support
Summary(pl):	Modu≥ PHP Data Objects (PDO) z obs≥ug± SQLite
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-pdo = %{epoch}:%{version}-%{release}

%description pdo-sqlite
This is a dynamic shared object (DSO) for PHP that will add PDO SQLite
support.

%description pdo-sqlite -l pl
Modu≥ dla PHP dodaj±cy obs≥ugÍ baz danych SQLite za po∂rednictwem
interfejsu PDO.

%package pgsql
Summary:	PostgreSQL database module for PHP
Summary(pl):	Modu≥ bazy danych PostgreSQL dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-common = %{epoch}:%{version}-%{release}

%description pgsql
This is a dynamic shared object (DSO) for PHP that will add PostgreSQL
database support.

%description pgsql -l pl
Modu≥ PHP umoøliwiaj±cy dostÍp do bazy danych PostgreSQL.

%description pgsql -l pt_BR
Um mÛdulo para aplicaÁıes PHP que usam bancos de dados postgresql.

%package posix
Summary:	POSIX extension module for PHP
Summary(pl):	Modu≥ POSIX dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-common = %{epoch}:%{version}-%{release}

%description posix
This is a dynamic shared object (DSO) for PHP that will add POSIX
functions support to PHP.

%description posix -l pl
Modu≥ PHP umoøliwiaj±cy korzystanie z funkcji POSIX.

%package pspell
Summary:	pspell extension module for PHP
Summary(pl):	Modu≥ pspell dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-common = %{epoch}:%{version}-%{release}

%description pspell
This is a dynamic shared object (DSO) for PHP that will add pspell
support to PHP. It allows to check the spelling of a word and offer
suggestions.

%description pspell -l pl
Modu≥ PHP umoøliwiaj±cy korzystanie z pspella. Pozwala on na
sprawdzanie pisowni s≥owa i sugerowanie poprawek.

%package readline
Summary:	readline extension module for PHP
Summary(pl):	Modu≥ readline dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-cli = %{epoch}:%{version}-%{release}
Requires:	%{name}-cli = %{epoch}:%{version}-%{release}

%description readline
This PHP module adds support for readline functions (only for cli and
cgi SAPIs).

%description readline -l pl
Modu≥ PHP dodaj±cy obs≥ugÍ funkcji readline (tylko do SAPI cli i cgi).

%package recode
Summary:	recode extension module for PHP
Summary(pl):	Modu≥ recode dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	recode >= 3.5d-3

%description recode
This is a dynamic shared object (DSO) for PHP that will add recode
support.

%description recode -l pl
Modu≥ PHP dodaj±cy moøliwo∂Ê konwersji kodowania plikÛw (poprzez
bibliotekÍ recode).

%package session
Summary:	session extension module for PHP
Summary(pl):	Modu≥ session dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-common = %{epoch}:%{version}-%{release}

%description session
This is a dynamic shared object (DSO) for PHP that will add session
support.

%description session -l pl
Modu≥ PHP dodaj±cy obs≥ugÍ sesji.

%package shmop
Summary:	Shared Memory Operations extension module for PHP
Summary(pl):	Modu≥ shmop dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-common = %{epoch}:%{version}-%{release}

%description shmop
This is a dynamic shared object (DSO) for PHP that will add Shared
Memory Operations support.

Warning: this is an experimental module.

%description shmop -l pl
Modu≥ PHP umoøliwiaj±cy korzystanie z pamiÍci dzielonej.

Uwaga: to jest modu≥ eksperymentalny.

%package simplexml
Summary:	Simple XML extension module for PHP
Summary(pl):	Modu≥ prostego rozszerzenia XML dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-common = %{epoch}:%{version}-%{release}

%description simplexml
This is a dynamic shared object (DSO) for PHP that will add Simple XML
support.

%description simplexml -l pl
Modu≥ PHP dodaj±cy obs≥ugÍ prostego XML-a.

%package snmp
Summary:	SNMP extension module for PHP
Summary(pl):	Modu≥ SNMP dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-sockets = %{epoch}:%{version}-%{release}

%description snmp
This is a dynamic shared object (DSO) for PHP that will add SNMP
support.

%description snmp -l pl
Modu≥ PHP dodaj±cy obs≥ugÍ SNMP.

%package soap
Summary:	soap extension module for PHP
Summary(pl):	Modu≥ soap dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-common = %{epoch}:%{version}-%{release}

%description soap
This is a dynamic shared object (DSO) for PHP that will add SOAP/WSDL
support.

%description soap -l pl
Modu≥ PHP dodaj±cy obs≥ugÍ SOAP/WSDL.

%package sockets
Summary:	sockets extension module for PHP
Summary(pl):	Modu≥ socket dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-common = %{epoch}:%{version}-%{release}

%description sockets
This is a dynamic shared object (DSO) for PHP that will add sockets
support.

Warning: this is an experimental module.

%description sockets -l pl
Modu≥ PHP dodaj±cy obs≥ugÍ gniazdek.

Uwaga: to jest modu≥ eksperymentalny.

%package sqlite
Summary:	SQLite extension module for PHP
Summary(pl):	Modu≥ SQLite dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-common = %{epoch}:%{version}-%{release}

%description sqlite
SQLite is a C library that implements an embeddable SQL database
engine. Programs that link with the SQLite library can have SQL
database access without running a separate RDBMS process.

SQLite is not a client library used to connect to a big database
server. SQLite is the server. The SQLite library reads and writes
directly to and from the database files on disk.

%description sqlite -l pl
SQLite jest napisan± w C bibliotek± implementuj±c± osadzalny silnik
bazodanowy SQL. Program linkuj±cy siÍ z bibliotek± SQLite moøe mieÊ
dostÍp do bazy SQL bez potrzeby uruchamiania dodatkowego procesu
RDBMS.

SQLite to nie klient baz danych - biblioteka nie ≥±czy siÍ z serwerami
baz danych. SQLite sam jest serwerem. Biblioteka SQLite czyta i
zapisuje dane bezpo∂rednio z/do plikÛw baz danych znajduj±cych siÍ na
dysku.

%package sybase
Summary:	Sybase DB extension module for PHP
Summary(pl):	Modu≥ Sybase DB dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Obsoletes:	php-sybase-ct

%description sybase
This is a dynamic shared object (DSO) for PHP that will add Sybase and
MS SQL databases support through SYBDB library. Currently Sybase
module is not maintained. Using Sybase-CT module is recommended
instead.

%description sybase -l pl
Modu≥ PHP dodaj±cy obs≥ugÍ baz danych Sybase oraz MS SQL poprzez
bibliotekÍ SYBDB. W chwili obecnej modu≥ Sybase nie jest wspierany.
Zaleca siÍ uøywanie modu≥u Sybase-CT.

%package sybase-ct
Summary:	Sybase-CT extension module for PHP
Summary(pl):	Modu≥ Sybase-CT dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Obsoletes:	php-sybase

%description sybase-ct
This is a dynamic shared object (DSO) for PHP that will add Sybase and
MS SQL databases support through CT-lib.

%description sybase-ct -l pl
Modu≥ PHP dodaj±cy obs≥ugÍ baz danych Sybase oraz MS SQL poprzez
CT-lib.

%package sysvmsg
Summary:	SysV msg extension module for PHP
Summary(pl):	Modu≥ SysV msg dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-common = %{epoch}:%{version}-%{release}

%description sysvmsg
This is a dynamic shared object (DSO) for PHP that will add SysV
message queues support.

%description sysvmsg -l pl
Modu≥ PHP umoøliwiaj±cy korzystanie z kolejek komunikatÛw SysV.

%package sysvsem
Summary:	SysV sem extension module for PHP
Summary(pl):	Modu≥ SysV sem dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-common = %{epoch}:%{version}-%{release}

%description sysvsem
This is a dynamic shared object (DSO) for PHP that will add SysV
semaphores support.

%description sysvsem -l pl
Modu≥ PHP umoøliwiaj±cy korzystanie z semaforÛw SysV.

%package sysvshm
Summary:	SysV shm extension module for PHP
Summary(pl):	Modu≥ SysV shm dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-common = %{epoch}:%{version}-%{release}

%description sysvshm
This is a dynamic shared object (DSO) for PHP that will add SysV
Shared Memory support.

%description sysvshm -l pl
Modu≥ PHP umoøliwiaj±cy korzystanie z pamiÍci dzielonej SysV.

%package tidy
Summary:	Tidy extension module for PHP
Summary(pl):	Modu≥ Tidy dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	tidy

%description tidy
This is a dynamic shared object (DSO) for PHP that will add Tidy
support.

%description tidy -l pl
Modu≥ PHP umoøliwiaj±cy korzystanie z tidy.

%package tokenizer
Summary:	tokenizer extension module for PHP
Summary(pl):	Modu≥ rozszerzenia tokenizer dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-common = %{epoch}:%{version}-%{release}

%description tokenizer
This is a dynamic shared object (DSO) for PHP that will add tokenizer
support.

%description tokenizer -l pl
Modu≥ PHP dodaj±cy obs≥ugÍ tokenizera do PHP.

%package wddx
Summary:	wddx extension module for PHP
Summary(pl):	Modu≥ wddx dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-session = %{epoch}:%{version}-%{release}
Requires:	%{name}-xml = %{epoch}:%{version}-%{release}

%description wddx
This is a dynamic shared object (DSO) for PHP that will add wddx
support.

%description wddx -l pl
Modu≥ PHP umoøliwiaj±cy korzystanie z wddx.

%package xml
Summary:	XML extension module for PHP
Summary(pl):	Modu≥ XML dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-common = %{epoch}:%{version}-%{release}

%description xml
This is a dynamic shared object (DSO) for PHP that will add XML
support. This extension lets you create XML parsers and then define
handlers for different XML events.

%description xml -l pl
Modu≥ PHP umoøliwiaj±cy parsowanie plikÛw XML i obs≥ugÍ zdarzeÒ
zwi±zanych z tymi plikami. Pozwala on tworzyÊ analizatory XML-a i
nastÍpnie definiowaÊ procedury obs≥ugi dla rÛønych zdarzeÒ XML.

%package xmlreader
Summary:	XML Reader extension module for PHP
Summary(pl):	Modu≥ XML Reader dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-common = %{epoch}:%{version}-%{release}

%description xmlreader
This is a dynamic shared object (DSO) for PHP that will add XML Reader
support. The XMLReader extension is an XML Pull parser. The reader
acts as a cursor going forward on the document stream and stopping at
each node on the way.

%description xmlreader -l pl
Modu≥ PHP umoøliwiaj±cy parsowanie plikÛw XML w trybie Pull. Czytnik
dzia≥a jako kursor przechodz±cy przez strumieÒ dokumentu i
zatrzymuj±cy siÍ nakaødym wÍºle po drodze.

%package xmlrpc
Summary:	xmlrpc extension module for PHP
Summary(pl):	Modu≥ xmlrpc dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-common = %{epoch}:%{version}-%{release}

%description xmlrpc
This is a dynamic shared object (DSO) for PHP that will add XMLRPC
support.

Warning: this is an experimental module.

%description xmlrpc -l pl
Modu≥ PHP dodaj±cy obs≥ugÍ XMLRPC.

Uwaga: to jest modu≥ eksperymentalny.

%package xsl
Summary:	xsl extension module for PHP
Summary(pl):	Modu≥ xsl dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	libxslt >= 1.0.18
# Maybe it would be nice to add it here?
#Provides:	php-xslt
# actually not true, functionality is similar, but API differs
Obsoletes:	php-xslt <= 3:4.3.8-1

%description xsl
This is a dynamic shared object (DSO) for PHP that will add new XSL
support (using libxslt).

%description xsl -l pl
Modu≥ PHP dodaj±cy now± obs≥ugÍ XSLT (przy uøyciu libxslt).

%package zlib
Summary:	Zlib extension module for PHP
Summary(pl):	Modu≥ zlib dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-common = %{epoch}:%{version}-%{release}

%description zlib
This is a dynamic shared object (DSO) for PHP that will add zlib
compression support to PHP.

%description zlib -l pl
Modu≥ PHP umoøliwiaj±cy uøywanie kompresji zlib.

%prep
%setup -q
# this patch is broken by design, breaks --enable-versioning for example
# update: --enable-version is broken by itself, it disables dynamic modules.
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
cp php.ini-dist php.ini
%patch10 -p1
# for ac2.53b/am1.6b - AC_LANG_CXX has AM_CONDITIONAL, so cannot be invoked
# conditionally...
%patch11 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch19 -p1
%patch20 -p1
%patch21 -p1
%patch23 -p1
%patch24 -p1
%patch25 -p1
%patch26 -p1

%if %{with hardening}
zcat %{SOURCE9} | patch -p1 || exit 1
patch -p1 < %{PATCH30} || exit 1
%endif
%patch31 -p1
%patch32 -p1

# conflict seems to be resolved by recode patches
rm -f ext/recode/config9.m4

# new apr
sed -i -e 's#apr-config#apr-1-config#g' sapi/apache*/*.m4

%build
if API=$(awk '/#define PHP_API_VERSION/{print $3}' main/php.h) && [ $API != %{php_api_version} ]; then
	echo "Set %%define php_api_version to $API and rerun."
	exit 1
fi

if API=$(awk '/#define ZEND_MODULE_API_NO/{print $3}' Zend/zend_modules.h) && [ $API != %{zend_module_api} ]; then
	echo "Set %%define zend_module_api to $API and rerun."
	exit 1
fi

if API=$(awk '/#define ZEND_EXTENSION_API_NO/{print $3}' Zend/zend_extensions.h) && [ $API != %{zend_extension_api} ]; then
	echo "Set %%define zend_extension_api to $API and rerun."
	exit 1
fi

CFLAGS="%{rpmcflags} -DEAPI=1 -I/usr/X11R6/include"
%if %{with apache2}
# Apache2 CFLAGS. harmless for other SAPIs.
CFLAGS="$CFLAGS $(%{_bindir}/apr-1-config --includes) $(%{_bindir}/apu-1-config --includes)"
%endif

EXTENSION_DIR="%{extensionsdir}"; export EXTENSION_DIR
if [ ! -f _built-conf ]; then # configure once (for faster debugging purposes)
	rm -f Makefile.{fcgi,cgi,cli,apxs{1,2}} # now remove Makefile copies
	%{__libtoolize}
	%{__aclocal}
	./buildconf --force
	touch _built-conf
fi
PROG_SENDMAIL="/usr/lib/sendmail"; export PROG_SENDMAIL

sapis="
%if %{with fcgi}
fcgi
%endif
cgi cli
%if %{with apache1}
apxs1
%endif
%if %{with apache2}
apxs2
%endif
"
for sapi in $sapis; do
	[ -f Makefile.$sapi ] && continue # skip if already configured (for faster debugging purposes)

	%configure \
	`
	case $sapi in
	cgi)
		echo --enable-discard-path --enable-force-cgi-redirect
	;;
	cli)
		echo --disable-cgi
	;;
	fcgi)
		echo --enable-fastcgi --with-fastcgi=/usr --enable-force-cgi-redirect
	;;
	apxs1)
		ver=%(rpm -q --qf '%%{version}' apache1-apxs)
		echo --with-apxs=%{apxs1} --with-apache-version=$ver
	;;
	apxs2)
		ver=%(rpm -q --qf '%%{version}' apache-apxs)
		echo --with-apxs2=%{apxs2} --with-apache-version=$ver
	;;
	esac
	` \
	--cache-file=config.cache \
	--with-libdir=%{_lib} \
	--with-config-file-path=%{_sysconfdir} \
	--with-config-file-scan-dir=%{_sysconfdir}/conf.d \
	--with-exec-dir=%{_bindir} \
	--%{!?debug:dis}%{?debug:en}able-debug \
	%{?with_zts:--enable-maintainer-zts} \
	--enable-memory-limit \
	--enable-bcmath=shared \
	--enable-calendar=shared \
	--enable-ctype=shared \
	--enable-dba=shared \
	--with-inifile \
	--with-flatfile \
	--enable-dom=shared \
	--enable-exif=shared \
	--enable-filepro=shared \
	--enable-ftp=shared \
	--enable-gd-native-ttf \
	--enable-gd-jus-conf \
	--enable-libxml \
	--enable-magic-quotes \
	--enable-mbstring=shared,all \
	--enable-mbregex \
	--enable-pcntl=shared \
	--enable-pdo=shared \
%if %{with mssql} || %{with sybase} || %{with sybase_ct}
	--with-pdo-dblib=shared \
%endif
%if %{with interbase} && %{without interbase_inst}
	--with-pdo-firebird=shared \
%endif
	--with-pdo-mysql=shared \
	%{?with_oci8:--with-pdo-oci=shared} \
	%{?with_odbc:--with-pdo-odbc=shared,unixODBC,/usr} \
	%{?with_pgsql:--with-pdo-pgsql=shared} \
	%{?with_sqlite:--with-pdo-sqlite=shared} \
	--enable-posix=shared \
	--enable-session \
	--enable-shared \
	--enable-shmop=shared \
	--enable-simplexml \
	--enable-sysvmsg=shared \
	--enable-sysvsem=shared \
	--enable-sysvshm=shared \
	--enable-track-vars \
	--enable-trans-sid \
	--enable-safe-mode \
	--enable-soap=shared \
	--enable-sockets=shared \
	--enable-tokenizer=shared \
	--enable-ucd-snmp-hack \
	%{?with_wddx:--enable-wddx=shared} \
	--enable-xml=shared \
	--with-xmlreader=shared \
	--with-bz2=shared \
	%{!?with_curl:--without-curl}%{?with_curl:--with-curl=shared} \
	%{?with_db3:--with-db3}%{!?with_db3:--with-db4} \
	--enable-dbase=shared \
%if %{with xmlrpc}
	--with-expat-dir=shared,/usr \
%else
	--without-expat-dir \
%endif
	%{?with_fdf:--with-fdftk=shared} \
	--with-iconv=shared \
	--with-filepro=shared \
	--with-freetype-dir=shared \
	--with-gettext=shared \
	--with-gd=shared,/usr \
	--with-gdbm \
	--with-gmp=shared \
	%{?with_hwapi:--with-hwapi=shared} \
	%{?with_imap:--with-imap=shared --with-imap-ssl} \
	%{?with_interbase:--with-interbase=shared%{!?with_interbase_inst:,/usr}} \
	--with-jpeg-dir=/usr \
	%{?with_ldap:--with-ldap=shared --with-ldap-sasl} \
	--with-mcrypt=shared \
	%{?with_mhash:--with-mhash=shared} \
	%{?with_mime_magic:--with-mime-magic=shared,/usr/share/file/magic.mime}%{!?with_mime_magic:--disable-mime-magic} \
	%{?with_ming:--with-ming=shared} \
	%{?with_mm:--with-mm} \
	%{?with_msession:--with-msession=shared}%{!?with_msession:--without-msession} \
	%{?with_mssql:--with-mssql=shared} \
	--with-mysql=shared,/usr \
	--with-mysql-sock=/var/lib/mysql/mysql.sock \
	%{?with_mysqli:--with-mysqli=shared} \
	--with-ncurses=shared \
	%{?with_oci8:--with-oci8=shared} \
	%{?with_openssl:--with-openssl=shared} \
	--with-kerberos \
	%{!?with_pcre:--without-pcre-regex}%{?with_pcre:--with-pcre-regex=shared,/usr} \
	--with-pear=%{php_pear_dir} \
	%{!?with_pgsql:--without-pgsql}%{?with_pgsql:--with-pgsql=shared,/usr} \
	--with-png-dir=/usr \
	%{?with_pspell:--with-pspell=shared} \
	--with-readline=shared \
	%{?with_recode:--with-recode=shared} \
	--with-regex=php \
	--without-sablot-js \
	%{?with_snmp:--with-snmp=shared} \
	%{?with_sybase:--with-sybase=shared,/usr} \
	%{?with_sybase_ct:--with-sybase-ct=shared,/usr} \
	%{?with_sqlite:--with-sqlite=shared,/usr --enable-sqlite-utf8} \
	--with-t1lib=shared \
	%{?with_tidy:--with-tidy=shared} \
	--with-tiff-dir=/usr \
	%{?with_odbc:--with-unixODBC=shared,/usr} \
	%{!?with_xmlrpc:--without-xmlrpc}%{?with_xmlrpc:--with-xmlrpc=shared,/usr} \
	--with-xsl=shared \
	--with-zlib=shared \
	--with-zlib-dir=shared,/usr

	cp -f Makefile Makefile.$sapi

	# left for debugging purposes
	cp -f main/php_config.h php_config.h.$sapi
done

# for now session_mm doesn't work with shared session module...
# --enable-session=shared
# %{!?with_mm:--with-mm=shared,no}%{?with_mm:--with-mm=shared}

%{__make} build-modules

%{__make} libphp_common.la
# fix install paths, avoid evil rpaths
sed -i -e "s|^libdir=.*|libdir='%{_libdir}'|" libphp_common.la

%if %{with apache1}
%{__make} libtool-sapi LIBTOOL_SAPI=sapi/apache/libphp5.la -f Makefile.apxs1
sed -i -e "
s|^libdir=.*|libdir='%{_libdir}/apache1'|;
s|^(relink_command=.* -rpath )[^ ]*/libs |$1%{_libdir}/apache1 |" sapi/apache/libphp5.la
%endif

%if %{with apache2}
%{__make} libtool-sapi LIBTOOL_SAPI=sapi/apache2handler/libphp5.la -f Makefile.apxs2
sed -i -e "
s|^libdir=.*|libdir='%{_libdir}/apache'|;
s|^(relink_command=.* -rpath )[^ ]*/libs |$1%{_libdir}/apache |" sapi/apache2handler/libphp5.la
%endif

# FCGI
%if %{with fcgi}
cp -af php_config.h.fcgi main/php_config.h
%{__make} sapi/cgi/php -f Makefile.fcgi
cp -r sapi/cgi sapi/fcgi
rm -rf sapi/cgi/.libs sapi/cgi/*.lo
%endif

# CGI
cp -af php_config.h.cgi main/php_config.h
%{__make} sapi/cgi/php -f Makefile.cgi

# CLI
cp -af php_config.h.cli main/php_config.h
%{__make} sapi/cli/php -f Makefile.cli

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir}/{php,apache{,1}},%{_sysconfdir}/{apache,cgi},%{_phpsharedir}} \
	$RPM_BUILD_ROOT/home/services/{httpd,apache}/icons \
	$RPM_BUILD_ROOT{%{_sbindir},%{_bindir}} \
	$RPM_BUILD_ROOT/var/run/php \
	$RPM_BUILD_ROOT{/etc/apache/conf.d,/etc/httpd/httpd.conf} \
	$RPM_BUILD_ROOT%{_mandir}/man1

# install apache1 DSO module
%if %{with apache1}
libtool --silent --mode=install install sapi/apache/libphp5.la $RPM_BUILD_ROOT%{_libdir}/apache1/
%endif

# install apache2 DSO module
%if %{with apache2}
libtool --silent --mode=install install sapi/apache2handler/libphp5.la $RPM_BUILD_ROOT%{_libdir}/apache/
%endif

libtool --silent --mode=install install libphp_common.la $RPM_BUILD_ROOT%{_libdir}

# install the apache modules' files
%{__make} install-headers install-build install-modules install-programs \
	INSTALL_ROOT=$RPM_BUILD_ROOT

# as of 5.0.5, phpextdist isn't installed by default
install scripts/dev/phpextdist $RPM_BUILD_ROOT%{_bindir}

# install CGI
libtool --silent --mode=install install sapi/cgi/php $RPM_BUILD_ROOT%{_bindir}/php.cgi

# install FCGI
%if %{with fcgi}
libtool --silent --mode=install install sapi/fcgi/php $RPM_BUILD_ROOT%{_bindir}/php.fcgi
%endif

# install CLI
libtool --silent --mode=install install sapi/cli/php $RPM_BUILD_ROOT%{_bindir}/php.cli
install sapi/cli/php.1 $RPM_BUILD_ROOT%{_mandir}/man1/php.1
echo ".so php.1" >$RPM_BUILD_ROOT%{_mandir}/man1/php.cli.1

# TODO:
# Why make install doesn't install libphp5.so ?
#install libs/libphp5.so $RPM_BUILD_ROOT%{apachelib}

ln -sf php.cli $RPM_BUILD_ROOT%{_bindir}/php

sed -e 's#%{_prefix}/lib/php#%{_libdir}/php#g' php.ini > $RPM_BUILD_ROOT%{_sysconfdir}/php.ini
%if %{with fcgi}
install %{SOURCE5} $RPM_BUILD_ROOT%{_sysconfdir}/php-cgi-fcgi.ini
%endif
install %{SOURCE6} $RPM_BUILD_ROOT%{_sysconfdir}/php-cgi.ini
install %{SOURCE8} $RPM_BUILD_ROOT%{_sysconfdir}/php-cli.ini
install %{SOURCE3} $RPM_BUILD_ROOT%{_sbindir}
install %{SOURCE1} .

%if %{with apache1}
install %{SOURCE2} php.gif $RPM_BUILD_ROOT/home/services/apache/icons
install %{SOURCE4} $RPM_BUILD_ROOT/etc/apache/conf.d/70_mod_php.conf
install %{SOURCE7} $RPM_BUILD_ROOT%{_sysconfdir}/php-apache.ini
rm -f $RPM_BUILD_ROOT%{_libdir}/apache1/libphp5.la
%endif

%if %{with apache2}
install %{SOURCE2} php.gif $RPM_BUILD_ROOT/home/services/httpd/icons
install %{SOURCE4} $RPM_BUILD_ROOT/etc/httpd/httpd.conf/70_mod_php.conf
install %{SOURCE7} $RPM_BUILD_ROOT%{_sysconfdir}/php-apache2handler.ini
rm -f $RPM_BUILD_ROOT%{_libdir}/apache/libphp5.la
%endif

cp -f Zend/LICENSE{,.Zend}

# Generate stub .ini files for each subpackage
install -d $RPM_BUILD_ROOT%{_sysconfdir}/conf.d
for so in modules/*.so; do
	mod=$(basename $so .so)
	conf="%{_sysconfdir}/conf.d/${mod}.ini"
	# xml needs to be loaded before wddx
	[ "$mod" = "wddx" ] && conf="%{_sysconfdir}/conf.d/xml_${mod}.ini"
	cat > $RPM_BUILD_ROOT${conf} <<EOF
; Enable ${mod} extension module
extension=${mod}.so
EOF
done

# Not in all SAPI, so don't need the .ini fragments.
rm -f $RPM_BUILD_ROOT%{_sysconfdir}/conf.d/{ncurses,pcntl,readline}.ini

# use system automake and {lib,sh}tool
ln -snf /usr/share/automake/config.{guess,sub} $RPM_BUILD_ROOT%{_libdir}/php/build
ln -snf %{_aclocaldir}/libtool.m4 $RPM_BUILD_ROOT%{_libdir}/php/build
ln -snf %{_datadir}/libtool/ltmain.sh $RPM_BUILD_ROOT%{_libdir}/php/build
ln -snf %{_bindir}/shtool $RPM_BUILD_ROOT%{_libdir}/php/build

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with apache1}
%triggerpostun -- %{name} < 4:5.0.4-9.11
%{apxs1} -e -A -n php5 %{_pkglibdir}/libphp5.so 1>&2
%{__perl} -pi -e \
	's|^AddType application/x-httpd-php \.php|#AddType application/x-httpd-php .php|' \
	/etc/apache/apache.conf
%service -q apache restart
%endif

%post
if [ "$1" = "1" ]; then
%if %{with apache1}
	%service -q apache restart
%endif
%if %{with apache2}
	%service -q httpd restart
%endif
fi

%postun
if [ "$1" = "0" ]; then
%if %{with apache1}
	%service -q apache restart
%endif
%if %{with apache2}
	%service -q httpd restart
%endif
fi

%post -n apache1-mod_php
if [ "$1" = "1" ]; then
	%service -q apache restart
fi

%postun -n apache1-mod_php
if [ "$1" = "0" ]; then
	%service -q apache restart
fi

%post -n apache-mod_php
if [ "$1" = "1" ]; then
	%service -q httpd restart
fi

%postun -n apache-mod_php
if [ "$1" = "0" ]; then
	%service -q httpd restart
fi

# so tired of typing... so decided to create macros
# macro called at extension post scriptlet
%define	extension_post \
if [ "$1" = "1" ]; then \
	[ ! -f /etc/apache/conf.d/??_mod_php.conf ] || %service -q apache restart \
	[ ! -f /etc/httpd/httpd.conf/??_mod_php.conf ] || %service -q httpd restart \
fi

# macro called at extension postun scriptlet
%define	extension_postun \
if [ "$1" = "0" ]; then \
	[ ! -f /etc/apache/conf.d/??_mod_php.conf ] || %service -q apache restart \
	[ ! -f /etc/httpd/httpd.conf/??_mod_php.conf ] || %service -q httpd restart \
fi

%post	common -p /sbin/ldconfig
%postun	common -p /sbin/ldconfig

%posttrans common
# minimizing apache restarts logics. we restart webserver:
#
# 1. at the end of transaction. (posttrans, feature from rpm 4.4.2)
# 2. first install of extension (post: $1 = 1)
# 2. uninstall of extension (postun: $1 == 0)
#
# the strict internal deps between extensions (and apache modules) and
# common package are very important for all this to work.

# restart webserver at the end of transaction
[ ! -f /etc/apache/conf.d/??_mod_php.conf ] || %service -q apache restart
[ ! -f /etc/httpd/httpd.conf/??_mod_php.conf ] || %service -q httpd restart

%if %{with apache2}
%triggerpostun -- php < 4:5.0.4-7.1
# for fixed php-SAPI.ini, the poor php-apache.ini was never read for apache2
if [ -f %{_sysconfdir}/php-apache.ini.rpmsave ]; then
	cp -f %{_sysconfdir}/php-apache2handler.ini{,.rpmnew}
	mv -f %{_sysconfdir}/php-apache.ini.rpmsave %{_sysconfdir}/php-apache2handler.ini
fi

# extra trigger, if they did not upgrade to 4:5.0.4-7 but still had old php-apache.ini
%triggerpostun -n apache-mod_php -- php < 4:5.0.4-7.1
# for fixed php-SAPI.ini, the poor php-apache.ini was never read for apache2
if [ -f %{_sysconfdir}/php-apache.ini.rpmsave ]; then
	cp -f %{_sysconfdir}/php-apache2handler.ini{,.rpmnew}
	mv -f %{_sysconfdir}/php-apache.ini.rpmsave %{_sysconfdir}/php-apache2handler.ini
fi
%endif

%post bcmath
%extension_post

%postun bcmath
%extension_postun

%post bzip2
%extension_post

%postun bzip2
%extension_postun

%post calendar
%extension_post

%postun calendar
%extension_postun

%post ctype
%extension_post

%postun ctype
%extension_postun

%post curl
%extension_post

%postun curl
%extension_postun

%post dba
%extension_post

%postun dba
%extension_postun

%post dbase
%extension_post

%postun dbase
%extension_postun

%post dom
%extension_post

%postun dom
%extension_postun

%post exif
%extension_post

%postun exif
%extension_postun

%post fdf
%extension_post

%postun fdf
%extension_postun

%post filepro
%extension_post

%postun filepro
%extension_postun

%post ftp
%extension_post

%postun ftp
%extension_postun

%post gd
%extension_post

%postun gd
%extension_postun

%post gettext
%extension_post

%postun gettext
%extension_postun

%post gmp
%extension_post

%postun gmp
%extension_postun

%post hwapi
%extension_post

%postun hwapi
%extension_postun

%post iconv
%extension_post

%postun iconv
%extension_postun

%post imap
%extension_post

%postun imap
%extension_postun

%post interbase
%extension_post

%postun interbase
%extension_postun

%post ldap
%extension_post

%postun ldap
%extension_postun

%post mbstring
%extension_post

%postun mbstring
%extension_postun

%post mcrypt
%extension_post

%postun mcrypt
%extension_postun

%post mhash
%extension_post

%postun mhash
%extension_postun

%post mime_magic
%extension_post

%postun mime_magic
%extension_postun

%post ming
%extension_post

%postun ming
%extension_postun

%post msession
%extension_post

%postun msession
%extension_postun

%post mssql
%extension_post

%postun mssql
%extension_postun

%post mysql
%extension_post

%postun mysql
%extension_postun

%post mysqli
%extension_post

%postun mysqli
%extension_postun

%post ncurses
if [ -f %{_sysconfdir}/php-cgi.ini ]; then
	%{_sbindir}/php-module-install install ncurses %{_sysconfdir}/php-cgi.ini
fi
if [ -f %{_sysconfdir}/php-cli.ini ]; then
	%{_sbindir}/php-module-install install ncurses %{_sysconfdir}/php-cli.ini
fi

%postun ncurses
if [ "$1" = "0" ]; then
	if [ -f %{_sysconfdir}/php-cgi.ini ]; then
		%{_sbindir}/php-module-install remove ncurses %{_sysconfdir}/php-cgi.ini
	fi
	if [ -f %{_sysconfdir}/php-cli.ini ]; then
		%{_sbindir}/php-module-install remove ncurses %{_sysconfdir}/php-cli.ini
	fi
fi

%post oci8
%extension_post

%postun oci8
%extension_postun

%post odbc
%extension_post

%postun odbc
%extension_postun

%post openssl
%extension_post

%postun openssl
%extension_postun

%post pcntl
if [ -f %{_sysconfdir}/php-cgi.ini ]; then
	%{_sbindir}/php-module-install install pcntl %{_sysconfdir}/php-cgi.ini
fi
if [ -f %{_sysconfdir}/php-cli.ini ]; then
	%{_sbindir}/php-module-install install pcntl %{_sysconfdir}/php-cli.ini
fi

%postun pcntl
if [ "$1" = "0" ]; then
	if [ -f %{_sysconfdir}/php-cgi.ini ]; then
		%{_sbindir}/php-module-install remove pcntl %{_sysconfdir}/php-cgi.ini
	fi
	if [ -f %{_sysconfdir}/php-cli.ini ]; then
		%{_sbindir}/php-module-install remove pcntl %{_sysconfdir}/php-cli.ini
	fi
fi

%post pcre
%extension_post

%postun pcre
%extension_postun

%post pdo-dblib
%extension_post

%postun pdo-dblib
%extension_postun

%post pdo-mysql
%extension_post

%postun pdo-mysql
%extension_postun

%post pdo-odbc
%extension_post

%postun pdo-odbc
%extension_postun

%post pdo-pgsql
%extension_post

%postun pdo-pgsql
%extension_postun

%post pdo-sqlite
%extension_post

%postun pdo-sqlite
%extension_postun

%post pgsql
%extension_post

%postun pgsql
%extension_postun

%post posix
%extension_post

%postun posix
%extension_postun

%post pspell
%extension_post

%postun pspell
%extension_postun

%post readline
if [ -f %{_sysconfdir}/php-cgi.ini ]; then
	%{_sbindir}/php-module-install install readline %{_sysconfdir}/php-cgi.ini
fi
if [ -f %{_sysconfdir}/php-cli.ini ]; then
	%{_sbindir}/php-module-install install readline %{_sysconfdir}/php-cli.ini
fi

%postun readline
if [ "$1" = "0" ]; then
	if [ -f %{_sysconfdir}/php-cgi.ini ]; then
		%{_sbindir}/php-module-install remove readline %{_sysconfdir}/php-cgi.ini
	fi
	if [ -f %{_sysconfdir}/php-cli.ini ]; then
		%{_sbindir}/php-module-install remove readline %{_sysconfdir}/php-cli.ini
	fi
fi

%post recode
%extension_post

%postun recode
%extension_postun

%post session
%extension_post

%postun session
%extension_postun

%post shmop
%extension_post

%postun shmop
%extension_postun

%post snmp
%extension_post

%postun snmp
%extension_postun

%post soap
%extension_post

%postun soap
%extension_postun
if [ "$1" = "0" ]; then
	%{_sbindir}/php-module-install remove soap %{_sysconfdir}/php.ini
fi

%post sockets
%extension_post

%postun sockets
%extension_postun

%post sqlite
%extension_post

%postun sqlite
%extension_postun

%post sybase
%extension_post

%postun sybase
%extension_postun

%post sybase-ct
%extension_post

%postun sybase-ct
%extension_postun

%post sysvmsg
%extension_post

%postun sysvmsg
%extension_postun

%post sysvsem
%extension_post

%postun sysvsem
%extension_postun

%post sysvshm
%extension_post

%postun sysvshm
%extension_postun

%post tidy
%extension_post

%postun tidy
%extension_postun

%post tokenizer
%extension_post

%postun tokenizer
%extension_postun

%post wddx
%extension_post

%postun wddx
%extension_postun

%post xml
%extension_post

%postun xml
%extension_postun

%post xmlreader
%extension_post

%postun xmlreader
%extension_postun

%post xmlrpc
%extension_post

%postun xmlrpc
%extension_postun

%post xsl
%extension_post

%postun xsl
%extension_postun

%post zlib
%extension_post

%postun zlib
%extension_postun

%triggerun bcmath -- %{name}-bcmath < 4:5.0.4-9.1
[ ! -x %{_sbindir}/php-module-install ] || %{_sbindir}/php-module-install remove bcmath %{_sysconfdir}/php.ini

%triggerun bzip2 -- %{name}-bzip2 < 4:5.0.4-9.1
[ ! -x %{_sbindir}/php-module-install ] || %{_sbindir}/php-module-install remove bzip2 %{_sysconfdir}/php.ini

%triggerun calendar -- %{name}-calendar < 4:5.0.4-9.1
[ ! -x %{_sbindir}/php-module-install ] || %{_sbindir}/php-module-install remove calendar %{_sysconfdir}/php.ini

%triggerun ctype -- %{name}-ctype < 4:5.0.4-9.1
[ ! -x %{_sbindir}/php-module-install ] || %{_sbindir}/php-module-install remove ctype %{_sysconfdir}/php.ini

%triggerun curl -- %{name}-curl < 4:5.0.4-9.1
[ ! -x %{_sbindir}/php-module-install ] || %{_sbindir}/php-module-install remove curl %{_sysconfdir}/php.ini

%triggerun dba -- %{name}-dba < 4:5.0.4-9.1
[ ! -x %{_sbindir}/php-module-install ] || %{_sbindir}/php-module-install remove dba %{_sysconfdir}/php.ini

%triggerun dbase -- %{name}-dbase < 4:5.0.4-9.1
[ ! -x %{_sbindir}/php-module-install ] || %{_sbindir}/php-module-install remove dbase %{_sysconfdir}/php.ini

%triggerun dom -- %{name}-dom < 4:5.0.4-9.1
[ ! -x %{_sbindir}/php-module-install ] || %{_sbindir}/php-module-install remove dom %{_sysconfdir}/php.ini

%triggerun exif -- %{name}-exif < 4:5.0.4-9.1
[ ! -x %{_sbindir}/php-module-install ] || %{_sbindir}/php-module-install remove exif %{_sysconfdir}/php.ini

%triggerun fdf -- %{name}-fdf < 4:5.0.4-9.1
[ ! -x %{_sbindir}/php-module-install ] || %{_sbindir}/php-module-install remove fdf %{_sysconfdir}/php.ini

%triggerun filepro -- %{name}-filepro < 4:5.0.4-9.1
[ ! -x %{_sbindir}/php-module-install ] || %{_sbindir}/php-module-install remove filepro %{_sysconfdir}/php.ini

%triggerun ftp -- %{name}-ftp < 4:5.0.4-9.1
[ ! -x %{_sbindir}/php-module-install ] || %{_sbindir}/php-module-install remove ftp %{_sysconfdir}/php.ini

%triggerun gd -- %{name}-gd < 4:5.0.4-9.1
[ ! -x %{_sbindir}/php-module-install ] || %{_sbindir}/php-module-install remove gd %{_sysconfdir}/php.ini

%triggerun gettext -- %{name}-gettext < 4:5.0.4-9.1
[ ! -x %{_sbindir}/php-module-install ] || %{_sbindir}/php-module-install remove gettext %{_sysconfdir}/php.ini

%triggerun gmp -- %{name}-gmp < 4:5.0.4-9.1
[ ! -x %{_sbindir}/php-module-install ] || %{_sbindir}/php-module-install remove gmp %{_sysconfdir}/php.ini

%triggerun hwapi -- %{name}-hwapi < 4:5.0.4-9.1
[ ! -x %{_sbindir}/php-module-install ] || %{_sbindir}/php-module-install remove hwapi %{_sysconfdir}/php.ini

%triggerun iconv -- %{name}-iconv < 4:5.0.4-9.1
[ ! -x %{_sbindir}/php-module-install ] || %{_sbindir}/php-module-install remove iconv %{_sysconfdir}/php.ini

%triggerun imap -- %{name}-imap < 4:5.0.4-9.1
[ ! -x %{_sbindir}/php-module-install ] || %{_sbindir}/php-module-install remove imap %{_sysconfdir}/php.ini

%triggerun interbase -- %{name}-interbase < 4:5.0.4-9.1
[ ! -x %{_sbindir}/php-module-install ] || %{_sbindir}/php-module-install remove interbase %{_sysconfdir}/php.ini

%triggerun ldap -- %{name}-ldap < 4:5.0.4-9.1
[ ! -x %{_sbindir}/php-module-install ] || %{_sbindir}/php-module-install remove ldap %{_sysconfdir}/php.ini

%triggerun mbstring -- %{name}-mbstring < 4:5.0.4-9.1
[ ! -x %{_sbindir}/php-module-install ] || %{_sbindir}/php-module-install remove mbstring %{_sysconfdir}/php.ini

%triggerun mcrypt -- %{name}-mcrypt < 4:5.0.4-9.1
[ ! -x %{_sbindir}/php-module-install ] || %{_sbindir}/php-module-install remove mcrypt %{_sysconfdir}/php.ini

%triggerun mhash -- %{name}-mhash < 4:5.0.4-9.1
[ ! -x %{_sbindir}/php-module-install ] || %{_sbindir}/php-module-install remove mhash %{_sysconfdir}/php.ini

%triggerun mime_magic -- %{name}-mime_magic < 4:5.0.4-9.1
[ ! -x %{_sbindir}/php-module-install ] || %{_sbindir}/php-module-install remove mime_magic %{_sysconfdir}/php.ini

%triggerun ming -- %{name}-ming < 4:5.0.4-9.1
[ ! -x %{_sbindir}/php-module-install ] || %{_sbindir}/php-module-install remove ming %{_sysconfdir}/php.ini

%triggerun msession -- %{name}-msession < 4:5.0.4-9.1
[ ! -x %{_sbindir}/php-module-install ] || %{_sbindir}/php-module-install remove msession %{_sysconfdir}/php.ini

%triggerun mssql -- %{name}-mssql < 4:5.0.4-9.1
[ ! -x %{_sbindir}/php-module-install ] || %{_sbindir}/php-module-install remove mssql %{_sysconfdir}/php.ini

%triggerun mysql -- %{name}-mysql < 4:5.0.4-9.1
[ ! -x %{_sbindir}/php-module-install ] || %{_sbindir}/php-module-install remove mysql %{_sysconfdir}/php.ini

%triggerun mysqli -- %{name}-mysqli < 4:5.0.4-9.1
[ ! -x %{_sbindir}/php-module-install ] || %{_sbindir}/php-module-install remove mysqli %{_sysconfdir}/php.ini

%triggerun oci8 -- %{name}-oci8 < 4:5.0.4-9.1
[ ! -x %{_sbindir}/php-module-install ] || %{_sbindir}/php-module-install remove oci8 %{_sysconfdir}/php.ini

%triggerun odbc -- %{name}-odbc < 4:5.0.4-9.1
[ ! -x %{_sbindir}/php-module-install ] || %{_sbindir}/php-module-install remove odbc %{_sysconfdir}/php.ini

%triggerun openssl -- %{name}-openssl < 4:5.0.4-9.1
[ ! -x %{_sbindir}/php-module-install ] || %{_sbindir}/php-module-install remove openssl %{_sysconfdir}/php.ini

%triggerun pcre -- %{name}-pcre < 4:5.0.4-9.1
[ ! -x %{_sbindir}/php-module-install ] || %{_sbindir}/php-module-install remove pcre %{_sysconfdir}/php.ini

%triggerun pgsql -- %{name}-pgsql < 4:5.0.4-9.1
[ ! -x %{_sbindir}/php-module-install ] || %{_sbindir}/php-module-install remove pgsql %{_sysconfdir}/php.ini

%triggerun posix -- %{name}-posix < 4:5.0.4-9.1
[ ! -x %{_sbindir}/php-module-install ] || %{_sbindir}/php-module-install remove posix %{_sysconfdir}/php.ini

%triggerun pspell -- %{name}-pspell < 4:5.0.4-9.1
[ ! -x %{_sbindir}/php-module-install ] || %{_sbindir}/php-module-install remove pspell %{_sysconfdir}/php.ini

%triggerun recode -- %{name}-recode < 4:5.0.4-9.1
[ ! -x %{_sbindir}/php-module-install ] || %{_sbindir}/php-module-install remove recode %{_sysconfdir}/php.ini

%triggerun session -- %{name}-session < 4:5.0.4-9.1
[ ! -x %{_sbindir}/php-module-install ] || %{_sbindir}/php-module-install remove session %{_sysconfdir}/php.ini

%triggerun shmop -- %{name}-shmop < 4:5.0.4-9.1
[ ! -x %{_sbindir}/php-module-install ] || %{_sbindir}/php-module-install remove shmop %{_sysconfdir}/php.ini

%triggerun snmp -- %{name}-snmp < 4:5.0.4-9.1
[ ! -x %{_sbindir}/php-module-install ] || %{_sbindir}/php-module-install remove snmp %{_sysconfdir}/php.ini

%triggerun soap -- %{name}-soap < 4:5.0.4-9.1
[ ! -x %{_sbindir}/php-module-install ] || %{_sbindir}/php-module-install remove soap %{_sysconfdir}/php.ini

%triggerun sockets -- %{name}-sockets < 4:5.0.4-9.1
[ ! -x %{_sbindir}/php-module-install ] || %{_sbindir}/php-module-install remove sockets %{_sysconfdir}/php.ini

%triggerun sqlite -- %{name}-sqlite < 4:5.0.4-9.1
[ ! -x %{_sbindir}/php-module-install ] || %{_sbindir}/php-module-install remove sqlite %{_sysconfdir}/php.ini

%triggerun sybase -- %{name}-sybase < 4:5.0.4-9.1
[ ! -x %{_sbindir}/php-module-install ] || %{_sbindir}/php-module-install remove sybase %{_sysconfdir}/php.ini

%triggerun sybase-ct -- %{name}-sybase-ct < 4:5.0.4-9.1
[ ! -x %{_sbindir}/php-module-install ] || %{_sbindir}/php-module-install remove sybase-ct %{_sysconfdir}/php.ini

%triggerun sysvmsg -- %{name}-sysvmsg < 4:5.0.4-9.1
[ ! -x %{_sbindir}/php-module-install ] || %{_sbindir}/php-module-install remove sysvmsg %{_sysconfdir}/php.ini

%triggerun sysvsem -- %{name}-sysvsem < 4:5.0.4-9.1
[ ! -x %{_sbindir}/php-module-install ] || %{_sbindir}/php-module-install remove sysvsem %{_sysconfdir}/php.ini

%triggerun sysvshm -- %{name}-sysvshm < 4:5.0.4-9.1
[ ! -x %{_sbindir}/php-module-install ] || %{_sbindir}/php-module-install remove sysvshm %{_sysconfdir}/php.ini

%triggerun tidy -- %{name}-tidy < 4:5.0.4-9.1
[ ! -x %{_sbindir}/php-module-install ] || %{_sbindir}/php-module-install remove tidy %{_sysconfdir}/php.ini

%triggerun wddx -- %{name}-wddx < 4:5.0.4-9.1
[ ! -x %{_sbindir}/php-module-install ] || %{_sbindir}/php-module-install remove wddx %{_sysconfdir}/php.ini

%triggerun xml -- %{name}-xml < 4:5.0.4-9.1
[ ! -x %{_sbindir}/php-module-install ] || %{_sbindir}/php-module-install remove xml %{_sysconfdir}/php.ini

%triggerun xmlrpc -- %{name}-xmlrpc < 4:5.0.4-9.1
[ ! -x %{_sbindir}/php-module-install ] || %{_sbindir}/php-module-install remove xmlrpc %{_sysconfdir}/php.ini

%triggerun xsl -- %{name}-xsl < 4:5.0.4-9.1
[ ! -x %{_sbindir}/php-module-install ] || %{_sbindir}/php-module-install remove xsl %{_sysconfdir}/php.ini

%triggerun zlib -- %{name}-zlib < 4:5.0.4-9.1
[ ! -x %{_sbindir}/php-module-install ] || %{_sbindir}/php-module-install remove zlib %{_sysconfdir}/php.ini

%if %{with apache1}
%files -n apache1-mod_php
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/apache/conf.d/*_mod_php.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/php-apache.ini
%attr(755,root,root) %{_libdir}/apache1/libphp5.so
/home/services/apache/icons/*
%endif

%if %{with apache2}
%files -n apache-mod_php
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/httpd/httpd.conf/*_mod_php.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/php-apache2handler.ini
%attr(755,root,root) %{_libdir}/apache/libphp5.so
/home/services/httpd/icons/*
%endif

%if %{with fcgi}
%files fcgi
%defattr(644,root,root,755)
%doc sapi/cgi/README.FastCGI
%attr(755,root,root) %{_bindir}/php.fcgi
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/php-cgi-fcgi.ini
%endif

%files cgi
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/php.cgi
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/php-cgi.ini

%files cli
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/php.cli
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/php-cli.ini
%{_mandir}/man1/php.1*
%{_mandir}/man1/php.cli.1*

%files program
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/php

%files common
%defattr(644,root,root,755)
%doc php.ini-*
%doc CREDITS Zend/ZEND_CHANGES
%doc LICENSE Zend/LICENSE.Zend EXTENSIONS NEWS TODO*

%dir %{_sysconfdir}
%dir %{_sysconfdir}/conf.d
%attr(644,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/php.ini
%attr(770,root,http) %dir %verify(not group mode) /var/run/php
%attr(755,root,root) %{_sbindir}/php-module-install
%attr(755,root,root) %{_libdir}/libphp_common-*.so
%dir %{extensionsdir}
%dir %{_phpsharedir}

%files devel
%defattr(644,root,root,755)
%doc README.UNIX-BUILD-SYSTEM
%doc README.EXT_SKEL README.SELF-CONTAINED-EXTENSIONS
%doc CODING_STANDARDS
%attr(755,root,root) %{_bindir}/phpextdist
%attr(755,root,root) %{_bindir}/phpize
%attr(755,root,root) %{_bindir}/php-config
%attr(755,root,root) %{_libdir}/libphp_common.so
%{_libdir}/libphp_common.la
%{_includedir}/php
%{_libdir}/php/build
%{_mandir}/man1/*

%files bcmath
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/bcmath.ini
%attr(755,root,root) %{extensionsdir}/bcmath.so

%files bzip2
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/bz2.ini
%attr(755,root,root) %{extensionsdir}/bz2.so

%files calendar
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/calendar.ini
%attr(755,root,root) %{extensionsdir}/calendar.so

%files ctype
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/ctype.ini
%attr(755,root,root) %{extensionsdir}/ctype.so

%if %{with curl}
%files curl
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/curl.ini
%attr(755,root,root) %{extensionsdir}/curl.so
%endif

%files dba
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/dba.ini
%attr(755,root,root) %{extensionsdir}/dba.so

%files dbase
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/dbase.ini
%attr(755,root,root) %{extensionsdir}/dbase.so

%files dom
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/dom.ini
%attr(755,root,root) %{extensionsdir}/dom.so

%if %{with fdf}
%files fdf
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/fdf.ini
%attr(755,root,root) %{extensionsdir}/fdf.so
%endif

%files exif
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/exif.ini
%attr(755,root,root) %{extensionsdir}/exif.so

%files filepro
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/filepro.ini
%attr(755,root,root) %{extensionsdir}/filepro.so

%files ftp
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/ftp.ini
%attr(755,root,root) %{extensionsdir}/ftp.so

%files gd
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/gd.ini
%attr(755,root,root) %{extensionsdir}/gd.so

%files gettext
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/gettext.ini
%attr(755,root,root) %{extensionsdir}/gettext.so

%files gmp
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/gmp.ini
%attr(755,root,root) %{extensionsdir}/gmp.so

%if %{with hwapi}
%files hwapi
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/hwapi.ini
%attr(755,root,root) %{extensionsdir}/hwapi.so
%endif

%files iconv
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/iconv.ini
%attr(755,root,root) %{extensionsdir}/iconv.so

%if %{with imap}
%files imap
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/imap.ini
%attr(755,root,root) %{extensionsdir}/imap.so
%endif

%if %{with interbase}
%files interbase
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/interbase.ini
%attr(755,root,root) %{extensionsdir}/interbase.so
%endif

%if %{with ldap}
%files ldap
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/ldap.ini
%attr(755,root,root) %{extensionsdir}/ldap.so
%endif

%files mbstring
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/mbstring.ini
%attr(755,root,root) %{extensionsdir}/mbstring.so

%files mcrypt
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/mcrypt.ini
%attr(755,root,root) %{extensionsdir}/mcrypt.so

%if %{with mhash}
%files mhash
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/mhash.ini
%attr(755,root,root) %{extensionsdir}/mhash.so
%endif

%if %{with mime_magic}
%files mime_magic
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/mime_magic.ini
%attr(755,root,root) %{extensionsdir}/mime_magic.so
%endif

%if %{with ming}
%files ming
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/ming.ini
%attr(755,root,root) %{extensionsdir}/ming.so
%endif

%if %{with msession}
%files msession
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/msession.ini
%attr(755,root,root) %{extensionsdir}/msession.so
%endif

%if %{with mssql}
%files mssql
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/mssql.ini
%attr(755,root,root) %{extensionsdir}/mssql.so
%endif

%files mysql
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/mysql.ini
%attr(755,root,root) %{extensionsdir}/mysql.so

%if %{with mysqli}
%files mysqli
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/mysqli.ini
%attr(755,root,root) %{extensionsdir}/mysqli.so
%endif

%files ncurses
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/ncurses.so

%if %{with oci8}
%files oci8
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/oci8.ini
%attr(755,root,root) %{extensionsdir}/oci8.so
%endif

%if %{with odbc}
%files odbc
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/odbc.ini
%attr(755,root,root) %{extensionsdir}/odbc.so
%endif

%if %{with openssl}
%files openssl
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/openssl.ini
%attr(755,root,root) %{extensionsdir}/openssl.so
%endif

%files pcntl
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/pcntl.so

%if %{with pcre}
%files pcre
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/pcre.ini
%attr(755,root,root) %{extensionsdir}/pcre.so
%endif

%files pdo
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/pdo.ini
%attr(755,root,root) %{extensionsdir}/pdo.so

%if %{with mssql} || %{with sybase} || %{with sybase_ct}
%files pdo-dblib
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/pdo_dblib.ini
%attr(755,root,root) %{extensionsdir}/pdo_dblib.so
%endif

%files pdo-mysql
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/pdo_mysql.ini
%attr(755,root,root) %{extensionsdir}/pdo_mysql.so

%if %{with oci8}
%files pdo-oci
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/pdo_oci.ini
%attr(755,root,root) %{extensionsdir}/pdo_oci.so
%endif

%if %{with odbc}
%files pdo-odbc
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/pdo_odbc.ini
%attr(755,root,root) %{extensionsdir}/pdo_odbc.so
%endif

%if %{with pgsql}
%files pdo-pgsql
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/pdo_pgsql.ini
%attr(755,root,root) %{extensionsdir}/pdo_pgsql.so
%endif

%if %{with sqlite}
%files pdo-sqlite
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/pdo_sqlite.ini
%attr(755,root,root) %{extensionsdir}/pdo_sqlite.so
%endif

%if %{with pgsql}
%files pgsql
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/pgsql.ini
%attr(755,root,root) %{extensionsdir}/pgsql.so
%endif

%files posix
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/posix.ini
%attr(755,root,root) %{extensionsdir}/posix.so

%if %{with pspell}
%files pspell
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/pspell.ini
%attr(755,root,root) %{extensionsdir}/pspell.so
%endif

%files readline
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/readline.so

%if %{with recode}
%files recode
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/recode.ini
%attr(755,root,root) %{extensionsdir}/recode.so
%endif

# session_mm doesn't work with shared session
#%files session
#%defattr(644,root,root,755)
#%attr(755,root,root) %{extensionsdir}/session.so

%if 0
# simplexml is needed by spl, and spl can't be built shared as of now (5.1.0RC3)
%files simplexml
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/simplexml.ini
%attr(755,root,root) %{extensionsdir}/simplexml.so
%endif

%files shmop
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/shmop.ini
%attr(755,root,root) %{extensionsdir}/shmop.so

%if %{with snmp}
%files snmp
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/snmp.ini
%attr(755,root,root) %{extensionsdir}/snmp.so
%endif

%files soap
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/soap.ini
%attr(755,root,root) %{extensionsdir}/soap.so

%files sockets
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/sockets.ini
%attr(755,root,root) %{extensionsdir}/sockets.so

%if %{with sqlite}
%files sqlite
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/sqlite.ini
%attr(755,root,root) %{extensionsdir}/sqlite.so
%endif

%if %{with sybase}
%files sybase
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/sybase.ini
%attr(755,root,root) %{extensionsdir}/sybase.so
%endif

%if %{with sybase_ct}
%files sybase-ct
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/sybase_ct.ini
%attr(755,root,root) %{extensionsdir}/sybase_ct.so
%endif

%files sysvmsg
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/sysvmsg.ini
%attr(755,root,root) %{extensionsdir}/sysvmsg.so

%files sysvsem
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/sysvsem.ini
%attr(755,root,root) %{extensionsdir}/sysvsem.so

%files sysvshm
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/sysvshm.ini
%attr(755,root,root) %{extensionsdir}/sysvshm.so

%if %{with tidy}
%files tidy
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/tidy.ini
%attr(755,root,root) %{extensionsdir}/tidy.so
%endif

%files tokenizer
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/tokenizer.ini
%attr(755,root,root) %{extensionsdir}/tokenizer.so

%if %{with wddx}
%files wddx
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*wddx.ini
%attr(755,root,root) %{extensionsdir}/wddx.so
%endif

%files xml
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/xml.ini
%attr(755,root,root) %{extensionsdir}/xml.so

%files xmlreader
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/xmlreader.ini
%attr(755,root,root) %{extensionsdir}/xmlreader.so

%if %{with xmlrpc}
%files xmlrpc
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/xmlrpc.ini
%attr(755,root,root) %{extensionsdir}/xmlrpc.so
%endif

%files xsl
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/xsl.ini
%attr(755,root,root) %{extensionsdir}/xsl.so

%files zlib
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/zlib.ini
%attr(755,root,root) %{extensionsdir}/zlib.so
