# TODO
# - fix -threads-acfix.patch
# - deal with modules removed from php and not moved to PECL, still not obsoleted anywhere
#   - removed from php 5.0 (currently in php4):
#   db, hyperwave, java, mcal, overload, qtdom
#   - removed from php 5.1:
#   cpdf, fam, oracle
#   - removed from php 5.2:
#   filepro, hw
# - mime_magic can't handle new "string/*" entries in magic.mime
#   thus doesn't work with system magic.mime database
# - make additional headers and checking added by mail patch configurable
# - apply -hardened patch by default ?
# - modularize session, standard (output from pure php -m)?
#
# Conditional build:
%bcond_with	fdf		# with FDF (PDF forms) module		(BR: proprietary lib)
%bcond_with	hardening	# build with hardening patch applied (http://www.hardened-php.net/)
%bcond_with	interbase_inst	# use InterBase install., not Firebird	(BR: proprietary libs)
%bcond_with	oci8		# with Oracle oci8 extension module	(BR: proprietary libs)
%bcond_without	curl		# without CURL extension module
%bcond_without	filter		# without filter extension module
%bcond_without	imap		# without IMAP extension module
%bcond_without	interbase	# without InterBase extension module
%bcond_without	ldap		# without LDAP extension module
%bcond_without	mhash		# without mhash extension module
%bcond_without	mime_magic	# without mime-magic module
%bcond_without	ming		# without ming extension module
%bcond_without	mm		# without mm support for session storage
%bcond_without	mssql		# without MS SQL extension module
%bcond_without	mysqli		# without mysqli support (Requires mysql > 4.1)
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
%bcond_with	versioning	# build with experimental versioning (to load php4/php5 into same apache)

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

# filter depends on pcre
%if %{without pcre}
%undefine	with_filter
%endif

%define	_rel 6
Summary:	PHP: Hypertext Preprocessor
Summary(fr):	Le langage de script embarque-HTML PHP
Summary(pl):	Jêzyk skryptowy PHP
Summary(pt_BR):	A linguagem de script PHP
Summary(ru):	PHP ÷ÅÒÓÉÉ 5 - ÑÚÙË ÐÒÅÐÒÏÃÅÓÓÉÒÏ×ÁÎÉÑ HTML-ÆÁÊÌÏ×, ×ÙÐÏÌÎÑÅÍÙÊ ÎÁ ÓÅÒ×ÅÒÅ
Summary(uk):	PHP ÷ÅÒÓ¦§ 5 - ÍÏ×Á ÐÒÅÐÒÏÃÅÓÕ×ÁÎÎÑ HTML-ÆÁÊÌ¦×, ×ÉËÏÎÕ×ÁÎÁ ÎÁ ÓÅÒ×ÅÒ¦
Name:		php
Version:	5.2.1
Release:	%{_rel}%{?with_hardening:hardened}
Epoch:		4.5
License:	PHP
Group:		Libraries
Source0:	http://www.php.net/distributions/%{name}-%{version}.tar.bz2
# Source0-md5:	261218e3569a777dbd87c16a15f05c8d
Source2:	zend.gif
Source3:	%{name}-mod_%{name}.conf
Source4:	%{name}-cgi-fcgi.ini
Source5:	%{name}-cgi.ini
Source6:	%{name}-apache.ini
Source7:	%{name}-cli.ini
Source8:	http://www.hardened-php.net/hardening-patch-5.0.4-0.3.0.patch.gz
# Source8-md5:	47a742fa9fab2826ad10c13a2376111a
# Taken from: http://browsers.garykeith.com/downloads.asp
Source9:	%{name}_browscap.ini
Patch0:		%{name}-shared.patch
Patch1:		%{name}-pldlogo.patch
Patch2:		%{name}-mail.patch
Patch3:		%{name}-link-libs.patch
Patch4:		%{name}-libpq_fs_h_path.patch
Patch5:		%{name}-filter-shared.patch
Patch6:		%{name}-build_modules.patch
Patch7:		%{name}-sapi-ini-file.patch
Patch8:		%{name}-no-metaccld.patch
Patch9:		%{name}-sh.patch
Patch10:	%{name}-ini.patch
Patch11:	%{name}-acam.patch
#Patch15:	%{name}-threads-acfix.patch
Patch16:	%{name}-tsrmlsfetchgcc2.patch
Patch17:	%{name}-no_pear_install.patch
Patch18:	%{name}-zlib.patch
Patch19:	%{name}-sybase-fix.patch
Patch20:	%{name}-readline.patch
Patch21:	%{name}-nohttpd.patch
Patch23:	%{name}-gd_imagerotate_enable.patch
Patch24:	%{name}-uint32_t.patch
Patch26:	%{name}-dba-link.patch
Patch30:	%{name}-hardening-fix.patch
Patch31:	%{name}-both-apxs.patch
Patch32:	%{name}-builddir.patch
Patch33:	%{name}-zlib-for-getimagesize.patch
Patch35:	%{name}-versioning.patch
Patch36:	%{name}-linkflags-clean.patch

Patch39:	%{name}-pear.patch
Patch41:	%{name}-config-dir.patch
# Security patches:
Patch100:	%{name}-5.1.6-CVE-2007-0455.patch
Patch101:	%{name}-5.1.6-CVE-2007-1001.patch
Patch102:	%{name}-5.1.6-CVE-2007-1583.patch
Patch103:	%{name}-5.1.6-CVE-2007-1718.patch
URL:		http://www.php.net/
%{?with_interbase:%{!?with_interbase_inst:BuildRequires:	Firebird-devel >= 1.0.2.908-2}}
%{?with_pspell:BuildRequires:	aspell-devel >= 2:0.50.0}
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake >= 1.4d
BuildRequires:	bison
BuildRequires:	bzip2-devel
%{?with_curl:BuildRequires:	curl-devel >= 7.12.0}
BuildRequires:	cyrus-sasl-devel
BuildRequires:	db-devel >= 4.0
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
BuildRequires:	gd-devel(imagerotate) = 5.2.0
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
BuildRequires:	libxslt-devel >= 1.1.0
%{?with_mhash:BuildRequires:	mhash-devel}
%{?with_ming:BuildRequires:	ming-devel >= 0.3}
%{?with_mm:BuildRequires:	mm-devel >= 1.3.0}
BuildRequires:	mysql-devel >= 4.0.0
%{?with_mysqli:BuildRequires:	mysql-devel >= 4.1.0}
BuildRequires:	ncurses-ext-devel
%{?with_ldap:BuildRequires:	openldap-devel >= 2.3.0}
%if %{with openssl} || %{with ldap}
BuildRequires:	openssl-devel >= 0.9.7d
%endif
%{?with_snmp:BuildRequires:	net-snmp-devel >= 5.0.7}
BuildRequires:	pam-devel
%{?with_pcre:BuildRequires:	pcre-devel >= 6.6}
%{?with_pgsql:BuildRequires:	postgresql-backend-devel >= 7.2}
%{?with_pgsql:BuildRequires:	postgresql-devel}
BuildRequires:	readline-devel
%{?with_recode:BuildRequires:	recode-devel >= 3.5d-3}
BuildRequires:	rpm-build >= 4.4.0
BuildRequires:	rpmbuild(macros) >= 1.238
%{?with_sqlite:BuildRequires:	sqlite-devel}
%{?with_sqlite:BuildRequires:	sqlite3-devel}
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

%define		php_sysconfdir		/etc/php
%define		php_extensiondir	%{_libdir}/php
%define		_sysconfdir		%{php_sysconfdir}

# must be in sync with source. extra check ensuring that it is so is done in %%build
%define		php_api_version		20041225
%define		zend_module_api		20060613
%define		zend_extension_api	220060519
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
version %{version}.

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
%{version}.

%description -l pl
PHP jest jêzykiem skryptowym, którego polecenia umieszcza siê w
plikach HTML. Jest prób± u³atwienia programistom pisania dynamicznie
generowanych stron WWW. Oferuje tak¿e wbudowan± integracjê z bazami
danych dla kilku komercyjnych i niekomercyjnych systemów baz danych,
co czyni tworzenie stron korzystaj±cych z baz danych w miarê ³atwym.
Najczê¶ciej PHP jest u¿ywany prawdopodobnie jako zamiennik skryptów
CGI. Modu³ mod_php pozwala serwerowi WWW Apache rozumieæ i przetwarzaæ
jêzyk PHP osadzony w stronach. Ten pakiet zawiera php w wersji
%{version}.

%description -l pt_BR
PHP: Preprocessador de Hipertexto versão 4 é uma linguagem script
embutida em HTML. Muito de sua sintaxe é emprestada de C, Java e Perl,
com algumas características únicas, específicas ao PHP. O objetivo da
linguagem é permitir que desenvolvedores web escrevam páginas
dinamicamente geradas de forma rápida.

%description -l ru
PHP - ÜÔÏ ÑÚÙË ÎÁÐÉÓÁÎÉÑ ÓËÒÉÐÔÏ×, ×ÓÔÒÁÉ×ÁÅÍÙÈ × HTML-ËÏÄ. PHP
ÐÒÅÄÌÁÇÁÅÔ ÉÎÔÅÒÇÒÁÃÉÀ Ó ÍÎÏÖÅÓÔ×ÏÍ óõâä, ÐÏÜÔÏÍÕ ÎÁÐÉÓÁÎÉÅ ÓËÒÉÐÔÏ×
ÄÌÑ ÒÁÂÏÔÙ Ó ÂÁÚÁÍÉ ÄÁÎÎÙÈ ÏÔÎÏÓÉÔÅÌØÎÏ ÐÒÏÓÔÏ. îÁÉÂÏÌÅÅ ÐÏÐÕÌÑÒÎÏÅ
ÉÓÐÏÌØÚÏ×ÁÎÉÅ PHP - ÚÁÍÅÎÁ ÄÌÑ CGI ÓËÒÉÐÔÏ×.

üÔÏÔ ÐÁËÅÔ ÓÏÄÅÒÖÉÔ ÓÁÍÏÄÏÓÔÁÔÏÞÎÕÀ (CGI) ×ÅÒÓÉÀ ÉÎÔÅÒÐÒÅÔÁÔÏÒÁ ÑÚÙËÁ.
÷Ù ÄÏÌÖÎÙ ÔÁËÖÅ ÕÓÔÁÎÏ×ÉÔØ ÐÁËÅÔ %{name}-common. åÓÌÉ ×ÁÍ ÎÕÖÅÎ
ÉÎÔÅÒÐÒÅÔÁÔÏÒ PHP × ËÁÞÅÓÔ×Å ÍÏÄÕÌÑ apache, ÕÓÔÁÎÏ×ÉÔÅ ÐÁËÅÔ
apache-mod_php.

%description -l uk
PHP - ÃÅ ÍÏ×Á ÎÁÐÉÓÁÎÎÑ ÓËÒÉÐÔ¦×, ÝÏ ×ÂÕÄÏ×ÕÀÔØÓÑ × HTML-ËÏÄ. PHP
ÐÒÏÐÏÎÕ¤ ¦ÎÔÅÇÒÁÃ¦À Ú ÂÁÇÁÔØÍÁ óõâä, ÔÏÍÕ ÎÁÐÉÓÁÎÎÑ ÓËÒÉÐÔ¦× ÄÌÑ
ÒÏÂÏÔÉ Ú ÂÁÚÁÍÉ ÄÁÎÉÈ ¤ ÄÏ×ÏÌ¦ ÐÒÏÓÔÉÍ. îÁÊÂ¦ÌØÛ ÐÏÐÕÌÑÒÎÅ
×ÉËÏÒÉÓÔÁÎÎÑ PHP - ÚÁÍ¦ÎÁ ÄÌÑ CGI ÓËÒÉÐÔ¦×.

ãÅÊ ÐÁËÅÔ Í¦ÓÔÉÔØ ÓÁÍÏÄÏÓÔÁÔÎÀ (CGI) ×ÅÒÓ¦À ¦ÎÔÅÒÐÒÅÔÁÔÏÒÁ ÍÏ×É. ÷É
ÍÁ¤ÔÅ ÔÁËÏÖ ×ÓÔÁÎÏ×ÉÔÉ ÐÁËÅÔ %{name}-common. ñËÝÏ ×ÁÍ ÐÏÔÒ¦ÂÅÎ
¦ÎÔÅÒÐÒÅÔÁÔÏÒ PHP × ÑËÏÓÔ¦ ÍÏÄÕÌÑ apache, ×ÓÔÁÎÏ×¦ÔØ ÐÁËÅÔ
apache-mod_php.

%package -n apache1-mod_php
Summary:	PHP DSO module for apache 1.3.x
Summary(pl):	Modu³ DSO (Dynamic Shared Object) php dla apache 1.3.x
Group:		Development/Languages/PHP
Requires(triggerpostun):	sed >= 4.0
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	apache1(EAPI) >= 1.3.33-2
Requires:	apache1-mod_mime
Provides:	webserver(php) = %{version}
Obsoletes:	apache-mod_php < 1:4.1.1
Obsoletes:	phpfi

%description -n apache1-mod_php
PHP as DSO module for apache 1.3.x.

%description -n apache1-mod_php -l pl
php jako modu³ DSO (Dynamic Shared Object) dla apache 1.3.x.

%package -n apache-mod_php
Summary:	PHP DSO module for apache 2.x
Summary(pl):	Modu³ DSO (Dynamic Shared Object) php dla apache 2.x
Group:		Development/Languages/PHP
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	apache(modules-api) = %{apache_modules_api}
Requires:	apache-mod_mime
Provides:	webserver(php) = %{version}
Obsoletes:	phpfi

%description -n apache-mod_php
PHP as DSO module for apache 2.x.

%description -n apache-mod_php -l pl
php jako modu³ DSO (Dynamic Shared Object) dla apache 2.x.

%package fcgi
Summary:	php as FastCGI program
Summary(pl):	php jako program FastCGI
Group:		Development/Languages/PHP
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	webserver(php) = %{version}

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
Summary(pl):	php jako interpreter dzia³aj±cy z linii poleceñ
Group:		Development/Languages/PHP
Requires:	%{name}-common = %{epoch}:%{version}-%{release}

%description cli
php as CLI interpreter.

%description cli -l pl
php jako interpreter dzia³aj±cy z linii poleceñ.

%package program
Summary:	/usr/bin/php symlink
Summary(pl):	Dowi±zanie symboliczne /usr/bin/php
Group:		Development/Languages/PHP
Requires:	%{name}-cli = %{epoch}:%{version}-%{release}
Obsoletes:	/usr/bin/php

%description program
Package providing /usr/bin/php symlink to PHP CLI.

%description program -l pl
Pakiet dostarczaj±cy dowi±zanie symboliczne /usr/bin/php do PHP CLI.

%package common
Summary:	Common files needed by both apache module and CGI
Summary(pl):	Wspólne pliki dla modu³u apache'a i programu CGI
Summary(ru):	òÁÚÄÅÌÑÅÍÙÅ ÂÉÂÌÉÏÔÅËÉ ÄÌÑ php
Summary(uk):	â¦ÂÌ¦ÏÔÅËÉ ÓÐ¦ÌØÎÏÇÏ ×ÉËÏÒÉÓÔÁÎÎÑ ÄÌÑ php
Group:		Libraries
# because of dlclose() bugs in glibc <= 2.3.4 causing SEGVs on exit
Requires:	glibc >= 6:2.3.5
Requires:	php-dirs
Provides:	php(date)
Provides:	php(libxml)
Provides:	php(modules_api) = %{php_api_version}
Provides:	php(overload)
%{?with_pcre:Provides:	php(pcre)}
Provides:	php(reflection)
Provides:	php(session)
Provides:	php(simplexml)
Provides:	php(spl)
Provides:	php(standard)
Provides:	php(zend_extension_api) = %{zend_extension_api}
Provides:	php(zend_module_api) = %{zend_module_api}
Provides:	php5(debug) = %{php_debug}
Provides:	php5(thread-safety) = %{zend_zts}
Obsoletes:	php-pcre < 4:5.2.0
Obsoletes:	php-pecl-domxml
Obsoletes:	php-session < 3:4.2.1-2
Conflicts:	php4-common < 3:4.4.4-8
Conflicts:	rpm < 4.4.2-0.2

%description common
Common files needed by both apache module and CGI.

%description common -l pl
Wspólne pliki dla modu³u apacha i programu CGI.

%description common -l ru
üÔÏÔ ÐÁËÅÔ ÓÏÄÅÒÖÉÔ ÏÂÝÉÅ ÆÁÊÌÙ ÄÌÑ ÒÁÚÎÙÈ ×ÁÒÉÁÎÔÏ× ÒÅÁÌÉÚÁÃÉÉ PHP
(ÓÁÍÏÄÏÓÔÁÔÏÞÎÏÊ É × ËÁÞÅÓÔ×Å ÍÏÄÕÌÑ apache).

%description common -l uk
ãÅÊ ÐÁËÅÔ Í¦ÓÔÉÔØ ÓÐ¦ÌØÎ¦ ÆÁÊÌÉ ÄÌÑ Ò¦ÚÎÉÈ ×ÁÒ¦ÁÎÔ¦× ÒÅÁÌ¦ÚÁÃ¦§ PHP
(ÓÁÍÏÄÏÓÔÁÔÎØÏ§ ÔÁ × ÑËÏÓÔ¦ ÍÏÄÕÌÑ apache).

%package devel
Summary:	Files for PHP modules development
Summary(pl):	Pliki do kompilacji modu³ów PHP
Summary(pt_BR):	Arquivos de desenvolvimento para PHP
Summary(ru):	ðÁËÅÔ ÒÁÚÒÁÂÏÔËÉ ÄÌÑ ÐÏÓÔÒÏÅÎÉÑ ÒÁÓÛÉÒÅÎÉÊ PHP
Summary(uk):	ðÁËÅÔ ÒÏÚÒÏÂËÉ ÄÌÑ ÐÏÂÕÄÏ×É ÒÏÚÛÉÒÅÎØ PHP
Group:		Development/Languages/PHP
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	autoconf
Requires:	automake
Requires:	libtool
Requires:	pcre-devel
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
Ten pakiet zawiera pliki potrzebne do kompilacji modu³ów PHP. Zamiast
rekompilowaæ ca³e php aby dodaæ obs³ugê np. oracle, mo¿na przy u¿yciu
tego pakietu skompilowaæ samodzielne rozszerzenie. Wiêcej informacji o
samodzielnych rozszerzeniach mo¿na znale¼æ w pliku
README.SELF-CONTAINED-EXTENSIONS.

%description devel -l pt_BR
Este pacote contém arquivos usados no desenvolvimento de programas ou
módulos PHP.

%description devel -l ru
ðÁËÅÔ php-devel ÄÁÅÔ ×ÏÚÍÏÖÎÏÓÔØ ËÏÍÐÉÌÉÒÏ×ÁÔØ ÄÉÎÁÍÉÞÅÓËÉÅ ÒÁÓÛÉÒÅÎÉÑ
PHP. ðÁËÅÔ ×ËÌÀÞÁÅÔ ÉÓÈÏÄÎÙÊ ËÏÄ ÜÔÉÈ ÒÁÓÛÉÒÅÎÉÊ. ÷ÍÅÓÔÏ ÐÏ×ÔÏÒÎÏÊ
ËÏÍÐÉÌÑÃÉÉ ÂÉÎÁÒÎÏÇÏ ÆÁÊÌÁ php ÄÌÑ ÄÏÂÁ×ÌÅÎÉÑ, ÎÁÐÒÉÍÅÒ, ÐÏÄÄÅÒÖËÉ
oracle, ÕÓÔÁÎÏ×ÉÔÅ ÜÔÏÔ ÐÁËÅÔ ÄÌÑ ËÏÍÐÉÌÉÒÏ×ÁÎÉÑ ÏÔÄÅÌØÎÙÈ ÒÁÓÛÉÒÅÎÉÊ.
ðÏÄÒÏÂÎÏÓÔÉ - × ÆÁÊÌÅ README.SELF-CONTAINED-EXTENSIONS.

%description devel -l uk
ðÁËÅÔ php-devel ÄÁ¤ ÍÏÖÌÉ×¦ÓÔØ ËÏÍÐ¦ÌÀ×ÁÔÉ ÄÉÎÁÍ¦ÞÎ¦ ÒÏÚÛÉÒÅÎÎÑ PHP.
äÏ ÐÁËÅÔÕ ×ËÌÀÞÅÎÏ ×ÉÈ¦ÄÎÉÊ ËÏÄ ÄÌÑ ÒÏÚÛÉÒÅÎØ. úÁÍ¦ÓÔØ ÐÏ×ÔÏÒÎÏ§
ËÏÍÐ¦ÌÑÃ¦§ Â¦ÎÁÒÎÏÇÏ ÆÁÊÌÕ php ÄÌÑ ÄÏÄÁÎÎÑ, ÎÁÐÒÉËÌÁÄ, Ð¦ÄÔÒÉÍËÉ
oracle, ×ÓÔÁÎÏ×¦ÔØ ÃÅÊ ÐÁËÅÔ ÄÌÑ ËÏÍÐ¦ÌÑÃ¦§ ÏËÒÅÍÉÈ ÒÏÚÛÉÒÅÎØ.
äÅÔÁÌØÎ¦ÛÁ ¦ÎÆÏÒÍÁÃ¦Ñ - × ÆÁÊÌ¦ README.SELF-CONTAINED-EXTENSIONS.

%package bcmath
Summary:	bcmath extension module for PHP
Summary(pl):	Modu³ bcmath dla PHP
Group:		Libraries
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php(bcmath)

%description bcmath
This is a dynamic shared object (DSO) for PHP that will add bc style
precision math functions support.

%description bcmath -l pl
Modu³ PHP umo¿liwiaj±cy korzystanie z dok³adnych funkcji
matematycznych takich jak w programie bc.

%package bzip2
Summary:	Bzip2 extension module for PHP
Summary(pl):	Modu³ bzip2 dla PHP
Group:		Libraries
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php(bzip2)

%description bzip2
This is a dynamic shared object (DSO) for PHP that will add bzip2
compression support to PHP.

%description bzip2 -l pl
Modu³ PHP umo¿liwiaj±cy u¿ywanie kompresji bzip2.

%package calendar
Summary:	Calendar extension module for PHP
Summary(pl):	Modu³ funkcji kalendarza dla PHP
Group:		Libraries
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php(calendar)

%description calendar
This is a dynamic shared object (DSO) for PHP that will add calendar
support.

%description calendar -l pl
Modu³ PHP dodaj±cy wsparcie dla kalendarza.

%package ctype
Summary:	ctype extension module for PHP
Summary(pl):	Modu³ ctype dla PHP
Group:		Libraries
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php(ctype)

%description ctype
This is a dynamic shared object (DSO) for PHP that will add ctype
support.

%description ctype -l pl
Modu³ PHP umo¿liwiaj±cy korzystanie z funkcji ctype.

%package curl
Summary:	curl extension module for PHP
Summary(pl):	Modu³ curl dla PHP
Group:		Libraries
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php(curl)

%description curl
This is a dynamic shared object (DSO) for PHP that will add curl
support.

%description curl -l pl
Modu³ PHP umo¿liwiaj±cy korzystanie z biblioteki curl.

%package dba
Summary:	DBA extension module for PHP
Summary(pl):	Modu³ DBA dla PHP
Group:		Libraries
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php(dba)

%description dba
This is a dynamic shared object (DSO) for PHP that will add flat-file
databases (DBA) support.

%description dba -l pl
Modu³ dla PHP dodaj±cy obs³ugê dla baz danych opartych na plikach
(DBA).

%package dbase
Summary:	DBase extension module for PHP
Summary(pl):	Modu³ DBase dla PHP
Group:		Libraries
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php(dbase)

%description dbase
This is a dynamic shared object (DSO) for PHP that will add DBase
support.

%description dbase -l pl
Modu³ PHP ze wsparciem dla DBase.

%package dom
Summary:	DOM extension module for PHP
Summary(pl):	Modu³ DOM dla PHP
Group:		Libraries
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php(dom)
# it has some compatibility functions
Provides:	php(domxml)
Obsoletes:	php-domxml <= 3:4.3.8-1

%description dom
This is a dynamic shared object (DSO) for PHP that will add new DOM
support.

%description dom -l pl
Modu³ PHP dodaj±cy now± obs³ugê DOM.

%package exif
Summary:	exif extension module for PHP
Summary(pl):	Modu³ exif dla PHP
Group:		Libraries
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php(exif)

%description exif
This is a dynamic shared object (DSO) for PHP that will add EXIF tags
support in image files.

%description exif -l pl
Modu³ PHP dodaj±cy obs³ugê znaczników EXIF w plikach obrazków.

%package fdf
Summary:	FDF extension module for PHP
Summary(pl):	Modu³ FDF dla PHP
Group:		Libraries
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php(fdf)

%description fdf
This PHP module adds support for PDF Forms through Adobe FDFTK
library.

%description fdf -l pl
Modu³ PHP dodaj±cy obs³ugê formularzy PDF poprzez bibliotekê Adobe
FDFTK.

%package filter
Summary:	Extension for safely dealing with input parameters
Summary(pl):	Rozszerzenie do bezpiecznej obs³ugi danych wej¶ciowych
Group:		Libraries
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php(filter)
Obsoletes:	php-pecl-filter

%description filter
We all know that you should always check input variables, but PHP does
not offer really good functionality for doing this in a safe way. The
Input Filter extension is meant to address this issue by implementing
a set of filters and mechanisms that users can use to safely access
their input data.

%description filter -l pl
Wiadomo, ¿e trzeba zawsze sprawdzaæ zmienne wej¶ciowe, ale PHP nie
oferuje naprawdê dobrej funkcjonalno¶ci do robienia tego w sposób
bezpieczny. Rozszerzenie Input Filter ma rozwi±zaæ ten problem poprzez
zaimplementowanie zestawu filtrów i mechanizmów, których u¿ytkownicy
mog± bezpiecznie u¿ywaæ do dostêpu do danych.

%package ftp
Summary:	FTP extension module for PHP
Summary(pl):	Modu³ FTP dla PHP
Group:		Libraries
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php(ftp)

%description ftp
This is a dynamic shared object (DSO) for PHP that will add FTP
support.

%description ftp -l pl
Modu³ PHP dodaj±cy obs³ugê protoko³u FTP.

%package gd
Summary:	GD extension module for PHP
Summary(pl):	Modu³ GD dla PHP
Group:		Libraries
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	gd >= 2.0.28-4
Requires:	gd(gif)
Requires:	gd(imagerotate) = 5.2.0
Provides:	php(gd)

%description gd
This is a dynamic shared object (DSO) for PHP that will add GD
support, allowing you to create and manipulate images with PHP.

%description gd -l pl
Modu³ PHP umo¿liwiaj±cy korzystanie z biblioteki GD, pozwalaj±cej na
tworzenie i obróbkê obrazków.

%package gettext
Summary:	gettext extension module for PHP
Summary(pl):	Modu³ gettext dla PHP
Group:		Libraries
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php(gettext)

%description gettext
This is a dynamic shared object (DSO) for PHP that will add gettext
support.

%description gettext -l pl
Modu³ PHP dodaj±cy obs³ugê lokalizacji przez gettext.

%package gmp
Summary:	gmp extension module for PHP
Summary(pl):	Modu³ gmp dla PHP
Group:		Libraries
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php(gmp)

%description gmp
This is a dynamic shared object (DSO) for PHP that will add arbitrary
length number support with GNU MP library.

%description gmp -l pl
Modu³ PHP umo¿liwiaj±cy korzystanie z biblioteki gmp do obliczeñ na
liczbach o dowolnej d³ugo¶ci.

%package hash
Summary:	HASH Message Digest Framework
Summary(pl):	Szkielet do obliczania skrótów wiadomo¶ci
Group:		Libraries
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php(hash)
Obsoletes:	php-pecl-hash

%description hash
Native implementations of common message digest algorithms using a
generic factory method.

%description hash -l pl
Natywne implementacje popularnych algorytmów obliczania skrótów
wiadomo¶ci przy u¿yciu wspólnego interfejsu.

%package iconv
Summary:	iconv extension module for PHP
Summary(pl):	Modu³ iconv dla PHP
Group:		Libraries
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php(iconv)

%description iconv
This is a dynamic shared object (DSO) for PHP that will add iconv
support.

%description iconv -l pl
Modu³ PHP dodaj±cy obs³ugê iconv.

%package imap
Summary:	IMAP extension module for PHP
Summary(pl):	Modu³ IMAP dla PHP
Summary(pt_BR):	Um módulo para aplicações PHP que usam IMAP
Group:		Libraries
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php(imap)

%description imap
This is a dynamic shared object (DSO) for PHP that will add IMAP
support.

%description imap -l pl
Modu³ PHP dodaj±cy obs³ugê skrzynek IMAP.

%description imap -l pt_BR
Um módulo para aplicações PHP que usam IMAP.

%package interbase
Summary:	InterBase/Firebird database module for PHP
Summary(pl):	Modu³ bazy danych InterBase/Firebird dla PHP
Group:		Libraries
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php(interbase)
%{?with_interbase_inst:Autoreq:	false}

%description interbase
This is a dynamic shared object (DSO) for PHP that will add InterBase
and Firebird database support.

%description interbase -l pl
Modu³ PHP umo¿liwiaj±cy dostêp do baz danych InterBase i Firebird.

%package json
Summary:	PHP C extension for JSON serialization
Summary(pl):	Rozszerzenie C PHP dla serializacji JSON
Group:		Libraries
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php(json)
Obsoletes:	php-pecl-json

%description json
php-json is an extremely fast PHP C extension for JSON (JavaScript
Object Notation) serialisation.

%description json -l pl
php-json to bardzo szybkie rozszerzenie C PHP dla serializacji JSON
(JavaScript Object Notation).

%package ldap
Summary:	LDAP extension module for PHP
Summary(pl):	Modu³ LDAP dla PHP
Summary(pt_BR):	Um módulo para aplicações PHP que usam LDAP
Group:		Libraries
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php(ldap)

%description ldap
This is a dynamic shared object (DSO) for PHP that will add LDAP
support.

%description ldap -l pl
Modu³ PHP dodaj±cy obs³ugê LDAP.

%description ldap -l pt_BR
Um módulo para aplicações PHP que usam LDAP.

%package mbstring
Summary:	mbstring extension module for PHP
Summary(pl):	Modu³ mbstring dla PHP
Group:		Libraries
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php(mbstring)

%description mbstring
This is a dynamic shared object (DSO) for PHP that will add multibyte
string support.

%description mbstring -l pl
Modu³ PHP dodaj±cy obs³ugê ci±gów znaków wielobajtowych.

%package mcrypt
Summary:	mcrypt extension module for PHP
Summary(pl):	Modu³ mcrypt dla PHP
Group:		Libraries
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php(mcrypt)

%description mcrypt
This is a dynamic shared object (DSO) for PHP that will add mcrypt
support.

%description mcrypt -l pl
Modu³ PHP dodaj±cy mo¿liwo¶æ szyfrowania poprzez bibliotekê mcrypt.

%package mhash
Summary:	mhash extension module for PHP
Summary(pl):	Modu³ mhash dla PHP
Group:		Libraries
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php(mhash)

%description mhash
This is a dynamic shared object (DSO) for PHP that will add mhash
support.

%description mhash -l pl
Modu³ PHP udostêpniaj±cy funkcje mieszaj±ce z biblioteki mhash.

%package mime_magic
Summary:	mime_magic extension module for PHP
Summary(pl):	Modu³ mime_magic dla PHP
Group:		Libraries
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	/usr/share/file/magic.mime
Provides:	php(mime_magic)

%description mime_magic
This PHP module adds support for MIME type lookup via file magic
numbers using magic.mime database.

%description mime_magic -l pl
Modu³ PHP dodaj±cy obs³ugê wyszukiwania typów MIME wed³ug magicznych
znaczników plików z u¿yciem bazy danych magic.mime.

%package ming
Summary:	ming extension module for PHP
Summary(pl):	Modu³ ming dla PHP
Group:		Libraries
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php(ming)

%description ming
This is a dynamic shared object (DSO) for PHP that will add ming
(Flash - .swf files) support.

%description ming -l pl
Modu³ PHP dodaj±cy obs³ugê plików Flash (.swf) poprzez bibliotekê
ming.

%package mssql
Summary:	MS SQL extension module for PHP
Summary(pl):	Modu³ MS SQL dla PHP
Group:		Libraries
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php(mssql)

%description mssql
This is a dynamic shared object (DSO) for PHP that will add MS SQL
databases support through FreeTDS library.

%description mssql -l pl
Modu³ PHP dodaj±cy obs³ugê baz danych MS SQL poprzez bibliotekê
FreeTDS.

%package mysql
Summary:	MySQL database module for PHP
Summary(pl):	Modu³ bazy danych MySQL dla PHP
Summary(pt_BR):	Um módulo para aplicações PHP que usam bancos de dados MySQL
Group:		Libraries
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php(mysql)

%description mysql
This is a dynamic shared object (DSO) for PHP that will add MySQL
database support.

%description mysql -l pl
Modu³ PHP umo¿liwiaj±cy dostêp do bazy danych MySQL.

%description mysql -l pt_BR
Um módulo para aplicações PHP que usam bancos de dados MySQL.

%package mysqli
Summary:	MySQLi module for PHP
Summary(pl):	Modu³ MySQLi dla PHP
Group:		Libraries
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	mysql-libs >= 4.1.0
Provides:	php(mysqli)

%description mysqli
This is a dynamic shared object (DSO) for PHP that will add MySQLi
(Improved MySQL) support. The difference between it and mysql module
is that it provides access to functionality of MySQL 4.1 and above.

%description mysqli -l pl
Modu³ PHP umo¿liwiaj±cy udoskonalony dostêp do bazy danych MySQL.
Ró¿nic± miêdzy nim a modu³em mysql jest dostêp do funkcjonalno¶ci
MySQL w wersji 4.1 i nowszych.

%package ncurses
Summary:	ncurses module for PHP
Summary(pl):	Modu³ ncurses dla PHP
Group:		Libraries
Requires:	%{name}-cli = %{epoch}:%{version}-%{release}
Provides:	php(ncurses)

%description ncurses
This PHP module adds support for ncurses functions (only for cli and
cgi SAPIs).

%description ncurses -l pl
Modu³ PHP dodaj±cy obs³ugê funkcji ncurses (tylko do SAPI cli i cgi).

%package oci8
Summary:	Oracle 8+ database module for PHP
Summary(pl):	Modu³ bazy danych Oracle 8+ dla PHP
Group:		Libraries
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php(oci8)
Autoreq:	false

%description oci8
This is a dynamic shared object (DSO) for PHP that will add Oracle 7,
8, 9 and 10 database support through Oracle8 Call-Interface (OCI8).

%description oci8 -l pl
Modu³ PHP umo¿liwiaj±cy dostêp do bazy danych Oracle 7, 8, 9 i 10
poprzez interfejs Oracle8 Call-Interface (OCI8).

%package odbc
Summary:	ODBC extension module for PHP
Summary(pl):	Modu³ ODBC dla PHP
Summary(pt_BR):	Um módulo para aplicações PHP que usam bases de dados ODBC
Group:		Libraries
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	unixODBC >= 2.1.1-3
Provides:	php(odbc)

%description odbc
This is a dynamic shared object (DSO) for PHP that will add ODBC
support.

%description odbc -l pl
Modu³ PHP ze wsparciem dla ODBC.

%description odbc -l pt_BR
Um módulo para aplicações PHP que usam ODBC.

%package openssl
Summary:	OpenSSL extension module for PHP
Summary(pl):	Modu³ OpenSSL dla PHP
Group:		Libraries
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php(openssl)

%description openssl
This is a dynamic shared object (DSO) for PHP that will add OpenSSL
support.

Warning: this is an experimental module.

%description openssl -l pl
Modu³ PHP umo¿liwiaj±cy korzystanie z biblioteki OpenSSL.

Uwaga: to jest modu³ eksperymentalny.

%package pcntl
Summary:	Process Control extension module for PHP
Summary(pl):	Modu³ Process Control dla PHP
Group:		Libraries
Requires:	%{name}-cli = %{epoch}:%{version}-%{release}
Provides:	php(pcntl)

%description pcntl
This is a dynamic shared object (DSO) for PHP that will add process
spawning and control support. It supports functions like fork(),
waitpid(), signal() etc.

Warning: this is an experimental module. Also, don't use it in
webserver environment!

%description pcntl -l pl
Modu³ PHP umo¿liwiaj±cy tworzenie nowych procesów i kontrolê nad nimi.
Obs³uguje funkcje takie jak fork(), waitpid(), signal() i podobne.

Uwaga: to jest modu³ eksperymentalny. Ponadto nie jest przeznaczony do
u¿ywania z serwerem WWW - nie próbuj tego!

%package pdo
Summary:	PHP Data Objects (PDO)
Summary(pl):	Obs³uga PHP Data Objects (PDO)
Group:		Libraries
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php(pdo)
Obsoletes:	php-pecl-PDO

%description pdo
This is a dynamic shared object (DSO) for PHP that will add PDO
support.

%description pdo -l pl
Modu³ PHP dodaj±cy obs³ugê PDO (PHP Data Objects).

%package pdo-dblib
Summary:	PHP Data Objects (PDO) FreeTDS support
Summary(pl):	Modu³ PHP Data Objects (PDO) z obs³ug± FreeTDS
Group:		Libraries
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-pdo = %{epoch}:%{version}-%{release}
Provides:	php(dblib)

%description pdo-dblib
This is a dynamic shared object (DSO) for PHP that will add PDO
FreeTDS support.

%description pdo-dblib -l pl
Modu³ dla PHP dodaj±cy obs³ugê baz danych FreeTDS za po¶rednictwem
interfejsu PDO.

%package pdo-firebird
Summary:	PHP Data Objects (PDO) Firebird support
Summary(pl):	Modu³ PHP Data Objects (PDO) z obs³ug± Firebirda
Group:		Libraries
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-pdo = %{epoch}:%{version}-%{release}
Provides:	php(pdo-firebird)
Obsoletes:	php-pecl-PDO_FIREBIRD

%description pdo-firebird
This is a dynamic shared object (DSO) for PHP that will add PDO
Firebird support.

%description pdo-firebird -l pl
Modu³ dla PHP dodaj±cy obs³ugê baz danych Firebird za po¶rednictwem
interfejsu PDO.

%package pdo-mysql
Summary:	PHP Data Objects (PDO) MySQL support
Summary(pl):	Modu³ PHP Data Objects (PDO) z obs³ug± MySQL-a
Group:		Libraries
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-pdo = %{epoch}:%{version}-%{release}
Provides:	php(pdo-mysql)
Obsoletes:	php-pecl-PDO_MYSQL

%description pdo-mysql
This is a dynamic shared object (DSO) for PHP that will add PDO MySQL
support.

%description pdo-mysql -l pl
Modu³ dla PHP dodaj±cy obs³ugê baz danych MySQL za po¶rednictwem
interfejsu PDO.

%package pdo-oci
Summary:	PHP Data Objects (PDO) Oracle support
Summary(pl):	Modu³ PHP Data Objects (PDO) z obs³ug± Oracle'a
Group:		Libraries
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-pdo = %{epoch}:%{version}-%{release}
Provides:	php(pdo-oci)
Obsoletes:	php-pecl-PDO_OCI

%description pdo-oci
This is a dynamic shared object (DSO) for PHP that will add PDO Oracle
support.

%description pdo-oci -l pl
Modu³ dla PHP dodaj±cy obs³ugê baz danych Oracle za po¶rednictwem
interfejsu PDO.

%package pdo-odbc
Summary:	PHP Data Objects (PDO) ODBC support
Summary(pl):	Modu³ PHP Data Objects (PDO) z obs³ug± ODBC
Group:		Libraries
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-pdo = %{epoch}:%{version}-%{release}
Provides:	php(pdo-odbc)
Obsoletes:	php-pecl-PDO_ODBC

%description pdo-odbc
This is a dynamic shared object (DSO) for PHP that will add PDO ODBC
support.

%description pdo-odbc -l pl
Modu³ dla PHP dodaj±cy obs³ugê baz danych ODBC za po¶rednictwem
interfejsu PDO.

%package pdo-pgsql
Summary:	PHP Data Objects (PDO) PostgreSQL support
Summary(pl):	Modu³ PHP Data Objects (PDO) z obs³ug± PostgreSQL-a
Group:		Libraries
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-pdo = %{epoch}:%{version}-%{release}
Provides:	php(pdo-pgsql)
Obsoletes:	php-pecl-PDO_PGSQL

%description pdo-pgsql
This is a dynamic shared object (DSO) for PHP that will add PDO
PostgreSQL support.

%description pdo-pgsql -l pl
Modu³ dla PHP dodaj±cy obs³ugê baz danych PostgreSQL za po¶rednictwem
interfejsu PDO.

%package pdo-sqlite
Summary:	PHP Data Objects (PDO) SQLite support
Summary(pl):	Modu³ PHP Data Objects (PDO) z obs³ug± SQLite
Group:		Libraries
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-pdo = %{epoch}:%{version}-%{release}
Provides:	php(pdo-sqlite)
Obsoletes:	php-pecl-PDO_SQLITE

%description pdo-sqlite
This is a dynamic shared object (DSO) for PHP that will add PDO SQLite
support.

%description pdo-sqlite -l pl
Modu³ dla PHP dodaj±cy obs³ugê baz danych SQLite za po¶rednictwem
interfejsu PDO.

%package pgsql
Summary:	PostgreSQL database module for PHP
Summary(pl):	Modu³ bazy danych PostgreSQL dla PHP
Group:		Libraries
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php(pgsql)
Provides:	php-pecl-PDO_PGSQL
Obsoletes:	php-pecl-PDO_PGSQL

%description pgsql
This is a dynamic shared object (DSO) for PHP that will add PostgreSQL
database support.

%description pgsql -l pl
Modu³ PHP umo¿liwiaj±cy dostêp do bazy danych PostgreSQL.

%description pgsql -l pt_BR
Um módulo para aplicações PHP que usam bancos de dados postgresql.

%package posix
Summary:	POSIX extension module for PHP
Summary(pl):	Modu³ POSIX dla PHP
Group:		Libraries
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php(posix)

%description posix
This is a dynamic shared object (DSO) for PHP that will add POSIX
functions support to PHP.

%description posix -l pl
Modu³ PHP umo¿liwiaj±cy korzystanie z funkcji POSIX.

%package pspell
Summary:	pspell extension module for PHP
Summary(pl):	Modu³ pspell dla PHP
Group:		Libraries
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php(pspell)

%description pspell
This is a dynamic shared object (DSO) for PHP that will add pspell
support to PHP. It allows to check the spelling of a word and offer
suggestions.

%description pspell -l pl
Modu³ PHP umo¿liwiaj±cy korzystanie z pspella. Pozwala on na
sprawdzanie pisowni s³owa i sugerowanie poprawek.

%package readline
Summary:	readline extension module for PHP
Summary(pl):	Modu³ readline dla PHP
Group:		Libraries
Requires:	%{name}-cli = %{epoch}:%{version}-%{release}
Provides:	php(readline)

%description readline
This PHP module adds support for readline functions (only for cli and
cgi SAPIs).

%description readline -l pl
Modu³ PHP dodaj±cy obs³ugê funkcji readline (tylko do SAPI cli i cgi).

%package recode
Summary:	recode extension module for PHP
Summary(pl):	Modu³ recode dla PHP
Group:		Libraries
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	recode >= 3.5d-3
Provides:	php(recode)

%description recode
This is a dynamic shared object (DSO) for PHP that will add recode
support.

%description recode -l pl
Modu³ PHP dodaj±cy mo¿liwo¶æ konwersji kodowania plików (poprzez
bibliotekê recode).

%package shmop
Summary:	Shared Memory Operations extension module for PHP
Summary(pl):	Modu³ shmop dla PHP
Group:		Libraries
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php(shmop)

%description shmop
This is a dynamic shared object (DSO) for PHP that will add Shared
Memory Operations support.

Warning: this is an experimental module.

%description shmop -l pl
Modu³ PHP umo¿liwiaj±cy korzystanie z pamiêci dzielonej.

Uwaga: to jest modu³ eksperymentalny.

%package simplexml
Summary:	Simple XML extension module for PHP
Summary(pl):	Modu³ prostego rozszerzenia XML dla PHP
Group:		Libraries
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php(simplexml)

%description simplexml
This is a dynamic shared object (DSO) for PHP that will add Simple XML
support.

%description simplexml -l pl
Modu³ PHP dodaj±cy obs³ugê prostego XML-a.

%package snmp
Summary:	SNMP extension module for PHP
Summary(pl):	Modu³ SNMP dla PHP
Group:		Libraries
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-sockets = %{epoch}:%{version}-%{release}
Provides:	php(snmp)

%description snmp
This is a dynamic shared object (DSO) for PHP that will add SNMP
support.

%description snmp -l pl
Modu³ PHP dodaj±cy obs³ugê SNMP.

%package soap
Summary:	soap extension module for PHP
Summary(pl):	Modu³ soap dla PHP
Group:		Libraries
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php(soap)

%description soap
This is a dynamic shared object (DSO) for PHP that will add SOAP/WSDL
support.

%description soap -l pl
Modu³ PHP dodaj±cy obs³ugê SOAP/WSDL.

%package sockets
Summary:	sockets extension module for PHP
Summary(pl):	Modu³ socket dla PHP
Group:		Libraries
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php(sockets)

%description sockets
This is a dynamic shared object (DSO) for PHP that will add sockets
support.

Warning: this is an experimental module.

%description sockets -l pl
Modu³ PHP dodaj±cy obs³ugê gniazdek.

Uwaga: to jest modu³ eksperymentalny.

%package sqlite
Summary:	SQLite extension module for PHP
Summary(pl):	Modu³ SQLite dla PHP
Group:		Libraries
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-pdo = %{epoch}:%{version}-%{release}
Provides:	php(sqlite)

%description sqlite
SQLite is a C library that implements an embeddable SQL database
engine. Programs that link with the SQLite library can have SQL
database access without running a separate RDBMS process.

SQLite is not a client library used to connect to a big database
server. SQLite is the server. The SQLite library reads and writes
directly to and from the database files on disk.

%description sqlite -l pl
SQLite jest napisan± w C bibliotek± implementuj±c± osadzalny silnik
bazodanowy SQL. Program linkuj±cy siê z bibliotek± SQLite mo¿e mieæ
dostêp do bazy SQL bez potrzeby uruchamiania dodatkowego procesu
RDBMS.

SQLite to nie klient baz danych - biblioteka nie ³±czy siê z serwerami
baz danych. SQLite sam jest serwerem. Biblioteka SQLite czyta i
zapisuje dane bezpo¶rednio z/do plików baz danych znajduj±cych siê na
dysku.

%package sybase
Summary:	Sybase DB extension module for PHP
Summary(pl):	Modu³ Sybase DB dla PHP
Group:		Libraries
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php(sybase)
Obsoletes:	php-sybase-ct
Conflicts:	php-sybase-ct

%description sybase
This is a dynamic shared object (DSO) for PHP that will add Sybase and
MS SQL databases support through SYBDB library. Currently Sybase
module is not maintained. Using Sybase-CT module is recommended
instead.

%description sybase -l pl
Modu³ PHP dodaj±cy obs³ugê baz danych Sybase oraz MS SQL poprzez
bibliotekê SYBDB. W chwili obecnej modu³ Sybase nie jest wspierany.
Zaleca siê u¿ywanie modu³u Sybase-CT.

%package sybase-ct
Summary:	Sybase-CT extension module for PHP
Summary(pl):	Modu³ Sybase-CT dla PHP
Group:		Libraries
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php(sybase-ct)
Obsoletes:	php-sybase
Conflicts:	php-sybase

%description sybase-ct
This is a dynamic shared object (DSO) for PHP that will add Sybase and
MS SQL databases support through CT-lib.

%description sybase-ct -l pl
Modu³ PHP dodaj±cy obs³ugê baz danych Sybase oraz MS SQL poprzez
CT-lib.

%package sysvmsg
Summary:	SysV msg extension module for PHP
Summary(pl):	Modu³ SysV msg dla PHP
Group:		Libraries
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php(sysvmsg)

%description sysvmsg
This is a dynamic shared object (DSO) for PHP that will add SysV
message queues support.

%description sysvmsg -l pl
Modu³ PHP umo¿liwiaj±cy korzystanie z kolejek komunikatów SysV.

%package sysvsem
Summary:	SysV sem extension module for PHP
Summary(pl):	Modu³ SysV sem dla PHP
Group:		Libraries
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php(sysvsem)

%description sysvsem
This is a dynamic shared object (DSO) for PHP that will add SysV
semaphores support.

%description sysvsem -l pl
Modu³ PHP umo¿liwiaj±cy korzystanie z semaforów SysV.

%package sysvshm
Summary:	SysV shm extension module for PHP
Summary(pl):	Modu³ SysV shm dla PHP
Group:		Libraries
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php(sysvshm)

%description sysvshm
This is a dynamic shared object (DSO) for PHP that will add SysV
Shared Memory support.

%description sysvshm -l pl
Modu³ PHP umo¿liwiaj±cy korzystanie z pamiêci dzielonej SysV.

%package tidy
Summary:	Tidy extension module for PHP
Summary(pl):	Modu³ Tidy dla PHP
Group:		Libraries
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	tidy
Provides:	php(tidy)

%description tidy
This is a dynamic shared object (DSO) for PHP that will add Tidy
support.

%description tidy -l pl
Modu³ PHP umo¿liwiaj±cy korzystanie z tidy.

%package tokenizer
Summary:	tokenizer extension module for PHP
Summary(pl):	Modu³ rozszerzenia tokenizer dla PHP
Group:		Libraries
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php(tokenizer)

%description tokenizer
This is a dynamic shared object (DSO) for PHP that will add tokenizer
support.

%description tokenizer -l pl
Modu³ PHP dodaj±cy obs³ugê tokenizera do PHP.

%package wddx
Summary:	wddx extension module for PHP
Summary(pl):	Modu³ wddx dla PHP
Group:		Libraries
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
#Requires:	%{name}-session = %{epoch}:%{version}-%{release}
Requires:	%{name}-xml = %{epoch}:%{version}-%{release}
Provides:	php(wddx)

%description wddx
This is a dynamic shared object (DSO) for PHP that will add wddx
support.

%description wddx -l pl
Modu³ PHP umo¿liwiaj±cy korzystanie z wddx.

%package xml
Summary:	XML extension module for PHP
Summary(pl):	Modu³ XML dla PHP
Group:		Libraries
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php(xml)

%description xml
This is a dynamic shared object (DSO) for PHP that will add XML
support. This extension lets you create XML parsers and then define
handlers for different XML events.

%description xml -l pl
Modu³ PHP umo¿liwiaj±cy parsowanie plików XML i obs³ugê zdarzeñ
zwi±zanych z tymi plikami. Pozwala on tworzyæ analizatory XML-a i
nastêpnie definiowaæ procedury obs³ugi dla ró¿nych zdarzeñ XML.

%package xmlreader
Summary:	XML Reader extension module for PHP
Summary(pl):	Modu³ XML Reader dla PHP
Group:		Libraries
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-dom = %{epoch}:%{version}-%{release}
Provides:	php(xmlreader)

%description xmlreader
This is a dynamic shared object (DSO) for PHP that will add XML Reader
support. The XMLReader extension is an XML Pull parser. The reader
acts as a cursor going forward on the document stream and stopping at
each node on the way.

%description xmlreader -l pl
Modu³ PHP umo¿liwiaj±cy analizê plików XML w trybie Pull. Czytnik
dzia³a jako kursor przechodz±cy przez strumieñ dokumentu i
zatrzymuj±cy siê na ka¿dym wê¼le po drodze.

%package xmlrpc
Summary:	xmlrpc extension module for PHP
Summary(pl):	Modu³ xmlrpc dla PHP
Group:		Libraries
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php(xmlrpc)

%description xmlrpc
This is a dynamic shared object (DSO) for PHP that will add XMLRPC
support.

Warning: this is an experimental module.

%description xmlrpc -l pl
Modu³ PHP dodaj±cy obs³ugê XMLRPC.

Uwaga: to jest modu³ eksperymentalny.

%package xmlwriter
Summary:	Fast, non-cached, forward-only means to write XML data
Summary(pl):	Szybka, nie cachowana metoda zapisu danych w formacie XML
Group:		Libraries
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php(xmlwriter)
Obsoletes:	php-pecl-xmlwriter

%description xmlwriter
This extension wraps the libxml xmlWriter API. Represents a writer
that provides a non-cached, forward-only means of generating streams
or files containing XML data.

%description xmlwriter -l pl
To rozszerzenie obudowuje API xmlWriter z libxml. Reprezentuje obs³ugê
zapisu dostarczaj±c± nie cachowanych metod generowania strumieni lub
plików zawieraj±cych dane XML.

%package xsl
Summary:	xsl extension module for PHP
Summary(pl):	Modu³ xsl dla PHP
Group:		Libraries
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	libxslt >= 1.0.18
# actually not true, functionality is similar, but API differs
Provides:	php(xsl)
Obsoletes:	php-xslt <= 3:4.3.8-1

%description xsl
This is a dynamic shared object (DSO) for PHP that will add new XSL
support (using libxslt).

%description xsl -l pl
Modu³ PHP dodaj±cy now± obs³ugê XSLT (przy u¿yciu libxslt).

%package zip
Summary:	Zip management extension
Summary(pl):	Zarz±dzanie archiwami zip
Group:		Libraries
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php(zip)
Obsoletes:	php-pecl-zip

%description zip
Zip is an extension to create, modify and read zip files.

%description zip -l pl
Zip jest rozszerzeniem umo¿liwiaj±cym tworzenie, modyfikacjê oraz
odczyt archiwów zip.

%package zlib
Summary:	Zlib extension module for PHP
Summary(pl):	Modu³ zlib dla PHP
Group:		Libraries
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php(zlib)

%description zlib
This is a dynamic shared object (DSO) for PHP that will add zlib
compression support to PHP.

%description zlib -l pl
Modu³ PHP umo¿liwiaj±cy u¿ywanie kompresji zlib.

%prep
%setup -q
%patch36 -p1
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1

cp php.ini-dist php.ini
%patch10 -p1
# for ac2.53b/am1.6b - AC_LANG_CXX has AM_CONDITIONAL, so cannot be invoked
# conditionally...
%patch11 -p1
#%patch15 -p1 # breaks with ac cache vars, but later -lpthread is missing ...
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch19 -p1
%patch20 -p1
%patch21 -p1
%patch23 -p1
%patch24 -p1
%patch26 -p1

%if %{with hardening}
zcat %{SOURCE8} | patch -p1 || exit 1
patch -p1 < %{PATCH30} || exit 1
%endif
%patch31 -p1
%patch32 -p1
%patch33 -p1

%{?with_versioning:%patch35 -p1}

%patch39 -p1
%patch41 -p1

# Security patches
%patch100 -p1
%patch101 -p1
%patch102 -p1
%patch103 -p1

# conflict seems to be resolved by recode patches
rm -f ext/recode/config9.m4

# remove all bundled libraries not to link with them accidentally
#rm -rf ext/sqlite/libsqlite
#rm -rf ext/bcmath/libbcmath
#rm -rf ext/date/lib
#rm -rf ext/dba/libcdb
#rm -rf ext/dba/libflatfile
#rm -rf ext/dba/libinifile
#rm -rf ext/gd/libgd
#rm -rf ext/mbstring/libmbfl
#rm -rf ext/mbstring/oniguruma
rm -rf ext/pcre/pcrelib
rm -rf ext/pdo_sqlite/sqlite
#rm -rf ext/soap/interop
rm -rf ext/xmlrpc/libxmlrpc

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

export EXTENSION_DIR="%{php_extensiondir}"
if [ ! -f _built-conf ]; then # configure once (for faster debugging purposes)
	rm -f Makefile.{fcgi,cgi,cli,apxs{1,2}} # now remove Makefile copies
	%{__libtoolize}
	%{__aclocal}
	./buildconf --force
	touch _built-conf
fi
export PROG_SENDMAIL="/usr/lib/sendmail"

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
%if "%{!?configure_cache:0}%{?configure_cache}" == "0"
	--cache-file=config.cache \
%endif
	--with-libdir=%{_lib} \
	--with-config-file-path=%{php_sysconfdir} \
	--with-config-file-scan-dir=%{php_sysconfdir}/conf.d \
	--with-exec-dir=%{_bindir} \
	--%{!?debug:dis}%{?debug:en}able-debug \
	%{?with_zts:--enable-maintainer-zts} \
	--enable-inline-optimization \
	--enable-memory-limit \
	--enable-bcmath=shared \
	--enable-calendar=shared \
	--enable-ctype=shared \
	--enable-dba=shared \
	--with-inifile \
	--with-flatfile \
	--enable-dom=shared \
	--enable-exif=shared \
	--enable-ftp=shared \
	--enable-gd-native-ttf \
	--enable-gd-jus-conf \
	--enable-libxml \
	--enable-magic-quotes \
	--enable-mbstring=shared,all \
	--enable-mbregex \
	--enable-pcntl=shared \
	--enable-pdo=shared \
	--enable-json=shared \
	--enable-hash=shared \
	--enable-xmlwriter=shared \
%if %{with mssql} || %{with sybase} || %{with sybase_ct}
	--with-pdo-dblib=shared \
%endif
%if %{with interbase} && !%{with interbase_inst}
	--with-pdo-firebird=shared,/usr \
%endif
	--with-pdo-mysql=shared \
	%{?with_oci8:--with-pdo-oci=shared} \
	%{?with_odbc:--with-pdo-odbc=shared,unixODBC,/usr} \
	%{?with_pgsql:--with-pdo-pgsql=shared} \
	%{?with_sqlite:--with-pdo-sqlite=shared,/usr} \
	--enable-posix=shared \
	--enable-reflection \
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
	--enable-xmlreader=shared \
	--with-bz2=shared \
	%{!?with_curl:--without-curl}%{?with_curl:--with-curl=shared} \
	--with-db4 \
	--enable-dbase=shared \
%if %{with xmlrpc}
	--with-expat-dir=shared,/usr \
%else
	--without-expat-dir \
%endif
	%{?with_fdf:--with-fdftk=shared} \
	--with-iconv=shared \
	--with-freetype-dir=shared \
	--with-gettext=shared \
	--with-gd=shared,/usr \
	--with-gdbm \
	--with-gmp=shared \
	%{?with_imap:--with-imap=shared --with-imap-ssl} \
	%{?with_interbase:--with-interbase=shared%{!?with_interbase_inst:,/usr}} \
	--with-jpeg-dir=/usr \
	%{?with_ldap:--with-ldap=shared --with-ldap-sasl} \
	--with-mcrypt=shared \
	%{?with_mhash:--with-mhash=shared} \
	%{?with_mime_magic:--with-mime-magic=shared,/usr/share/file/magic.mime}%{!?with_mime_magic:--disable-mime-magic} \
	%{?with_ming:--with-ming=shared} \
	%{?with_mm:--with-mm} \
	%{?with_mssql:--with-mssql=shared} \
	--with-mysql=shared,/usr \
	--with-mysql-sock=/var/lib/mysql/mysql.sock \
	%{?with_mysqli:--with-mysqli=shared} \
	--with-ncurses=shared \
	%{?with_oci8:--with-oci8=shared} \
	%{?with_openssl:--with-openssl=shared} \
	--with-kerberos \
	%{!?with_pcre:--without-pcre-regex}%{?with_pcre:--with-pcre-regex=/usr} \
	%{!?with_filter:--disable-filter}%{?with_filter:--enable-filter=shared} \
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
	--with-zlib-dir=shared,/usr \
	--enable-zip=shared,/usr \

	cp -f Makefile Makefile.$sapi
	cp -f main/php_config.h php_config.h.$sapi
done

# must make this first, so modules can link against it.
%{__make} libphp_common.la
%{__make} build-modules

%if %{with apache1}
%{__make} libtool-sapi LIBTOOL_SAPI=sapi/apache/libphp5.la -f Makefile.apxs1 LDFLAGS=-lpthread
%endif

%if %{with apache2}
%{__make} libtool-sapi LIBTOOL_SAPI=sapi/apache2handler/libphp5.la -f Makefile.apxs2
%endif

# FCGI
%if %{with fcgi}
cp -af php_config.h.fcgi main/php_config.h
%{__make} sapi/cgi/php -f Makefile.fcgi LDFLAGS=-lpthread
cp -r sapi/cgi sapi/fcgi
rm -rf sapi/cgi/.libs sapi/cgi/*.lo
%endif

# CGI
cp -af php_config.h.cgi main/php_config.h
%{__make} sapi/cgi/php -f Makefile.cgi LDFLAGS=-lpthread

# CLI
cp -af php_config.h.cli main/php_config.h
%{__make} sapi/cli/php -f Makefile.cli LDFLAGS=-lpthread

%check
# Run tests, using the CLI SAPI
export NO_INTERACTION=1 REPORT_EXIT_STATUS=1 MALLOC_CHECK_=2
unset TZ LANG LC_ALL || :
%{__make} test
unset NO_INTERACTION REPORT_EXIT_STATUS MALLOC_CHECK_

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir}/{php,apache{,1}},%{php_sysconfdir}/{apache,cgi}} \
	$RPM_BUILD_ROOT/home/services/{httpd,apache}/icons \
	$RPM_BUILD_ROOT{%{_sbindir},%{_bindir}} \
	$RPM_BUILD_ROOT/etc/{apache/conf.d,httpd/httpd.conf} \
	$RPM_BUILD_ROOT%{_mandir}/man1 \

# install the apache modules' files
%{__make} install-headers install-build install-modules install-programs \
	INSTALL_ROOT=$RPM_BUILD_ROOT

# install apache1 DSO module
%if %{with apache1}
libtool --silent --mode=install install sapi/apache/libphp5.la $RPM_BUILD_ROOT%{_libdir}/apache1
%endif

# install apache2 DSO module
%if %{with apache2}
libtool --silent --mode=install install sapi/apache2handler/libphp5.la $RPM_BUILD_ROOT%{_libdir}/apache
%endif

libtool --silent --mode=install install libphp_common.la $RPM_BUILD_ROOT%{_libdir}
# fix install paths, avoid evil rpaths
sed -i -e "s|^libdir=.*|libdir='%{_libdir}'|" $RPM_BUILD_ROOT%{_libdir}/libphp_common.la
# better solution?
sed -i -e 's|libphp_common.la|$(libdir)/libphp_common.la|' $RPM_BUILD_ROOT%{_libdir}/php/build/acinclude.m4

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

ln -sf php.cli $RPM_BUILD_ROOT%{_bindir}/php

sed -e 's#%{_prefix}/lib/php#%{_libdir}/php#g' php.ini > $RPM_BUILD_ROOT%{php_sysconfdir}/php.ini
%if %{with fcgi}
install %{SOURCE4} $RPM_BUILD_ROOT%{php_sysconfdir}/php-cgi-fcgi.ini
%endif
install %{SOURCE5} $RPM_BUILD_ROOT%{php_sysconfdir}/php-cgi.ini
install %{SOURCE7} $RPM_BUILD_ROOT%{php_sysconfdir}/php-cli.ini
install %{SOURCE9} $RPM_BUILD_ROOT%{php_sysconfdir}/browscap.ini

%if %{with apache1}
install %{SOURCE2} php.gif $RPM_BUILD_ROOT/home/services/apache/icons
install %{SOURCE3} $RPM_BUILD_ROOT/etc/apache/conf.d/70_mod_php.conf
install %{SOURCE6} $RPM_BUILD_ROOT%{php_sysconfdir}/php-apache.ini
rm -f $RPM_BUILD_ROOT%{_libdir}/apache1/libphp5.la
%endif

%if %{with apache2}
install %{SOURCE2} php.gif $RPM_BUILD_ROOT/home/services/httpd/icons
install %{SOURCE3} $RPM_BUILD_ROOT/etc/httpd/httpd.conf/70_mod_php.conf
install %{SOURCE6} $RPM_BUILD_ROOT%{php_sysconfdir}/php-apache2handler.ini
rm -f $RPM_BUILD_ROOT%{_libdir}/apache/libphp5.la
%endif

cp -f Zend/LICENSE{,.Zend}

# Generate stub .ini files for each subpackage
install -d $RPM_BUILD_ROOT%{php_sysconfdir}/conf.d
for so in modules/*.so; do
	mod=$(basename $so .so)
	conf="%{php_sysconfdir}/conf.d/${mod}.ini"
	# xml needs to be loaded before wddx
	[ "$mod" = "wddx" ] && conf="%{php_sysconfdir}/conf.d/xml_${mod}.ini"
	cat > $RPM_BUILD_ROOT${conf} <<EOF
; Enable ${mod} extension module
extension=${mod}.so
EOF
done

# per SAPI ini directories
install -d $RPM_BUILD_ROOT%{php_sysconfdir}/{cgi,cli,cgi-fcgi,apache,apache2handler}.d

# for CLI SAPI only
mv $RPM_BUILD_ROOT%{php_sysconfdir}/{conf.d/{ncurses,pcntl,readline}.ini,cli.d}

# use system automake and {lib,sh}tool
ln -snf /usr/share/automake/config.{guess,sub} $RPM_BUILD_ROOT%{_libdir}/php/build
ln -snf %{_aclocaldir}/libtool.m4 $RPM_BUILD_ROOT%{_libdir}/php/build
ln -snf %{_datadir}/libtool/ltmain.sh $RPM_BUILD_ROOT%{_libdir}/php/build
ln -snf %{_bindir}/shtool $RPM_BUILD_ROOT%{_libdir}/php/build

# as a result of ext/pcre/pcrelib removal in %%prep, ext/pcre/php_pcre.h
# isn't installed by install-headers make target, we do it manually here.
# this header file is required by e.g. filter PECL extension
install -D ext/pcre/php_pcre.h $RPM_BUILD_ROOT%{_includedir}/php/ext/pcre/php_pcre.h
# for php-pecl-mailparse
install -d $RPM_BUILD_ROOT%{_includedir}/php/ext/mbstring
cp -a ext/mbstring/libmbfl/mbfl/*.h $RPM_BUILD_ROOT%{_includedir}/php/ext/mbstring

%clean
rm -rf $RPM_BUILD_ROOT

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

%if %{with apache1}
%triggerpostun -n apache1-mod_php -- php < 4:5.0.4-9.11
sed -i -e '
	/^AddType application\/x-httpd-php \.php/s,^,#,
	/^\(Add\|Load\)Module.*php5\.\(so\|c\)/d
' /etc/apache/apache.conf
%service -q apache restart
%endif

%if %{with apache2}
%triggerpostun -n apache-mod_php -- php < 4:5.0.4-7.1, php < 4:5.0.4-7.1
# for fixed php-SAPI.ini, the poor php-apache.ini was never read for apache2
if [ -f %{php_sysconfdir}/php-apache.ini.rpmsave ]; then
	cp -f %{php_sysconfdir}/php-apache2handler.ini{,.rpmnew}
	mv -f %{php_sysconfdir}/php-apache.ini.rpmsave %{php_sysconfdir}/php-apache2handler.ini
fi
%endif

# common macros called at extension post/postun scriptlet
%define	extension_scripts() \
%post %1 \
if [ "$1" = "1" ]; then \
	%php_webserver_restart \
fi \
\
%postun %1 \
if [ "$1" = "0" ]; then \
	%php_webserver_restart \
fi
%{nil}

# extension scripts defines
%extension_scripts bcmath
%extension_scripts bzip2
%extension_scripts calendar
%extension_scripts ctype
%extension_scripts curl
%extension_scripts dba
%extension_scripts dbase
%extension_scripts dom
%extension_scripts exif
%extension_scripts fdf
%extension_scripts filter
%extension_scripts ftp
%extension_scripts gd
%extension_scripts gettext
%extension_scripts gmp
%extension_scripts hash
%extension_scripts iconv
%extension_scripts imap
%extension_scripts interbase
%extension_scripts json
%extension_scripts ldap
%extension_scripts mbstring
%extension_scripts mcrypt
%extension_scripts mhash
%extension_scripts mime_magic
%extension_scripts ming
%extension_scripts mssql
%extension_scripts mysql
%extension_scripts mysqli
%extension_scripts oci8
%extension_scripts odbc
%extension_scripts openssl
%extension_scripts pdo-dblib
%extension_scripts pdo-firebird
%extension_scripts pdo-mysql
%extension_scripts pdo-odbc
%extension_scripts pdo-pgsql
%extension_scripts pdo-sqlite
%extension_scripts pgsql
%extension_scripts posix
%extension_scripts pspell
%extension_scripts recode
%extension_scripts shmop
%extension_scripts snmp
%extension_scripts soap
%extension_scripts sockets
%extension_scripts sqlite
%extension_scripts sybase
%extension_scripts sybase-ct
%extension_scripts sysvmsg
%extension_scripts sysvsem
%extension_scripts sysvshm
%extension_scripts tidy
%extension_scripts tokenizer
%extension_scripts wddx
%extension_scripts xml
%extension_scripts xmlreader
%extension_scripts xmlrpc
%extension_scripts xmlwriter
%extension_scripts xsl
%extension_scripts zip
%extension_scripts zlib

%triggerun bcmath -- %{name}-bcmath < 4:5.0.4-9.1
%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*bcmath\.so/d' %{php_sysconfdir}/php.ini

%triggerun bzip2 -- %{name}-bzip2 < 4:5.0.4-9.1
%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*bzip2\.so/d' %{php_sysconfdir}/php.ini

%triggerun calendar -- %{name}-calendar < 4:5.0.4-9.1
%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*calendar\.so/d' %{php_sysconfdir}/php.ini

%triggerun ctype -- %{name}-ctype < 4:5.0.4-9.1
%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*ctype\.so/d' %{php_sysconfdir}/php.ini

%triggerun curl -- %{name}-curl < 4:5.0.4-9.1
%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*curl\.so/d' %{php_sysconfdir}/php.ini

%triggerun dba -- %{name}-dba < 4:5.0.4-9.1
%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*dba\.so/d' %{php_sysconfdir}/php.ini

%triggerun dbase -- %{name}-dbase < 4:5.0.4-9.1
%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*dbase\.so/d' %{php_sysconfdir}/php.ini

%triggerun dom -- %{name}-dom < 4:5.0.4-9.1
%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*dom\.so/d' %{php_sysconfdir}/php.ini

%triggerun exif -- %{name}-exif < 4:5.0.4-9.1
%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*exif\.so/d' %{php_sysconfdir}/php.ini

%triggerun fdf -- %{name}-fdf < 4:5.0.4-9.1
%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*fdf\.so/d' %{php_sysconfdir}/php.ini

%triggerun ftp -- %{name}-ftp < 4:5.0.4-9.1
%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*ftp\.so/d' %{php_sysconfdir}/php.ini

%triggerun gd -- %{name}-gd < 4:5.0.4-9.1
%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*gd\.so/d' %{php_sysconfdir}/php.ini

%triggerun gettext -- %{name}-gettext < 4:5.0.4-9.1
%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*gettext\.so/d' %{php_sysconfdir}/php.ini

%triggerun gmp -- %{name}-gmp < 4:5.0.4-9.1
%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*gmp\.so/d' %{php_sysconfdir}/php.ini

%triggerun iconv -- %{name}-iconv < 4:5.0.4-9.1
%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*iconv\.so/d' %{php_sysconfdir}/php.ini

%triggerun imap -- %{name}-imap < 4:5.0.4-9.1
%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*imap\.so/d' %{php_sysconfdir}/php.ini

%triggerun interbase -- %{name}-interbase < 4:5.0.4-9.1
%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*interbase\.so/d' %{php_sysconfdir}/php.ini

%triggerun ldap -- %{name}-ldap < 4:5.0.4-9.1
%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*ldap\.so/d' %{php_sysconfdir}/php.ini

%triggerun mbstring -- %{name}-mbstring < 4:5.0.4-9.1
%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*mbstring\.so/d' %{php_sysconfdir}/php.ini

%triggerun mcrypt -- %{name}-mcrypt < 4:5.0.4-9.1
%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*mcrypt\.so/d' %{php_sysconfdir}/php.ini

%triggerun mhash -- %{name}-mhash < 4:5.0.4-9.1
%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*mhash\.so/d' %{php_sysconfdir}/php.ini

%triggerun mime_magic -- %{name}-mime_magic < 4:5.0.4-9.1
%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*mime_magic\.so/d' %{php_sysconfdir}/php.ini

%triggerun ming -- %{name}-ming < 4:5.0.4-9.1
%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*ming\.so/d' %{php_sysconfdir}/php.ini

%triggerun mssql -- %{name}-mssql < 4:5.0.4-9.1
%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*mssql\.so/d' %{php_sysconfdir}/php.ini

%triggerun mysql -- %{name}-mysql < 4:5.0.4-9.1
%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*mysql\.so/d' %{php_sysconfdir}/php.ini

%triggerun ncurses -- %{name}-ncurses < 4:5.1.2-9.5
if [ -f %{php_sysconfdir}/php-cgi.ini ]; then
	%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*ncurses\.so/d' %{php_sysconfdir}/php-cgi.ini
fi
if [ -f %{php_sysconfdir}/php-cli.ini ]; then
	%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*ncurses\.so/d' %{php_sysconfdir}/php-cli.ini
fi

%triggerun mysqli -- %{name}-mysqli < 4:5.0.4-9.1
%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*mysqli\.so/d' %{php_sysconfdir}/php.ini

%triggerun oci8 -- %{name}-oci8 < 4:5.0.4-9.1
%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*oci8\.so/d' %{php_sysconfdir}/php.ini

%triggerun odbc -- %{name}-odbc < 4:5.0.4-9.1
%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*odbc\.so/d' %{php_sysconfdir}/php.ini

%triggerun openssl -- %{name}-openssl < 4:5.0.4-9.1
%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*openssl\.so/d' %{php_sysconfdir}/php.ini

%triggerun pcntl -- %{name}-pcntl < 4:5.1.2-9.5
if [ -f %{php_sysconfdir}/php-cgi.ini ]; then
	%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*pcntl\.so/d' %{php_sysconfdir}/php-cgi.ini
fi
if [ -f %{php_sysconfdir}/php-cli.ini ]; then
	%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*pcntl\.so/d' %{php_sysconfdir}/php-cli.ini
fi

%triggerun pgsql -- %{name}-pgsql < 4:5.0.4-9.1
%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*pgsql\.so/d' %{php_sysconfdir}/php.ini

%triggerun posix -- %{name}-posix < 4:5.0.4-9.1
%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*posix\.so/d' %{php_sysconfdir}/php.ini

%triggerun pspell -- %{name}-pspell < 4:5.0.4-9.1
%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*pspell\.so/d' %{php_sysconfdir}/php.ini

%triggerun readline -- %{name}-readline < 4:5.1.2-9.5
if [ -f %{php_sysconfdir}/php-cgi.ini ]; then
	%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*readline\.so/d' %{php_sysconfdir}/php-cgi.ini
fi
if [ -f %{php_sysconfdir}/php-cli.ini ]; then
	%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*readline\.so/d' %{php_sysconfdir}/php-cli.ini
fi

%triggerun recode -- %{name}-recode < 4:5.0.4-9.1
%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*recode\.so/d' %{php_sysconfdir}/php.ini

%triggerun shmop -- %{name}-shmop < 4:5.0.4-9.1
%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*shmop\.so/d' %{php_sysconfdir}/php.ini

%triggerun snmp -- %{name}-snmp < 4:5.0.4-9.1
%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*snmp\.so/d' %{php_sysconfdir}/php.ini

%triggerun soap -- %{name}-soap < 4:5.0.4-9.1
%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*soap\.so/d' %{php_sysconfdir}/php.ini

%triggerun sockets -- %{name}-sockets < 4:5.0.4-9.1
%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*sockets\.so/d' %{php_sysconfdir}/php.ini

%triggerun sqlite -- %{name}-sqlite < 4:5.0.4-9.1
%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*sqlite\.so/d' %{php_sysconfdir}/php.ini

%triggerun sybase -- %{name}-sybase < 4:5.0.4-9.1
%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*sybase\.so/d' %{php_sysconfdir}/php.ini

%triggerun sybase-ct -- %{name}-sybase-ct < 4:5.0.4-9.1
%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*sybase-ct\.so/d' %{php_sysconfdir}/php.ini

%triggerun sysvmsg -- %{name}-sysvmsg < 4:5.0.4-9.1
%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*sysvmsg\.so/d' %{php_sysconfdir}/php.ini

%triggerun sysvsem -- %{name}-sysvsem < 4:5.0.4-9.1
%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*sysvsem\.so/d' %{php_sysconfdir}/php.ini

%triggerun sysvshm -- %{name}-sysvshm < 4:5.0.4-9.1
%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*sysvshm\.so/d' %{php_sysconfdir}/php.ini

%triggerun tidy -- %{name}-tidy < 4:5.0.4-9.1
%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*tidy\.so/d' %{php_sysconfdir}/php.ini

%triggerun wddx -- %{name}-wddx < 4:5.0.4-9.1
%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*wddx\.so/d' %{php_sysconfdir}/php.ini

%triggerun xml -- %{name}-xml < 4:5.0.4-9.1
%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*xml\.so/d' %{php_sysconfdir}/php.ini

%triggerun xmlrpc -- %{name}-xmlrpc < 4:5.0.4-9.1
%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*xmlrpc\.so/d' %{php_sysconfdir}/php.ini

%triggerun xsl -- %{name}-xsl < 4:5.0.4-9.1
%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*xsl\.so/d' %{php_sysconfdir}/php.ini

%triggerun zlib -- %{name}-zlib < 4:5.0.4-9.1
%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*zlib\.so/d' %{php_sysconfdir}/php.ini

%if %{with apache1}
%files -n apache1-mod_php
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/apache/conf.d/*_mod_php.conf
%dir %{php_sysconfdir}/apache.d
%config(noreplace) %verify(not md5 mtime size) %{php_sysconfdir}/php-apache.ini
%attr(755,root,root) %{_libdir}/apache1/libphp5.so
/home/services/apache/icons/*
%endif

%if %{with apache2}
%files -n apache-mod_php
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/httpd/httpd.conf/*_mod_php.conf
%dir %{php_sysconfdir}/apache2handler.d
%config(noreplace) %verify(not md5 mtime size) %{php_sysconfdir}/php-apache2handler.ini
%attr(755,root,root) %{_libdir}/apache/libphp5.so
/home/services/httpd/icons/*
%endif

%if %{with fcgi}
%files fcgi
%defattr(644,root,root,755)
%doc sapi/cgi/README.FastCGI
%dir %{php_sysconfdir}/cgi-fcgi.d
%config(noreplace) %verify(not md5 mtime size) %{php_sysconfdir}/php-cgi-fcgi.ini
%attr(755,root,root) %{_bindir}/php.fcgi
%endif

%files cgi
%defattr(644,root,root,755)
%dir %{php_sysconfdir}/cgi.d
%config(noreplace) %verify(not md5 mtime size) %{php_sysconfdir}/php-cgi.ini
%attr(755,root,root) %{_bindir}/php.cgi

%files cli
%defattr(644,root,root,755)
%dir %{php_sysconfdir}/cli.d
%config(noreplace) %verify(not md5 mtime size) %{php_sysconfdir}/php-cli.ini
%attr(755,root,root) %{_bindir}/php.cli
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
%doc README.PHP4-TO-PHP5-THIN-CHANGES README.UPDATE_5_2

%dir %{php_sysconfdir}
%dir %{php_sysconfdir}/conf.d
%config(noreplace) %verify(not md5 mtime size) %{php_sysconfdir}/php.ini
%config(noreplace) %verify(not md5 mtime size) %{php_sysconfdir}/browscap.ini
%attr(755,root,root) %{_libdir}/libphp_common-*.so
%dir %{php_extensiondir}

%doc ext/session/mod_files.sh

%files devel
%defattr(644,root,root,755)
%doc README.UNIX-BUILD-SYSTEM
%doc README.EXT_SKEL README.SELF-CONTAINED-EXTENSIONS
%doc CODING_STANDARDS README.EXTENSIONS README.PARAMETER_PARSING_API README.STREAMS
%doc README.SUBMITTING_PATCH README.TESTING README.TESTING2
%attr(755,root,root) %{_bindir}/phpize
%attr(755,root,root) %{_bindir}/php-config
%attr(755,root,root) %{_libdir}/libphp_common.so
%{_libdir}/libphp_common.la
%{_includedir}/php
%{_libdir}/php/build
%{_mandir}/man1/*

%files bcmath
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{php_sysconfdir}/conf.d/bcmath.ini
%attr(755,root,root) %{php_extensiondir}/bcmath.so

%files bzip2
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{php_sysconfdir}/conf.d/bz2.ini
%attr(755,root,root) %{php_extensiondir}/bz2.so

%files calendar
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{php_sysconfdir}/conf.d/calendar.ini
%attr(755,root,root) %{php_extensiondir}/calendar.so

%files ctype
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{php_sysconfdir}/conf.d/ctype.ini
%attr(755,root,root) %{php_extensiondir}/ctype.so

%if %{with curl}
%files curl
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{php_sysconfdir}/conf.d/curl.ini
%attr(755,root,root) %{php_extensiondir}/curl.so
%endif

%files dba
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{php_sysconfdir}/conf.d/dba.ini
%attr(755,root,root) %{php_extensiondir}/dba.so

%files dbase
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{php_sysconfdir}/conf.d/dbase.ini
%attr(755,root,root) %{php_extensiondir}/dbase.so

%files dom
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{php_sysconfdir}/conf.d/dom.ini
%attr(755,root,root) %{php_extensiondir}/dom.so

%if %{with fdf}
%files fdf
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{php_sysconfdir}/conf.d/fdf.ini
%attr(755,root,root) %{php_extensiondir}/fdf.so
%endif

%if %{with filter}
%files filter
%defattr(644,root,root,755)
%doc README.input_filter
%config(noreplace) %verify(not md5 mtime size) %{php_sysconfdir}/conf.d/filter.ini
%attr(755,root,root) %{php_extensiondir}/filter.so
%endif

%files exif
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{php_sysconfdir}/conf.d/exif.ini
%attr(755,root,root) %{php_extensiondir}/exif.so

%files ftp
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{php_sysconfdir}/conf.d/ftp.ini
%attr(755,root,root) %{php_extensiondir}/ftp.so

%files gd
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{php_sysconfdir}/conf.d/gd.ini
%attr(755,root,root) %{php_extensiondir}/gd.so

%files gettext
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{php_sysconfdir}/conf.d/gettext.ini
%attr(755,root,root) %{php_extensiondir}/gettext.so

%files gmp
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{php_sysconfdir}/conf.d/gmp.ini
%attr(755,root,root) %{php_extensiondir}/gmp.so

%files hash
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{php_sysconfdir}/conf.d/hash.ini
%attr(755,root,root) %{php_extensiondir}/hash.so

%files iconv
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{php_sysconfdir}/conf.d/iconv.ini
%attr(755,root,root) %{php_extensiondir}/iconv.so

%if %{with imap}
%files imap
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{php_sysconfdir}/conf.d/imap.ini
%attr(755,root,root) %{php_extensiondir}/imap.so
%endif

%if %{with interbase}
%files interbase
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{php_sysconfdir}/conf.d/interbase.ini
%attr(755,root,root) %{php_extensiondir}/interbase.so
%endif

%files json
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{php_sysconfdir}/conf.d/json.ini
%attr(755,root,root) %{php_extensiondir}/json.so

%if %{with ldap}
%files ldap
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{php_sysconfdir}/conf.d/ldap.ini
%attr(755,root,root) %{php_extensiondir}/ldap.so
%endif

%files mbstring
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{php_sysconfdir}/conf.d/mbstring.ini
%attr(755,root,root) %{php_extensiondir}/mbstring.so

%files mcrypt
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{php_sysconfdir}/conf.d/mcrypt.ini
%attr(755,root,root) %{php_extensiondir}/mcrypt.so

%if %{with mhash}
%files mhash
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{php_sysconfdir}/conf.d/mhash.ini
%attr(755,root,root) %{php_extensiondir}/mhash.so
%endif

%if %{with mime_magic}
%files mime_magic
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{php_sysconfdir}/conf.d/mime_magic.ini
%attr(755,root,root) %{php_extensiondir}/mime_magic.so
%endif

%if %{with ming}
%files ming
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{php_sysconfdir}/conf.d/ming.ini
%attr(755,root,root) %{php_extensiondir}/ming.so
%endif

%if %{with mssql}
%files mssql
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{php_sysconfdir}/conf.d/mssql.ini
%attr(755,root,root) %{php_extensiondir}/mssql.so
%endif

%files mysql
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{php_sysconfdir}/conf.d/mysql.ini
%attr(755,root,root) %{php_extensiondir}/mysql.so

%if %{with mysqli}
%files mysqli
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{php_sysconfdir}/conf.d/mysqli.ini
%attr(755,root,root) %{php_extensiondir}/mysqli.so
%endif

%files ncurses
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{php_sysconfdir}/cli.d/ncurses.ini
%attr(755,root,root) %{php_extensiondir}/ncurses.so

%if %{with oci8}
%files oci8
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{php_sysconfdir}/conf.d/oci8.ini
%attr(755,root,root) %{php_extensiondir}/oci8.so
%endif

%if %{with odbc}
%files odbc
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{php_sysconfdir}/conf.d/odbc.ini
%attr(755,root,root) %{php_extensiondir}/odbc.so
%endif

%if %{with openssl}
%files openssl
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{php_sysconfdir}/conf.d/openssl.ini
%attr(755,root,root) %{php_extensiondir}/openssl.so
%endif

%files pcntl
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{php_sysconfdir}/cli.d/pcntl.ini
%attr(755,root,root) %{php_extensiondir}/pcntl.so

%files pdo
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{php_sysconfdir}/conf.d/pdo.ini
%attr(755,root,root) %{php_extensiondir}/pdo.so

%if %{with mssql} || %{with sybase} || %{with sybase_ct}
%files pdo-dblib
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{php_sysconfdir}/conf.d/pdo_dblib.ini
%attr(755,root,root) %{php_extensiondir}/pdo_dblib.so
%endif

%if %{with interbase} && !%{with interbase_inst}
%files pdo-firebird
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{php_sysconfdir}/conf.d/pdo_firebird.ini
%attr(755,root,root) %{php_extensiondir}/pdo_firebird.so
%endif

%files pdo-mysql
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{php_sysconfdir}/conf.d/pdo_mysql.ini
%attr(755,root,root) %{php_extensiondir}/pdo_mysql.so

%if %{with oci8}
%files pdo-oci
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{php_sysconfdir}/conf.d/pdo_oci.ini
%attr(755,root,root) %{php_extensiondir}/pdo_oci.so
%endif

%if %{with odbc}
%files pdo-odbc
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{php_sysconfdir}/conf.d/pdo_odbc.ini
%attr(755,root,root) %{php_extensiondir}/pdo_odbc.so
%endif

%if %{with pgsql}
%files pdo-pgsql
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{php_sysconfdir}/conf.d/pdo_pgsql.ini
%attr(755,root,root) %{php_extensiondir}/pdo_pgsql.so
%endif

%if %{with sqlite}
%files pdo-sqlite
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{php_sysconfdir}/conf.d/pdo_sqlite.ini
%attr(755,root,root) %{php_extensiondir}/pdo_sqlite.so
%endif

%if %{with pgsql}
%files pgsql
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{php_sysconfdir}/conf.d/pgsql.ini
%attr(755,root,root) %{php_extensiondir}/pgsql.so
%endif

%files posix
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{php_sysconfdir}/conf.d/posix.ini
%attr(755,root,root) %{php_extensiondir}/posix.so

%if %{with pspell}
%files pspell
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{php_sysconfdir}/conf.d/pspell.ini
%attr(755,root,root) %{php_extensiondir}/pspell.so
%endif

%files readline
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{php_sysconfdir}/cli.d/readline.ini
%attr(755,root,root) %{php_extensiondir}/readline.so

%if %{with recode}
%files recode
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{php_sysconfdir}/conf.d/recode.ini
%attr(755,root,root) %{php_extensiondir}/recode.so
%endif

%if 0
# simplexml is needed by spl, and spl can't be built shared as of now (5.2.0)
# simplexml can be built shared, but SPL startup fails
# we could add R: -simplexml to -common...
%files simplexml
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{php_sysconfdir}/conf.d/simplexml.ini
%attr(755,root,root) %{php_extensiondir}/simplexml.so
%endif

%files shmop
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{php_sysconfdir}/conf.d/shmop.ini
%attr(755,root,root) %{php_extensiondir}/shmop.so

%if %{with snmp}
%files snmp
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{php_sysconfdir}/conf.d/snmp.ini
%attr(755,root,root) %{php_extensiondir}/snmp.so
%endif

%files soap
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{php_sysconfdir}/conf.d/soap.ini
%attr(755,root,root) %{php_extensiondir}/soap.so

%files sockets
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{php_sysconfdir}/conf.d/sockets.ini
%attr(755,root,root) %{php_extensiondir}/sockets.so

%if %{with sqlite}
%files sqlite
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{php_sysconfdir}/conf.d/sqlite.ini
%attr(755,root,root) %{php_extensiondir}/sqlite.so
%endif

%if %{with sybase}
%files sybase
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{php_sysconfdir}/conf.d/sybase.ini
%attr(755,root,root) %{php_extensiondir}/sybase.so
%endif

%if %{with sybase_ct}
%files sybase-ct
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{php_sysconfdir}/conf.d/sybase_ct.ini
%attr(755,root,root) %{php_extensiondir}/sybase_ct.so
%endif

%files sysvmsg
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{php_sysconfdir}/conf.d/sysvmsg.ini
%attr(755,root,root) %{php_extensiondir}/sysvmsg.so

%files sysvsem
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{php_sysconfdir}/conf.d/sysvsem.ini
%attr(755,root,root) %{php_extensiondir}/sysvsem.so

%files sysvshm
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{php_sysconfdir}/conf.d/sysvshm.ini
%attr(755,root,root) %{php_extensiondir}/sysvshm.so

%if %{with tidy}
%files tidy
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{php_sysconfdir}/conf.d/tidy.ini
%attr(755,root,root) %{php_extensiondir}/tidy.so
%endif

%files tokenizer
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{php_sysconfdir}/conf.d/tokenizer.ini
%attr(755,root,root) %{php_extensiondir}/tokenizer.so

%if %{with wddx}
%files wddx
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{php_sysconfdir}/conf.d/*wddx.ini
%attr(755,root,root) %{php_extensiondir}/wddx.so
%endif

%files xml
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{php_sysconfdir}/conf.d/xml.ini
%attr(755,root,root) %{php_extensiondir}/xml.so

%files xmlreader
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{php_sysconfdir}/conf.d/xmlreader.ini
%attr(755,root,root) %{php_extensiondir}/xmlreader.so

%if %{with xmlrpc}
%files xmlrpc
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{php_sysconfdir}/conf.d/xmlrpc.ini
%attr(755,root,root) %{php_extensiondir}/xmlrpc.so
%endif

%files xmlwriter
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{php_sysconfdir}/conf.d/xmlwriter.ini
%attr(755,root,root) %{php_extensiondir}/xmlwriter.so

%files xsl
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{php_sysconfdir}/conf.d/xsl.ini
%attr(755,root,root) %{php_extensiondir}/xsl.so

%files zip
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{php_sysconfdir}/conf.d/zip.ini
%attr(755,root,root) %{php_extensiondir}/zip.so

%files zlib
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{php_sysconfdir}/conf.d/zlib.ini
%attr(755,root,root) %{php_extensiondir}/zlib.so
