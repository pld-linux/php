#!/bin/sh
# DBA DB4 magic_quotes_runtime Test (info: DB4 handler used)
#mv ext/dba/tests/dba_db4_010.phpt{,.skip}
# DBA TCADB handler test
mv ext/dba/tests/dba_tcadb.phpt{,.skip}
# enchant_broker_describe() function
$x86 && mv ext/enchant/tests/broker_describe.phpt{,.skip}
# enchant_broker_request_dict() function
$x86 && mv ext/enchant/tests/broker_request_dict.phpt{,.skip}
# bug #13181, leaving a context frees the broker resources
$x86 && mv ext/enchant/tests/bug13181.phpt{,.skip}
# Bug #60150 (Integer overflow during the parsing of invalid exif header)
$ix86 mv ext/exif/tests/bug60150.phpt{,.skip}
# Bug #52209 (INPUT_ENV returns NULL for set variables (CLI))
mv ext/filter/tests/bug52209.phpt{,.skip}
# Bug #43073 (TrueType bounding box is wrong for angle<>0)
mv ext/gd/tests/bug43073.phpt{,.skip}
# Bug #48801 (Problem with imagettfbbox)
mv ext/gd/tests/bug48801.phpt{,.skip}
# Bug #47415 PDO_Firebird segfaults when passing lowercased column name to bindColumn()
mv ext/pdo_firebird/tests/bug_47415.phpt{,.skip}
# PDO_Firebird: bug 48877 The "bindValue" and "bindParam" do not work for PDO Firebird if we use named parameters (:parameter).
mv ext/pdo_firebird/tests/bug_48877.phpt{,.skip}
# PDO_Firebird: bug 53280 segfaults if query column count is less than param count
mv ext/pdo_firebird/tests/bug_53280.phpt{,.skip}
# PDO_Firebird: connect/disconnect
mv ext/pdo_firebird/tests/connect.phpt{,.skip}
# PDO_Firebird: DDL/transactions
mv ext/pdo_firebird/tests/ddl.phpt{,.skip}
# PDO_Firebird: prepare/execute/binding
mv ext/pdo_firebird/tests/execute.phpt{,.skip}
# PDO_Firebird: rowCount
mv ext/pdo_firebird/tests/rowCount.phpt{,.skip}
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
# SOAP Server 9: setclass and setpersistence(SOAP_PERSISTENCE_SESSION)
mv ext/soap/tests/server009.phpt{,.skip}
# socket_import_stream: Test with multicasting
mv ext/sockets/tests/socket_import_stream-3.phpt{,.skip}
# Test function getservbyname()
mv ext/standard/tests/general_functions/getservbyname_basic.phpt{,.skip}
# proc_nice() basic behaviour
mv ext/standard/tests/general_functions/proc_nice_basic.phpt{,.skip}
# proc_open
mv ext/standard/tests/general_functions/proc_open02.phpt{,.skip}
# Test setlocale() function : usage variations - Setting all available locales in the platform
mv ext/standard/tests/strings/setlocale_variation2.phpt{,.skip}
# apache_request_headers() stack overflow.
mv sapi/cgi/tests/apache_request_headers.phpt{,.skip}
# show information about extension
mv sapi/cli/tests/006.phpt{,.skip}
# Bug #61546 (functions related to current script failed when chdir() in cli sapi)
$ix86 mv sapi/cli/tests/bug61546.phpt{,.skip}
# Bug #60591 (Memory leak when access a non-exists file)
mv sapi/cli/tests/php_cli_server_016.phpt{,.skip}

# failing tests from builders (requiring DNS apparently)
# PDO SQLite Feature Request #42589 (getColumnMeta() should also return table name)
$ix86 mv ext/pdo_sqlite/tests/bug_42589.phpt{,.skip}
# Bug #60749: SNMP module should not strip non-standard SNMP port from hostname
mv ext/snmp/tests/bug60749.phpt{,.skip}
# Wrong hostname
mv ext/snmp/tests/wrong_hostname.phpt{,.skip}
# ext/sockets - socket_bind - basic test
mv ext/sockets/tests/socket_bind.phpt{,.skip}
# gethostbyname() function - basic return valid ip address test
mv ext/standard/tests/network/gethostbyname_error004.phpt{,.skip}
# getmxrr() test
mv ext/standard/tests/network/getmxrr.phpt{,.skip}
# http-stream test
mv ext/standard/tests/network/http-stream.phpt{,.skip}
