#!/bin/sh
# inter-dependencies checker.

with_mysqlnd=mysqlnd

dep_session=""
dep_filter=''
dep_eaccelerator='session'
dep_mysqlnd=''
dep_mysql="$dep_mysqlnd $with_mysqlnd"
dep_mysqli="$dep_mysqlnd $with_mysqlnd"
dep_pdo=""
dep_pdo_sqlite="$dep_pdo pdo"
dep_pdo_pgsql="$dep_pdo pdo"
dep_pdo_oci="$dep_pdo pdo"
dep_pdo_odbc="$dep_pdo pdo"
dep_pdo_firebird="$dep_pdo pdo"
dep_pdo_dblib="$dep_pdo pdo"
dep_pdo_mysql="$dep_pdo pdo $dep_mysqlnd $with_mysqlnd"
dep_simplexml=""
dep_imap=""
dep_phar=""
dep_sqlite="$dep_pdo pdo"
dep_fileinfo=""
dep_wddx='xml'
dep_xmlreader='dom'
dep_xmlrpc='xml'
dep_xsl='dom'
dep_snmp="snmp"
dep_opcache=''

php=${PHP:-$(php-config --php-binary)}
ext_dir=${EXTENSION_DIR:-$(php-config --extension-dir)}
conf_dir=${CONFIG_DIR:-$(php-config --sysconfdir)/conf.d $(php-config --sysconfdir)/cli.d}

test_deps() {
	tmpini=$(mktemp)

	# poldek --sn ac-ready -u php-*
	for ext in ${*:-$ext_dir/*.so}; do
		[ -f $ext ] || continue
		ext=${ext##*/}; ext=${ext%.so}

		deps=$(eval echo \$dep_$ext)
		# add ext itself, if already not in list (spl case)
		[[ $deps = *\ $ext\ * ]] || deps="$deps $ext"

		echo -n "$ext (deps: ${deps# })..."

		# special: opcache is listed as "Zend Opcache"
		[ "$ext" = "opcache" ] && ext="zend opcache"

		grep -rlE '^(zend_)?extension=('$(echo "${deps# }" | tr ' ' '|')')$' $conf_dir | LC_ALL=C sort | xargs cat > $tmpini
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
}

_resolve_extension_deps() {
	local name="$1"

	eval echo \$dep_$ext
}

# Prints a load order (0-based integer) for the given extension name. Extension
# with lower load order should be loaded before exts with higher load order.
# It's based on number of dependencies of the extension (with exception for
# "imap"), which is flawed, but simple and good enough for now.
#
# _extension_load_order adopted from alpine linux:
# https://github.com/alpinelinux/aports/blob/v3.10.1/community/php7/APKBUILD#L639-L653
_extension_load_order() {
	local name="$1"
	local deps=$(eval "echo \$dep_$name")

	case "$name" in
		# XXX: This must be loaded after recode, even though it does
		# not depend on it. So we must use this hack...
		imap) echo 1;;
		*) echo "${deps:=$(_resolve_extension_deps $name)}" | wc -w;;
	esac
}

generate_ini() {
	local load_order

	rm -rf conf.d
	install -d conf.d
	for module in ${*:-$ext_dir/*.so}; do
		[ -f $module ] || continue
		extname=${module##*/}; extname=${extname%.so}

		ext=extension
		# opcache.so is zend extension
		nm $module | grep -q zend_extension_entry && ext=zend_extension

		load_order=$(_extension_load_order "$extname")
		cat > conf.d/$(printf %02d $load_order)_$extname.ini <<-EOF
			; Enable $extname $ext module
			$ext=$extname
		EOF
	done
}

if [ -n "$GENERATE_INI" ]; then
	generate_ini "$@"
else
	test_deps "$@"
fi
