#!/bin/sh
set -e
svn=http://svn.php.net/repository/php/php-src
tag=php_5_2_11
branch=PHP_5_2

d=$-
filter() {
	set -$d
	# remove revno's for smaller diffs
	sed -e 's,^\([-+]\{3\} .*\)\t(revision [0-9]\+)$,\1,'
}

old=$svn/tags/$tag
new=$svn/branches/$branch
echo >&2 "Running diff: $old -> $new"
LC_ALL=C svn diff --old=$old --new=$new | filter > php-branch.diff.tmp

if cmp -s php-branch.diff{,.tmp}; then
	echo >&2 "No new diffs..."
	rm -f php-branch.diff.tmp
	exit 0
fi
mv -f php-branch.diff{.tmp,}
