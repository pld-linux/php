#!/bin/sh
# inter-dependencies checker.

with_mysqlnd=mysqlnd

dep_spl="pcre simplexml"
dep_session="spl $dep_spl"
dep_filter='pcre'
dep_eaccelerator='session'
dep_mysql="$with_mysqlnd"
dep_mysqli="$dep_spl spl $with_mysqlnd"
dep_pdo="$dep_spl spl"
dep_pdo_sqlite="$dep_pdo pdo"
dep_pdo_pgsql="$dep_pdo pdo"
dep_pdo_oci="$dep_pdo pdo"
dep_pdo_odbc="$dep_pdo pdo"
dep_pdo_firebird="$dep_pdo pdo"
dep_pdo_dblib="$dep_pdo pdo"
dep_pdo_mysql="$dep_pdo pdo $with_mysqlnd"
dep_simplexml="$dep_spl spl"
dep_imap="pcre"
dep_phar="$dep_spl spl"
dep_sqlite="$dep_pdo pdo"
dep_fileinfo="pcre"
dep_wddx='xml'
dep_xmlreader='dom'
dep_xmlrpc='xml'
dep_xsl='dom'

php=${PHP:-$(php-config --php-binary)}
ext_dir=${EXTENSION_DIR:-$(php-config --extension-dir)}
conf_dir=${CONFIG_DIR:-$(php-config --sysconfdir)/conf.d $(php-config --sysconfdir)/cli.d}
tmpini=$(mktemp)

# poldek --sn ac-ready -u php-*
for ext in $ext_dir/*.so; do
	[ -f $ext ] || continue
	ext=${ext##*/}; ext=${ext%.so}

	deps=$(eval echo \$dep_$ext)
	# add ext itself, if already not in list (spl case)
	[[ $deps = *\ $ext\ * ]] || deps="$deps $ext"

	echo -n "$ext (deps: ${deps# })..."

	grep -rlE '^extension=('$(echo "${deps# }" | tr ' ' '|')').so$' $conf_dir | LC_CTYPE=C LC_ALL= sort | xargs cat > $tmpini
	$php -n -d extension_dir=$ext_dir -c $tmpini -r "exit(extension_loaded('${ext}') ? 0 : 1);"
	rc=$?
	if [ $rc = 0 ]; then
		echo OK
	else
		echo FAIL
		echo "Failed config was:"
		cat $tmpini
	fi
done
rm -f $t
