#!/bin/sh
tag=php_5_2_10
branch=PHP_5_2

if [ ! -d $tag ]; then
	cvs -d :pserver:cvsread@cvs.php.net:/repository checkout -r $tag -d $tag php5
fi
if [ ! -d $branch ]; then
	cvs -d :pserver:cvsread@cvs.php.net:/repository checkout -r $branch -d $branch php5
fi

cd $tag && cvs up -d && cd ..
cd $branch && cvs up -d && cd ..

diff -ur -x CVS $tag $branch > php-branch.diff
