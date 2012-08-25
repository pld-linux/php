#!/bin/sh
# Test open_basedir configuration
mv tests/security/open_basedir_linkinfo.phpt{,.skip}  XFAIL REASON: BUG: open_basedir cannot delete symlink to prohibited file. See also
# Inconsistencies when accessing protected members
mv Zend/tests/access_modifiers_008.phpt{,.skip}  XFAIL REASON: Discussion: http://marc.info/?l=php-internals&m=120221184420957&w=2
# Inconsistencies when accessing protected members - 2
mv Zend/tests/access_modifiers_009.phpt{,.skip}  XFAIL REASON: Discussion: http://marc.info/?l=php-internals&m=120221184420957&w=2
# Bug #48770 (call_user_func_array() fails to call parent from inheriting class)
mv Zend/tests/bug48770.phpt{,.skip}  XFAIL REASON: See Bug #48770
# Bug #48770 (call_user_func_array() fails to call parent from inheriting class)
mv Zend/tests/bug48770_2.phpt{,.skip}  XFAIL REASON: See Bug #48770
# Bug #48770 (call_user_func_array() fails to call parent from inheriting class)
mv Zend/tests/bug48770_3.phpt{,.skip}  XFAIL REASON: See Bug #48770
# Initial value of static var in method depends on the include time of the class definition
mv Zend/tests/method_static_var.phpt{,.skip}  XFAIL REASON: Maybe not a bug
# DBA with persistent connections
mv ext/dba/tests/dba015.phpt{,.skip}  XFAIL REASON: Test 6 crashes in flatfile_findkey with dba pointer of NULL, bug http://bugs.php.net/bug.php?id=51278
# DBA DB4 with persistent connections
mv ext/dba/tests/dba_db4_018.phpt{,.skip}  XFAIL REASON: Test 6 crashes with dba pointer of NULL, bug http://bugs.php.net/bug.php?id=51278
# Bug #42718 (unsafe_raw filter not applied when configured as default filter)
mv ext/filter/tests/bug42718.phpt{,.skip}  XFAIL REASON: FILTER_UNSAFE_RAW not applied when configured as default filter, even with flags
# Optional long parameter might be null
mv ext/mbstring/tests/mb_str_functions_opt-parameter.phpt{,.skip}  XFAIL REASON: mb functions fail to allow null instead of actual value
# Bug #60634 (Segmentation fault when trying to die() in SessionHandler::write())
mv ext/session/tests/bug60634.phpt{,.skip}  XFAIL REASON: Long term low priority bug, working on it
# Bug #60634 (Segmentation fault when trying to die() in SessionHandler::write()) - fatal error in write during exec
mv ext/session/tests/bug60634_error_1.phpt{,.skip}  XFAIL REASON: Long term low priority bug, working on it
# Bug #60634 (Segmentation fault when trying to die() in SessionHandler::write()) - exception in write during exec
mv ext/session/tests/bug60634_error_2.phpt{,.skip}  XFAIL REASON: Long term low priority bug, working on it
# Bug #60634 (Segmentation fault when trying to die() in SessionHandler::write()) - fatal error in write after exec
mv ext/session/tests/bug60634_error_3.phpt{,.skip}  XFAIL REASON: Long term low priority bug, working on it
# Bug #60634 (Segmentation fault when trying to die() in SessionHandler::write()) - exception in write after exec
mv ext/session/tests/bug60634_error_4.phpt{,.skip}  XFAIL REASON: Long term low priority bug, working on it
# Bug #60634 (Segmentation fault when trying to die() in SessionHandler::write()) - fatal error in close during exec
mv ext/session/tests/bug60634_error_5.phpt{,.skip}  XFAIL REASON: Long term low priority bug, working on it
# Bug #45712 (NaN/INF comparison)
mv ext/standard/tests/math/bug45712.phpt{,.skip}  XFAIL REASON: Bug 45712 not fixed yet.
# CLI -a and readline
mv sapi/cli/tests/016.phpt{,.skip}  XFAIL REASON: https://bugs.php.net/bug.php?id=55496
