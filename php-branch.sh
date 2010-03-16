#!/bin/sh
set -e
svn=http://svn.php.net/repository/php/php-src
tag=php_5_3_2
branch=PHP_5_3
out=php-branch.diff

d=$-
filter() {
	set -$d
	# remove revno's for smaller diffs
	sed -e 's,^\([-+]\{3\} .*\)\t(revision [0-9]\+)$,\1,'
}

old=$svn/tags/$tag
new=$svn/branches/$branch
echo >&2 "Running diff: $old -> $new"
LC_ALL=C svn diff --old=$old --new=$new | filter > $out.tmp

if cmp -s $out{,.tmp}; then
	echo >&2 "No new diffs..."
	rm -f $out.tmp
	exit 0
fi
mv -f $out{.tmp,}
