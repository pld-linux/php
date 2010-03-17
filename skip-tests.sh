# easter_date()
mv ext/calendar/tests/easter_date.phpt{,.skip}
# unixtojd()
mv ext/calendar/tests/unixtojd.phpt{,.skip}
# Test DateTime::modify() function : usage variation - Passing unexpected values to first argument $modify.
mv ext/date/tests/DateTime_modify_variation1.phpt{,.skip}
# Bug #50392 date_create_from_format enforces 6 digits for 'u' format character
mv ext/date/tests/bug50392.phpt{,.skip}
# Test date_modify() function : usage variation - Passing unexpected values to second argument $format.
mv ext/date/tests/date_modify_variation2.phpt{,.skip}
# Bug #48555 (ImageFTBBox() differs from previous versions for texts with new lines)
mv ext/gd/tests/bug48555.phpt{,.skip}
# Feature Request #50283 (allow base in gmp_strval to use full range: 2 to 62, and -2 to -36)
mv ext/gmp/tests/bug50283.phpt{,.skip}
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
# numfmt_get/set_symbol()
mv ext/intl/tests/formatter_get_set_symbol.phpt{,.skip}
# numfmt_parse_currency()
mv ext/intl/tests/formatter_parse_currency.phpt{,.skip}
# locale_get_display_language()
mv ext/intl/tests/locale_get_display_language.phpt{,.skip}
# locale_get_display_name()
mv ext/intl/tests/locale_get_display_name.phpt{,.skip}
# locale_get_display_region()
mv ext/intl/tests/locale_get_display_region.phpt{,.skip}
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
# pcntl_exec()
mv ext/pcntl/tests/pcntl_exec.phpt{,.skip}
# pcntl_exec() 2
mv ext/pcntl/tests/pcntl_exec_2.phpt{,.skip}
# PDO_Firebird: connect/disconnect
mv ext/pdo_firebird/tests/connect.phpt{,.skip}
# PDO_Firebird: DDL/transactions
mv ext/pdo_firebird/tests/ddl.phpt{,.skip}
# PDO_Firebird: prepare/execute/binding
mv ext/pdo_firebird/tests/execute.phpt{,.skip}
# MySQL PDO->__construct(), options
mv ext/pdo_mysql/tests/pdo_mysql___construct_options.phpt{,.skip}
# MySQL PDO class interface
mv ext/pdo_mysql/tests/pdo_mysql_interface.phpt{,.skip}
# PDO ODBC "long" columns
mv ext/pdo_odbc/tests/long_columns.phpt{,.skip}
# PDO SQLite Feature Request #42589 (getColumnMeta() should also return table name)
mv ext/pdo_sqlite/tests/bug_42589.phpt{,.skip}
# Test posix_getgrgid() function : basic functionality
mv ext/posix/tests/posix_getgrgid_basic.phpt{,.skip}
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
# Test filetype() function: Check character type
mv ext/standard/tests/file/filetype_variation2.phpt{,.skip}
# realpath_cache_size() and realpath_cache_get()
mv ext/standard/tests/file/realpath_cache.phpt{,.skip}
# proc_open
mv ext/standard/tests/general_functions/proc_open02.phpt{,.skip}
# Test Blowfish crypt() with invalid rounds
mv ext/standard/tests/strings/crypt_blowfish_invalid_rounds.phpt{,.skip}
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
# wddx session serializer handler (serialize)
mv ext/wddx/tests/004.phpt{,.skip}
# wddx session serializer handler (deserialize)
mv ext/wddx/tests/005.phpt{,.skip}
# Bug #35447 (xml_parse_into_struct() chokes on the UTF-8 BOM)
mv ext/xml/tests/bug35447.phpt{,.skip}
# XML Parser test: concat character data and set empty handlers
mv ext/xml/tests/xml011.phpt{,.skip}
# xmlrpc_encode_request() and various arguments
mv ext/xmlrpc/tests/002.phpt{,.skip}
# Bug #40576 (double values are truncated to 6 decimal digits when encoding)
mv ext/xmlrpc/tests/bug40576.phpt{,.skip}
# Bug #42189 (xmlrpc_get_type() crashes PHP on invalid dates)
mv ext/xmlrpc/tests/bug42189.phpt{,.skip}
# Bug #44996 (xmlrpc_decode() ignores time zone on iso8601.datetime)
mv ext/xmlrpc/tests/bug44996.phpt{,.skip}
# Bug #45226 (xmlrpc_set_type() segfaults with valid ISO8601 date string)
mv ext/xmlrpc/tests/bug45226.phpt{,.skip}
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
# CLI php -m
mv sapi/cli/tests/018.phpt{,.skip}
# easter_date()
mv ext/calendar/tests/easter_date.phpt{,.skip}
# unixtojd()
mv ext/calendar/tests/unixtojd.phpt{,.skip}
# Test DateTime::modify() function : usage variation - Passing unexpected values to first argument $modify.
mv ext/date/tests/DateTime_modify_variation1.phpt{,.skip}
# Bug #50392 date_create_from_format enforces 6 digits for 'u' format character
mv ext/date/tests/bug50392.phpt{,.skip}
# Test date_modify() function : usage variation - Passing unexpected values to second argument $format.
mv ext/date/tests/date_modify_variation2.phpt{,.skip}
# Bug #48555 (ImageFTBBox() differs from previous versions for texts with new lines)
mv ext/gd/tests/bug48555.phpt{,.skip}
# Feature Request #50283 (allow base in gmp_strval to use full range: 2 to 62, and -2 to -36)
mv ext/gmp/tests/bug50283.phpt{,.skip}
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
# numfmt_get/set_symbol()
mv ext/intl/tests/formatter_get_set_symbol.phpt{,.skip}
# numfmt_parse_currency()
mv ext/intl/tests/formatter_parse_currency.phpt{,.skip}
# locale_get_display_language()
mv ext/intl/tests/locale_get_display_language.phpt{,.skip}
# locale_get_display_name()
mv ext/intl/tests/locale_get_display_name.phpt{,.skip}
# locale_get_display_region()
mv ext/intl/tests/locale_get_display_region.phpt{,.skip}
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
# pcntl_exec()
mv ext/pcntl/tests/pcntl_exec.phpt{,.skip}
# pcntl_exec() 2
mv ext/pcntl/tests/pcntl_exec_2.phpt{,.skip}
# PDO_Firebird: connect/disconnect
mv ext/pdo_firebird/tests/connect.phpt{,.skip}
# PDO_Firebird: DDL/transactions
mv ext/pdo_firebird/tests/ddl.phpt{,.skip}
# PDO_Firebird: prepare/execute/binding
mv ext/pdo_firebird/tests/execute.phpt{,.skip}
# MySQL PDO->__construct(), options
mv ext/pdo_mysql/tests/pdo_mysql___construct_options.phpt{,.skip}
# MySQL PDO class interface
mv ext/pdo_mysql/tests/pdo_mysql_interface.phpt{,.skip}
# PDO ODBC "long" columns
mv ext/pdo_odbc/tests/long_columns.phpt{,.skip}
# PDO SQLite Feature Request #42589 (getColumnMeta() should also return table name)
mv ext/pdo_sqlite/tests/bug_42589.phpt{,.skip}
# Test posix_getgrgid() function : basic functionality
mv ext/posix/tests/posix_getgrgid_basic.phpt{,.skip}
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
# Test filetype() function: Check character type
mv ext/standard/tests/file/filetype_variation2.phpt{,.skip}
# realpath_cache_size() and realpath_cache_get()
mv ext/standard/tests/file/realpath_cache.phpt{,.skip}
# proc_open
mv ext/standard/tests/general_functions/proc_open02.phpt{,.skip}
# Test Blowfish crypt() with invalid rounds
mv ext/standard/tests/strings/crypt_blowfish_invalid_rounds.phpt{,.skip}
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
# wddx session serializer handler (serialize)
mv ext/wddx/tests/004.phpt{,.skip}
# wddx session serializer handler (deserialize)
mv ext/wddx/tests/005.phpt{,.skip}
# Bug #35447 (xml_parse_into_struct() chokes on the UTF-8 BOM)
mv ext/xml/tests/bug35447.phpt{,.skip}
# XML Parser test: concat character data and set empty handlers
mv ext/xml/tests/xml011.phpt{,.skip}
# xmlrpc_encode_request() and various arguments
mv ext/xmlrpc/tests/002.phpt{,.skip}
# Bug #40576 (double values are truncated to 6 decimal digits when encoding)
mv ext/xmlrpc/tests/bug40576.phpt{,.skip}
# Bug #42189 (xmlrpc_get_type() crashes PHP on invalid dates)
mv ext/xmlrpc/tests/bug42189.phpt{,.skip}
# Bug #44996 (xmlrpc_decode() ignores time zone on iso8601.datetime)
mv ext/xmlrpc/tests/bug44996.phpt{,.skip}
# Bug #45226 (xmlrpc_set_type() segfaults with valid ISO8601 date string)
mv ext/xmlrpc/tests/bug45226.phpt{,.skip}
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
# CLI php -m
mv sapi/cli/tests/018.phpt{,.skip}
# Test open_basedir configuration
mv tests/security/open_basedir_fileinode.phpt{,.skip}
# Test fileinode() function: Variations
mv ext/standard/tests/file/fileinode_variation.phpt{,.skip}
# Test lstat() and stat() functions: usage variations - dir/file name stored in object
mv ext/standard/tests/file/lstat_stat_variation18.phpt{,.skip}
: Test lstat() and stat() functions: usage variations - dir/file names in array
mv ext/standard/tests/file/lstat_stat_variation19.phpt{,.skip}
