#!/bin/sh
# Test open_basedir configuration  XFAIL REASON: BUG: open_basedir cannot delete symlink to prohibited file. See also
mv tests/security/open_basedir_linkinfo.phpt{,.skip}
# Inconsistencies when accessing protected members  XFAIL REASON: Discussion: http://marc.info/?l=php-internals&m=120221184420957&w=2
mv Zend/tests/access_modifiers_008.phpt{,.skip}
# Inconsistencies when accessing protected members - 2  XFAIL REASON: Discussion: http://marc.info/?l=php-internals&m=120221184420957&w=2
mv Zend/tests/access_modifiers_009.phpt{,.skip}
# Bug #48770 (call_user_func_array() fails to call parent from inheriting class)  XFAIL REASON: See Bug #48770
mv Zend/tests/bug48770.phpt{,.skip}
# Bug #48770 (call_user_func_array() fails to call parent from inheriting class)  XFAIL REASON: See Bug #48770
mv Zend/tests/bug48770_2.phpt{,.skip}
# Bug #48770 (call_user_func_array() fails to call parent from inheriting class)  XFAIL REASON: See Bug #48770
mv Zend/tests/bug48770_3.phpt{,.skip}
# Initial value of static var in method depends on the include time of the class definition  XFAIL REASON: Maybe not a bug
mv Zend/tests/method_static_var.phpt{,.skip}
# DBA with persistent connections  XFAIL REASON: Test 6 crashes in flatfile_findkey with dba pointer of NULL, bug http://bugs.php.net/bug.php?id=51278
mv ext/dba/tests/dba015.phpt{,.skip}
# DBA DB4 with persistent connections  XFAIL REASON: Test 6 crashes with dba pointer of NULL, bug http://bugs.php.net/bug.php?id=51278
mv ext/dba/tests/dba_db4_018.phpt{,.skip}
# Bug #42718 (unsafe_raw filter not applied when configured as default filter)  XFAIL REASON: FILTER_UNSAFE_RAW not applied when configured as default filter, even with flags
mv ext/filter/tests/bug42718.phpt{,.skip}
# Optional long parameter might be null  XFAIL REASON: mb functions fail to allow null instead of actual value
mv ext/mbstring/tests/mb_str_functions_opt-parameter.phpt{,.skip}
# Bug #60634 (Segmentation fault when trying to die() in SessionHandler::write())  XFAIL REASON: Long term low priority bug, working on it
mv ext/session/tests/bug60634.phpt{,.skip}
# Bug #60634 (Segmentation fault when trying to die() in SessionHandler::write()) - fatal error in write during exec  XFAIL REASON: Long term low priority bug, working on it
mv ext/session/tests/bug60634_error_1.phpt{,.skip}
# Bug #60634 (Segmentation fault when trying to die() in SessionHandler::write()) - exception in write during exec  XFAIL REASON: Long term low priority bug, working on it
mv ext/session/tests/bug60634_error_2.phpt{,.skip}
# Bug #60634 (Segmentation fault when trying to die() in SessionHandler::write()) - fatal error in write after exec  XFAIL REASON: Long term low priority bug, working on it
mv ext/session/tests/bug60634_error_3.phpt{,.skip}
# Bug #60634 (Segmentation fault when trying to die() in SessionHandler::write()) - exception in write after exec  XFAIL REASON: Long term low priority bug, working on it
mv ext/session/tests/bug60634_error_4.phpt{,.skip}
# Bug #60634 (Segmentation fault when trying to die() in SessionHandler::write()) - fatal error in close during exec  XFAIL REASON: Long term low priority bug, working on it
mv ext/session/tests/bug60634_error_5.phpt{,.skip}
# Bug #45712 (NaN/INF comparison)  XFAIL REASON: Bug 45712 not fixed yet.
mv ext/standard/tests/math/bug45712.phpt{,.skip}
# CLI -a and readline  XFAIL REASON: https://bugs.php.net/bug.php?id=55496
mv sapi/cli/tests/016.phpt{,.skip}
