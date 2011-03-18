# NOTE: mysqlnd does not support ssl or compression (see FAQ at http://dev.mysql.com/downloads/connector/php-mysqlnd/)
# TODO:
# - ttyname_r() misdetected http://bugs.php.net/bug.php?id=48820
# - wddx: restore session support (not compiled in due DL extension check)
# - deal with modules removed from php and not moved to PECL, still not obsoleted anywhere
#   - removed from php 5.0 (currently in php4):
#   db [pecl-svn], hyperwave [pecl-svn], java [pecl-svn], mcal [pecl-svn], overload [???], qtdom [pecl-svn]
#   - removed from php 5.1:
#   oracle [pecl-svn]
#   - removed from php 5.2:
#   filepro [pecl-svn], hwapi [pecl-svn]
# - make additional headers and checking added by mail patch configurable
# - modularize standard (output from pure php -m)?
# - lib64 patch obsolete by $PHP_LIBDIR ?
# - WARNING: Phar: sha256/sha512 signature support disabled if ext/hash is
#   built shared, also PHAR_HAVE_OPENSSL is false if openssl is built shared.
#   make it runtime dep and add Suggests (or php warning messages)
# - some mods should be shared:
#$ php -m
# [PHP Modules]
#+Core
# date
#+ereg
# libxml
# Reflection
#
# Conditional build:
%bcond_with	interbase_inst	# use InterBase install., not Firebird	(BR: proprietary libs)
%bcond_with	oci8		# with Oracle oci8 extension module	(BR: proprietary libs)
%bcond_with	instantclient	# build Oracle oci8 extension module against oracle-instantclient package
%bcond_with	system_gd	# with system gd (we prefer internal since it enables few more features)
%bcond_without	curl		# without CURL extension module
%bcond_without	filter		# without filter extension module
%bcond_without	imap		# without IMAP extension module
%bcond_without	interbase	# without InterBase extension module
%bcond_without	litespeed	# build litespeed module
%bcond_without	ldap		# without LDAP extension module
%bcond_without	mm		# without mm support for session storage
%bcond_without	mssql		# without MS SQL extension module
# don't turn it on by default; see TODO item for mysqlnd in this spec
%bcond_with	mysqlnd		# with mysqlnd support in mysql related extensions
%bcond_without	mysqli		# without mysqli support (Requires mysql > 4.1)
%bcond_without	odbc		# without ODBC extension module
%bcond_without	openssl		# without OpenSSL support and OpenSSL extension (module)
%bcond_without	pcre		# without PCRE extension module
%bcond_without	pgsql		# without PostgreSQL extension module
%bcond_without	phar		# without phar extension module
%bcond_without	pspell		# without pspell extension module
%bcond_without	recode		# without recode extension module
%bcond_without	snmp		# without SNMP extension module
%bcond_without	sqlite		# without SQLite extension module
%bcond_without	sqlite3		# without SQLite3 extension module
%bcond_without	sybase_ct	# without Sybase-CT extension module
%bcond_without	tidy		# without Tidy extension module
%bcond_without	wddx		# without WDDX extension module
%bcond_without	xmlrpc		# without XML-RPC extension module
%bcond_without	apache1		# disable building Apache 1.3.x SAPI
%bcond_without	apache2		# disable building Apache 2.x SAPI
%bcond_with	zts		# Zend Thread Safety
%bcond_without	cgi		# disable CGI/FCGI SAPI
%bcond_without	fpm		# disable FPM
%bcond_without	suhosin		# with suhosin patch
%bcond_with	tests		# default off; test process very often hangs on builders, approx run time 45m; perform "make test"
%bcond_with	gcov		# Enable Code coverage reporting
%bcond_with	type_hints	# experimental support for strict typing/casting

%define apxs1		/usr/sbin/apxs1
%define	apxs2		/usr/sbin/apxs
%define	litespeed_version	5.5

# disable all sapis
%if %{with gcov}
%undefine	with_apache1
%undefine	with_apache2
%undefine	with_cgi
%undefine	with_litespeed
%endif

# mm is not thread safe
%if %{with zts}
%undefine	with_mm
%endif

%ifnarch %{ix86} %{x8664} sparc sparcv9 alpha
# ppc disabled (broken on th-ppc)
%undefine	with_interbase
%endif

%ifnarch %{ix86} %{x8664}
# unsupported, see sapi/cgi/fpm/fpm_atomic.h
%undefine	with_fpm
%endif

%if 0
%if %{without apache1} && %{without apache2}
ERROR: You need to select at least one Apache SAPI to build shared modules.
%endif
%endif

# filter depends on pcre
%if %{without pcre}
%undefine	with_filter
%endif

%define		rel	0.1
Summary:	PHP: Hypertext Preprocessor
Summary(fr.UTF-8):	Le langage de script embarque-HTML PHP
Summary(pl.UTF-8):	Język skryptowy PHP
Summary(pt_BR.UTF-8):	A linguagem de script PHP
Summary(ru.UTF-8):	PHP Версии 5 - язык препроцессирования HTML-файлов, выполняемый на сервере
Summary(uk.UTF-8):	PHP Версії 5 - мова препроцесування HTML-файлів, виконувана на сервері
Name:		php
Version:	5.3.6
Release:	%{rel}%{?with_type_hints:.th}%{?with_oci8:.oci}
Epoch:		4
License:	PHP
Group:		Libraries
Source0:	http://www.php.net/distributions/%{name}-%{version}.tar.bz2
# Source0-md5:	2286f5a82a6e8397955a0025c1c2ad98
Source2:	%{name}-mod_%{name}.conf
Source3:	%{name}-cgi-fcgi.ini
Source4:	%{name}-apache.ini
Source5:	%{name}-cli.ini
# Taken from: http://browsers.garykeith.com/downloads.asp
Source9:	%{name}_browscap.ini
Source10:	%{name}-fpm.init
Source11:	%{name}-fpm.logrotate
Source12:	%{name}-branch.sh
Source13:	dep-tests.sh
Source14:	skip-tests.sh
Source15:	http://litespeedtech.com/packages/lsapi/%{name}-litespeed-%{litespeed_version}.tgz
# Source15-md5:	9d58485d5fd6b5f5fefcec41b9ce283e
Patch0:		%{name}-shared.patch
Patch1:		%{name}-pldlogo.patch
Patch2:		%{name}-mail.patch
Patch3:		%{name}-link-libs.patch
Patch4:		%{name}-libpq_fs_h_path.patch
Patch5:		%{name}-filter-shared.patch
Patch6:		%{name}-build_modules.patch
Patch7:		%{name}-sapi-ini-file.patch
Patch8:		%{name}-config-file-scan-dir.patch
Patch9:		%{name}-sh.patch
Patch10:	%{name}-ini.patch
%if %{with type_hints}
Patch12:	http://ilia.ws/patch/type_hint_53_v2.txt
%endif
Patch14:	%{name}-no_pear_install.patch
Patch15:	%{name}-zlib.patch
Patch17:	%{name}-readline.patch
Patch18:	%{name}-nohttpd.patch
Patch19:	%{name}-gd_imagerotate_enable.patch
Patch20:	%{name}-uint32_t.patch
Patch21:	%{name}-dba-link.patch
Patch22:	%{name}-both-apxs.patch
Patch23:	%{name}-builddir.patch
Patch24:	%{name}-zlib-for-getimagesize.patch
Patch25:	%{name}-stupidapache_version.patch
Patch26:	%{name}-pear.patch
Patch27:	%{name}-config-dir.patch
Patch29:	%{name}-fcgi-graceful.patch
Patch31:	%{name}-fcgi-error_log-no-newlines.patch
Patch32:	%{name}-curl-limit-speed.patch
Patch34:	%{name}-libtool.patch
Patch35:	%{name}-tds.patch
Patch36:	%{name}-mysql-charsetphpini.patch
Patch37:	%{name}-mysqli-charsetphpini.patch
Patch38:	%{name}-pdo_mysql-charsetphpini.patch
Patch39:	%{name}-use-prog_sendmail.patch
Patch41:	%{name}-fpm-config.patch
Patch42:	%{name}-fpm-shared.patch
Patch43:	%{name}-silent-session-cleanup.patch
Patch44:	%{name}-include_path.patch
Patch45:	%{name}-imap-annotations.patch
Patch46:	%{name}-imap-myrights.patch
Patch47:	suhosin.patch
Patch49:	%{name}-m4-divert.patch
Patch50:	extension-shared-optional-dep.patch
Patch51:	spl-shared.patch
Patch52:	pcre-shared.patch
Patch53:	fix-test-run.patch
Patch54:	mysqlnd-shared.patch
Patch55:	bug-52078-fileinode.patch
Patch57:	bug-52448.patch
Patch59:	%{name}-systzdata.patch
Patch60:	%{name}-oracle-instantclient.patch
Patch61:	%{name}-krb5-ac.patch
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
#BuildRequires:	fcgi-devel
#BuildRequires:	flex
BuildRequires:	mysql-devel
BuildRequires:	pkgconfig
BuildRequires:	sed >= 4.0
%if %{with mssql} || %{with sybase_ct}
BuildRequires:	freetds-devel >= 0.82
%endif
BuildRequires:	freetype-devel >= 2.0
%if %{with system_gd}
BuildRequires:	gd-devel >= 2.0.28-4
BuildRequires:	gd-devel(imagerotate) = 5.2.0
%endif
BuildRequires:	gdbm-devel
BuildRequires:	gmp-devel
%{?with_imap:BuildRequires:	imap-devel >= 1:2007e-2}
BuildRequires:	libicu-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libltdl-devel >= 1.4
BuildRequires:	libmcrypt-devel >= 2.4.4
BuildRequires:	libpng-devel >= 1.0.8
#BuildRequires:	libtiff-devel
%if "%{pld_release}" != "ac"
BuildRequires:	libtool >= 2:2.2
%else
BuildRequires:	libtool >= 1.4.3
%endif
#BuildRequires:	libwrap-devel
BuildRequires:	libxml2-devel >= 1:2.7.6-4
BuildRequires:	libxslt-devel >= 1.1.0
%{?with_mm:BuildRequires:	mm-devel >= 1.3.0}
%{?with_ldap:BuildRequires:	openldap-devel >= 2.3.0}
%if %{with openssl} || %{with ldap}
BuildRequires:	openssl-devel >= 0.9.7d
%endif
%{?with_gcov:BuildRequires:	lcov}
%{?with_snmp:%{?with_tests:BuildRequires:	mibs-net-snmp}}
%{?with_snmp:BuildRequires:	net-snmp-devel >= 5.0.7}
%{?with_instantclient:BuildRequires:	oracle-instantclient-devel}
BuildRequires:	pam-devel
%{?with_pcre:BuildRequires:	pcre-devel >= 8.10}
BuildRequires:	pkgconfig
%{?with_pgsql:BuildRequires:	postgresql-backend-devel >= 7.2}
%{?with_pgsql:BuildRequires:	postgresql-devel}
BuildRequires:	readline-devel
%{?with_recode:BuildRequires:	recode-devel >= 3.5d-3}
BuildRequires:	rpm >= 4.4.9-56
BuildRequires:	rpm-build >= 4.4.0
BuildRequires:	rpmbuild(macros) >= 1.566
%{?with_sqlite:BuildRequires:	sqlite-devel}
%{?with_sqlite3:BuildRequires:	sqlite3-devel >= 3.3.9}
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
%if %{with fpm}
#BuildRequires:	judy-devel
BuildRequires:	libevent-devel >= 1.4.7-3
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		php_sysconfdir		/etc/php
%define		php_extensiondir	%{_libdir}/php
%define		_sysconfdir			%{php_sysconfdir}

# must be in sync with source. extra check ensuring that it is so is done in %%build
%define		php_api_version		20090626
%define		zend_module_api		20090626
%define		zend_extension_api	220090626

%define		zend_zts		%{!?with_zts:0}%{?with_zts:1}
%define		php_debug		%{!?debug:0}%{?debug:1}

%if %{with gcov}
%undefine	with_ccache
%endif

%if %{with oci8}
# ORACLE_HOME is required for oci8 ext to build
%define _preserve_env %_preserve_env_base ORACLE_HOME
%endif

%description
PHP is an HTML-embedded scripting language. PHP attempts to make it
easy for developers to write dynamically generated web pages. PHP also
offers built-in database integration for several commercial and
non-commercial database management systems, so writing a
database-enabled web page with PHP is fairly simple. The most common
use of PHP coding is probably as a replacement for CGI scripts. The
mod_php module enables the Apache web server to understand and process
the embedded PHP language in web pages. This package contains PHP
version %{version}.

%description -l fr.UTF-8
PHP est un langage de script embarque dans le HTM. PHP essaye de
rendre simple aux developpeurs d'ecrire des pages web generees
dynamiquement. PHP incorpore egalement une integration avec plusieurs
systemes de gestion de bases de donnees commerciaux et
non-connerciaux, qui rent facile la creation de pages web liees avec
des bases de donnees. L'utilisation la plus commune de PHP est
probablement en remplacement de scripts CGI. Le module mod_php permet
au serveur web Apache de comprendre et de traiter le langage PHP
integre dans des pages web. Ce package contient PHP version
%{version}.

%description -l pl.UTF-8
PHP jest językiem skryptowym, którego polecenia umieszcza się w
plikach HTML. Jest próbą ułatwienia programistom pisania dynamicznie
generowanych stron WWW. Oferuje także wbudowaną integrację z bazami
danych dla kilku komercyjnych i niekomercyjnych systemów baz danych,
co czyni tworzenie stron korzystających z baz danych w miarę łatwym.
Najczęściej PHP jest używany prawdopodobnie jako zamiennik skryptów
CGI. Moduł mod_php pozwala serwerowi WWW Apache rozumieć i przetwarzać
język PHP osadzony w stronach. Ten pakiet zawiera PHP w wersji
%{version}.

%description -l pt_BR.UTF-8
PHP: Preprocessador de Hipertexto versão 4 é uma linguagem script
embutida em HTML. Muito de sua sintaxe é emprestada de C, Java e Perl,
com algumas características únicas, específicas ao PHP. O objetivo da
linguagem é permitir que desenvolvedores web escrevam páginas
dinamicamente geradas de forma rápida.

%description -l ru.UTF-8
PHP - это язык написания скриптов, встраиваемых в HTML-код. PHP
предлагает интерграцию с множеством СУБД, поэтому написание скриптов
для работы с базами данных относительно просто. Наиболее популярное
использование PHP - замена для CGI скриптов.

%description -l uk.UTF-8
PHP - це мова написання скриптів, що вбудовуються в HTML-код. PHP
пропонує інтеграцію з багатьма СУБД, тому написання скриптів для
роботи з базами даних є доволі простим. Найбільш популярне
використання PHP - заміна для CGI скриптів.

%package -n apache1-mod_php
Summary:	PHP DSO module for Apache 1.3.x
Summary(pl.UTF-8):	Moduł DSO (Dynamic Shared Object) PHP dla Apache 1.3.x
Group:		Development/Languages/PHP
Requires(triggerpostun):	sed >= 4.0
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	apache1(EAPI) >= 1.3.33-2
Requires:	apache1-mod_mime
Provides:	webserver(php) = %{version}
Obsoletes:	apache-mod_php < 1:4.1.1
Obsoletes:	phpfi

%description -n apache1-mod_php
PHP as DSO module for Apache 1.3.x.

%description -n apache1-mod_php -l pl.UTF-8
PHP jako moduł DSO (Dynamic Shared Object) dla Apache 1.3.x.

%package -n apache-mod_php
Summary:	PHP DSO module for Apache 2.x
Summary(pl.UTF-8):	Moduł DSO (Dynamic Shared Object) PHP dla Apache 2.x
Group:		Development/Languages/PHP
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	apache(modules-api) = %{apache_modules_api}
Requires:	apache-mod_mime
Provides:	webserver(php) = %{version}
Obsoletes:	phpfi

%description -n apache-mod_php
PHP as DSO module for Apache 2.x.

%description -n apache-mod_php -l pl.UTF-8
PHP jako moduł DSO (Dynamic Shared Object) dla Apache 2.x.

%package litespeed
Summary:	PHP for litespeed HTTP server
Summary(pl.UTF-8):	PHP dla serwera HTTP litespeed
Group:		Development/Languages/PHP
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	webserver(php) = %{version}

%description litespeed
PHP for litespeed HTTP server.

%description litespeed -l pl.UTF-8
PHP dla serwera HTTP litespeed.

%package cgi
Summary:	PHP as CGI/FastCGI program
Summary(pl.UTF-8):	PHP jako program CGI/FastCGI
Group:		Development/Languages/PHP
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	%{name}-fcgi = %{epoch}:%{version}-%{release}
Provides:	php(cgi)
Provides:	php(fcgi)
Provides:	webserver(php)
Obsoletes:	php-fcgi < 4:5.3.0

%description cgi
PHP as CGI or FastCGI program.

%description cgi -l pl.UTF-8
PHP jako program CGI lub FastCGI.

%package cli
Summary:	PHP as CLI interpreter
Summary(pl.UTF-8):	PHP jako interpreter działający z linii poleceń
Group:		Development/Languages/PHP
Requires:	%{name}-common = %{epoch}:%{version}-%{release}

%description cli
PHP as CLI interpreter.

%description cli -l pl.UTF-8
PHP jako interpreter działający z linii poleceń.

%package program
Summary:	/usr/bin/php symlink
Summary(pl.UTF-8):	Dowiązanie symboliczne /usr/bin/php
Group:		Development/Languages/PHP
Requires:	%{name}-cli = %{epoch}:%{version}-%{release}
Obsoletes:	/usr/bin/php

%description program
Package providing /usr/bin/php symlink to PHP CLI.

%description program -l pl.UTF-8
Pakiet dostarczający dowiązanie symboliczne /usr/bin/php do PHP CLI.

%package fpm
Summary:	PHP FastCGI Process Manager
Summary(pl.UTF-8):	PHP FastCGI Process Manager - zarządca procesów FastCGI
Group:		Development/Languages/PHP
URL:		http://www.php-fpm.org/
Requires(post,preun):	/sbin/chkconfig
Requires(postun):	/usr/sbin/userdel
Requires(pre):	/bin/id
Requires(pre):	/usr/sbin/useradd
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	libevent >= 1.4.7-3
Requires:	rc-scripts
Provides:	user(http)
Provides:	webserver(php) = %{version}

%description fpm
PHP FastCGI Process Manager.

%description fpm -l pl.UTF-8
PHP FastCGI Process Manager - zarządca procesów FastCGI.

%package common
Summary:	Common files needed by both Apache modules and CGI/CLI SAPIs
Summary(pl.UTF-8):	Wspólne pliki dla modułu Apache'a i programu CGI
Summary(ru.UTF-8):	Разделяемые библиотеки для PHP
Summary(uk.UTF-8):	Бібліотеки спільного використання для PHP
Group:		Libraries
Requires(post):	sed >= 4.0
# because of dlclose() bugs in glibc <= 2.3.4 causing SEGVs on exit
Requires:	glibc >= 6:2.3.5
Requires:	php-dirs
Requires:	rpm-whiteout >= 1.28
Requires:	tzdata
Provides:	php(date)
Provides:	php(ereg)
Provides:	php(hash)
Provides:	php(libxml)
Provides:	php(modules_api) = %{php_api_version}
Provides:	php(overload)
Provides:	php(reflection)
Provides:	php(standard)
Provides:	php(zend_extension_api) = %{zend_extension_api}
Provides:	php(zend_module_api) = %{zend_module_api}
Provides:	php-date
Provides:	php-ereg
Provides:	php-overload
Provides:	php-reflection
Provides:	php-standard
Provides:	php5(debug) = %{php_debug}
Provides:	php5(thread-safety) = %{zend_zts}
%{!?with_mysqlnd:Obsoletes:	php-mysqlnd}
Obsoletes:	php-pecl-domxml
Conflicts:	php4-common < 3:4.4.4-8
Conflicts:	rpm < 4.4.2-0.2

%description common
Common files needed by both Apache modules and CGI/CLI SAPIs.

%description common -l pl.UTF-8
Wspólne pliki dla modułu Apache'a i programu CGI.

%description common -l ru.UTF-8
Этот пакет содержит общие файлы для разных вариантов реализации PHP
(самодостаточной и в качестве модуля Apache).

%description common -l uk.UTF-8
Цей пакет містить спільні файли для різних варіантів реалізації PHP
(самодостатньої та в якості модуля Apache).

%package devel
Summary:	Files for PHP modules development
Summary(pl.UTF-8):	Pliki do kompilacji modułów PHP
Summary(pt_BR.UTF-8):	Arquivos de desenvolvimento para PHP
Summary(ru.UTF-8):	Пакет разработки для построения расширений PHP
Summary(uk.UTF-8):	Пакет розробки для побудови розширень PHP
Group:		Development/Languages/PHP
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	autoconf
Requires:	automake
%if "%{pld_release}" != "ac"
Requires:	libtool >= 2:2.2
%else
Requires:	libtool
%endif
%{?with_pcre:Requires:	pcre-devel >= 8.10}
Requires:	shtool
Obsoletes:	php-pear-devel
Obsoletes:	php4-devel

%description devel
The php-devel package lets you compile dynamic extensions to PHP.
Included here is the source for the PHP extensions. Instead of
recompiling the whole PHP binary to add support for, say, oracle,
install this package and use the new self-contained extensions
support. For more information, read the file
README.SELF-CONTAINED-EXTENSIONS.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki potrzebne do kompilacji modułów PHP. Zamiast
rekompilować całe PHP aby dodać obsługę np. oracle, można przy użyciu
tego pakietu skompilować samodzielne rozszerzenie. Więcej informacji o
samodzielnych rozszerzeniach można znaleźć w pliku
README.SELF-CONTAINED-EXTENSIONS.

%description devel -l pt_BR.UTF-8
Este pacote contém arquivos usados no desenvolvimento de programas ou
módulos PHP.

%description devel -l ru.UTF-8
Пакет php-devel дает возможность компилировать динамические расширения
PHP. Пакет включает исходный код этих расширений. Вместо повторной
компиляции бинарного файла PHP для добавления, например, поддержки
oracle, установите этот пакет для компилирования отдельных расширений.
Подробности - в файле README.SELF-CONTAINED-EXTENSIONS.

%description devel -l uk.UTF-8
Пакет php-devel дає можливість компілювати динамічні розширення PHP.
До пакету включено вихідний код для розширень. Замість повторної
компіляції бінарного файлу PHP для додання, наприклад, підтримки
oracle, встановіть цей пакет для компіляції окремих розширень.
Детальніша інформація - в файлі README.SELF-CONTAINED-EXTENSIONS.

%package bcmath
Summary:	bcmath extension module for PHP
Summary(pl.UTF-8):	Moduł bcmath dla PHP
Group:		Libraries
URL:		http://www.php.net/manual/en/book.bc.php
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php(bcmath)

%description bcmath
This is a dynamic shared object (DSO) for PHP that will add bc style
precision math functions support.

%description bcmath -l pl.UTF-8
Moduł PHP umożliwiający korzystanie z dokładnych funkcji
matematycznych takich jak w programie bc.

%package bz2
Summary:	Bzip2 extension module for PHP
Summary(pl.UTF-8):	Moduł bzip2 dla PHP
Group:		Libraries
URL:		http://www.php.net/manual/en/book.bzip2.php
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php(bz2)
Provides:	php(bzip2)
Provides:	php-bzip2 = %{epoch}:%{version}-%{release}
Obsoletes:	php-bzip2 < 4:5.2.14-3

%description bz2
This is a dynamic shared object (DSO) for PHP that will add bzip2
compression support to PHP.

%description bz2 -l pl.UTF-8
Moduł PHP umożliwiający używanie kompresji bzip2.

%package calendar
Summary:	Calendar extension module for PHP
Summary(pl.UTF-8):	Moduł funkcji kalendarza dla PHP
Group:		Libraries
URL:		http://www.php.net/manual/en/book.calendar.php
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php(calendar)

%description calendar
This is a dynamic shared object (DSO) for PHP that will add calendar
support.

%description calendar -l pl.UTF-8
Moduł PHP dodający wsparcie dla kalendarza.

%package ctype
Summary:	ctype extension module for PHP
Summary(pl.UTF-8):	Moduł ctype dla PHP
Group:		Libraries
URL:		http://www.php.net/manual/en/book.ctype.php
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php(ctype)

%description ctype
This is a dynamic shared object (DSO) for PHP that will add ctype
support.

%description ctype -l pl.UTF-8
Moduł PHP umożliwiający korzystanie z funkcji ctype.

%package curl
Summary:	curl extension module for PHP
Summary(pl.UTF-8):	Moduł curl dla PHP
Group:		Libraries
URL:		http://www.php.net/manual/en/book.curl.php
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php(curl)

%description curl
This is a dynamic shared object (DSO) for PHP that will add curl
support.

%description curl -l pl.UTF-8
Moduł PHP umożliwiający korzystanie z biblioteki curl.

%package dba
Summary:	DBA extension module for PHP
Summary(pl.UTF-8):	Moduł DBA dla PHP
Group:		Libraries
URL:		http://www.php.net/manual/en/book.dba.php
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php(dba)

%description dba
This is a dynamic shared object (DSO) for PHP that will add flat-file
databases (DBA) support.

%description dba -l pl.UTF-8
Moduł dla PHP dodający obsługę dla baz danych opartych na plikach
(DBA).

%package dom
Summary:	DOM extension module for PHP
Summary(pl.UTF-8):	Moduł DOM dla PHP
Group:		Libraries
URL:		http://www.php.net/manual/en/book.dom.php
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php(dom)
# it has some compatibility functions
Provides:	php(domxml)
Provides:	php-domxml = %{epoch}:%{version}-%{release}
Obsoletes:	php-domxml <= 3:4.3.8-1

%description dom
This is a dynamic shared object (DSO) for PHP that will add new DOM
support.

%description dom -l pl.UTF-8
Moduł PHP dodający nową obsługę DOM.

%package exif
Summary:	exif extension module for PHP
Summary(pl.UTF-8):	Moduł exif dla PHP
Group:		Libraries
URL:		http://www.php.net/manual/en/book.exif.php
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php(exif)

%description exif
This is a dynamic shared object (DSO) for PHP that will add EXIF tags
support in image files.

%description exif -l pl.UTF-8
Moduł PHP dodający obsługę znaczników EXIF w plikach obrazków.

%package fileinfo
Summary:	libmagic bindings
Summary(pl.UTF-8):	Wiązania do libmagic
Group:		Libraries
URL:		http://www.php.net/manual/en/book.fileinfo.php
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-pcre = %{epoch}:%{version}-%{release}
Provides:	php(fileinfo)
Obsoletes:	php-mime_magic
Obsoletes:	php-pecl-fileinfo

%description fileinfo
This extension allows retrieval of information regarding vast majority
of file. This information may include dimensions, quality, length
etc...

Additionally it can also be used to retrieve the MIME type for a
particular file and for text files proper language encoding.

%description fileinfo -l pl.UTF-8
To rozszerzenie pozwala na uzyskanie informacji dotyczących większości
plików. Informacje mogą zawierać wymiary, jakość, długość itp.

Ponadto rozszerzenie można wykorzystać do odczytania typu MIME danego
pliku oraz kodowania plików tekstowych.

%package filter
Summary:	Extension for safely dealing with input parameters
Summary(pl.UTF-8):	Rozszerzenie do bezpiecznej obsługi danych wejściowych
Group:		Libraries
URL:		http://www.php.net/manual/en/book.filter.php
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-pcre = %{epoch}:%{version}-%{release}
Provides:	php(filter)
Obsoletes:	php-pecl-filter

%description filter
We all know that you should always check input variables, but PHP does
not offer really good functionality for doing this in a safe way. The
Input Filter extension is meant to address this issue by implementing
a set of filters and mechanisms that users can use to safely access
their input data.

%description filter -l pl.UTF-8
Wiadomo, że trzeba zawsze sprawdzać zmienne wejściowe, ale PHP nie
oferuje naprawdę dobrej funkcjonalności do robienia tego w sposób
bezpieczny. Rozszerzenie Input Filter ma rozwiązać ten problem poprzez
zaimplementowanie zestawu filtrów i mechanizmów, których użytkownicy
mogą bezpiecznie używać do dostępu do danych.

%package ftp
Summary:	FTP extension module for PHP
Summary(pl.UTF-8):	Moduł FTP dla PHP
Group:		Libraries
URL:		http://www.php.net/manual/en/book.ftp.php
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php(ftp)

%description ftp
This is a dynamic shared object (DSO) for PHP that will add FTP
support.

%description ftp -l pl.UTF-8
Moduł PHP dodający obsługę protokołu FTP.

%package gd
Summary:	GD extension module for PHP
Summary(pl.UTF-8):	Moduł GD dla PHP
Group:		Libraries
URL:		http://www.php.net/manual/en/book.image.php
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
%if %{with system_gd}
Requires:	gd >= 2.0.28-4
Requires:	gd(gif)
Requires:	gd(imagerotate) = 5.2.0
%endif
Provides:	php(gd)

%description gd
This is a dynamic shared object (DSO) for PHP that will add GD
support, allowing you to create and manipulate images with PHP.

%description gd -l pl.UTF-8
Moduł PHP umożliwiający korzystanie z biblioteki GD, pozwalającej na
tworzenie i obróbkę obrazków.

%package gettext
Summary:	gettext extension module for PHP
Summary(pl.UTF-8):	Moduł gettext dla PHP
Group:		Libraries
URL:		http://www.php.net/manual/en/book.gettext.php
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php(gettext)

%description gettext
This is a dynamic shared object (DSO) for PHP that will add gettext
support.

%description gettext -l pl.UTF-8
Moduł PHP dodający obsługę lokalizacji przez gettext.

%package gmp
Summary:	gmp extension module for PHP
Summary(pl.UTF-8):	Moduł gmp dla PHP
Group:		Libraries
URL:		http://www.php.net/manual/en/book.gmp.php
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php(gmp)

%description gmp
This is a dynamic shared object (DSO) for PHP that will add arbitrary
length number support with GNU MP library.

%description gmp -l pl.UTF-8
Moduł PHP umożliwiający korzystanie z biblioteki gmp do obliczeń na
liczbach o dowolnej długości.

%package hash
Summary:	HASH Message Digest Framework
Summary(pl.UTF-8):	Szkielet do obliczania skrótów wiadomości
Group:		Libraries
URL:		http://www.php.net/manual/en/book.gmp.php
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php(hash)
Provides:	php(mhash)
Provides:	php-mhash = %{epoch}:%{version}-%{release}
Obsoletes:	php-mhash < 4:5.3.0
Obsoletes:	php-pecl-hash

%description hash
Native implementations of common message digest algorithms using a
generic factory method.

%description hash -l pl.UTF-8
Natywne implementacje popularnych algorytmów obliczania skrótów
wiadomości przy użyciu wspólnego interfejsu.

%package iconv
Summary:	iconv extension module for PHP
Summary(pl.UTF-8):	Moduł iconv dla PHP
Group:		Libraries
URL:		http://www.php.net/manual/en/book.iconv.php
Requires:	%{_libdir}/gconv
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	iconv
Provides:	php(iconv)

%description iconv
This is a dynamic shared object (DSO) for PHP that will add iconv
support.

%description iconv -l pl.UTF-8
Moduł PHP dodający obsługę iconv.

%package imap
Summary:	IMAP extension module for PHP
Summary(pl.UTF-8):	Moduł IMAP dla PHP
Summary(pt_BR.UTF-8):	Um módulo para aplicações PHP que usam IMAP
Group:		Libraries
URL:		http://www.php.net/manual/en/book.imap.php
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-pcre = %{epoch}:%{version}-%{release}
Requires:	imap-lib >= 1:2007e-2
Provides:	php(imap)

%description imap
This is a dynamic shared object (DSO) for PHP that will add IMAP
support.

%description imap -l pl.UTF-8
Moduł PHP dodający obsługę skrzynek IMAP.

%description imap -l pt_BR.UTF-8
Um módulo para aplicações PHP que usam IMAP.

%package interbase
Summary:	InterBase/Firebird database module for PHP
Summary(pl.UTF-8):	Moduł bazy danych InterBase/Firebird dla PHP
Group:		Libraries
URL:		http://www.php.net/manual/en/book.ibase.php
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php(interbase)
%{?with_interbase_inst:Autoreq:	false}

%description interbase
This is a dynamic shared object (DSO) for PHP that will add InterBase
and Firebird database support.

%description interbase -l pl.UTF-8
Moduł PHP umożliwiający dostęp do baz danych InterBase i Firebird.

%package intl
Summary:	Internationalization extension (ICU wrapper)
Summary(pl.UTF-8):	Rozszerzenie do internacjonalizacji (interfejs do ICU)
Group:		Libraries
URL:		http://www.php.net/intl
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php(intl)

%description intl
Internationalization extension (further is referred as Intl) is a
wrapper for ICU library, enabling PHP programmers to perform
UCA-conformant collation and date/time/number/currency formatting in
their scripts.

%description intl -l pl.UTF-8
Rozszerzenie do internacjonalizacji (dalej nazywane Intl) jest
interfejsem do biblioteki ICU, pozwalającym programistom PHP na
wykonywanie w skryptach porównań zgodnych z UCA oraz formatowania
daty/czasu/walut.

%package json
Summary:	PHP C extension for JSON serialization
Summary(pl.UTF-8):	Rozszerzenie C PHP dla serializacji JSON
Group:		Libraries
URL:		http://www.php.net/manual/en/book.json.php
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php(json)
Obsoletes:	php-pecl-json

%description json
php-json is an extremely fast PHP C extension for JSON (JavaScript
Object Notation) serialisation.

%description json -l pl.UTF-8
php-json to bardzo szybkie rozszerzenie C PHP dla serializacji JSON
(JavaScript Object Notation).

%package ldap
Summary:	LDAP extension module for PHP
Summary(pl.UTF-8):	Moduł LDAP dla PHP
Summary(pt_BR.UTF-8):	Um módulo para aplicações PHP que usam LDAP
Group:		Libraries
URL:		http://www.php.net/manual/en/book.ldap.php
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php(ldap)

%description ldap
This is a dynamic shared object (DSO) for PHP that will add LDAP
support.

%description ldap -l pl.UTF-8
Moduł PHP dodający obsługę LDAP.

%description ldap -l pt_BR.UTF-8
Um módulo para aplicações PHP que usam LDAP.

%package mbstring
Summary:	mbstring extension module for PHP
Summary(pl.UTF-8):	Moduł mbstring dla PHP
Group:		Libraries
URL:		http://www.php.net/manual/en/book.mbstring.php
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php(mbstring)

%description mbstring
This is a dynamic shared object (DSO) for PHP that will add multibyte
string support.

%description mbstring -l pl.UTF-8
Moduł PHP dodający obsługę ciągów znaków wielobajtowych.

%package mcrypt
Summary:	mcrypt extension module for PHP
Summary(pl.UTF-8):	Moduł mcrypt dla PHP
Group:		Libraries
URL:		http://www.php.net/manual/en/book.mcrypt.php
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php(mcrypt)

%description mcrypt
This is a dynamic shared object (DSO) for PHP that will add mcrypt
support.

%description mcrypt -l pl.UTF-8
Moduł PHP dodający możliwość szyfrowania poprzez bibliotekę mcrypt.

%package mssql
Summary:	MS SQL extension module for PHP
Summary(pl.UTF-8):	Moduł MS SQL dla PHP
Group:		Libraries
URL:		http://www.php.net/manual/en/book.mssql.php
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php(mssql)

%description mssql
This is a dynamic shared object (DSO) for PHP that will add MS SQL
databases support through FreeTDS library.

%description mssql -l pl.UTF-8
Moduł PHP dodający obsługę baz danych MS SQL poprzez bibliotekę
FreeTDS.

%package mysql
Summary:	MySQL database module for PHP
Summary(pl.UTF-8):	Moduł bazy danych MySQL dla PHP
Summary(pt_BR.UTF-8):	Um módulo para aplicações PHP que usam bancos de dados MySQL
Group:		Libraries
URL:		http://www.php.net/manual/en/book.mysql.php
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
%{?with_mysqlnd:Requires:	%{name}-mysqlnd = %{epoch}:%{version}-%{release}}
Provides:	php(mysql)

%description mysql
This is a dynamic shared object (DSO) for PHP that will add MySQL
database support.

%description mysql -l pl.UTF-8
Moduł PHP umożliwiający dostęp do bazy danych MySQL.

%description mysql -l pt_BR.UTF-8
Um módulo para aplicações PHP que usam bancos de dados MySQL.

%package mysqli
Summary:	MySQLi module for PHP
Summary(pl.UTF-8):	Moduł MySQLi dla PHP
Group:		Libraries
URL:		http://www.php.net/manual/en/book.mysqli.php
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
%{?with_mysqlnd:Requires:	%{name}-mysqlnd = %{epoch}:%{version}-%{release}}
Requires:	%{name}-spl = %{epoch}:%{version}-%{release}
Provides:	php(mysqli)

%description mysqli
This is a dynamic shared object (DSO) for PHP that will add MySQLi
(Improved MySQL) support. The difference between it and mysql module
is that it provides access to functionality of MySQL 4.1 and above.

%description mysqli -l pl.UTF-8
Moduł PHP umożliwiający udoskonalony dostęp do bazy danych MySQL.
Różnicą między nim a modułem mysql jest dostęp do funkcjonalności
MySQL w wersji 4.1 i nowszych.

%package mysqlnd
Summary:	MySQL Native Client Driver for PHP
Summary(pl.UTF-8):	Sterownik natywnego klienta MySQL dla PHP
Group:		Libraries
URL:		http://www.php.net/manual/en/book.mysqlnd.php
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php(mysqlnd)

%description mysqlnd
MySQL Native Driver is a replacement for the MySQL Client Library
(libmysql).

Because MySQL Native Driver is written as a PHP extension, it is
tightly coupled to the workings of PHP. This leads to gains in
efficiency, especially when it comes to memory usage, as the driver
uses the PHP memory management system. It also supports the PHP memory
limit. Using MySQL Native Driver leads to comparable or better
performance than using MySQL Client Library, it always ensures the
most efficient use of memory. One example of the memory efficiency is
the fact that when using the MySQL Client Library, each row is stored
in memory twice, whereas with the MySQL Native Driver each row is only
stored once in memory.

%description mysqlnd -l pl.UTF-8
MySQL Native Driver (natywny sterownik MySQL) to zamiennik biblioteki
klienckiej MySQL (libmysql).

Ponieważ sterownik natywny jest napisany jako rozszerzenie PHP, jest
ściśle powiązany z pracą PHP. Daje to większą wydajność, zwłaszcza
jeśli chodzi o wykorzystanie pamięci, jako że sterownik wykorzystuje
system zarządzania pamięcią PHP; obsługuje także ograniczenie pamięci
z PHP. Niniejszy sterownik ma wydajność porównywalną lub lepszą niż
biblioteka kliencka MySQL, a pamięć zawsze wykorzystuje efektywniej.
Przykładem tego może być fakt, że w przypadku biblioteki klienckiej
każdy wiersz jest przechowywany w pamięci dwukrotnie, natomiast przy
tym sterowniku - tylko raz.

%package oci8
Summary:	Oracle 8+ database module for PHP
Summary(pl.UTF-8):	Moduł bazy danych Oracle 8+ dla PHP
Group:		Libraries
URL:		http://www.php.net/manual/en/book.oci8.php
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php(oci8)
AutoReq:	false

%description oci8
This is a dynamic shared object (DSO) for PHP that will add Oracle 7,
8, 9 and 10 database support through Oracle8 Call-Interface (OCI8).

%description oci8 -l pl.UTF-8
Moduł PHP umożliwiający dostęp do bazy danych Oracle 7, 8, 9 i 10
poprzez interfejs Oracle8 Call-Interface (OCI8).

%package odbc
Summary:	ODBC extension module for PHP
Summary(pl.UTF-8):	Moduł ODBC dla PHP
Summary(pt_BR.UTF-8):	Um módulo para aplicações PHP que usam bases de dados ODBC
Group:		Libraries
URL:		http://www.php.net/manual/en/book.uodbc.php
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	unixODBC >= 2.1.1-3
Provides:	php(odbc)

%description odbc
This is a dynamic shared object (DSO) for PHP that will add ODBC
support.

%description odbc -l pl.UTF-8
Moduł PHP ze wsparciem dla ODBC.

%description odbc -l pt_BR.UTF-8
Um módulo para aplicações PHP que usam ODBC.

%package openssl
Summary:	OpenSSL extension module for PHP
Summary(pl.UTF-8):	Moduł OpenSSL dla PHP
Group:		Libraries
URL:		http://www.php.net/manual/en/book.openssl.php
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php(openssl)

%description openssl
This is a dynamic shared object (DSO) for PHP that will add OpenSSL
support.

%description openssl -l pl.UTF-8
Moduł PHP umożliwiający korzystanie z biblioteki OpenSSL.

%package pcntl
Summary:	Process Control extension module for PHP
Summary(pl.UTF-8):	Moduł Process Control dla PHP
Group:		Libraries
URL:		http://www.php.net/manual/en/book.pcntl.php
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php(pcntl)

%description pcntl
This is a dynamic shared object (DSO) for PHP that will add process
spawning and control support. It supports functions like fork(),
waitpid(), signal() etc.

%description pcntl -l pl.UTF-8
Moduł PHP umożliwiający tworzenie nowych procesów i kontrolę nad nimi.
Obsługuje funkcje takie jak fork(), waitpid(), signal() i podobne.

%package pcre
Summary:	PCRE extension module for PHP
Summary(pl.UTF-8):	Moduł PCRE dla PHP
Group:		Libraries
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php(pcre)

%description pcre
This is a dynamic shared object (DSO) for PHP that will add Perl
Compatible Regular Expression support.

%description pcre -l pl.UTF-8
Moduł PHP umożliwiający korzystanie z perlowych wyrażeń regularnych
(Perl Compatible Regular Expressions)

%package pdo
Summary:	PHP Data Objects (PDO)
Summary(pl.UTF-8):	Obsługa PHP Data Objects (PDO)
Group:		Libraries
URL:		http://www.php.net/manual/en/book.pdo.php
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-spl = %{epoch}:%{version}-%{release}
Provides:	php(pdo)
Obsoletes:	php-pecl-PDO

%description pdo
This is a dynamic shared object (DSO) for PHP that will add PDO
support.

%description pdo -l pl.UTF-8
Moduł PHP dodający obsługę PDO (PHP Data Objects).

%package pdo-dblib
Summary:	PHP Data Objects (PDO) FreeTDS support
Summary(pl.UTF-8):	Moduł PHP Data Objects (PDO) z obsługą FreeTDS
Group:		Libraries
URL:		http://www.php.net/manual/en/ref.pdo-dblib.php
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-pdo = %{epoch}:%{version}-%{release}
Provides:	php(dblib)

%description pdo-dblib
This is a dynamic shared object (DSO) for PHP that will add PDO
FreeTDS support.

%description pdo-dblib -l pl.UTF-8
Moduł dla PHP dodający obsługę baz danych FreeTDS za pośrednictwem
interfejsu PDO.

%package pdo-firebird
Summary:	PHP Data Objects (PDO) Firebird support
Summary(pl.UTF-8):	Moduł PHP Data Objects (PDO) z obsługą Firebirda
Group:		Libraries
URL:		http://www.php.net/manual/en/ref.pdo-firebird.php
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-pdo = %{epoch}:%{version}-%{release}
Provides:	php(pdo-firebird)
Obsoletes:	php-pecl-PDO_FIREBIRD

%description pdo-firebird
This is a dynamic shared object (DSO) for PHP that will add PDO
Firebird support.

%description pdo-firebird -l pl.UTF-8
Moduł dla PHP dodający obsługę baz danych Firebird za pośrednictwem
interfejsu PDO.

%package pdo-mysql
Summary:	PHP Data Objects (PDO) MySQL support
Summary(pl.UTF-8):	Moduł PHP Data Objects (PDO) z obsługą MySQL-a
Group:		Libraries
URL:		http://www.php.net/manual/en/ref.pdo-mysql.php
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
%{?with_mysqlnd:Requires:	%{name}-mysqlnd = %{epoch}:%{version}-%{release}}
Requires:	%{name}-pdo = %{epoch}:%{version}-%{release}
Provides:	php(pdo-mysql)
Obsoletes:	php-pecl-PDO_MYSQL

%description pdo-mysql
This is a dynamic shared object (DSO) for PHP that will add PDO MySQL
support.

%description pdo-mysql -l pl.UTF-8
Moduł dla PHP dodający obsługę baz danych MySQL za pośrednictwem
interfejsu PDO.

%package pdo-oci
Summary:	PHP Data Objects (PDO) Oracle support
Summary(pl.UTF-8):	Moduł PHP Data Objects (PDO) z obsługą Oracle'a
Group:		Libraries
URL:		http://www.php.net/manual/en/ref.pdo-oci.php
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-pdo = %{epoch}:%{version}-%{release}
Provides:	php(pdo-oci)
Obsoletes:	php-pecl-PDO_OCI

%description pdo-oci
This is a dynamic shared object (DSO) for PHP that will add PDO Oracle
support.

%description pdo-oci -l pl.UTF-8
Moduł dla PHP dodający obsługę baz danych Oracle za pośrednictwem
interfejsu PDO.

%package pdo-odbc
Summary:	PHP Data Objects (PDO) ODBC support
Summary(pl.UTF-8):	Moduł PHP Data Objects (PDO) z obsługą ODBC
Group:		Libraries
URL:		http://www.php.net/manual/en/ref.pdo-odbc.php
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-pdo = %{epoch}:%{version}-%{release}
Provides:	php(pdo-odbc)
Obsoletes:	php-pecl-PDO_ODBC

%description pdo-odbc
This is a dynamic shared object (DSO) for PHP that will add PDO ODBC
support.

%description pdo-odbc -l pl.UTF-8
Moduł dla PHP dodający obsługę baz danych ODBC za pośrednictwem
interfejsu PDO.

%package pdo-pgsql
Summary:	PHP Data Objects (PDO) PostgreSQL support
Summary(pl.UTF-8):	Moduł PHP Data Objects (PDO) z obsługą PostgreSQL-a
Group:		Libraries
URL:		http://www.php.net/manual/en/ref.pdo-pgsql.php
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-pdo = %{epoch}:%{version}-%{release}
Provides:	php(pdo-pgsql)
Provides:	php-pecl-PDO_PGSQL
Obsoletes:	php-pecl-PDO_PGSQL < 4:5.2.1-2

%description pdo-pgsql
This is a dynamic shared object (DSO) for PHP that will add PDO
PostgreSQL support.

%description pdo-pgsql -l pl.UTF-8
Moduł dla PHP dodający obsługę baz danych PostgreSQL za pośrednictwem
interfejsu PDO.

%package pdo-sqlite
Summary:	PHP Data Objects (PDO) SQLite support
Summary(pl.UTF-8):	Moduł PHP Data Objects (PDO) z obsługą SQLite
Group:		Libraries
URL:		http://www.php.net/manual/en/ref.pdo-sqlite.php
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-pdo = %{epoch}:%{version}-%{release}
Provides:	php(pdo-sqlite)
Obsoletes:	php-pecl-PDO_SQLITE

%description pdo-sqlite
This is a dynamic shared object (DSO) for PHP that will add PDO SQLite
support.

%description pdo-sqlite -l pl.UTF-8
Moduł dla PHP dodający obsługę baz danych SQLite za pośrednictwem
interfejsu PDO.

%package pgsql
Summary:	PostgreSQL database module for PHP
Summary(pl.UTF-8):	Moduł bazy danych PostgreSQL dla PHP
Group:		Libraries
URL:		http://www.php.net/manual/en/book.pgsql.php
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php(pgsql)

%description pgsql
This is a dynamic shared object (DSO) for PHP that will add PostgreSQL
database support.

%description pgsql -l pl.UTF-8
Moduł PHP umożliwiający dostęp do bazy danych PostgreSQL.

%description pgsql -l pt_BR.UTF-8
Um módulo para aplicações PHP que usam bancos de dados postgresql.

%package phar
Summary:	phar database module for PHP
Summary(pl.UTF-8):	Moduł phar dla PHP
Group:		Libraries
URL:		http://www.php.net/manual/en/book.phar.php
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-spl = %{epoch}:%{version}-%{release}
Provides:	php(phar)

%description phar
This is a dynamic shared object (DSO) for PHP that will add phar
archive a support.

%description phar -l pl.UTF-8
Moduł PHP umożliwiający dostęp do achiwów .phar.

%package posix
Summary:	POSIX extension module for PHP
Summary(pl.UTF-8):	Moduł POSIX dla PHP
Group:		Libraries
URL:		http://www.php.net/manual/en/book.posix.php
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php(posix)

%description posix
This is a dynamic shared object (DSO) for PHP that will add POSIX
functions support to PHP.

%description posix -l pl.UTF-8
Moduł PHP umożliwiający korzystanie z funkcji POSIX.

%package pspell
Summary:	pspell extension module for PHP
Summary(pl.UTF-8):	Moduł pspell dla PHP
Group:		Libraries
URL:		http://www.php.net/manual/en/book.pspell.php
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php(pspell)

%description pspell
This is a dynamic shared object (DSO) for PHP that will add pspell
support to PHP. It allows to check the spelling of a word and offer
suggestions.

%description pspell -l pl.UTF-8
Moduł PHP umożliwiający korzystanie z pspella. Pozwala on na
sprawdzanie pisowni słowa i sugerowanie poprawek.

%package readline
Summary:	readline extension module for PHP
Summary(pl.UTF-8):	Moduł readline dla PHP
Group:		Libraries
URL:		http://www.php.net/manual/en/book.readline.php
Requires:	%{name}-cli = %{epoch}:%{version}-%{release}
Provides:	php(readline)

%description readline
This PHP module adds support for readline functions (only for cli and
cgi SAPIs).

%description readline -l pl.UTF-8
Moduł PHP dodający obsługę funkcji readline (tylko do SAPI cli i cgi).

%package recode
Summary:	recode extension module for PHP
Summary(pl.UTF-8):	Moduł recode dla PHP
Group:		Libraries
URL:		http://www.php.net/manual/en/book.recode.php
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	recode >= 3.5d-3
Provides:	php(recode)

%description recode
This is a dynamic shared object (DSO) for PHP that will add recode
support.

%description recode -l pl.UTF-8
Moduł PHP dodający możliwość konwersji kodowania plików (poprzez
bibliotekę recode).

%package session
Summary:	session extension module for PHP
Summary(pl.UTF-8):	Moduł session dla PHP
Group:		Libraries
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-spl = %{epoch}:%{version}-%{release}
Suggests:	%{name}-hash = %{epoch}:%{version}-%{release}
Provides:	php(session)

%description session
This is a dynamic shared object (DSO) for PHP that will add session
support.

%description session -l pl.UTF-8
Moduł PHP dodający obsługę sesji.

%package shmop
Summary:	Shared Memory Operations extension module for PHP
Summary(pl.UTF-8):	Moduł shmop dla PHP
Group:		Libraries
URL:		http://www.php.net/manual/en/book.shmop.php
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php(shmop)

%description shmop
This is a dynamic shared object (DSO) for PHP that will add Shared
Memory Operations support.

%description shmop -l pl.UTF-8
Moduł PHP umożliwiający korzystanie z pamięci dzielonej.

%package simplexml
Summary:	Simple XML extension module for PHP
Summary(pl.UTF-8):	Moduł prostego rozszerzenia XML dla PHP
Group:		Libraries
URL:		http://www.php.net/manual/en/book.simplexml.php
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-spl = %{epoch}:%{version}-%{release}
Provides:	php(simplexml)

%description simplexml
This is a dynamic shared object (DSO) for PHP that will add Simple XML
support.

%description simplexml -l pl.UTF-8
Moduł PHP dodający obsługę prostego XML-a.

%package snmp
Summary:	SNMP extension module for PHP
Summary(pl.UTF-8):	Moduł SNMP dla PHP
Group:		Libraries
URL:		http://www.php.net/manual/en/book.snmp.php
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-sockets = %{epoch}:%{version}-%{release}
Provides:	php(snmp)

%description snmp
This is a dynamic shared object (DSO) for PHP that will add SNMP
support.

%description snmp -l pl.UTF-8
Moduł PHP dodający obsługę SNMP.

%package soap
Summary:	soap extension module for PHP
Summary(pl.UTF-8):	Moduł soap dla PHP
Group:		Libraries
URL:		http://www.php.net/manual/en/book.soap.php
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php(soap)

%description soap
This is a dynamic shared object (DSO) for PHP that will add SOAP/WSDL
support.

%description soap -l pl.UTF-8
Moduł PHP dodający obsługę SOAP/WSDL.

%package sockets
Summary:	sockets extension module for PHP
Summary(pl.UTF-8):	Moduł socket dla PHP
Group:		Libraries
URL:		http://www.php.net/manual/en/book.sockets.php
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php(sockets)

%description sockets
This is a dynamic shared object (DSO) for PHP that will add sockets
support.

%description sockets -l pl.UTF-8
Moduł PHP dodający obsługę gniazdek.

%package spl
Summary:	Standard PHP Library module for PHP
Summary(pl.UTF-8):	Moduł biblioteki standardowej (Standard PHP Library) dla PHP
Group:		Libraries
URL:		http://php.net/manual/en/book.spl.php
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-pcre = %{epoch}:%{version}-%{release}
Requires:	%{name}-simplexml = %{epoch}:%{version}-%{release}
Provides:	php(spl)

%description spl
This is a dynamic shared object (DSO) for PHP that will add Standard
PHP Library support.

%description spl -l pl.UTF-8
Moduł PHP z biblioteką standardową PHP (SPL - Standard PHP Library).

%package sqlite
Summary:	SQLite extension module for PHP
Summary(pl.UTF-8):	Moduł SQLite dla PHP
Group:		Libraries
URL:		http://www.php.net/manual/en/book.sqlite.php
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-pdo = %{epoch}:%{version}-%{release}
Requires:	%{name}-spl = %{epoch}:%{version}-%{release}
Provides:	php(sqlite)

%description sqlite
SQLite is a C library that implements an embeddable SQL database
engine. Programs that link with the SQLite library can have SQL
database access without running a separate RDBMS process.

SQLite is not a client library used to connect to a big database
server. SQLite is the server. The SQLite library reads and writes
directly to and from the database files on disk.

%description sqlite -l pl.UTF-8
SQLite jest napisaną w C biblioteką implementującą osadzalny silnik
bazodanowy SQL. Program linkujący się z biblioteką SQLite może mieć
dostęp do bazy SQL bez potrzeby uruchamiania dodatkowego procesu
RDBMS.

SQLite to nie klient baz danych - biblioteka nie łączy się z serwerami
baz danych. SQLite sam jest serwerem. Biblioteka SQLite czyta i
zapisuje dane bezpośrednio z/do plików baz danych znajdujących się na
dysku.

%package sqlite3
Summary:	SQLite3 extension module for PHP
Summary(pl.UTF-8):	Moduł SQLite3 dla PHP
Group:		Libraries
URL:		http://php.net/manual/en/book.sqlite3.php
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php(sqlite3)

%description sqlite3
SQLite is a C library that implements an embeddable SQL database
engine. Programs that link with the SQLite library can have SQL
database access without running a separate RDBMS process.

SQLite is not a client library used to connect to a big database
server. SQLite is the server. The SQLite library reads and writes
directly to and from the database files on disk.

%description sqlite3 -l pl.UTF-8
SQLite jest napisaną w C biblioteką implementującą osadzalny silnik
bazodanowy SQL. Program linkujący się z biblioteką SQLite może mieć
dostęp do bazy SQL bez potrzeby uruchamiania dodatkowego procesu
RDBMS.

SQLite to nie klient baz danych - biblioteka nie łączy się z serwerami
baz danych. SQLite sam jest serwerem. Biblioteka SQLite czyta i
zapisuje dane bezpośrednio z/do plików baz danych znajdujących się na
dysku.

%package sybase-ct
Summary:	Sybase-CT extension module for PHP
Summary(pl.UTF-8):	Moduł Sybase-CT dla PHP
Group:		Libraries
URL:		http://www.php.net/manual/en/book.sybase.php
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php(sybase-ct)
Obsoletes:	php-sybase

%description sybase-ct
This is a dynamic shared object (DSO) for PHP that will add Sybase and
MS SQL databases support through CT-lib.

%description sybase-ct -l pl.UTF-8
Moduł PHP dodający obsługę baz danych Sybase oraz MS SQL poprzez
CT-lib.

%package sysvmsg
Summary:	SysV msg extension module for PHP
Summary(pl.UTF-8):	Moduł SysV msg dla PHP
Group:		Libraries
URL:		http://www.php.net/manual/en/book.sem.php
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php(sysvmsg)

%description sysvmsg
This is a dynamic shared object (DSO) for PHP that will add SysV
message queues support.

%description sysvmsg -l pl.UTF-8
Moduł PHP umożliwiający korzystanie z kolejek komunikatów SysV.

%package sysvsem
Summary:	SysV sem extension module for PHP
Summary(pl.UTF-8):	Moduł SysV sem dla PHP
Group:		Libraries
URL:		http://www.php.net/manual/en/book.sem.php
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php(sysvsem)

%description sysvsem
This is a dynamic shared object (DSO) for PHP that will add SysV
semaphores support.

%description sysvsem -l pl.UTF-8
Moduł PHP umożliwiający korzystanie z semaforów SysV.

%package sysvshm
Summary:	SysV shm extension module for PHP
Summary(pl.UTF-8):	Moduł SysV shm dla PHP
Group:		Libraries
URL:		http://www.php.net/manual/en/book.shmop.php
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php(sysvshm)

%description sysvshm
This is a dynamic shared object (DSO) for PHP that will add SysV
Shared Memory support.

%description sysvshm -l pl.UTF-8
Moduł PHP umożliwiający korzystanie z pamięci dzielonej SysV.

%package tests
Summary:	Contains unit test files for PHP and extensions
Summary(pl.UTF-8):	Zawiera pliki testów jednostkowych dla PHP i rozszerzeń
Group:		Libraries
URL:		http://qa.php.net/
Requires:	%{name}-cli

%description tests
This package contains unit tests for PHP and it's extensions.

%description tests -l pl.UTF-8
Ten pakiet zawiera pliki testów jednostkowych dla PHP i rozszerzeń

%package tidy
Summary:	Tidy extension module for PHP
Summary(pl.UTF-8):	Moduł Tidy dla PHP
Group:		Libraries
URL:		http://www.php.net/manual/en/book.tidy.php
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	tidy
Provides:	php(tidy)

%description tidy
This is a dynamic shared object (DSO) for PHP that will add Tidy
support.

%description tidy -l pl.UTF-8
Moduł PHP umożliwiający korzystanie z tidy.

%package tokenizer
Summary:	tokenizer extension module for PHP
Summary(pl.UTF-8):	Moduł rozszerzenia tokenizer dla PHP
Group:		Libraries
URL:		http://www.php.net/manual/en/book.tokenizer.php
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php(tokenizer)

%description tokenizer
This is a dynamic shared object (DSO) for PHP that will add tokenizer
support.

%description tokenizer -l pl.UTF-8
Moduł PHP dodający obsługę tokenizera do PHP.

%package wddx
Summary:	wddx extension module for PHP
Summary(pl.UTF-8):	Moduł wddx dla PHP
Group:		Libraries
URL:		http://www.php.net/manual/en/book.wddx.php
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
# - wddx doesn't require session as it's disabled at compile time:
#   if HAVE_PHP_SESSION && !defined(COMPILE_DL_SESSION)
#   see also php.spec#rev1.120.2.22
#Requires:	%{name}-session = %{epoch}:%{version}-%{release}
Requires:	%{name}-xml = %{epoch}:%{version}-%{release}
Provides:	php(wddx)

%description wddx
This is a dynamic shared object (DSO) for PHP that will add wddx
support.

%description wddx -l pl.UTF-8
Moduł PHP umożliwiający korzystanie z wddx.

%package xml
Summary:	XML extension module for PHP
Summary(pl.UTF-8):	Moduł XML dla PHP
Group:		Libraries
URL:		http://www.php.net/manual/en/book.xml.php
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php(xml)

%description xml
This is a dynamic shared object (DSO) for PHP that will add XML
support. This extension lets you create XML parsers and then define
handlers for different XML events.

%description xml -l pl.UTF-8
Moduł PHP umożliwiający parsowanie plików XML i obsługę zdarzeń
związanych z tymi plikami. Pozwala on tworzyć analizatory XML-a i
następnie definiować procedury obsługi dla różnych zdarzeń XML.

%package xmlreader
Summary:	XML Reader extension module for PHP
Summary(pl.UTF-8):	Moduł XML Reader dla PHP
Group:		Libraries
URL:		http://www.php.net/manual/en/book.xmlreader.php
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Suggests:	%{name}-dom = %{epoch}:%{version}-%{release}
Provides:	php(xmlreader)

%description xmlreader
This is a dynamic shared object (DSO) for PHP that will add XML Reader
support. The XMLReader extension is an XML Pull parser. The reader
acts as a cursor going forward on the document stream and stopping at
each node on the way.

%description xmlreader -l pl.UTF-8
Moduł PHP umożliwiający analizę plików XML w trybie Pull. Czytnik
działa jako kursor przechodzący przez strumień dokumentu i
zatrzymujący się na każdym węźle po drodze.

%package xmlrpc
Summary:	xmlrpc extension module for PHP
Summary(pl.UTF-8):	Moduł xmlrpc dla PHP
Group:		Libraries
URL:		http://www.php.net/manual/en/book.xmlrpc.php
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-xml = %{epoch}:%{version}-%{release}
Provides:	php(xmlrpc)

%description xmlrpc
This is a dynamic shared object (DSO) for PHP that will add XMLRPC
support.

%description xmlrpc -l pl.UTF-8
Moduł PHP dodający obsługę XMLRPC.

%package xmlwriter
Summary:	Fast, non-cached, forward-only means to write XML data
Summary(pl.UTF-8):	Szybka, nie cachowana metoda zapisu danych w formacie XML
Group:		Libraries
URL:		http://www.php.net/manual/en/book.xmlwriter.php
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php(xmlwriter)
Obsoletes:	php-pecl-xmlwriter

%description xmlwriter
This extension wraps the libxml xmlWriter API. Represents a writer
that provides a non-cached, forward-only means of generating streams
or files containing XML data.

%description xmlwriter -l pl.UTF-8
To rozszerzenie obudowuje API xmlWriter z libxml. Reprezentuje obsługę
zapisu dostarczającą nie cachowanych metod generowania strumieni lub
plików zawierających dane XML.

%package xsl
Summary:	xsl extension module for PHP
Summary(pl.UTF-8):	Moduł xsl dla PHP
Group:		Libraries
URL:		http://www.php.net/manual/en/book.xsl.php
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-dom = %{epoch}:%{version}-%{release}
Requires:	libxslt >= 1.0.18
# actually not true, functionality is similar, but API differs
Provides:	php(xsl)
Obsoletes:	php-xslt <= 3:4.3.8-1

%description xsl
This is a dynamic shared object (DSO) for PHP that will add new XSL
support (using libxslt).

%description xsl -l pl.UTF-8
Moduł PHP dodający nową obsługę XSLT (przy użyciu libxslt).

%package zip
Summary:	Zip management extension
Summary(pl.UTF-8):	Zarządzanie archiwami zip
Group:		Libraries
URL:		http://www.php.net/manual/en/book.zip.php
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php(zip)
Obsoletes:	php-pecl-zip

%description zip
Zip is an extension to create, modify and read zip files.

%description zip -l pl.UTF-8
Zip jest rozszerzeniem umożliwiającym tworzenie, modyfikację oraz
odczyt archiwów zip.

%package zlib
Summary:	Zlib extension module for PHP
Summary(pl.UTF-8):	Moduł zlib dla PHP
Group:		Libraries
URL:		http://www.php.net/manual/en/book.zlib.php
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php(zlib)

%description zlib
This is a dynamic shared object (DSO) for PHP that will add zlib
compression support to PHP.

%description zlib -l pl.UTF-8
Moduł PHP umożliwiający używanie kompresji zlib.

%prep
%setup -q
# prep for suhosin patch
%{__sed} -i -e 's,\r$,,' Zend/Zend.dsp Zend/ZendTS.dsp
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch8 -p1
%patch7 -p1
%patch9 -p1
cp php.ini-production php.ini
%patch10 -p1
%if %{with type_hints}
%patch12 -p0
%endif
%patch14 -p1
%patch15 -p1
%patch17 -p1
%patch18 -p1
%if %{with system_gd}
%patch19 -p1
%endif
%patch20 -p1
%patch21 -p1
%patch22 -p1
%patch23 -p1
%patch24 -p1
%patch25 -p1
%patch26 -p1
%patch27 -p1
%patch29 -p1
%patch31 -p1
%patch32 -p1
%if "%{pld_release}" != "ac"
%patch34 -p1
%endif
%patch35 -p1
%patch36 -p1
%patch37 -p1
%patch38 -p1
%patch39 -p1
%if %{with fpm}
%patch41 -p1
%patch42 -p1
%endif
%patch43 -p1
%patch44 -p1
%patch45 -p1
%patch46 -p1
%if %{with suhosin}
%patch47 -p1
%endif
%patch49 -p1
%patch50 -p1
%patch51 -p1
%patch52 -p1
%patch53 -p1
%patch54 -p1
%undos ext/spl/tests/SplFileInfo_getInode_basic.phpt
%patch55 -p1
%patch57 -p1
%patch59 -p1
%patch60 -p1
%patch61 -p1

%{__rm} -r sapi/litespeed
gzip -dc %{SOURCE15} | tar xf - -C sapi/

%if "%{pld_release}" != "ac"
sed -i -e '/PHP_ADD_LIBRARY_WITH_PATH/s#xmlrpc,#xmlrpc-epi,#' ext/xmlrpc/config.m4
%endif

# cleanup backups after patching
find '(' -name '*~' -o -name '*.orig' ')' -print0 | xargs -0 -r -l512 rm -f

# conflict seems to be resolved by recode patches
%{__rm} ext/recode/config9.m4

# remove all bundled libraries not to link with them accidentally
#%{__rm} -r ext/sqlite/libsqlite
%{__rm} -r ext/sqlite3/libsqlite
#%{__rm} -r ext/bcmath/libbcmath
#%{__rm} -r ext/date/lib
#%{__rm} -r ext/fileinfo/libmagic
#%{__rm} -r ext/dba/libcdb
#%{__rm} -r ext/dba/libflatfile
#%{__rm} -r ext/dba/libinifile
#%{__rm} -r ext/gd/libgd
#%{__rm} -r ext/mbstring/libmbfl
#%{__rm} -r ext/mbstring/oniguruma
%{__rm} -r ext/pcre/pcrelib
#%{__rm} -r ext/soap/interop
%{__rm} -r ext/xmlrpc/libxmlrpc
#%{__rm} -r ext/zip/lib

cp -af Zend/LICENSE{,.Zend}
install -p %{SOURCE13} dep-tests.sh

# breaks build
sed -i -e 's#-fvisibility=hidden##g' configure*

# disable broken tests
# says just "Terminated" twice and fails
mv sapi/cli/tests/022.phpt{,.broken}

# php-5.3.3/ext/standard/tests/file/statpage.phpt
%{__rm} ext/standard/tests/file/statpage.phpt

# idiotic test, it will fail if somebody else makes space on disk or if disk
# space is not yet allocated (xfs). report upstream to advice bogus test is
# probably pointless.
%{__rm} ext/standard/tests/file/disk_free_space_basic.phpt

sh -xe %{_sourcedir}/skip-tests.sh

%build
API=$(awk '/#define PHP_API_VERSION/{print $3}' main/php.h)
if [ $API != %{php_api_version} ]; then
	echo "Set %%define php_api_version to $API and re-run."
	exit 1
fi

API=$(awk '/#define ZEND_MODULE_API_NO/{print $3}' Zend/zend_modules.h)
if [ $API != %{zend_module_api} ]; then
	echo "Set %%define zend_module_api to $API and re-run."
	exit 1
fi

API=$(awk '/#define ZEND_EXTENSION_API_NO/{print $3}' Zend/zend_extensions.h)
if [ $API != %{zend_extension_api} ]; then
	echo "Set %%define zend_extension_api to $API and re-run."
	exit 1
fi

export EXTENSION_DIR="%{php_extensiondir}"
# configure once (for faster debugging purposes)
if [ ! -f _built-conf ]; then
	# now remove Makefile copies
	rm -f Makefile.{cgi-fcgi,fpm,cli,apxs1,apxs2,litespeed}
	%{__libtoolize}
	%{__aclocal}
	cp -f /usr/share/automake/config.* .
	./buildconf --force
	touch _built-conf
fi
export PROG_SENDMAIL="/usr/lib/sendmail"
export CPPFLAGS="-DDEBUG_FASTCGI -DHAVE_STRNDUP %{rpmcppflags} \
	-I%{_includedir}/xmlrpc-epi"

sapis="
cli
%if %{with cgi}
cgi-fcgi
%endif
%if %{with litespeed}
litespeed
%endif
%if %{with fpm}
fpm
%endif
%if %{with apache1}
apxs1
%endif
%if %{with apache2}
apxs2
%endif
"
for sapi in $sapis; do
	: SAPI $sapi
	# skip if already configured (for faster debugging purposes)
	[ -f Makefile.$sapi ] && continue

	sapi_args=''
	case $sapi in
	cgi-fcgi)
		sapi_args='--disable-cli'
	;;
	cli)
		sapi_args='--disable-cgi %{?with_gcov:--enable-gcov}'
	;;
	fpm)
		sapi_args='--disable-cli --enable-fpm'
		;;
	apxs1)
		ver=$(rpm -q --qf '%{V}' apache1-devel)
		sapi_args="--disable-cli --with-apxs=%{apxs1} --with-apache-version=$ver"
	;;
	apxs2)
		ver=$(rpm -q --qf '%{V}' apache-devel)
		sapi_args="--disable-cli --with-apxs2=%{apxs2} --with-apache-version=$ver"
	;;
	litespeed)
		sapi_args='--with-litespeed'
	;;
	esac

	%configure \
	$sapi_args \
%if "%{!?configure_cache:0}%{?configure_cache}" == "0"
	--cache-file=config.cache \
%endif
	--with-libdir=%{_lib} \
	--with-config-file-path=%{_sysconfdir} \
	--with-config-file-scan-dir=%{_sysconfdir}/conf.d \
	--with-exec-dir=%{_bindir} \
	--with-system-tzdata \
	--%{!?debug:dis}%{?debug:en}able-debug \
	%{?with_zts:--enable-maintainer-zts} \
	--enable-inline-optimization \
	--enable-bcmath=shared \
	--enable-calendar=shared \
	--enable-ctype=shared \
	--enable-dba=shared \
	--enable-dom=shared \
	--enable-exif=shared \
	--enable-fileinfo=shared \
	--enable-ftp=shared \
	--enable-gd-native-ttf \
	--enable-intl=shared \
	--enable-libxml \
	--enable-magic-quotes \
	--enable-mbstring=shared,all \
	--enable-mbregex \
	--enable-pcntl=shared \
	--enable-pdo=shared \
	--enable-json=shared \
	--enable-hash=shared \
	--enable-xmlwriter=shared \
%if %{with fpm}
	--with-fpm-user=http \
	--with-fpm-group=http \
%endif
%if %{with mssql} || %{with sybase_ct}
	--with-pdo-dblib=shared \
%endif
%if %{with interbase} && %{without interbase_inst}
	--with-pdo-firebird=shared,/usr \
%endif
	--with-mysql-sock=/var/lib/mysql/mysql.sock \
	--with-pdo-mysql=shared%{?with_mysqlnd:,mysqlnd} \
	%{?with_oci8:--with-pdo-oci=shared%{?with_instantclient:,instantclient,%{_libdir}}} \
	%{?with_odbc:--with-pdo-odbc=shared,unixODBC,/usr} \
	%{?with_pgsql:--with-pdo-pgsql=shared} \
	%{?with_sqlite:--with-pdo-sqlite=shared,/usr} \
	--without-libexpat-dir \
	--enable-overload=shared \
	--enable-posix=shared \
	--enable-shared \
	--enable-session=shared \
	--enable-shmop=shared \
	--enable-simplexml=shared \
	--enable-spl=shared \
	--enable-sysvmsg=shared \
	--enable-sysvsem=shared \
	--enable-sysvshm=shared \
	--enable-safe-mode \
	--enable-soap=shared \
	--enable-sockets=shared \
	--enable-tokenizer=shared \
	--enable-ucd-snmp-hack \
	%{?with_wddx:--enable-wddx=shared} \
	--enable-xml=shared \
	--enable-xmlreader=shared \
	--with-bz2=shared \
	%{__with_without curl curl shared} \
	--with-db4 \
	--with-iconv=shared \
	--with-freetype-dir=shared \
	--with-gettext=shared \
	--with-gd=shared%{?with_system_gd:,/usr} \
	--with-gdbm \
	--with-gmp=shared \
	%{?with_imap:--with-imap=shared --with-imap-ssl} \
	%{?with_interbase:--with-interbase=shared%{!?with_interbase_inst:,/usr}} \
	--with-jpeg-dir=/usr \
	%{?with_ldap:--with-ldap=shared --with-ldap-sasl} \
	--with-mcrypt=shared \
	%{?with_mm:--with-mm} \
	%{?with_mssql:--with-mssql=shared} \
	%{?with_mysqlnd:--with-mysqlnd=shared} \
	--with-mysql=shared%{?with_mysqlnd:,mysqlnd} \
	%{?with_mysqli:--with-mysqli=shared%{?with_mysqlnd:,mysqlnd}} \
	%{?with_oci8:--with-oci8=shared%{?with_instantclient:,instantclient,%{_libdir}}} \
	%{?with_openssl:--with-openssl=shared} \
	--with-kerberos \
	%{__with_without pcre pcre-regex /usr} \
	%{__enable_disable filter filter shared} \
	--with-pear=%{php_pear_dir} \
	%{__with_without pgsql pgsql shared,/usr} \
	%{__enable_disable phar phar shared} \
	--with-png-dir=/usr \
	%{?with_pspell:--with-pspell=shared} \
	--with-readline=shared \
	%{?with_recode:--with-recode=shared} \
	--with-regex=system \
	%{?with_snmp:--with-snmp=shared} \
	%{?with_sybase_ct:--with-sybase-ct=shared,/usr} \
	%{!?with_sqlite:--without-sqlite --without-pdo-sqlite}%{?with_sqlite:--with-sqlite=shared,/usr --enable-sqlite-utf8} \
	%{__with_without sqlite3 sqlite3 shared,/usr} \
	--with-t1lib=shared \
	%{?with_tidy:--with-tidy=shared} \
	%{?with_odbc:--with-unixODBC=shared,/usr} \
	%{__with_without xmlrpc xmlrpc shared,/usr} \
	--with-xsl=shared \
	--with-zlib=shared \
	--with-zlib-dir=shared,/usr \
	--enable-zip=shared,/usr \

	# save for debug
	cp -f Makefile Makefile.$sapi
	cp -f main/php_config.h php_config.h.$sapi
	cp -f config.log config.log.$sapi
done

# as we build each SAPI in own make, adjust php-config.in forehead
sapis=$(awk '/^PHP_SAPI = /{print $3}' Makefile.* | sort -u | xargs)
sed -i -e "s,@PHP_INSTALLED_SAPIS@,$sapis," "scripts/php-config.in"

# must make libphp_common first, so modules can link against it.
cp -af php_config.h.cli main/php_config.h
cp -af Makefile.cli Makefile
%{__make} libphp_common.la
%{__make} build-modules

%if %{with apache1}
%{__make} libtool-sapi LIBTOOL_SAPI=sapi/apache/libphp5.la -f Makefile.apxs1
%endif

%if %{with apache2}
%{__make} libtool-sapi LIBTOOL_SAPI=sapi/apache2handler/libphp5.la -f Makefile.apxs2
%endif

%if %{with litespeed}
%{__make} -f Makefile.litespeed
%endif

# CGI/FCGI
%if %{with cgi}
cp -af php_config.h.cgi-fcgi main/php_config.h
%{__make} -f Makefile.cgi-fcgi
[ "$(echo '<?=php_sapi_name();' | ./sapi/cgi/php-cgi -qn)" = cgi-fcgi ] || exit 1
%endif

# PHP FPM
%if %{with fpm}
cp -af php_config.h.fpm main/php_config.h
%{__make} -f Makefile.fpm
 ./sapi/fpm/php-fpm -qn -m > /dev/null
%endif

# CLI
cp -af php_config.h.cli main/php_config.h
%{__make} -f Makefile.cli
[ "$(echo '<?=php_sapi_name();' | ./sapi/cli/php -qn)" = cli ] || exit 1

# check for stupid xml parse breakage where &lt; and &gt; just get lost in parse result
./sapi/cli/php -n -dextension_dir=modules -dextension=xml.so -r '$p = xml_parser_create(); xml_parse_into_struct($p, "<x>&lt;</x>", $vals, $index); exit((int )empty($vals[0]["value"]));'

# Generate stub .ini files for each extension
rm -rf conf.d
install -d conf.d
generate_inifiles() {
	for so in modules/*.so; do
		mod=$(basename $so .so)
		conf="$mod.ini"
		# xml needs to be loaded before wddx
		[ "$mod" = "wddx" ] && conf="xml_$mod.ini"
		# pre needs to be loaded before SPL
		[ "$mod" = "pcre" ] && conf="PCRE.ini"
		# spl needs to be loaded before mysqli
		[ "$mod" = "spl" ] && conf="SPL.ini"
		# session needs to be loaded before php-pecl-http, php-pecl-memcache, php-pecl-session_mysql
		[ "$mod" = "session" ] && conf="Session.ini"
		# mysqlnd needs to be loaded before mysql,mysqli,pdo_mysqli
		[ "$mod" = "mysqlnd" ] && conf="MySQLND.ini"
		echo "+ $conf"
		cat > conf.d/$conf <<-EOF
			; Enable $mod extension module
			extension=$mod.so
		EOF
	done
}
generate_inifiles

# Check that the module inner-dependencies are intact
PHP=./sapi/cli/php EXTENSION_DIR=modules CONFIG_DIR=conf.d ./dep-tests.sh > dep-tests.log
if grep -v OK dep-tests.log; then
	echo >&2 "The results above were not expected"
	exit 1
fi

%if %{with gcov}
# Use CLI SAPI
cp -af php_config.h.cli main/php_config.h
cp -af Makefile.cli Makefile
%{__make} lcov
# you really don't want to package result of gcov build
exit 1
%endif

%if %{with tests}
# Run tests, using the CLI SAPI
cp -af php_config.h.cli main/php_config.h
cp -af Makefile.cli Makefile

cat <<'EOF' > run-tests.sh
#!/bin/sh
export NO_INTERACTION=1 REPORT_EXIT_STATUS=1 MALLOC_CHECK_=2
unset TZ LANG LC_ALL || :
%{__make} test \
	EXTENSION_DIR=modules \
	PHP_TEST_SHARED_SYSTEM_EXTENSIONS= \
	RUN_TESTS_SETTINGS="-q $*"
EOF
chmod +x run-tests.sh
./run-tests.sh -w failed.log -s test.log

# collect failed tests into cleanup script used in prep.
sed -ne '/FAILED TEST SUMMARY/,/^===/p' test.log | sed -e '1,/^---/d;/^===/,$d' > tests-failed.log
sed -ne '/\[.*\]/{s/\(.*\) \[\(.*\)\]/# \1\nmv \2{,.skip}/p}' tests-failed.log \
	>> %{_sourcedir}/skip-tests.sh

failed=$(wc -l < tests-failed.log)
if [ "$failed" != 0 ]; then
	exit 1
fi
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir}/{php,apache{,1}},%{_sysconfdir}/{apache,cgi}} \
	$RPM_BUILD_ROOT{%{_sbindir},%{_bindir}} \
	$RPM_BUILD_ROOT/etc/{apache/conf.d,httpd/conf.d} \
	$RPM_BUILD_ROOT%{_mandir}/man{1,8} \

cp -af php_config.h.cli main/php_config.h
cp -af Makefile.cli Makefile
%{__make} install \
	INSTALL_ROOT=$RPM_BUILD_ROOT

# make link relative
ln -sfn phar.phar $RPM_BUILD_ROOT%{_bindir}/phar

# install Apache1 DSO module
%if %{with apache1}
libtool --mode=install install sapi/apache/libphp5.la $RPM_BUILD_ROOT%{_libdir}/apache1
%endif

# install Apache2 DSO module
%if %{with apache2}
libtool --mode=install install sapi/apache2handler/libphp5.la $RPM_BUILD_ROOT%{_libdir}/apache
%endif

# install litespeed sapi
%if %{with litespeed}
libtool --mode=install install sapi/litespeed/php $RPM_BUILD_ROOT%{_sbindir}/php.litespeed
%endif

libtool --mode=install install libphp_common.la $RPM_BUILD_ROOT%{_libdir}
# fix install paths, avoid evil rpaths
sed -i -e "s|^libdir=.*|libdir='%{_libdir}'|" $RPM_BUILD_ROOT%{_libdir}/libphp_common.la
# better solution?
sed -i -e 's|libphp_common.la|$(libdir)/libphp_common.la|' $RPM_BUILD_ROOT%{_libdir}/php/build/acinclude.m4

# install CGI/FCGI
%if %{with cgi}
libtool --mode=install install sapi/cgi/php-cgi $RPM_BUILD_ROOT%{_bindir}/php.cgi
ln -sf php.cgi $RPM_BUILD_ROOT%{_bindir}/php.fcgi
cp -a %{SOURCE3} $RPM_BUILD_ROOT%{_sysconfdir}/php-cgi-fcgi.ini
%endif

# install FCGI PM
%if %{with fpm}
install -d $RPM_BUILD_ROOT{%{_sysconfdir}/fpm.d,%{_sbindir}}
libtool --mode=install install sapi/fpm/php-fpm $RPM_BUILD_ROOT%{_sbindir}
cp -a sapi/fpm/php-fpm.8 $RPM_BUILD_ROOT%{_mandir}/man8
cp -a sapi/fpm/php-fpm.conf $RPM_BUILD_ROOT%{_sysconfdir}
install -d $RPM_BUILD_ROOT/etc/rc.d/init.d
install -p %{SOURCE10} $RPM_BUILD_ROOT/etc/rc.d/init.d/php-fpm
install -d $RPM_BUILD_ROOT/etc/logrotate.d
cp -a %{SOURCE11} $RPM_BUILD_ROOT/etc/logrotate.d/php-fpm
%endif

# install CLI
libtool --mode=install install sapi/cli/php $RPM_BUILD_ROOT%{_bindir}/php.cli
install sapi/cli/php.1 $RPM_BUILD_ROOT%{_mandir}/man1/php.1
echo ".so php.1" >$RPM_BUILD_ROOT%{_mandir}/man1/php.cli.1
ln -sf php.cli $RPM_BUILD_ROOT%{_bindir}/php

sed -e 's#%{_prefix}/lib/php#%{_libdir}/php#g' php.ini > $RPM_BUILD_ROOT%{_sysconfdir}/php.ini

cp -a %{SOURCE5} $RPM_BUILD_ROOT%{_sysconfdir}/php-cli.ini
cp -a %{SOURCE9} $RPM_BUILD_ROOT%{_sysconfdir}/browscap.ini

%if %{with apache1}
cp -a %{SOURCE2} $RPM_BUILD_ROOT/etc/apache/conf.d/70_mod_php.conf
cp -a %{SOURCE4} $RPM_BUILD_ROOT%{_sysconfdir}/php-apache.ini
rm -f $RPM_BUILD_ROOT%{_libdir}/apache1/libphp5.la
%endif

%if %{with apache2}
cp -a %{SOURCE2} $RPM_BUILD_ROOT/etc/httpd/conf.d/70_mod_php.conf
cp -a %{SOURCE4} $RPM_BUILD_ROOT%{_sysconfdir}/php-apache2handler.ini
rm -f $RPM_BUILD_ROOT%{_libdir}/apache/libphp5.la
%endif

install -d $RPM_BUILD_ROOT%{_sysconfdir}/conf.d
cp -a conf.d/*.ini $RPM_BUILD_ROOT%{_sysconfdir}/conf.d

# per SAPI ini directories
install -d $RPM_BUILD_ROOT%{_sysconfdir}/{cgi-fcgi,cli,apache,apache2handler}.d

# for CLI SAPI only
mv $RPM_BUILD_ROOT%{_sysconfdir}/{conf.d/readline.ini,cli.d}

# use system automake and {lib,sh}tool
%if "%{pld_release}" != "ac"
	ln -snf /usr/share/automake/config.{guess,sub} $RPM_BUILD_ROOT%{_libdir}/php/build
	for i in libtool.m4 lt~obsolete.m4 ltoptions.m4 ltsugar.m4 ltversion.m4; do
		ln -snf %{_aclocaldir}/${i} $RPM_BUILD_ROOT%{_libdir}/php/build
	done
	ln -snf %{_datadir}/libtool/config/ltmain.sh $RPM_BUILD_ROOT%{_libdir}/php/build
%else
	ln -snf %{_aclocaldir}/libtool.m4 $RPM_BUILD_ROOT%{_libdir}/php/build
	ln -snf %{_datadir}/libtool/ltmain.sh $RPM_BUILD_ROOT%{_libdir}/php/build
%endif
ln -snf %{_bindir}/shtool $RPM_BUILD_ROOT%{_libdir}/php/build

# for php-pecl-mailparse
install -d $RPM_BUILD_ROOT%{_includedir}/php/ext/mbstring
cp -a ext/mbstring/libmbfl/mbfl/*.h $RPM_BUILD_ROOT%{_includedir}/php/ext/mbstring

# tests
install -d $RPM_BUILD_ROOT%{php_data_dir}/tests/php
install -p run-tests.php $RPM_BUILD_ROOT%{php_data_dir}/tests/php/run-tests.php
cp -a tests/* $RPM_BUILD_ROOT%{php_data_dir}/tests/php

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

%pre fpm
%useradd -u 51 -r -s /bin/false -c "HTTP User" -g http http

%post fpm
/sbin/chkconfig --add php-fpm
%service php-fpm restart

%preun fpm
if [ "$1" = 0 ]; then
	%service php-fpm stop
	/sbin/chkconfig --del php-fpm
fi

%postun fpm
if [ "$1" = "0" ]; then
	%userremove http
fi

%post common
# PHP 5.3 requires timezone being setup, try setup it from tzdata
if ! grep -q '^date.timezone[[:space:]]*=' %{_sysconfdir}/php.ini && [ -f /etc/sysconfig/timezone ]; then
	TIMEZONE=
	. /etc/sysconfig/timezone
	if [ "$TIMEZONE" ]; then
		%{__sed} -i -e "s,^;date.timezone[[:space:]]*=.*,date.timezone = $TIMEZONE," %{_sysconfdir}/php.ini
	fi
fi

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
[ ! -f /etc/httpd/conf.d/??_mod_php.conf ] || %service -q httpd restart

%if %{with apache1}
%triggerpostun -n apache1-mod_php -- php < 4:5.0.4-9.11
sed -i -e '
	/^AddType application\/x-httpd-php \.php/s,^,#,
	/^\(Add\|Load\)Module.*php5\.\(so\|c\)/d
' /etc/apache/apache.conf
%service -q apache restart
%endif

%if %{with apache2}
%triggerpostun -n apache-mod_php -- php < 4:5.0.4-7.1
# for fixed php-SAPI.ini, the poor php-apache.ini was never read for apache2
if [ -f %{_sysconfdir}/php-apache.ini.rpmsave ]; then
	cp -f %{_sysconfdir}/php-apache2handler.ini{,.rpmnew}
	mv -f %{_sysconfdir}/php-apache.ini.rpmsave %{_sysconfdir}/php-apache2handler.ini
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
%extension_scripts bz2
%extension_scripts calendar
%extension_scripts ctype
%extension_scripts curl
%extension_scripts dba
%extension_scripts dom
%extension_scripts exif
%extension_scripts fileinfo
%extension_scripts filter
%extension_scripts ftp
%extension_scripts gd
%extension_scripts gettext
%extension_scripts gmp
%extension_scripts hash
%extension_scripts iconv
%extension_scripts imap
%extension_scripts interbase
%extension_scripts intl
%extension_scripts json
%extension_scripts ldap
%extension_scripts mbstring
%extension_scripts mcrypt
%extension_scripts mssql
%extension_scripts mysql
%extension_scripts mysqli
%extension_scripts mysqlnd
%extension_scripts oci8
%extension_scripts odbc
%extension_scripts openssl
%extension_scripts pcre
%extension_scripts pdo-dblib
%extension_scripts pdo-firebird
%extension_scripts pdo-mysql
%extension_scripts pdo-odbc
%extension_scripts pdo-pgsql
%extension_scripts pdo-sqlite
%extension_scripts pgsql
%extension_scripts phar
%extension_scripts posix
%extension_scripts pspell
%extension_scripts recode
%extension_scripts session
%extension_scripts shmop
%extension_scripts snmp
%extension_scripts soap
%extension_scripts sockets
%extension_scripts spl
%extension_scripts sqlite
%extension_scripts sqlite3
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
%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*bcmath\.so/d' %{_sysconfdir}/php.ini

%triggerun calendar -- %{name}-calendar < 4:5.0.4-9.1
%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*calendar\.so/d' %{_sysconfdir}/php.ini

%triggerun ctype -- %{name}-ctype < 4:5.0.4-9.1
%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*ctype\.so/d' %{_sysconfdir}/php.ini

%triggerun curl -- %{name}-curl < 4:5.0.4-9.1
%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*curl\.so/d' %{_sysconfdir}/php.ini

%triggerun dba -- %{name}-dba < 4:5.0.4-9.1
%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*dba\.so/d' %{_sysconfdir}/php.ini

%triggerun dom -- %{name}-dom < 4:5.0.4-9.1
%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*dom\.so/d' %{_sysconfdir}/php.ini

%triggerun exif -- %{name}-exif < 4:5.0.4-9.1
%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*exif\.so/d' %{_sysconfdir}/php.ini

%triggerun ftp -- %{name}-ftp < 4:5.0.4-9.1
%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*ftp\.so/d' %{_sysconfdir}/php.ini

%triggerun gd -- %{name}-gd < 4:5.0.4-9.1
%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*gd\.so/d' %{_sysconfdir}/php.ini

%triggerun gettext -- %{name}-gettext < 4:5.0.4-9.1
%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*gettext\.so/d' %{_sysconfdir}/php.ini

%triggerun gmp -- %{name}-gmp < 4:5.0.4-9.1
%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*gmp\.so/d' %{_sysconfdir}/php.ini

%triggerun iconv -- %{name}-iconv < 4:5.0.4-9.1
%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*iconv\.so/d' %{_sysconfdir}/php.ini

%triggerun imap -- %{name}-imap < 4:5.0.4-9.1
%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*imap\.so/d' %{_sysconfdir}/php.ini

%triggerun interbase -- %{name}-interbase < 4:5.0.4-9.1
%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*interbase\.so/d' %{_sysconfdir}/php.ini

%triggerun ldap -- %{name}-ldap < 4:5.0.4-9.1
%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*ldap\.so/d' %{_sysconfdir}/php.ini

%triggerun mbstring -- %{name}-mbstring < 4:5.0.4-9.1
%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*mbstring\.so/d' %{_sysconfdir}/php.ini

%triggerun mcrypt -- %{name}-mcrypt < 4:5.0.4-9.1
%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*mcrypt\.so/d' %{_sysconfdir}/php.ini

%triggerun mssql -- %{name}-mssql < 4:5.0.4-9.1
%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*mssql\.so/d' %{_sysconfdir}/php.ini

%triggerun mysql -- %{name}-mysql < 4:5.0.4-9.1
%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*mysql\.so/d' %{_sysconfdir}/php.ini

%triggerun mysqli -- %{name}-mysqli < 4:5.0.4-9.1
%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*mysqli\.so/d' %{_sysconfdir}/php.ini

%triggerun oci8 -- %{name}-oci8 < 4:5.0.4-9.1
%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*oci8\.so/d' %{_sysconfdir}/php.ini

%triggerun odbc -- %{name}-odbc < 4:5.0.4-9.1
%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*odbc\.so/d' %{_sysconfdir}/php.ini

%triggerun openssl -- %{name}-openssl < 4:5.0.4-9.1
%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*openssl\.so/d' %{_sysconfdir}/php.ini

%triggerun pcntl -- %{name}-pcntl < 4:5.1.2-9.5
if [ -f %{_sysconfdir}/php-cgi.ini ]; then
	%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*pcntl\.so/d' %{_sysconfdir}/php-cgi.ini
fi
if [ -f %{_sysconfdir}/php-cli.ini ]; then
	%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*pcntl\.so/d' %{_sysconfdir}/php-cli.ini
fi

%triggerun pcre -- %{name}-pcre < 4:5.0.4-9.1
%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*pcre\.so/d' %{_sysconfdir}/php.ini

%triggerun pgsql -- %{name}-pgsql < 4:5.0.4-9.1
%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*pgsql\.so/d' %{_sysconfdir}/php.ini

%triggerun posix -- %{name}-posix < 4:5.0.4-9.1
%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*posix\.so/d' %{_sysconfdir}/php.ini

%triggerun pspell -- %{name}-pspell < 4:5.0.4-9.1
%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*pspell\.so/d' %{_sysconfdir}/php.ini

%triggerun readline -- %{name}-readline < 4:5.1.2-9.5
if [ -f %{_sysconfdir}/php-cgi.ini ]; then
	%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*readline\.so/d' %{_sysconfdir}/php-cgi.ini
fi
if [ -f %{_sysconfdir}/php-cli.ini ]; then
	%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*readline\.so/d' %{_sysconfdir}/php-cli.ini
fi

%triggerun recode -- %{name}-recode < 4:5.0.4-9.1
%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*recode\.so/d' %{_sysconfdir}/php.ini

%triggerun session -- %{name}-session < 4:5.0.4-9.1
%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*session\.so/d' %{_sysconfdir}/php.ini

%triggerun shmop -- %{name}-shmop < 4:5.0.4-9.1
%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*shmop\.so/d' %{_sysconfdir}/php.ini

%triggerun snmp -- %{name}-snmp < 4:5.0.4-9.1
%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*snmp\.so/d' %{_sysconfdir}/php.ini

%triggerun soap -- %{name}-soap < 4:5.0.4-9.1
%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*soap\.so/d' %{_sysconfdir}/php.ini

%triggerun sockets -- %{name}-sockets < 4:5.0.4-9.1
%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*sockets\.so/d' %{_sysconfdir}/php.ini

%triggerun sqlite -- %{name}-sqlite < 4:5.0.4-9.1
%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*sqlite\.so/d' %{_sysconfdir}/php.ini

%triggerun sybase-ct -- %{name}-sybase-ct < 4:5.0.4-9.1
%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*sybase-ct\.so/d' %{_sysconfdir}/php.ini

%triggerun sysvmsg -- %{name}-sysvmsg < 4:5.0.4-9.1
%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*sysvmsg\.so/d' %{_sysconfdir}/php.ini

%triggerun sysvsem -- %{name}-sysvsem < 4:5.0.4-9.1
%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*sysvsem\.so/d' %{_sysconfdir}/php.ini

%triggerun sysvshm -- %{name}-sysvshm < 4:5.0.4-9.1
%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*sysvshm\.so/d' %{_sysconfdir}/php.ini

%triggerun tidy -- %{name}-tidy < 4:5.0.4-9.1
%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*tidy\.so/d' %{_sysconfdir}/php.ini

%triggerun wddx -- %{name}-wddx < 4:5.0.4-9.1
%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*wddx\.so/d' %{_sysconfdir}/php.ini

%triggerun xml -- %{name}-xml < 4:5.0.4-9.1
%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*xml\.so/d' %{_sysconfdir}/php.ini

%triggerun xmlrpc -- %{name}-xmlrpc < 4:5.0.4-9.1
%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*xmlrpc\.so/d' %{_sysconfdir}/php.ini

%triggerun xsl -- %{name}-xsl < 4:5.0.4-9.1
%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*xsl\.so/d' %{_sysconfdir}/php.ini

%triggerun zlib -- %{name}-zlib < 4:5.0.4-9.1
%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*zlib\.so/d' %{_sysconfdir}/php.ini

%if %{with apache1}
%files -n apache1-mod_php
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/apache/conf.d/*_mod_php.conf
%dir %{_sysconfdir}/apache.d
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/php-apache.ini
%attr(755,root,root) %{_libdir}/apache1/libphp5.so
%endif

%if %{with apache2}
%files -n apache-mod_php
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/httpd/conf.d/*_mod_php.conf
%dir %{_sysconfdir}/apache2handler.d
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/php-apache2handler.ini
%attr(755,root,root) %{_libdir}/apache/libphp5.so
%endif

%if %{with litespeed}
%files litespeed
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/php.litespeed
%endif

%if %{with cgi}
%files cgi
%defattr(644,root,root,755)
%dir %{_sysconfdir}/cgi-fcgi.d
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/php-cgi-fcgi.ini
%attr(755,root,root) %{_bindir}/php.cgi
%attr(755,root,root) %{_bindir}/php.fcgi
%endif

%files cli
%defattr(644,root,root,755)
%dir %{_sysconfdir}/cli.d
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/php-cli.ini
%attr(755,root,root) %{_bindir}/php.cli
%{_mandir}/man1/php.1*
%{_mandir}/man1/php.cli.1*

%files program
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/php

%if %{with fpm}
%files fpm
%defattr(644,root,root,755)
%doc sapi/fpm/CREDITS
%doc sapi/fpm/LICENSE
%dir %{_sysconfdir}/fpm.d
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/php-fpm.conf
%attr(755,root,root) %{_sbindir}/php-fpm
%{_mandir}/man8/php-fpm.8*
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/logrotate.d/php-fpm
%attr(754,root,root) /etc/rc.d/init.d/php-fpm
%endif

%files common
%defattr(644,root,root,755)
%doc php.ini-*
%doc CREDITS Zend/ZEND_CHANGES
%doc LICENSE Zend/LICENSE.Zend EXTENSIONS NEWS TODO*
%doc README.PHP4-TO-PHP5-THIN-CHANGES
%doc README.namespaces

%dir %{_sysconfdir}
%dir %{_sysconfdir}/conf.d
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/php.ini
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/browscap.ini
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
%{_mandir}/man1/php-config.1*
%{_mandir}/man1/phpize.1*

%files bcmath
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/bcmath.ini
%attr(755,root,root) %{php_extensiondir}/bcmath.so

%files bz2
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/bz2.ini
%attr(755,root,root) %{php_extensiondir}/bz2.so

%files calendar
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/calendar.ini
%attr(755,root,root) %{php_extensiondir}/calendar.so

%files ctype
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/ctype.ini
%attr(755,root,root) %{php_extensiondir}/ctype.so

%if %{with curl}
%files curl
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/curl.ini
%attr(755,root,root) %{php_extensiondir}/curl.so
%endif

%files dba
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/dba.ini
%attr(755,root,root) %{php_extensiondir}/dba.so

%files dom
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/dom.ini
%attr(755,root,root) %{php_extensiondir}/dom.so

%files exif
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/exif.ini
%attr(755,root,root) %{php_extensiondir}/exif.so

%files fileinfo
%defattr(644,root,root,755)
%doc README.input_filter
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/fileinfo.ini
%attr(755,root,root) %{php_extensiondir}/fileinfo.so

%if %{with filter}
%files filter
%defattr(644,root,root,755)
%doc README.input_filter
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/filter.ini
%attr(755,root,root) %{php_extensiondir}/filter.so
%endif

%files ftp
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/ftp.ini
%attr(755,root,root) %{php_extensiondir}/ftp.so

%files gd
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/gd.ini
%attr(755,root,root) %{php_extensiondir}/gd.so

%files gettext
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/gettext.ini
%attr(755,root,root) %{php_extensiondir}/gettext.so

%files gmp
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/gmp.ini
%attr(755,root,root) %{php_extensiondir}/gmp.so

%files hash
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/hash.ini
%attr(755,root,root) %{php_extensiondir}/hash.so

%files iconv
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/iconv.ini
%attr(755,root,root) %{php_extensiondir}/iconv.so

%if %{with imap}
%files imap
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/imap.ini
%attr(755,root,root) %{php_extensiondir}/imap.so
%endif

%if %{with interbase}
%files interbase
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/interbase.ini
%attr(755,root,root) %{php_extensiondir}/interbase.so
%endif

%files intl
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/intl.ini
%attr(755,root,root) %{php_extensiondir}/intl.so

%files json
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/json.ini
%attr(755,root,root) %{php_extensiondir}/json.so

%if %{with ldap}
%files ldap
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/ldap.ini
%attr(755,root,root) %{php_extensiondir}/ldap.so
%endif

%files mbstring
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/mbstring.ini
%attr(755,root,root) %{php_extensiondir}/mbstring.so

%files mcrypt
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/mcrypt.ini
%attr(755,root,root) %{php_extensiondir}/mcrypt.so

%if %{with mssql}
%files mssql
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/mssql.ini
%attr(755,root,root) %{php_extensiondir}/mssql.so
%endif

%files mysql
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/mysql.ini
%attr(755,root,root) %{php_extensiondir}/mysql.so

%if %{with mysqli}
%files mysqli
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/mysqli.ini
%attr(755,root,root) %{php_extensiondir}/mysqli.so
%endif

%if %{with mysqlnd}
%files mysqlnd
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/MySQLND.ini
%attr(755,root,root) %{php_extensiondir}/mysqlnd.so
%endif

%if %{with oci8}
%files oci8
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/oci8.ini
%attr(755,root,root) %{php_extensiondir}/oci8.so
%endif

%if %{with odbc}
%files odbc
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/odbc.ini
%attr(755,root,root) %{php_extensiondir}/odbc.so
%endif

%if %{with openssl}
%files openssl
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/openssl.ini
%attr(755,root,root) %{php_extensiondir}/openssl.so
%endif

%files pcntl
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/pcntl.ini
%attr(755,root,root) %{php_extensiondir}/pcntl.so

%if %{with pcre}
%files pcre
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/PCRE.ini
%attr(755,root,root) %{php_extensiondir}/pcre.so
%endif

%files pdo
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/pdo.ini
%attr(755,root,root) %{php_extensiondir}/pdo.so

%if %{with mssql} || %{with sybase_ct}
%files pdo-dblib
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/pdo_dblib.ini
%attr(755,root,root) %{php_extensiondir}/pdo_dblib.so
%endif

%if %{with interbase} && !%{with interbase_inst}
%files pdo-firebird
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/pdo_firebird.ini
%attr(755,root,root) %{php_extensiondir}/pdo_firebird.so
%endif

%files pdo-mysql
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/pdo_mysql.ini
%attr(755,root,root) %{php_extensiondir}/pdo_mysql.so

%if %{with oci8}
%files pdo-oci
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/pdo_oci.ini
%attr(755,root,root) %{php_extensiondir}/pdo_oci.so
%endif

%if %{with odbc}
%files pdo-odbc
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/pdo_odbc.ini
%attr(755,root,root) %{php_extensiondir}/pdo_odbc.so
%endif

%if %{with pgsql}
%files pdo-pgsql
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/pdo_pgsql.ini
%attr(755,root,root) %{php_extensiondir}/pdo_pgsql.so
%endif

%if %{with sqlite}
%files pdo-sqlite
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/pdo_sqlite.ini
%attr(755,root,root) %{php_extensiondir}/pdo_sqlite.so
%endif

%if %{with pgsql}
%files pgsql
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/pgsql.ini
%attr(755,root,root) %{php_extensiondir}/pgsql.so
%endif

%if %{with phar}
%files phar
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/phar.ini
%attr(755,root,root) %{php_extensiondir}/phar.so
%attr(755,root,root) %{_bindir}/phar
%attr(755,root,root) %{_bindir}/phar.phar
%endif

%files posix
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/posix.ini
%attr(755,root,root) %{php_extensiondir}/posix.so

%if %{with pspell}
%files pspell
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/pspell.ini
%attr(755,root,root) %{php_extensiondir}/pspell.so
%endif

%files readline
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/cli.d/readline.ini
%attr(755,root,root) %{php_extensiondir}/readline.so

%if %{with recode}
%files recode
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/recode.ini
%attr(755,root,root) %{php_extensiondir}/recode.so
%endif

%files session
%defattr(644,root,root,755)
%doc ext/session/mod_files.sh
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/Session.ini
%attr(755,root,root) %{php_extensiondir}/session.so

%files shmop
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/shmop.ini
%attr(755,root,root) %{php_extensiondir}/shmop.so

%files simplexml
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/simplexml.ini
%attr(755,root,root) %{php_extensiondir}/simplexml.so

%if %{with snmp}
%files snmp
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/snmp.ini
%attr(755,root,root) %{php_extensiondir}/snmp.so
%endif

%files soap
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/soap.ini
%attr(755,root,root) %{php_extensiondir}/soap.so

%files sockets
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/sockets.ini
%attr(755,root,root) %{php_extensiondir}/sockets.so

%files spl
%defattr(644,root,root,755)
%doc ext/spl/{CREDITS,README,TODO}
%doc ext/spl/examples
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/SPL.ini
%attr(755,root,root) %{php_extensiondir}/spl.so

%if %{with sqlite}
%files sqlite
%defattr(644,root,root,755)
%doc ext/sqlite/{README,TODO,CREDITS}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/sqlite.ini
%attr(755,root,root) %{php_extensiondir}/sqlite.so
%endif

%if %{with sqlite3}
%files sqlite3
%defattr(644,root,root,755)
%doc ext/sqlite3/CREDITS
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/sqlite3.ini
%attr(755,root,root) %{php_extensiondir}/sqlite3.so
%endif

%if %{with sybase_ct}
%files sybase-ct
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/sybase_ct.ini
%attr(755,root,root) %{php_extensiondir}/sybase_ct.so
%endif

%files sysvmsg
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/sysvmsg.ini
%attr(755,root,root) %{php_extensiondir}/sysvmsg.so

%files sysvsem
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/sysvsem.ini
%attr(755,root,root) %{php_extensiondir}/sysvsem.so

%files sysvshm
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/sysvshm.ini
%attr(755,root,root) %{php_extensiondir}/sysvshm.so

%files tests
%defattr(644,root,root,755)
%dir %{php_data_dir}/tests/php
%{php_data_dir}/tests/php/basic
%{php_data_dir}/tests/php/classes
%{php_data_dir}/tests/php/func
%{php_data_dir}/tests/php/lang
%{php_data_dir}/tests/php/output
%{php_data_dir}/tests/php/run-test
%{php_data_dir}/tests/php/security
%{php_data_dir}/tests/php/strings
%{php_data_dir}/tests/php/quicktester.inc
%attr(755,root,root) %{php_data_dir}/tests/php/run-tests.php

%if %{with tidy}
%files tidy
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/tidy.ini
%attr(755,root,root) %{php_extensiondir}/tidy.so
%endif

%files tokenizer
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/tokenizer.ini
%attr(755,root,root) %{php_extensiondir}/tokenizer.so

%if %{with wddx}
%files wddx
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*wddx.ini
%attr(755,root,root) %{php_extensiondir}/wddx.so
%endif

%files xml
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/xml.ini
%attr(755,root,root) %{php_extensiondir}/xml.so

%files xmlreader
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/xmlreader.ini
%attr(755,root,root) %{php_extensiondir}/xmlreader.so

%if %{with xmlrpc}
%files xmlrpc
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/xmlrpc.ini
%attr(755,root,root) %{php_extensiondir}/xmlrpc.so
%endif

%files xmlwriter
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/xmlwriter.ini
%attr(755,root,root) %{php_extensiondir}/xmlwriter.so

%files xsl
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/xsl.ini
%attr(755,root,root) %{php_extensiondir}/xsl.so

%files zip
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/zip.ini
%attr(755,root,root) %{php_extensiondir}/zip.so

%files zlib
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/zlib.ini
%attr(755,root,root) %{php_extensiondir}/zlib.so