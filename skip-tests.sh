# DBA DB4 magic_quotes_runtime Test (info: DB4 handler used)
mv ext/dba/tests/dba_db4_010.phpt{,.skip}
# DBA TCADB handler test
mv ext/dba/tests/dba_tcadb.phpt{,.skip}
# Test ereg() function : basic functionality (with $regs)
mv ext/ereg/tests/ereg_basic_001.phpt{,.skip}
# Test ereg() function : basic functionality  (without $regs)
mv ext/ereg/tests/ereg_basic_002.phpt{,.skip}
# Test ereg() function : error conditions - test bad regular expressions
mv ext/ereg/tests/ereg_error_002.phpt{,.skip}
# Test ereg_replace() function : basic functionality
mv ext/ereg/tests/ereg_replace_basic_001.phpt{,.skip}
# Test ereg_replace() function : error conditions - bad regular expressions
mv ext/ereg/tests/ereg_replace_error_002.phpt{,.skip}
# Test ereg_replace() function : usage variations - unexpected type arg 1
mv ext/ereg/tests/ereg_replace_variation_001.phpt{,.skip}
# Test ereg() function : usage variations  - unexpected type arg 1
mv ext/ereg/tests/ereg_variation_001.phpt{,.skip}
# Test eregi() function : basic functionality (with $regs)
mv ext/ereg/tests/eregi_basic_001.phpt{,.skip}
# Test eregi() function : basic functionality  (without $regs)
mv ext/ereg/tests/eregi_basic_002.phpt{,.skip}
# Test eregi() function : error conditions - test bad regular expressions
mv ext/ereg/tests/eregi_error_002.phpt{,.skip}
# Test ereg() function : basic functionality
mv ext/ereg/tests/eregi_replace_basic_001.phpt{,.skip}
# Test eregi_replace() function : error conditions - bad regular expressions
mv ext/ereg/tests/eregi_replace_error_002.phpt{,.skip}
# Test eregi_replace() function : usage variations - unexpected type arg 1
mv ext/ereg/tests/eregi_replace_variation_001.phpt{,.skip}
# Test eregi() function : usage variations  - unexpected type arg 1
mv ext/ereg/tests/eregi_variation_001.phpt{,.skip}
# Test split() function : basic functionality - test a number of simple split, specifying a limit
mv ext/ereg/tests/split_basic_001.phpt{,.skip}
# Test split() function : basic functionality - test a number of simple split, without specifying a limit
mv ext/ereg/tests/split_basic_002.phpt{,.skip}
# Test split() function : error conditions - test bad regular expressions
mv ext/ereg/tests/split_error_002.phpt{,.skip}
# Test split() function : usage variations  - unexpected type for arg 1
mv ext/ereg/tests/split_variation_001.phpt{,.skip}
# Test spliti() function : basic functionality - test a number of simple spliti, specifying a limit
mv ext/ereg/tests/spliti_basic_001.phpt{,.skip}
# Test spliti() function : basic functionality - test a number of simple spliti, without specifying a limit
mv ext/ereg/tests/spliti_basic_002.phpt{,.skip}
# Test spliti() function : error conditions - test bad regular expressions
mv ext/ereg/tests/spliti_error_002.phpt{,.skip}
# Test spliti() function : usage variations  - unexpected type for arg 1
mv ext/ereg/tests/spliti_variation_001.phpt{,.skip}
# Bug #52209 (INPUT_ENV returns NULL for set variables (CLI))
mv ext/filter/tests/bug52209.phpt{,.skip}
# Bug #43073 (TrueType bounding box is wrong for angle<>0)
mv ext/gd/tests/bug43073.phpt{,.skip}
# Bug #48801 (Problem with imagettfbbox)
mv ext/gd/tests/bug48801.phpt{,.skip}
# PDO Common: PDORow + get_parent_class()
mv ext/pdo/tests/pdo_035.phpt{,.skip}
# Bug #47415 PDO_Firebird segfaults when passing lowercased column name to bindColumn()
mv ext/pdo_firebird/tests/bug_47415.phpt{,.skip}
# PDO_Firebird: bug 48877 The "bindValue" and "bindParam" do not work for PDO Firebird if we use named parameters (:parameter).
mv ext/pdo_firebird/tests/bug_48877.phpt{,.skip}
# PDO_Firebird: bug 53280 segfaults if query column count is less than param count
mv ext/pdo_firebird/tests/bug_53280.phpt{,.skip}
# FIREBIRD PDO Common: PDORow + get_parent_class()
mv ext/pdo_firebird/tests/pdo_035.phpt{,.skip}
# PDO_Firebird: connect/disconnect
mv ext/pdo_firebird/tests/connect.phpt{,.skip}
# PDO_Firebird: DDL/transactions
mv ext/pdo_firebird/tests/ddl.phpt{,.skip}
# PDO_Firebird: prepare/execute/binding
mv ext/pdo_firebird/tests/execute.phpt{,.skip}
# PDO_Firebird: rowCount
mv ext/pdo_firebird/tests/rowCount.phpt{,.skip}
# MySQL PDO Common: PDORow + get_parent_class()
mv ext/pdo_mysql/tests/pdo_035.phpt{,.skip}
# ODBC PDO Common: PDORow + get_parent_class()
mv ext/pdo_odbc/tests/pdo_035.phpt{,.skip}
# Postgres PDO Common: PDORow + get_parent_class()
mv ext/pdo_pgsql/tests/pdo_035.phpt{,.skip}
# PDO SQLite Bug #33841 (rowCount() does not work on prepared statements)
mv ext/pdo_sqlite/tests/bug33841.phpt{,.skip}
# Bug #35336 (crash on PDO::FETCH_CLASS + __set())
mv ext/pdo_sqlite/tests/bug35336.phpt{,.skip}
# PDO SQLite Feature Request #42589 (getColumnMeta() should also return table name)
mv ext/pdo_sqlite/tests/bug_42589.phpt{,.skip}
# SQLite PDO Common: Bug #34630 (inserting streams as LOBs)
mv ext/pdo_sqlite/tests/bug_34630.phpt{,.skip}
# SQLite PDO Common: Bug #35671 (binding by name breakage)
mv ext/pdo_sqlite/tests/bug_35671.phpt{,.skip}
# SQLite PDO Common: Bug #36428 (Incorrect error message for PDO::fetchAll())
mv ext/pdo_sqlite/tests/bug_36428.phpt{,.skip}
# SQLite PDO Common: Bug #36798 (Error parsing named parameters with queries containing high-ascii chars)
mv ext/pdo_sqlite/tests/bug_36798.phpt{,.skip}
# SQLite PDO Common: Bug #38253 (PDO produces segfault with default fetch mode)
mv ext/pdo_sqlite/tests/bug_38253.phpt{,.skip}
# SQLite PDO Common: Bug #38394 (Prepared statement error stops subsequent statements)
mv ext/pdo_sqlite/tests/bug_38394.phpt{,.skip}
# SQLite PDO Common: Bug #39398 (Booleans are not automatically translated to integers)
mv ext/pdo_sqlite/tests/bug_39398.phpt{,.skip}
# SQLite PDO Common: Bug #39656 (Crash when calling fetch() on a PDO statment object after closeCursor())
mv ext/pdo_sqlite/tests/bug_39656.phpt{,.skip}
# SQLite PDO Common: Bug #40285 (The prepare parser goes into an infinite loop on ': or ":)
mv ext/pdo_sqlite/tests/bug_40285.phpt{,.skip}
# SQLite PDO Common: Bug #42917 (PDO::FETCH_KEY_PAIR doesn't work with setFetchMode)
mv ext/pdo_sqlite/tests/bug_42917.phpt{,.skip}
# SQLite PDO Common: Bug #44173 (PDO->query() parameter parsing/checking needs an update)
mv ext/pdo_sqlite/tests/bug_44173.phpt{,.skip}
# SQLite PDO Common: Bug #44409 (PDO::FETCH_SERIALIZE calls __construct())
mv ext/pdo_sqlite/tests/bug_44409.phpt{,.skip}
# SQLite PDO Common: Bug #50458 (PDO::FETCH_FUNC fails with Closures)
mv ext/pdo_sqlite/tests/bug_50458.phpt{,.skip}
# SQLite PDO Common: PDO::FETCH_ASSOC
mv ext/pdo_sqlite/tests/pdo_001.phpt{,.skip}
# SQLite PDO Common: PDO::FETCH_NUM
mv ext/pdo_sqlite/tests/pdo_002.phpt{,.skip}
# SQLite PDO Common: PDO::FETCH_BOTH
mv ext/pdo_sqlite/tests/pdo_003.phpt{,.skip}
# SQLite PDO Common: PDO::FETCH_OBJ
mv ext/pdo_sqlite/tests/pdo_004.phpt{,.skip}
# SQLite PDO Common: PDO::FETCH_CLASS
mv ext/pdo_sqlite/tests/pdo_005.phpt{,.skip}
# SQLite PDO Common: PDO::FETCH_GROUP
mv ext/pdo_sqlite/tests/pdo_006.phpt{,.skip}
# SQLite PDO Common: PDO::FETCH_UNIQUE
mv ext/pdo_sqlite/tests/pdo_007.phpt{,.skip}
# SQLite PDO Common: PDO::FETCH_UNIQUE conflict
mv ext/pdo_sqlite/tests/pdo_008.phpt{,.skip}
# SQLite PDO Common: PDO::FETCH_CLASSTYPE
mv ext/pdo_sqlite/tests/pdo_009.phpt{,.skip}
# SQLite PDO Common: PDO::FETCH_CLASSTYPE and GROUP/UNIQUE
mv ext/pdo_sqlite/tests/pdo_010.phpt{,.skip}
# SQLite PDO Common: PDO::FETCH_FUNC and statement overloading
mv ext/pdo_sqlite/tests/pdo_011.phpt{,.skip}
# SQLite PDO Common: PDOStatement::setFetchMode
mv ext/pdo_sqlite/tests/pdo_012.phpt{,.skip}
# SQLite PDO Common: PDOStatement iterator
mv ext/pdo_sqlite/tests/pdo_013.phpt{,.skip}
# SQLite PDO Common: PDOStatement SPL iterator
mv ext/pdo_sqlite/tests/pdo_014.phpt{,.skip}
# SQLite PDO Common: PDO::FETCH_COLUMN
mv ext/pdo_sqlite/tests/pdo_015.phpt{,.skip}
# SQLite PDO Common: PDO::FETCH_BOUND
mv ext/pdo_sqlite/tests/pdo_016.phpt{,.skip}
# SQLite PDO Common: PDO::FETCH_BOUND w/o :
mv ext/pdo_sqlite/tests/pdo_016a.phpt{,.skip}
# SQLite PDO Common: transactions
mv ext/pdo_sqlite/tests/pdo_017.phpt{,.skip}
# SQLite PDO Common: serializing
mv ext/pdo_sqlite/tests/pdo_018.phpt{,.skip}
# SQLite PDO Common: fetch() and while()
mv ext/pdo_sqlite/tests/pdo_019.phpt{,.skip}
# SQLite PDO Common: PDOStatement::columnCount
mv ext/pdo_sqlite/tests/pdo_020.phpt{,.skip}
# SQLite PDO Common: PDOStatement::execute with parameters
mv ext/pdo_sqlite/tests/pdo_021.phpt{,.skip}
# SQLite PDO Common: extending PDO
mv ext/pdo_sqlite/tests/pdo_023.phpt{,.skip}
# SQLite PDO Common: assert that bindParam does not modify parameter
mv ext/pdo_sqlite/tests/pdo_024.phpt{,.skip}
# SQLite PDO Common: PDO::FETCH_INTO
mv ext/pdo_sqlite/tests/pdo_025.phpt{,.skip}
# SQLite PDO Common: extending PDO (2)
mv ext/pdo_sqlite/tests/pdo_026.phpt{,.skip}
# SQLite PDO Common: PDO::FETCH_LAZY
mv ext/pdo_sqlite/tests/pdo_027.phpt{,.skip}
# SQLite PDO Common: bindValue
mv ext/pdo_sqlite/tests/pdo_028.phpt{,.skip}
# SQLite PDO Common: extending PDO (3)
mv ext/pdo_sqlite/tests/pdo_029.phpt{,.skip}
# SQLite PDO Common: extending PDO (4)
mv ext/pdo_sqlite/tests/pdo_030.phpt{,.skip}
# SQLite PDO Common: PDOStatement SPL iterator
mv ext/pdo_sqlite/tests/pdo_031.phpt{,.skip}
# SQLite PDO Common: PDO::ATTR_CASE
mv ext/pdo_sqlite/tests/pdo_032.phpt{,.skip}
# SQLite PDO Common: PDO::quote()
mv ext/pdo_sqlite/tests/pdo_033.phpt{,.skip}
# SQLite PDO Common: PDO::FETCH_KEY_PAIR fetch mode test
mv ext/pdo_sqlite/tests/pdo_034.phpt{,.skip}
# SQLite PDO Common: PDORow + get_parent_class()
mv ext/pdo_sqlite/tests/pdo_035.phpt{,.skip}
# SQLite PDO Common: PECL Bug #5772 (PDO::FETCH_FUNC breaks on mixed case func name)
mv ext/pdo_sqlite/tests/pecl_bug_5772.phpt{,.skip}
# SQLite PDO Common: PECL Bug #5809 (PDOStatement::execute(array()) changes param)
mv ext/pdo_sqlite/tests/pecl_bug_5809.phpt{,.skip}
# Testing several callbacks using PDO::FETCH_FUNC
mv ext/pdo_sqlite/tests/pdo_fetch_func_001.phpt{,.skip}
# PDO_sqlite: Testing sqliteCreateAggregate()
mv ext/pdo_sqlite/tests/pdo_sqlite_createaggregate.phpt{,.skip}
# PDO_sqlite: Testing sqliteCreateCollation()
mv ext/pdo_sqlite/tests/pdo_sqlite_createcollation.phpt{,.skip}
# PDO_sqlite: Testing sqliteCreateFunction()
mv ext/pdo_sqlite/tests/pdo_sqlite_createfunction.phpt{,.skip}
# PDO_sqlite: Testing lastInsertId()
mv ext/pdo_sqlite/tests/pdo_sqlite_lastinsertid.phpt{,.skip}
# PDO_sqlite: Testing transaction
mv ext/pdo_sqlite/tests/pdo_sqlite_transaction.phpt{,.skip}
# Test posix_getgrgid() function : basic functionality
mv ext/posix/tests/posix_getgrgid_basic.phpt{,.skip}
# IPv6 support
mv ext/snmp/tests/ipv6.phpt{,.skip}
# OO API: getErrno & getError methods
mv ext/snmp/tests/snmp-object-errno-errstr.phpt{,.skip}
# OO API
mv ext/snmp/tests/snmp-object.phpt{,.skip}
# Function snmp2_get
mv ext/snmp/tests/snmp2_get.phpt{,.skip}
# Function snmp2_getnext
mv ext/snmp/tests/snmp2_getnext.phpt{,.skip}
# Function snmp2_real_walk
mv ext/snmp/tests/snmp2_real_walk.phpt{,.skip}
# Function snmp2_set (without MIBs loading)
mv ext/snmp/tests/snmp2_set-nomib.phpt{,.skip}
# Function snmp2_set
mv ext/snmp/tests/snmp2_set.phpt{,.skip}
# Function snmp2_walk
mv ext/snmp/tests/snmp2_walk.phpt{,.skip}
# SNMPv3 Support
mv ext/snmp/tests/snmp3.phpt{,.skip}
# Function snmp_getvalue
mv ext/snmp/tests/snmp_getvalue.phpt{,.skip}
# Function snmp_read_mib
mv ext/snmp/tests/snmp_read_mib.phpt{,.skip}
# Function snmpget
mv ext/snmp/tests/snmpget.phpt{,.skip}
# Function snmpgetnext
mv ext/snmp/tests/snmpgetnext.phpt{,.skip}
# Function snmprealwalk
mv ext/snmp/tests/snmprealwalk.phpt{,.skip}
# Function snmpset (without MIBs loading)
mv ext/snmp/tests/snmpset-nomib.phpt{,.skip}
# Function snmpset
mv ext/snmp/tests/snmpset.phpt{,.skip}
# Function snmpwalk
mv ext/snmp/tests/snmpwalk.phpt{,.skip}
# Multicast support: IPv4 receive options
mv ext/sockets/tests/mcast_ipv4_recv.phpt{,.skip}
# Multicast support: IPv6 receive options
mv ext/sockets/tests/mcast_ipv6_recv.phpt{,.skip}
# socket_import_stream: Test with multicasting
mv ext/sockets/tests/socket_import_stream-3.phpt{,.skip}
# Bug #45798 (sqlite3 doesn't notice if variable was bound)
mv ext/sqlite3/tests/bug45798.phpt{,.skip}
# Bug #53463 (sqlite3 columnName() segfaults on bad column_number)
mv ext/sqlite3/tests/bug53463.phpt{,.skip}
# SQLite3::query CREATE tests
mv ext/sqlite3/tests/sqlite3_02_create.phpt{,.skip}
# SQLite3::query INSERT tests
mv ext/sqlite3/tests/sqlite3_03_insert.phpt{,.skip}
# SQLite3::query UPDATE tests
mv ext/sqlite3/tests/sqlite3_04_update.phpt{,.skip}
# SQLite3::query DELETE tests
mv ext/sqlite3/tests/sqlite3_05_delete.phpt{,.skip}
# SQLite3::prepare Bound Variable test
mv ext/sqlite3/tests/sqlite3_06_prepared_stmt.phpt{,.skip}
# SQLite3::prepare Bound Value test
mv ext/sqlite3/tests/sqlite3_07_prepared_stmt.phpt{,.skip}
# SQLite3::createFunction
mv ext/sqlite3/tests/sqlite3_08_udf.phpt{,.skip}
# SQLite3::prepare Bound Variable Blob test
mv ext/sqlite3/tests/sqlite3_09_blob_bound_param.phpt{,.skip}
# SQLite3::prepare Bound Value test
mv ext/sqlite3/tests/sqlite3_10_bound_value_name.phpt{,.skip}
# SQLite3::query Unfinalized statement tests
mv ext/sqlite3/tests/sqlite3_12_unfinalized_stmt_cleanup.phpt{,.skip}
# SQLite3::query Skip all cleanup
mv ext/sqlite3/tests/sqlite3_13_skip_all_cleanup.phpt{,.skip}
# SQLite3::querySingle tests
mv ext/sqlite3/tests/sqlite3_14_querysingle.phpt{,.skip}
# SQLite3::query SELECT with no results
mv ext/sqlite3/tests/sqlite3_16_select_no_results.phpt{,.skip}
# SQLite3::changes() tests
mv ext/sqlite3/tests/sqlite3_18_changes.phpt{,.skip}
# SQLite3 columnType and columnName
mv ext/sqlite3/tests/sqlite3_19_columninfo.phpt{,.skip}
# SQLite3::escapeString
mv ext/sqlite3/tests/sqlite3_23_escape_string.phpt{,.skip}
# SQLite3::lastInsertRowID tests
mv ext/sqlite3/tests/sqlite3_24_last_insert_rowid.phpt{,.skip}
# SQLite3::createAggregate() test
mv ext/sqlite3/tests/sqlite3_25_create_aggregate.phpt{,.skip}
# SQLite3::reset prepared statement
mv ext/sqlite3/tests/sqlite3_26_reset_prepared_stmt.phpt{,.skip}
# SQLite3::reset prepared statement results
mv ext/sqlite3/tests/sqlite3_27_reset_prepared_stmt_result.phpt{,.skip}
# SQLite3_stmt::clear prepared statement results
mv ext/sqlite3/tests/sqlite3_28_clear_bindings.phpt{,.skip}
# SQLite3::blobOpen stream test
mv ext/sqlite3/tests/sqlite3_30_blobopen.phpt{,.skip}
# SQLite3::changes empty str tests
mv ext/sqlite3/tests/sqlite3_32_changes.phpt{,.skip}
# SQLite3::lastInsertRowID parameter test
mv ext/sqlite3/tests/sqlite3_32_last_insert_rowid_param.phpt{,.skip}
# SQLite3:: reset
mv ext/sqlite3/tests/sqlite3_33_reset.phpt{,.skip}
# SQLite3_stmt::readOnly check
mv ext/sqlite3/tests/sqlite3_35_stmt_readonly.phpt{,.skip}
# Test SQLite3::createCollation() by adding strnatcmp() as an SQL COLLATE sequence
mv ext/sqlite3/tests/sqlite3_36_create_collation.phpt{,.skip}
# SQLite3::blobOpen test, testing stream with wrong parameter count
mv ext/sqlite3/tests/sqlite3_openblob_wrongparams.phpt{,.skip}
# SQLite3::prepare test, testing for faulty statement
mv ext/sqlite3/tests/sqlite3_prepare_faultystmt.phpt{,.skip}
# SQLite3::prepare test, testing for wrong parameters
mv ext/sqlite3/tests/sqlite3_prepare_wrongparams.phpt{,.skip}
# SQLite3Stmt::clear test with parameters
mv ext/sqlite3/tests/sqlite3_prepared_stmt_clear_with_params.phpt{,.skip}
# SQLite3Result::fetchArray() test, testing two params causes a failure
mv ext/sqlite3/tests/sqlite3result_fetcharray_with_two_params_fails.phpt{,.skip}
# SQLite3Result::numColumns parameters
mv ext/sqlite3/tests/sqlite3result_numcolumns_error.phpt{,.skip}
# SQLite3Result::reset test, testing an exception is raised when calling reset with parameters
mv ext/sqlite3/tests/sqlite3result_reset_with_params_fails.phpt{,.skip}
# SQLite3Stmt::paramCount basic test
mv ext/sqlite3/tests/sqlite3stmt_paramCount_basic.phpt{,.skip}
# SQLite3Stmt::paramCount error test
mv ext/sqlite3/tests/sqlite3stmt_paramCount_error.phpt{,.skip}
# SQLite3Stmt::reset with parameter test
mv ext/sqlite3/tests/sqlite3stmt_reset_params.phpt{,.skip}
# Test function getservbyname()
mv ext/standard/tests/general_functions/getservbyname_basic.phpt{,.skip}
# proc_nice() basic behaviour
mv ext/standard/tests/general_functions/proc_nice_basic.phpt{,.skip}
# proc_open
mv ext/standard/tests/general_functions/proc_open02.phpt{,.skip}
# Test setlocale() function : usage variations - Setting all available locales in the platform
mv ext/standard/tests/strings/setlocale_variation2.phpt{,.skip}
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
# apache_request_headers() stack overflow.
mv sapi/cgi/tests/apache_request_headers.phpt{,.skip}
# show information about extension
mv sapi/cli/tests/006.phpt{,.skip}
# Bug #60591 (Memory leak when access a non-exists file)
mv sapi/cli/tests/php_cli_server_016.phpt{,.skip}
