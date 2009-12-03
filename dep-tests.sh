#!/bin/sh
# inter-dependencies checker.

# spl must be loaded before simplexml, therefore spl has itself before its deps
dep_spl="pcre spl simplexml"
dep_filter='pcre'
dep_eaccelerator='session'
dep_mysqli="$dep_spl"
dep_pdo="$dep_spl"
dep_pdo_sqlite="$dep_pdo pdo"
dep_pdo_pgsql="$dep_pdo pdo"
dep_pdo_odbc="$dep_pdo pdo"
dep_pdo_firebird="$dep_pdo pdo"
dep_pdo_dblib="$dep_pdo pdo"
dep_pdo_mysql="$dep_pdo pdo"
dep_simplexml="$dep_spl"
dep_sqlite="$dep_pdo pdo"
dep_wddx='xml'
dep_xmlreader='dom'
dep_xmlrpc='xml'
dep_xsl='dom'

php=${PHP:-$(php-config --php-binary)}
ext_dir=${EXTENSION_DIR:-$(php-config --extension-dir)}
conf_dir=${CONFIG_DIR:-$(php-config --sysconfdir)/conf.d}

# poldek --sn ac-ready -u php-*
for ext in $ext_dir/*.so; do
	[ -f $ext ] || continue
	ext=${ext##*/}; ext=${ext%.so}
	deps=$(eval echo \$dep_$ext)
	# add ext itself, if already not in list (spl case)
	[[ $deps = *$ext* ]] || deps="$deps $ext"

	args=$(for e in $deps; do echo -d extension=$e.so; done)
	echo -n "$ext (deps: ${deps# })..."
	$php -n -d extension_dir=$ext_dir $args -r "exit(extension_loaded('${ext}') ? 0 : 1);" && echo OK || echo FAIL
done
