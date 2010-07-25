#!/bin/sh
# Class constant whose initial value refereces a non-existent class
mv tests/classes/constants_error_004.phpt{,.skip}
# easter_date()
mv ext/calendar/tests/easter_date.phpt{,.skip}
# unixtojd()
mv ext/calendar/tests/unixtojd.phpt{,.skip}
# curl_error() function - basic test for curl_error using a fake url
mv ext/curl/tests/curl_error_basic.phpt{,.skip}
# curl_setopt() basic parameter test
mv ext/curl/tests/curl_setopt_error.phpt{,.skip}
# timezone_abbreviations_list() tests
mv ext/date/tests/010.phpt{,.skip}
# Test DateTime::modify() function : usage variation - Passing unexpected values to first argument $modify.
mv ext/date/tests/DateTime_modify_variation1.phpt{,.skip}
# Bug #48187 (DateTime::diff() corrupting microtime() result)
mv ext/date/tests/bug48187.phpt{,.skip}
# Bug #50475 (DateTime::setISODate followed by DateTime::setTime)
mv ext/date/tests/bug50475.phpt{,.skip}
# Bug #51819 (Case discrepancy in timezone names cause Uncaught exception and fatal error)
mv ext/date/tests/bug51819.phpt{,.skip}
# Bug #51994 (date_parse_from_format is parsing invalid date using 'yz' format)
mv ext/date/tests/bug51994.phpt{,.skip}
# Bug #52290 (setDate, setISODate, setTime works wrong when DateTime created from timestamp)
mv ext/date/tests/bug52290.phpt{,.skip}
# Test date_modify() function : usage variation - Passing unexpected values to second argument $format.
mv ext/date/tests/date_modify_variation2.phpt{,.skip}
# Test timezone_abbreviations_list() function : basic functionality
mv ext/date/tests/timezone_abbreviations_list_basic1.phpt{,.skip}
# Test 5: HTML Test
mv ext/dom/tests/dom005.phpt{,.skip}
# Bug #48555 (ImageFTBBox() differs from previous versions for texts with new lines)
mv ext/gd/tests/bug48555.phpt{,.skip}
# Feature Request #50283 (allow base in gmp_strval to use full range: 2 to 62, and -2 to -36)
mv ext/gmp/tests/bug50283.phpt{,.skip}
# gmp_nextprime()
mv ext/gmp/tests/gmp_nextprime.phpt{,.skip}
# InterBase: connect, close and pconnect
mv ext/interbase/tests/002.phpt{,.skip}
# InterBase: misc sql types (may take a while)
mv ext/interbase/tests/003.phpt{,.skip}
# InterBase: BLOB test
mv ext/interbase/tests/004.phpt{,.skip}
# InterBase: transactions
mv ext/interbase/tests/005.phpt{,.skip}
# InterBase: binding (may take a while)
mv ext/interbase/tests/006.phpt{,.skip}
# InterBase: array handling
mv ext/interbase/tests/007.phpt{,.skip}
# InterBase: event handling
mv ext/interbase/tests/008.phpt{,.skip}
# Bug #45373 (php crash on query with errors in params)
mv ext/interbase/tests/bug45373.phpt{,.skip}
# Bug #45575 (Segfault with invalid non-string as event handler callback)
mv ext/interbase/tests/bug45575.phpt{,.skip}
# Bug #46247 (ibase_set_event_handler() is allowing to pass callback without event)
mv ext/interbase/tests/bug46247.phpt{,.skip}
# Bug #46543 (ibase_trans() memory leaks when using wrong parameters)
mv ext/interbase/tests/bug46543.phpt{,.skip}
# ibase_affected_rows(): Basic test
mv ext/interbase/tests/ibase_affected_rows_001.phpt{,.skip}
# ibase_close(): Basic test
mv ext/interbase/tests/ibase_close_001.phpt{,.skip}
# ibase_drop_db(): Basic test
mv ext/interbase/tests/ibase_drop_db_001.phpt{,.skip}
# ibase_errmsg(): Basic test
mv ext/interbase/tests/ibase_errmsg_001.phpt{,.skip}
# ibase_free_query(): Basic test
mv ext/interbase/tests/ibase_free_query_001.phpt{,.skip}
# ibase_num_fields(): Basic test
mv ext/interbase/tests/ibase_num_fields_001.phpt{,.skip}
# ibase_num_params(): Basic test
mv ext/interbase/tests/ibase_num_params_001.phpt{,.skip}
# ibase_param_info(): Basic test
mv ext/interbase/tests/ibase_param_info_001.phpt{,.skip}
# ibase_rollback(): Basic test
mv ext/interbase/tests/ibase_rollback_001.phpt{,.skip}
# ibase_trans(): Basic test
mv ext/interbase/tests/ibase_trans_001.phpt{,.skip}
# ibase_trans(): Basic operations
mv ext/interbase/tests/ibase_trans_002.phpt{,.skip}
# get_locale()
mv ext/intl/tests/collator_get_locale.phpt{,.skip}
# collator_get_sort_key()
mv ext/intl/tests/collator_get_sort_key.phpt{,.skip}
# datefmt_format_code() and datefmt_parse_code()
mv ext/intl/tests/dateformat_format_parse.phpt{,.skip}
# datefmt_get_pattern_code and datefmt_set_pattern_code()
mv ext/intl/tests/dateformat_get_set_pattern.phpt{,.skip}
# datefmt_localtime_code()
mv ext/intl/tests/dateformat_localtime.phpt{,.skip}
# datefmt_parse_code()
mv ext/intl/tests/dateformat_parse.phpt{,.skip}
# datefmt_parse_localtime() with parse pos
mv ext/intl/tests/dateformat_parse_localtime_parsepos.phpt{,.skip}
# datefmt_parse_timestamp_code()  with parse pos
mv ext/intl/tests/dateformat_parse_timestamp_parsepos.phpt{,.skip}
# datefmt_set_timezone_id_code()
mv ext/intl/tests/dateformat_set_timezone_id.phpt{,.skip}
# numfmt_format()
mv ext/intl/tests/formatter_format.phpt{,.skip}
# numfmt_format_currency()
mv ext/intl/tests/formatter_format_currency.phpt{,.skip}
# numfmt_get/set_attribute()
mv ext/intl/tests/formatter_get_set_attribute.phpt{,.skip}
# grapheme()
mv ext/intl/tests/grapheme.phpt{,.skip}
# locale_get_display_name()
mv ext/intl/tests/locale_get_display_name.phpt{,.skip}
# locale_get_display_script()
mv ext/intl/tests/locale_get_display_script.phpt{,.skip}
# locale_get_display_variant()
mv ext/intl/tests/locale_get_display_variant.phpt{,.skip}
# ldap_sasl_bind() - Basic anonymous binding
mv ext/ldap/tests/ldap_sasl_bind_basic.phpt{,.skip}
# mysql connect
mv ext/mysql/tests/001.phpt{,.skip}
# mysql_connect()
mv ext/mysql/tests/mysql_connect.phpt{,.skip}
# mysql_[p]connect() - max_links/max_persistent
mv ext/mysql/tests/mysql_max_links.phpt{,.skip}
# mysql_[p]connect() - safe_mode
mv ext/mysql/tests/mysql_sql_safe_mode.phpt{,.skip}
# mysqli_connect()
mv ext/mysqli/tests/mysqli_connect.phpt{,.skip}
# new mysqli()
mv ext/mysqli/tests/mysqli_connect_oo.phpt{,.skip}
# new mysqli()
mv ext/mysqli/tests/mysqli_connect_oo_defaults.phpt{,.skip}
# Bug #28382 (openssl_x509_parse extensions support)
mv ext/openssl/tests/bug28382.phpt{,.skip}
# Bug #47828 (segfaults when a UTF-8 conversion fails openssl_x509_parse())
mv ext/openssl/tests/bug47828.phpt{,.skip}
# openssl_x509_parse() basic test
mv ext/openssl/tests/openssl_x509_parse_basic.phpt{,.skip}
# PDO_Firebird: connect/disconnect
mv ext/pdo_firebird/tests/connect.phpt{,.skip}
# PDO_Firebird: DDL/transactions
mv ext/pdo_firebird/tests/ddl.phpt{,.skip}
# PDO_Firebird: prepare/execute/binding
mv ext/pdo_firebird/tests/execute.phpt{,.skip}
# MySQL PDO->__construct(), options
mv ext/pdo_mysql/tests/pdo_mysql___construct_options.phpt{,.skip}
# MySQL PDO->__construct(), libmysql only options
mv ext/pdo_mysql/tests/pdo_mysql___construct_options_libmysql.phpt{,.skip}
# MySQL PDO class interface
mv ext/pdo_mysql/tests/pdo_mysql_interface.phpt{,.skip}
# PDO ODBC "long" columns
mv ext/pdo_odbc/tests/long_columns.phpt{,.skip}
# PDO SQLite Feature Request #42589 (getColumnMeta() should also return table name)
mv ext/pdo_sqlite/tests/bug_42589.phpt{,.skip}
# Test for bug 52013 about Phar::decompressFiles().
mv ext/phar/tests/bug52013.phpt{,.skip}
# Phar and RecursiveDirectoryIterator
mv ext/phar/tests/phar_oo_005.phpt{,.skip}
# Test posix_getgrgid() function : basic functionality
mv ext/posix/tests/posix_getgrgid_basic.phpt{,.skip}
# ReflectionClass::getConstructor()
mv ext/reflection/tests/ReflectionClass_getConstructor_basic.phpt{,.skip}
# ReflectionMethod::isConstructor()
mv ext/reflection/tests/ReflectionMethod_constructor_basic.phpt{,.skip}
# ReflectionObject::getConstructor() - basic function test
mv ext/reflection/tests/ReflectionObject_getConstructor_basic.phpt{,.skip}
# a script should not be able to modify session.use_trans_sid
mv ext/session/tests/014.phpt{,.skip}
# use_trans_sid should not affect SID
mv ext/session/tests/015.phpt{,.skip}
# rewriter correctly handles attribute names which contain dashes
mv ext/session/tests/018.phpt{,.skip}
# rewriter uses arg_seperator.output for modifying URLs
mv ext/session/tests/020.phpt{,.skip}
# rewriter handles form and fieldset tags correctly
mv ext/session/tests/021.phpt{,.skip}
# Bug #31454 (Incorrect adding PHPSESSID to links, which contains \r\n)
mv ext/session/tests/bug36459.phpt{,.skip}
# Bug #41600 (url rewriter tags doesn't work with namespaced tags)
mv ext/session/tests/bug41600.phpt{,.skip}
# Test session_encode() function : error functionality
mv ext/session/tests/session_encode_error2.phpt{,.skip}
# SimpleXML: XPath
mv ext/simplexml/tests/008.phpt{,.skip}
# SOAP Server 9: setclass and setpersistence(SOAP_PERSISTENCE_SESSION)
mv ext/soap/tests/server009.phpt{,.skip}
# ext/sockets - socket_strerror - basic test
mv ext/sockets/tests/socket_strerror.phpt{,.skip}
# Bug #38759 (sqlite2 empty query causes segfault)
mv ext/sqlite/tests/bug38759.phpt{,.skip}
# sqlite, session storage test
mv ext/sqlite/tests/sqlite_session_001.phpt{,.skip}
# sqlite, session destroy test
mv ext/sqlite/tests/sqlite_session_002.phpt{,.skip}
# SQLite3::loadExtension with empty extension test
mv ext/sqlite3/tests/sqlite3_33_load_extension_param.phpt{,.skip}
# SQLite3::loadExtension with disabled extensions
mv ext/sqlite3/tests/sqlite3_34_load_extension_ext_dir.phpt{,.skip}
# SQLite3::loadExtension test with wrong parameter type
mv ext/sqlite3/tests/sqlite3_loadextension_with_wrong_param.phpt{,.skip}
# Test fscanf() function: usage variations - unsigned int formats with integer values
mv ext/standard/tests/file/fscanf_variation39.phpt{,.skip}
# Test fscanf() function: usage variations - tracking file pointer while reading
mv ext/standard/tests/file/fscanf_variation55.phpt{,.skip}
# Bug #44394 (Last two bytes missing from output) with session.use_trans_id
mv ext/standard/tests/general_functions/bug44394_2.phpt{,.skip}
# Test function getservbyname()
mv ext/standard/tests/general_functions/getservbyname_basic.phpt{,.skip}
# proc_open
mv ext/standard/tests/general_functions/proc_open02.phpt{,.skip}
# time_sleep_until() function - basic test for time_sleep_until()
mv ext/standard/tests/misc/time_sleep_until_basic.phpt{,.skip}
# htmlentities() test 2 (setlocale / fr_FR.ISO-8859-15)
mv ext/standard/tests/strings/htmlentities02.phpt{,.skip}
# htmlentities() test 4 (setlocale / ja_JP.EUC-JP)
mv ext/standard/tests/strings/htmlentities04.phpt{,.skip}
# htmlentities() test 10 (default_charset / cp1252)
mv ext/standard/tests/strings/htmlentities10.phpt{,.skip}
# htmlentities() test 11 (default_charset / ISO-8859-15)
mv ext/standard/tests/strings/htmlentities11.phpt{,.skip}
# htmlentities() test 13 (default_charset / EUC-JP)
mv ext/standard/tests/strings/htmlentities13.phpt{,.skip}
# htmlentities() test 15 (setlocale / KOI8-R)
mv ext/standard/tests/strings/htmlentities15.phpt{,.skip}
# htmlentities() / html_entity_decode() #8592 - #9002 table test
mv ext/standard/tests/strings/htmlentities17.phpt{,.skip}
# Test setlocale() function : usage variations - Setting all available locales in the platform
mv ext/standard/tests/strings/setlocale_variation2.phpt{,.skip}
# Test sscanf() function : basic functionality - unsigned format
mv ext/standard/tests/strings/sscanf_basic6.phpt{,.skip}
# msg_send() data types when not serializing
mv ext/sysvmsg/tests/006.phpt{,.skip}
# wddx session serializer handler (serialize)
mv ext/wddx/tests/004.phpt{,.skip}
# wddx session serializer handler (deserialize)
mv ext/wddx/tests/005.phpt{,.skip}
# xmlrpc_encode_request() and various arguments
mv ext/xmlrpc/tests/002.phpt{,.skip}
# Bug #40576 (double values are truncated to 6 decimal digits when encoding)
mv ext/xmlrpc/tests/bug40576_64bit.phpt{,.skip}
# Bug #45555 (Segfault with invalid non-string as register_introspection_callback)
mv ext/xmlrpc/tests/bug45555.phpt{,.skip}
# Bug #45556 (Return value from callback isn't freed)
mv ext/xmlrpc/tests/bug45556.phpt{,.skip}
# Test 10: EXSLT Support
mv ext/xsl/tests/xslt010.phpt{,.skip}
# Check xsltprocessor::registerPHPFunctions and a non-string function in xsl
mv ext/xsl/tests/xsltprocessor_registerPHPFunctions-funcnostring.phpt{,.skip}
# Check xsltprocessor::registerPHPFunctions and a undefined php function
mv ext/xsl/tests/xsltprocessor_registerPHPFunctions-funcundef.phpt{,.skip}
# show information about extension
mv sapi/cli/tests/006.phpt{,.skip}
# CLI -a and readline
mv sapi/cli/tests/016.phpt{,.skip}
# Phar::buildFromIterator() RegexIterator(RecursiveIteratorIterator), SplFileInfo as current
mv ext/phar/tests/phar_buildfromiterator10.phpt{,.skip}
# output buffering - fatalism
mv tests/output/ob_011.phpt{,.skip}
# Inconsistencies when accessing protected members
mv Zend/tests/access_modifiers_008.phpt{,.skip}
# Inconsistencies when accessing protected members - 2
mv Zend/tests/access_modifiers_009.phpt{,.skip}
# Bug #48770 (call_user_func_array() fails to call parent from inheriting class)
mv Zend/tests/bug48770.phpt{,.skip}
# Bug #48770 (call_user_func_array() fails to call parent from inheriting class)
mv Zend/tests/bug48770_2.phpt{,.skip}
# Bug #48770 (call_user_func_array() fails to call parent from inheriting class)
mv Zend/tests/bug48770_3.phpt{,.skip}
# DBA with persistent connections
mv ext/dba/tests/dba015.phpt{,.skip}
# DBA DB4 with persistent connections
mv ext/dba/tests/dba_db4_018.phpt{,.skip}
# Bug #42718 (unsafe_raw filter not applied when configured as default filter)
mv ext/filter/tests/bug42718.phpt{,.skip}
# SimpleXML: array casting bug
mv ext/simplexml/tests/034.phpt{,.skip}
# Bug #39863 (file_exists() silently truncates after a null byte)
mv ext/standard/tests/file/bug39863.phpt{,.skip}
