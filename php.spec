Summary:	The PHP HTML-embedded scripting language for use with Apache.
Summary(fr):	Le langage de script embarque-HTML PHP pour Apache.
Summary(pl):	J�zyk skryptowy PHP -- u�ywany wraz z serwerem Apache.
Name:		php
Version:	4.0RC1
Release:	1
Group:		Libraries
Group(fr):	Librairies
Group(pl):	Biblioteki
License: The PHP license (see "LICENSE" file included in distribution)
Source0:	http://www.php.net/distributions/%{name}-%{version}.tar.gz
Source1:	FAQ.php
Source2:	php.ini
Source3:	zend.gif
Source4:	http://www.php.net/distributions/manual.tar.gz
Icon:		php4.gif
URL:		http://www.php.net/
BuildRequires:	apache(EAPI)-devel
BuildRequires:	zlib-devel
# BuildRequires:	mysql-devel >= 3.22.30-2
BuildRequires:	kaffe-devel
BuildRequires:	libxml-devel >= 1.0.0
BuildRequires:	postgresql-devel
BuildRequires:	pdflib-devel >= 3.0
BuildRequires:	gd-devel
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	libpng-devel
BuildRequires:	libtiff-devel
BuildRequires:	libjpeg-devel
BuildRequires:	zlib-devel
Requires:	apache(EAPI) >= 1.3.9
Prereq:		%{_sbindir}/apxs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_pkglibdir	%{_libdir}/apache

%description
PHP is an HTML-embedded scripting language.  PHP attempts to make it easy
for developers to write dynamically generated web pages.  PHP also offers
built-in database integration for several commercial and non-commercial
database management systems, so writing a database-enabled web page with
PHP is fairly simple.  The most common use of PHP coding is probably as a
replacement for CGI scripts.  The mod_php module enables the Apache web
server to understand and process the embedded PHP language in web pages.
This package contains PHP version %{version}.  If you use applications which
specifically rely on PHP/FI (PHP v2 and earlier), you should instead install
the PHP/FI module contained in the phpfi package.  If you're just starting
with PHP, you should install this package.  You'll also need to install
the Apache web server.

%description -l fr
PHP est un langage de script embarque dans le HTM. PHP essaye de rendre
simple aux developpeurs d'ecrire des pages web generees dynamiquement.
PHP incorpore egalement une integration avec plusieurs systemes de gestion
de bases de donnees commerciaux et non-connerciaux, qui rent facile
la creation de pages web liees avec des bases de donnees. L'utilisation la
plus commune de PHP est probablement en remplacement de scripts CGI. Le
module mod_php permet au serveur web apache de comprendre et de traiter le
langage PHP integre dans des pages web.
Ce package contient PHP version %{version}. Si vous utilisez des
applications qui utilisent specifiquement PHP/FI, vous devrez installer le
module PHP/FI inclus dans le package mod_php. Si vous debutez avec PHP, vous
devriez installer ce package. Vous aurez egalement besoin d'installer le
serveur web Apache.

%description -l pl
PHP jest j�zykiem skryptowym, kt�rego polecenia umieszcza si� w plikach
HTML. Pakiet ten zawiera modu� przeznaczony dla serwera HTTP (jak np.
Apache), kt�ry interpretuje te polecenia.  Umo�liwia to tworzenie
dynamicznie stron WWW. Spora cz�� sk�adni PHP zapo�yczona zosta�a
z j�zyk�w: C, Java i Perl.

#%package mysql
#Summary:	MySQL database module for PHP4
#Summary(pl):	Modu� bazy danych MySQL dla PHP4
#Group:		Libraries
#Group(fr):	Librairies
#Group(pl):	Biblioteki
#Requires: 	%{name} = %{version}
#
#%description mysql
#This is a dynamic shared object (DSO) for Apache that will add MySQL
#database support to PHP4.  If you need back-end support for MySQL,
#you should install this package in addition to the main %{name} package.
#
#%description mysql -l pl
#Modu� PHP4 umo�liwiaj�cy dost�p do bazy danych MySQL.


#%package pgsql
#Summary:	PostgreSQL database module for PHP4
#Summary(pl):	Modu� bazy danych PostgreSQL dla PHP4
#Group:		Libraries
#Group(fr):	Librairies
#Group(pl):	Biblioteki
#Requires: 	%{name} = %{version}
#
#%description pgsql
#This is a dynamic shared object (DSO) for Apache that will add PostgreSQL
#database support to PHP4.  If you need back-end support for PostgreSQL,
#you should install this package in addition to the main %{name} package.
#
#%description pgsql -l pl
#Modu� PHP4 umo�liwiaj�cy dost�p do bazy danych PostgreSQL.

#%package gd
#Summary:	GD extension module for PHP4
#Summary:	Modu� GD dla PHP4
#Group:		Libraries
#Group(fr):	Librairies
#Group(pl):	Biblioteki
#Requires: 	%{name} = %{version}
#
#%description gd
#This is a dynamic shared object (DSO) for Apache that will add GD
#support to PHP4. You should install this package in addition to the main
#%{name} package if you want to create and manipulate images with PHP.
#
#%description gd -l pl

%package java
Summary:	Java extension module for PHP4
Summary(pl):	Modu� Javy dla PHP4
Group:		Libraries
Group(fr):	Librairies
Group(pl):	Biblioteki
Requires: 	%{name} = %{version}

%description java
This is a dynamic shared object (DSO) for Apache that will add JAVA
support to PHP4. This extension provides a simple and effective means
for creating and invoking methods on Java objects from PHP.

%description java -l pl

%package xml
Summary:	XML extension module for PHP4
Summary(pl):	Modu� XML dla PHP4
Group:		Libraries
Group(fr):	Librairies
Group(pl):	Biblioteki
Requires: 	%{name} = %{version}

%description xml
This is a dynamic shared object (DSO) for Apache that will add XML
support to PHP4. This extension lets you create XML parsers and then
define handlers for different XML events. If you want to be able to parse
XML documents you should install this package in addition to the main 
%{name} package.

%description xml -l pl

%package doc
Summary:     Online manual for PHP4
Summary(pl): Dokumentacja dla PHP4
Group:       Networking/Daemons

%description doc
Comprehensive documentation for PHP4, viewable through your web server, too!

%description doc -l pl
Dokumentacja dla pakietu PHP4.  Mo�na j� r�wnie� ogl�da� poprzez serwer WWW.
%prep
%setup -q

%build
LDFLAGS=""; export LDFLAGS
CFLAGS="$RPM_OPT_FLAGS -DEAPI"; export CFLAGS
./buildconf
%configure \
	--with-apxs=%{_sbindir}/apxs \
	--with-config-file-path=%{_sysconfdir}/httpd \
	--with-exec-dir=%{_bindir} \
	--disable-debug \
	--enable-magic-quotes \
	--enable-shared \
	--enable-track-vars \
	--enable-safe-mode \
	--enable-trans-sid \
	--enable-sysvsem \
	--enable-sysvshm \
	--enable-xml=shared \
	--with-zlib \
	--with-regex=system \
	--with-gettext \
	--with-mysql \
   --enable-versioning \
	--with-gd \
	--with-dbase \
	--with-filepro \
	--with-ftp \
	--with-hyperwave \
	--with-pdflib \
	--with-java \
	--with-pgsql=/usr

#	--with-snmp=shared  \

make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_pkglibdir}/php,%{_sysconfdir}/httpd} \
		$RPM_BUILD_ROOT/home/httpd/html/{icons,docs,docs/php4-doc}

install .libs/*.so	$RPM_BUILD_ROOT%{_pkglibdir}
install modules/*.so	$RPM_BUILD_ROOT%{_pkglibdir}/php

install %{SOURCE2}		$RPM_BUILD_ROOT%{_sysconfdir}/httpd/php.ini
install %{SOURCE3} php4.gif	$RPM_BUILD_ROOT/home/httpd/html/icons

cd $RPM_BUILD_ROOT/home/httpd/html/docs/php4-doc
tar zxf %{SOURCE4}
ln -s manual.html index.html
cd -

strip --strip-unneeded	\
	$RPM_BUILD_ROOT%{_pkglibdir}/*.so \
	$RPM_BUILD_ROOT%{_pkglibdir}/php/*.so

install %{SOURCE1} .
gzip -9nf CODING_STANDARDS CREDITS ChangeLog FUNCTION_LIST.txt \
      MAINTAINERS MODULES_STATUS NEWS TODO* LICENSE Zend/LICENSE \
      Zend/ZEND_CHANGES

%post
%{_sbindir}/apxs -e -a -n php4 %{_pkglibdir}/libphp4.so 1>&2
perl -pi -e 's|^#AddType application/x-httpd-php .php|AddType application/x-httpd-php .php|'
echo "There were some conflicts with mod_magic module."
echo "If you ecounter problems with running .php files"
echo "try turn off it in httpd.conf before using php4."
if [ -f /var/lock/subsys/httpd ]; then
	/etc/rc.d/init.d/httpd restart 1>&2
fi

%postun
perl -pi -e 's|^AddType application/x-httpd-php .php|#AddType application/x-httpd-php .php|'
if [ -f /var/lock/subsys/httpd ]; then
      /etc/rc.d/init.d/httpd restart 1>&2
fi

%preun
if [ "$1" = "0" ]; then
	%{_sbindir}/apxs -e -A -n php4 %{_pkglibdir}/libphp4.so 1>&2
	if [ -f /var/lock/subsys/httpd ]; then
		/etc/rc.d/init.d/httpd restart 1>&2
	fi
fi

#%post mysql
#if [ -f %{_sysconfdir}/httpd/php.ini ]; then
#	echo "activating module 'mysql.so' in /etc/httpd/php.ini" 1>&2
#	perl -pi -e 's|^;extension=mysql.so|extension=mysql.so|g' \
#	%{_sysconfdir}/httpd/php.ini
#fi
#if [ -f /var/lock/subsys/httpd ]; then
#	/etc/rc.d/init.d/httpd restart 1>&2
#fi
#
#%postun mysql
#if [ -f %{_sysconfdir}/httpd/php.ini ]; then
#	echo "deactivating module 'mysql.so' in /etc/httpd/php.ini" 1>&2
#	perl -pi -e 's|^extension=mysql.so|;extension=mysql.so|g' \
#	%{_sysconfdir}/httpd/php.ini
#fi
#if [ -f /var/lock/subsys/httpd ]; then
#	/etc/rc.d/init.d/httpd restart 1>&2
#fi
#
#%post pgsql
#if [ -f %{_sysconfdir}/httpd/php.ini ]; then
#	echo "activating module 'pgsql.so' in /etc/httpd/php.ini" 1>&2
#	perl -pi -e 's|^;extension=pgsql.so|extension=pgsql.so|g' \
#	%{_sysconfdir}/httpd/php.ini
#fi
#if [ -f /var/lock/subsys/httpd ]; then
#	/etc/rc.d/init.d/httpd restart 1>&2
#fi
#
#%postun pgsql
#if [ -f %{_sysconfdir}/httpd/php.ini ]; then
#	echo "deactivating module 'pgsql.so' in /etc/httpd/php.ini" 1>&2
#	perl -pi -e 's|^extension=pgsql.so|;extension=pgsql.so|g' \
#	%{_sysconfdir}/httpd/php.ini
#fi
#if [ -f /var/lock/subsys/httpd ]; then
#	/etc/rc.d/init.d/httpd restart 1>&2
#fi
#
#%post gd
#if [ -f %{_sysconfdir}/httpd/php.ini ]; then
#	echo "activating module 'gd.so' in /etc/httpd/php.ini" 1>&2
#	perl -pi -e 's|^;extension=gd.so|extension=gd.so|g' \
#	%{_sysconfdir}/httpd/php.ini
#fi
#if [ -f /var/lock/subsys/httpd ]; then
#	/etc/rc.d/init.d/httpd restart 1>&2
#fi
#
#%postun gd
#if [ -f %{_sysconfdir}/httpd/php.ini ]; then
#	echo "deactivating module 'gd.so' in /etc/httpd/php.ini" 1>&2
#	perl -pi -e 's|^extension=gd.so|;extension=gd.so|g' \
#	%{_sysconfdir}/httpd/php.ini
#fi
#if [ -f /var/lock/subsys/httpd ]; then
#	/etc/rc.d/init.d/httpd restart 1>&2
#fi

%post xml
if [ -f %{_sysconfdir}/httpd/php.ini ]; then
	echo "activating module 'xml.so' in /etc/httpd/php.ini" 1>&2
	perl -pi -e 's|^;extension=xml.so|extension=xml.so|g' \
	%{_sysconfdir}/httpd/php.ini
fi
if [ -f /var/lock/subsys/httpd ]; then
	/etc/rc.d/init.d/httpd restart 1>&2
fi

%postun xml
if [ -f %{_sysconfdir}/httpd/php.ini ]; then
	echo "deactivating module 'xml.so' in /etc/httpd/php.ini" 1>&2
	perl -pi -e 's|^extension=xml.so|;extension=xml.so|g' \
	%{_sysconfdir}/httpd/php.ini
fi
if [ -f /var/lock/subsys/httpd ]; then
	/etc/rc.d/init.d/httpd restart 1>&2
fi

%post java
if [ -f %{_sysconfdir}/httpd/php.ini ]; then
	echo "activating module 'libphp_java.so' in /etc/httpd/php.ini" 1>&2
	perl -pi -e 's|^;extension=libphp_java.so|extension=libphp_java.so|g' \
	%{_sysconfdir}/httpd/php.ini
fi
if [ -f /var/lock/subsys/httpd ]; then
	/etc/rc.d/init.d/httpd restart 1>&2
fi

%postun java
if [ -f %{_sysconfdir}/httpd/php.ini ]; then
	echo "deactivating module 'libphp_java.so' in /etc/httpd/php.ini" 1>&2
	perl -pi -e 's|^extension=libphp_java.so|;extension=libphp_java.so|g' \
	%{_sysconfdir}/httpd/php.ini
fi
if [ -f /var/lock/subsys/httpd ]; then
	/etc/rc.d/init.d/httpd restart 1>&2
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {CODING_STANDARDS,CREDITS,ChangeLog,FUNCTION_LIST.txt,Zend/ZEND_CHANGES}.gz
%doc {LICENSE,Zend/LICENSE,MAINTAINERS,MODULES_STATUS,NEWS,TODO*}.gz  

%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/httpd/*
%dir %{_pkglibdir}/php

#%attr(755,root,root) %{_libdir}/apache/php/*.so

/home/httpd/html/icons/*

%attr(755,root,root) %{_pkglibdir}/libphp4.so

#%files mysql
#%defattr(644,root,root,755)
#%attr(755,root,root) %{_pkglibdir}/php/mysql.so
#
#%files pgsql
#%defattr(644,root,root,755)
#%attr(755,root,root) %{_pkglibdir}/php/pgsql.so
#
#%files gd
#%defattr(644,root,root,755)
#%attr(755,root,root) %{_pkglibdir}/php/gd.so

%files xml
%defattr(644,root,root,755)
%attr(755,root,root) %{_pkglibdir}/php/xml.so

%files java
%defattr(644,root,root,755)
%attr(755,root,root) %{_pkglibdir}/php/libphp_java.so

%files doc
/home/httpd/html/docs/php4-doc
