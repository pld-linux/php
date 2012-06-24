<!-- X-URL: http://www.php.net/FAQ.php3 -->
<BASE HREF="http://www.php.net/FAQ.php3">

<HTML>
<HEAD>
<TITLE>PHP3: Frequently Asked Questions</TITLE>


<SCRIPT LANGUAGE="JavaScript">
<!--
var loaded = 0;
var gotlayers = 0;
var lastbutton='top';

function popUp(menuName,on) {
}
function moveLayers() {
}



function change(Name,No) {
}
function changebullet(Name,No) {
}
function hide() {
}


//--->
</SCRIPT>

</HEAD>

<BODY MARGINHEIGHT=3 MARGINWIDTH=3 TOPMARGIN=3 LEFTMARGIN=3 BGCOLOR="#FFFFFF" TEXT="#000000" LINK="#5B69A6" VLINK="#5B69A6" ALINK="#00FF00"
><A NAME="top">
<TABLE BORDER=0 CELLPADDING=0 CELLSPACING=0 WIDTH="100%">
 <TR valign=top>
  <TD ALIGN=left width=150 BGCOLOR="#5B69A6">
   <TABLE BORDER=0 CELLPADDING=0 CELLSPACING=0 WIDTH="150">
    <TR VALIGN=top>
     <TD ALIGN=left>
      <IMG SRC="/gifs/cap-ul.gif" WIDTH=9 HEIGHT=9 BORDER=0><BR>
      <IMG SRC='/gifs/spacer.gif' WIDTH=15 HEIGHT=67 BORDER=0 ALT=' '><A HREF="/index.php3"><IMG SRC="/gifs/logo.gif" ALT="PHP3 Home Page" WIDTH=130 HEIGHT=67 BORDER=0></A><BR>
      <IMG SRC='/gifs/spacer.gif' WIDTH=1 HEIGHT=10 BORDER=0 ALT=' '><BR>
     </TD>
    </TR>
    <TR VALIGN=top>
     <TD ALIGN=left>
	<A HREF="downloads.php3" onMouseover="change('down',1);" 
 onMouseout="hide();"><IMG SRC="/gifs/b-downloads-p.gif" 
 ALT="Downloads" 
 WIDTH=129 HEIGHT=30 BORDER=0 
 NAME="down" 
 HSPACE=10 VSPACE=0></A><BR>
<A HREF="docs.php3" onMouseover="change('docs',1);" 
 onMouseout="hide();"><IMG SRC="/gifs/b-docs-p.gif" 
 ALT="Documentation" 
 WIDTH=129 HEIGHT=30 BORDER=0 
 NAME="docs" 
 HSPACE=10 VSPACE=0></A><BR>
<A HREF="support.php3" onMouseover="change('dev',1);" 
 onMouseout="hide();"><IMG SRC="/gifs/b-development-p.gif" 
 ALT="Getting Help" 
 WIDTH=129 HEIGHT=30 BORDER=0 
 NAME="dev" 
 HSPACE=10 VSPACE=0></A><BR>
<A HREF="news.php3" onMouseover="change('news',1);" 
 onMouseout="hide();"><IMG SRC="/gifs/b-news-p.gif" 
 ALT="PHP News last updated: Jun 10, 1998" 
 WIDTH=129 HEIGHT=30 BORDER=0 
 NAME="news" 
 HSPACE=10 VSPACE=0></A><BR>
<A HREF="projects.php3" onMouseover="change('proj',1);" 
 onMouseout="hide();"><IMG SRC="/gifs/b-projects-p.gif" 
 ALT="Projects using PHP" 
 WIDTH=129 HEIGHT=30 BORDER=0 
 NAME="proj" 
 HSPACE=10 VSPACE=0></A><BR>
<A HREF="links.php3" onMouseover="change('link',1);" 
 onMouseout="hide();"><IMG SRC="/gifs/b-links-p.gif" 
 ALT="PHP Links" 
 WIDTH=129 HEIGHT=30 BORDER=0 
 NAME="link" 
 HSPACE=10 VSPACE=0></A><BR>
<A HREF="mirrors.php3" onMouseover="change('mirr',1); popUp('mirrorsKick',true);" 
 ><IMG SRC="/gifs/b-mirror-p.gif" 
 ALT="Mirror sites" 
 WIDTH=129 HEIGHT=30 BORDER=0 
 NAME="mirr" 
 HSPACE=10 VSPACE=0></A><BR>
     </TD>
    </TR>
   </TABLE>
  </TD>
  <TD align=left width="100%">
   <TABLE BORDER=0 CELLPADDING=0 CELLSPACING=0 width="100%">
    <TR VALIGN=middle BGCOLOR="#5B69A6">
     <TD ALIGN=left>
      <IMG SRC='/gifs/spacer.gif' WIDTH=5 HEIGHT=1 BORDER=0 ALT=' '><FONT FACE="tahoma, verdana, arial, helvetica, sans-serif" SIZE=4><B>Frequently Asked Questions</B></FONT><BR>
     </TD>
     <TD ALIGN=right>
      <IMG SRC="/gifs/b-close-p.gif" 
 ALT="" 
 WIDTH=1 HEIGHT=1 BORDER=0 
 NAME="close" 
 HSPACE=0 VSPACE=0><A HREF="/source.php3?page_url=/FAQ.php3" onMouseover="change('sour',1);" 
 onMouseout="hide();"><IMG SRC="/gifs/b-source-p.gif" 
 ALT="View the source code for this page" 
 WIDTH=75 HEIGHT=30 BORDER=0 
 NAME="sour" 
 HSPACE=5 VSPACE=9></A><A HREF="/search.php3" onMouseover="change('sear',1); popUp('searchKick',true);" 
 ><IMG SRC="/gifs/b-search-p.gif" 
 ALT="Search the site" 
 WIDTH=75 HEIGHT=30 BORDER=0 
 NAME="sear" 
 HSPACE=5 VSPACE=9></A><IMG SRC="/gifs/cap-right.gif" WIDTH=24 HEIGHT=48 BORDER=0><BR></TD>
    </TR>
   </TABLE>
   <TABLE BORDER=0 CELLPADDING=0 CELLSPACING=0 width="100%">
    <TR VALIGN=top BGCOLOR="#FFFFFF">
     <TD ALIGN=left WIDTH="12">
      <IMG SRC="/gifs/corner-ul.gif" WIDTH=12 HEIGHT=12 BORDER=0><BR>
     </TD>
     <TD ALIGN=left WIDTH="100%">
            <FONT FACE="tahoma, verdana, arial, helvetica, sans-serif">
            <BR CLEAR=ALL>
      <!-- start body -->

<P>This is a list of Frequently Asked Questions about PHP3 and
their answers. If you have suggestions or additions, send them to
<CODE>php3@lists.php.net</CODE>.

<HR noshade>

<H2>General Information</H2>

<DL>
  <DT><B>
    What is PHP3?
  </B></DT>
  <DD>
    From the <A href="http://www.php.net/manual/">manual</A>:

    <BLOCKQUOTE>
    <P>PHP Version 3.0 is an HTML-embedded scripting
    language. Much of its syntax is borrowed from C, Java and Perl with a
    couple of unique PHP-specific features thrown in. The goal of the language
    is to allow web developers to write dynamically generated pages quickly.
    </BLOCKQUOTE>
  <P>
  </DD>

  <DT><B>
    What is its relation to PHP/FI?
  </B></DT>
  <DD>
    PHP3 is the successor to PHP/FI 2.0.
  <P>
  </DD>
  <DT><B>
    Can I run both PHP/FI 2.0 and PHP3 at the same time?
  </B></DT>
  <DD>
    Yes, PHP3 was written so as to not interfere with an existing PHP/FI 2 installation.
    Instructions for building Apache 1.3.0 with both PHP/FI 2 and PHP3 modules can be
    found <a href="php2.php3">HERE</a>.
  <P>

  <DT><B>
    What are the differences between PHP3 and PHP/FI 2.0?
  </B></DT>
  <DD>
    For a complete list of the changes, read the <A
    href="changes.php3">CHANGES</A> file included in the PHP3
    distribution. Some highlights:

    <UL>
      <LI>All-new parser.
      <LI>Persistent database connections.
      <LI>A native Windows95/NT port.
      <LI>IMAP, SNMP, and LDAP extensions.
    </UL>
  <P>
  </DD>

  <DT><B>
    I heard it's possible to access Microsoft SQL Server from PHP3. How?
  </B></DT>
  <DD>
    On Windows 95/NT machines, you can simply use the included ODBC support
    and the correct ODBC driver.

    <P>On Unix machines, you can use the Sybase-CT driver
    to access Microsoft SQL Servers because they are (at
    least mostly) protocol-compatible. Sybase has made a <A
    href="/extra/ctlib-linux-elf.tar.gz">free version of the necessary
    libraries for Linux systems</A>.  For other Unix operating systems,
    you need to contact Sybase for the correct libraries (which cost
    money).
  <P>
  </DD>

  <DT><B>
    Can I access Microsoft Access databases?
  </B></DT>
  <DD>
    Yes. You already have all the tools you need if you are running
    entirely under Windows 95 or NT, where you can use ODBC and Microsoft's
    ODBC drivers for Microsoft Access databases. From other platforms, you
    would need to have a server running Windows NT (or possibly Windows 95)
    which you connected to using ODBC drivers from your other platform and
    <A href="http://www.openlinksw.com/">OpenLink Software's ODBC Agent</A>
    software, which runs US$4,000.

    <P>Some better alternatives are to use an SQL server that has
    Windows ODBC drivers and use that to store the data, which you can
    then access from Microsoft Access (using ODBC) and PHP3 (using the
    built-in drivers), or to use an intermediary file format that Access
    and PHP3 both understand, such as flat-files or dBase databases.
  <P>
  </DD>

  <DT><B>
    Is there a PHP3 mailing list?
  </B></DT>
  <DD>
    Of course! To subscribe, send mail to
    <CODE>php3-subscribe@lists.php.net</CODE>. You don't need to include
    anything special in the subject or body of the message.

    <P>To unsubscribe, send mail to <CODE>php3-unsubscribe@lists.php.net</CODE>.
  <P>
  </DD>

  <DT><B>
    Help! I can't seem to subscribe to the mailing list!
  </B></DT>
  <DT><B>
    Help! I can't seem to unsubscribe from the mailing list!
  </B></DT>
  <DD>
    If you have problems subscribing to or unsubscribing from the
    PHP3 mailng list, it may be because the mailing list software
    can't figure out the correct mailing address to use. If
    your email address was <CODE>joeblow@example.com</CODE>,
    you can send your subscription request to
    <CODE>php3-subscribe-joeblow=example.com@lists.php.net</CODE>,
    or your unsubscription request to
    <CODE>php3-unsubscribe-joeblow=example.com@lists.php.net</CODE>.
  <P>
  </DD>

  <DT><B>
    Is there an archive of the mailing list anywhere?
  </B></DT>
  <DD>
    Yes, it's located at <A
    href="http://www.tryc.on.ca/php3.html">http://www.tryc.on.ca/php3.html</A>.
  </DD>
</DL>

<HR noshade>

<H2>Obtaining PHP3</H2>

<DL>
  <DT><B>
    Where can I obtain PHP3?
  </B></DT>
  <DD>
    You can download PHP3 from any of the members of the
    PHP3 network of sites. These can be found at <A
    href="http://www.php.net/">http://www.php.net/</A>.
    You can also use anonymous CVS to get the absolute latest
    version of the source. For more information, go to <A
    href="http://ca.php.net/cvsweb.cgi">http://ca.php.net/cvsweb.cgi</A>.
  <P>
  </DD>

  <DT><B>
    Are pre-compiled binary versions available?
  </B></DT>
  <DD>
    Yes, as long as you're looking for binaries for Windows 95 or NT.
    They're available in the same place as the source.
  <P>
  </DD>

  <DT><B>
    Where can I get libraries needed to compile some of the optional
    PHP3 extensions?
  </B></DT>
  <DD>
    <B>Note:</B> Those marked with * are not thread-safe libraries, and
    should not be used with PHP3 as a server module in the multi-threaded
    Windows web servers (IIS, Netscape).  This does not matter in Unix
    environments, yet.

    <UL>
      <LI>LDAP* (unix): <A href="ftp://terminator.rs.itd.umich.edu/ldap/ldap-3.3.tar.Z">ftp://terminator.rs.itd.umich.edu/ldap/ldap-3.3.tar.Z</A>
      <LI>LDAP (unix/win): <A HREF="http://developer.netscape.com/tech/directory/downloads.html" TARGET="_top">Netscape Directory (LDAP) SDK 1.1</A>
          There is also a free LDAP server at: <A href="ftp://ftp.critical-angle.com/pub/cai/slapd/">ftp://ftp.critical-angle.com/pub/cai/slapd/</A>.
      <LI>Berkeley DB2 (Unix/Win): <A href="http://www.sleepycat.com/">http://www.sleepycat.com/</A>
      <LI>SNMP* (Unix): <A href="http://www.ece.ucdavis.edu/ucd-snmp/">http://www.ece.ucdavis.edu/ucd-snmp/</A> (Note: PHP3 uses the native SNMP interface in Windows.)
      <LI>GD* (Unix/Win): <A href="http://www.boutell.com/gd/#buildgd">http://www.boutell.com/gd/#buildgd</A> 
      <LI>mSQL* (Unix): <A href="http://www.hughes.com.au/">http://www.hughes.com.au/</A> 
      <LI>mSQL* (Win) : <A HREF="http://blnet.com/msqlpc/">MSQL PC Home Page</a>
      <LI>MySQL (Unix): <A href="http://www.tcx.se/">http://www.tcx.se/</A>
      <LI>IMAP* (Win/Unix): <A HREF="ftp://ftp.cac.washington.edu/imap/old/imap-4.tar.Z">ftp://ftp.cac.washington.edu/imap/old/imap-4.tar.Z</A>
      <LI>Sybase-CT* (Linux, libc5):  <A href="/extra/ctlib-linux-elf.tar.gz">Available locally</A>
      <LI>FreeType: <A HREF="http://www.physiol.med.tu-muenchen.de/~robert/freetype.html">http://www.physiol.med.tu-muenchen.de/~robert/freetype.html</A>
	  <LI>ZLib (Unix/Win32): <A HREF="http://www.cdrom.com/pub/infozip/zlib/">http://www.cdrom.com/pub/infozip/zlib/</a>
    </UL>
  <P>
  </DD>

  <DT><B>
    How do I get these libraries to work?
  </B></DT>
  <DD>
    You will need to follow instructions provided with the library. Some of
    these libraries are detected automatically when you run the 'configure'
    script of PHP3 (such as the GD library), and others you will have to
    enable using '--with-EXTENSION' options to 'configure'. Run 'configure
    --help' for a listing of these.
  <P>
  </DD>

  <DT><B>
    I got the latest version of the PHP3 source code from the CVS
    repository on my Windows 95/NT machine, what do I need to compile it?
  </B></DT>
  <DD>
    First, you will need Microsoft Visual C++ v5 (v4 may do
    it also, but we do it with v5), and you will need to <A
    href="http://www.php.net/win32/makeparser.zip">download Bison and
    Flex</A>.  You will need to put Bison and Flex somewhere in your
    path, or add their location to your path.  Then run the batch file
    'makeparser' before compiling with MSVC.  You also may need to edit
    some settings in the project settings.  You should be familier enough
    with MSVC to know what to do ;).
  <P>
  </DD>
</DL>

  <DT><B>
    Where do I find the Browser Capabilities File?
  </B></DT>
  <DD>
    You can find PHP's own browscap.ini file at <a href="http://php.netvision.net.il/browscap/">http://php.netvision.net.il/browscap/</a>.
	There is also another browscap.ini file at <a href="http://www.cyscape.com/asp/browscap/">http://www.cyscape.com/asp/browscap/</a>.
  <P>
  </DD>

<HR noshade>

<H2>Installation</H2>

<P>To install PHP3, follow the instructions in the <A
href="http://ca.php.net/cvsweb.cgi/INSTALL?rev=1.18">INSTALL</A>
file located in the distribution. Windows
95 and NT users should also read the <A
href="http://ca.php.net/cvsweb.cgi/README.WIN32?rev=1.3">README.WIN32</A>
file.  There are also some helpful hints for Windows users here:
<a href="http://leonard.staff.imaginet.fr/Doc/php/configuration_NT.html">
http://leonard.staff.imaginet.fr/Doc/php/configuration_NT.html</a>.

<H3>Common Problems</H3>

<DL>
  <DT><B>
    I got the latest version of PHP3 using the anonymous CVS service,
    but there's no configure script!
  </B></DT>
  <DD>
    You have to have the GNU autoconf package installed so you can
    generate the configure script from configure.in. Just run
    <CODE>autoconf</CODE> in the top-level directory after getting
    the sources from the CVS server. (Also, unless you run configure
    with the <CODE>--enable-maintainer-mode</CODE> option, the
    configure script will not automatically get rebuilt when the
    configure.in file is updated, so you should make sure to do that
    manually when you notice configure.in has changed. One symptom
    of this is finding things like @VARIABLE@ in your Makefile after
    configure or config.status is run.
  <P>
  </DD>
  <DT><B>
    I'm having problems configuring PHP3 to work with Apache. It says
    it can't find httpd.h, but it's right where I said it is!
  </B></DT>
  <DD>
    You need to tell the configure/setup script the location of the
    <EM>top-level</EM> of your Apache source tree. This means that
    you want to specify '<CODE>--with-apache=/path/to/apache</CODE>'
    and <EM>not</EM> '<CODE>--with-apache=/path/to/apache/src</CODE>'.
  <P>
  </DD>
  <DT><B>
    When I run configure, it says that it can't find the include files or
    library for GD, gdbm, or some other package!
  </B></DT>
  <DD>
    You can make the configure script looks for header files and libraries
    in non-standard locations by specifying additional flags to pass to
    the C preprocessor and linker, such as:
<FONT FACE="monospaced"><PRE>
    CPPFLAGS=-I/path/to/include LDFLAGS=-L/path/to/library ./configure
</PRE></FONT>
    If you're using a csh-variant for your login shell (why?), it would be:
<FONT FACE="monospaced"><PRE>
    env CPPFLAGS=-I/path/to/include LDFLAGS=-L/path/to/library ./configure
</PRE></FONT>
  <P>
  </DD>

  <DT><B>
    When it is compiling the file language-parser.tab.c, it gives me errors
    that say 'yytname undeclared'.
  </B></DT>
  <DD>
    You need to update your version of Bison. You can find the latest version
    at <A href="ftp://prep.ai.mit.edu/pub/gnu/">ftp://prep.ai.mit.edu/pub/gnu/</A>.
  <P>
  </DD>
            
  <DT><B>
    When I run 'make', it seems to run fine but then fails when it
    tries to link the final application complaining that it can't find
    some files.
  </B></DT>
  <DD>
    Some old versions of make that don't correctly put the compiled
    versions of the files in the functions directory into that same
    directory. Try running "<CODE>cp *.o functions</CODE>" and then
    re-running 'make' to see if that helps. If it does, you should really
    upgrade to a recent version of GNU make.
  <P>
  </DD>

  <DT><B>
    When linking PHP3, it complains about a number of undefined references.
  </B></DT>
  <DD>
    Take a look at the link line and make sure that all of the appropriate
    libraries are being included at the end. Common ones that you might have
    missed are '-ldl' and any libraries required for any database support
    you included.
    <P>
    If you're linking with Apache 1.2.x, did you remember to add the
    appropriate information to the EXTRA_LIBS line of the Configuration
    file and re-rerun Apache's Configure script? See the <A href="http://ca.php.net/cvsweb.cgi/INSTALL?rev=1.18">INSTALL</A> file that
    comes with the distribution for more information.
    <P>
    Some people have also reported that they had to add '-ldl' immediately
    following 'libphp3.a' when linking with Apache.
  <P>
  </DD>

  <DT><B>
	I can't figure out how to build PHP3 with Apache 1.3.
  </B></DT>
  <DD>
    <P>This is actually quite easy.  Follow these steps carefully:
    <UL>
	<LI>Grab the latest Apache 1.3 distribution from <A href="http://www.apache.org/dist/">www.apache.org</A>.
	<LI>Ungzip and untar it somewhere, for example /usr/local/src/apache-1.3.
	<LI>Compile PHP3 by first running ./configure --with-apache=/<i>&lt;path&gt;</i>/apache-1.3  (substitute <i>&lt;path&gt;</i> for the actual path to your apache-1.3 directory.
	<LI>Type 'make' followed by 'make install' to build PHP3 and copy the
            necessary files to the Apache distribution tree.
	<LI>Change directories into to your /<i>&lt;path&gt;</i>/apache-1.3/src directory and edit the <i>Configuration</i> file.  At the end of the file, add: <tt>AddModule modules/php3/libphp3.a</tt>.
	<LI>Type: './Configure' followed by 'make'.
	<LI>You should now have a PHP3-enabled httpd binary!
    </UL>
    <b>Note:</b> You can also use the new Apache ./configure script.  See the instructions in the README.configure file
    which is part of your Apache distribution.  Also have a look at the INSTALL file in the PHP distribution.
  <P>
  </DD>
</DL>

<HR noshade>

<H2>Using PHP3</H2>

<DL>
  <DT><B>
    I would like to write a generic PHP script that can handle data coming
    from any form.  How do I know which POST method variables are available?
  </B></DT>
  <DD>
    You need to compile PHP with the "--enable-track-vars" configure switch.
    This creates three associative arrays.  $HTTP_GET_VARS, $HTTP_POST_VARS
    and $HTTP_COOKIE_VARS.  So, to write a generic script to handle POST
    method variables you would need something similar to the following:<PRE>
    while (list($var, $value) = each($HTTP_POST_VARS)) {
        echo "$var = $value&lt;br&gt;n";
    }</PRE>
  <P>
  </DD>

  <DT><B>
    I need to convert all single-quotes (') to a backslash followed by
    a single-quote. How can I do this with a regular expression?
  </B></DT>
  <DD>
    First off, take a look at the <A href="manual/function.addslashes.php3">addslashes()</A> function. It will do
    exactly what you want.
  <P>
    The ereg_replace magic you're looking for, however, is simply:<PRE>
    $escaped = ereg_replace("'", "\'", $input);</PRE>
  <P>
  </DD>

  <DT><B>
    When I do the following, the output is printed in the wrong order:<PRE>
      function myfunc($argument) {
        echo $myfunc + 10;
      }
      $variable = 10;
      echo "myfunc($variable) = " . myfunc($variable);
    </PRE>
    <P>What's going on?
  </B></DT>
  <DD>
    To be able to use the results of your function in an expression (such
    as concatenating it with other strings in the example above), you need
    to <B>return</B> the value, not echo it.
  <P>
  </DD>

  <DT><B>
    Hey, what happened to my newlines in:
<PRE>
&lt;PRE&gt;
  1 &lt;?echo $result[1];?&gt;
  2 &lt;?echo $result[2];?&gt;
</PRE>
  </B></DT>
  <DD>
    In PHP, the ending for a block of code is either "?&gt;" <B>or</B>
    "?&gt;n" (where n means a newline). This means that you need to
    insert an extra newline after each block of PHP code in the above
    example.
    <P>
    Why does PHP do this? Because when formatting normal HTML, this
    usually makes your life easier because you don't want that newline,
    but you'd have to create extremely long lines or otherwise make the
    raw page source unreadable to achieve that effect.
  <P>
  </DD>

  <DT><B>
    I need to access information in the request header directly.  How can
    I do this?
  </B></DT>
  <DD>
    The getallheaders() function will do this if you are running PHP as a
    module.  So, the following bit of code will show you all the request
    headers:<PRE>
    $headers = getallheaders();
	for(reset($headers); $key = key($headers); next($headers)) {
        echo "headers[$key] = ".$headers[$key]."&lt;br&gt;n";
    }
</PRE>
  <P>
  </DD>

  <DT><B>
    When I try to use authentication with IIS I get 'No Input file specified'
  </B></DT>
  <DD>
    The security model of IIS is at fault here. This is a problem
    common to all CGI programs running under IIS.  A workaround is
    to create a plain HTML file (not parsed by php) as the entry page
    into an authenticated directory.  Then use a META tag to redirect
    to the PHP page, or have a link to the PHP page.  PHP will
    then recognize the authentication correctly.  When the ISAPI
    module is ready, this will no longer be a problem.  This should
    not effect other NT web servers.  For more information, see: <A
    href="http://support.microsoft.com/support/kb/articles/q160/4/22.asp"
    target="_new">http://support.microsoft.com/support/kb/articles/q160/4/22.asp</A>.
  <P>
  </DD>

  <DT><B>
    I've followed all the instructions, but still can't get PHP and IIS
    to work together!
  </B></DT>
  <DD>
    Make sure any user who needs to run a PHP script has the rights
    to run php.exe!  IIS uses an anonymous user which is added at the
    time IIS is installed.  This user needs rights to php.exe.  Also,
    any authenticated user will also need rights to execute php.exe.
  <P>
  </DD>

</DL>

<H3>New Features</H3>

<DL>
  <DT><B>
    I saw PHP3 offers persistent database connections.   What does that mean?
  </B></DT>
  <DD>
    Persistent connections are SQL links that do not close when the
    execution of your script ends.  When a persistent connection is
    requested, PHP checks if there's already an identical persistent
    connection (that remained open from earlier) - and if it exists, it
    uses it.  If it does not exist, it creates the link.  An 'identical'
    connection is a connection that was opened to the same host, with
    the same username and the same password (where applicable).

    <P>People who aren't thoroughly familiar with the way web servers
    work and distribute the load may mistake persistent connects for what
    they're not.  In particular, they do <B>not</B> give you an ability
    to open 'user sessions' on the same SQL link, they do <B>not</B>
    give you an ability to build up a transaction efficently, and they
    don't do a whole lot of other things.  In fact, to be extremely
    clear about the subject, persistent connections don't give you <B>any</B>
    functionality that wasn't possible with their non-persistent brothers.

    <P>Why?

    <P>This has to do with the way web servers work. There are three ways
    in which your web server can utilize PHP to generate web pages.

    <P>The first method is to use PHP as a CGI "wrapper". When run this
    way, an instance of the PHP interpreter is created and destroyed for
    every page request (for a PHP page) to your web server. Because it
    is destroyed after every request, any resources that it acquires (such
    as a link to an SQL database server) are closed when it is destroyed.
    In this case, you do not gain anything from trying to use persistent
    connections -- they simply don't persist.

    <P>The second, and most popular, method is to run PHP as a module
    in a <I>multiprocess</I> web server, which currently only includes
    Apache. A multiprocess server typically has one process (the parent)
    which coordinates a set of processes (its children) who actually do
    the work of serving up web pages. When each request comes in from a a
    client, it is handed off to one of the children that is not already
    serving another client. This means that when the same client makes
    a second request to the server, it may be serviced by a different
    child process than the first time. What a persistent connection does
    for you in this case it make it so each child process only needs
    to connect to your SQL server the first time that it serves a page
    that makes us of such a connection. When another page then requires
    a connection to the SQL server, it can reuse the connection that
    child established earlier.

    <P>The last method is to use PHP as a plug-in for a <I>multithreaded</I>
    web server. Currently this is only theoretical -- PHP does not
    yet work as a plug-in for any multithreaded web servers. Work is
    progressing on support for ISAPI, WSAPI, and NSAPI (on Windows),
    which will all allow PHP to be used as a plug-in on multithreaded
    servers like Netscape FastTrack, Microsoft's Internet Information
    Server (IIS), and O'Reilly's WebSite Pro. When this happens, the
    behavior will be essentially the same as for the multiprocess model
    described before.

    <P>If persistent connections don't have any added functionality,
    what are they good for?

    <P>The answer here is extremely simple -- efficiency.  Persistent
    connections are good if the overhead to create a link to your SQL
    server is high.  Whether or not this overhead is really high depends
    on many factors.  Like, what kind of database it is, whether or
    not it sits on the same computer on which your web server sits,
    how loaded the machine the SQL server sits on is and so forth.
    The bottom line is that if that connection overhead is high,
    persistent connections help you considerably.  They cause the child
    process to simply connect only once for its entire lifespan, instead
    of every time it processes a page that requires connecting to the
    SQL server.  This means that for every child that opened a persistent
    connection will have its own open persistent connection to the server.
    For example, if you had 20 different child processes that ran a script
    that made a persistent connection to your SQL server, you'd have 20
    different connections to the SQL server, one from each child.

    <P>An important summary.  Persistent connections were designed to
    have one-to-one mapping to regular connections.  That means that you
    should <B>always</B> be able to replace persistent connections with
    non-persistent connections, and it won't change the way your script
    behaves.  It <B>may</B> (and probably will) change the efficiency
    of the script, but not its behavior!
  <P>
  </DD>
</DL>

<H3>Common Problems</H3>

<DL>
  <DT><b>
    I installed PHP3, but every time I load a document, I get the
    message 'Document Contains No Data'! What's going on here?
  </b></DT>
  <DD>
    This probably means that PHP3 is having some sort of problem
    and is core-dumping. Look in your server error log to see if
    this is the case, and then try to reproduce the problem with
    a small test case. If you know how to use 'gdb', it is very
    helpful when you can provide a backtrace with your bug report
    to help the developers pinpoint the problem.
    <P>
    If your script uses the regular expression functions (<CODE>ereg()</CODE>
    and friends), you should make sure that you compiled PHP3 and
    Apache with the same regular expression package. (This should
    happen automatically with PHP3 and Apache 1.3.)
  <P>
  </DD>

  <DT><B>
    I'm trying to access one of the standard CGI variables (such
    as $DOCUMENT_ROOT or $HTTP_REFERER) in a user-defined function,
    and it can't seem to find it. What's wrong?
  </B></DT>
  <DD>
    Environment variables are now normal global variables, so you must
    either declare them as global variables in your function (by using
    "<CODE>global $DOCUMENT_ROOT;</CODE>", for example) or by using
    the global variable array (ie, "<CODE>$GLOBALS["DOCUMENT_ROOT"]</CODE>".
  <P>
  </DD>

  <DT><B>
    I think I found a bug! Who should I tell?
  </B></DT>
  <DD>
    You should go to the PHP Bug Database and make sure the bug
    isn't a known bug.  If you don't see it in the database, use
    the reporting form to report the bug.  It is important to use
    the bug database instead of just sending an email to one of the
    mailing lists because the bug will have a tracking number assigned
    and it will then be possible for you to go back later and check
    on the status of the bug.  The bug database can be found at <A
    href="http://ca.php.net/bugs.php3">http://ca.php.net/bugs.php3</A>.
  <P>
  </DD>
</DL>

<HR noshade>

<H2>Migrating from PHP/FI 2.0</H2>

<H3>Common Problems</H3>

<DL>
  <DT><B>
    When I add two strings together and then echo it, it echoes zero instead
    of the concatenation of the two strings! What's going on? Wouldn't it
    be great if adding two strings just concatenated them together?
  </B></DT>
  <DD>
    PHP3 does not support the overloading of the addition operator for
    strings because values that arrive via the GET and POST methods and
    from databases are always stored as strings. This means that if the
    plus operator were overloaded to concatenate strings, you could add
    what you thought were two numbers and get the wrong result! (For
    example, "4" + "5" would be equal to "45".) One way around this would
    be to explicitly type-cast one or both of the operands, which is what
    PHP/FI 2 did.

   <P>This has been simplified in PHP3 by the addition of a real string
   concatenation operator. If you want to "add" two strings together,
   just write it like: <CODE>"this" . "that"</CODE> which will result in
   the string "thisthat".

   <P>The answer to the final part of the question is an emphatic no.
   Operator overloading can be a source of great confusion, especially
   when variables aren't very strongly typed to begin with, as they are
   in PHP3.
  <P>
  </DD>

  <DT><B>
    When I use the chmod(), umask(), or mkdir() functions, the permissions
    are wrong!
  </B></DT>
  <DD>
    Unlike PHP/FI 2, PHP3 does not interpret the numeric arguments for
    these functions any differently than for any other function, which
    means you need to pass in an octal value if you are specifying an
    octal number, such as:
<PRE>
        chmod($myfile, 0600);
</PRE>
    <B>not</B>
<PRE>
        chmod($myfile, 600);
</PRE>
  <P>
  </DD>

  <DT><B>
    I converted my script from PHP/FI 2.0 to PHP3 syntax, but now it just
    hangs! When I looked at the processes running on my server, there was
    one process that was chewing up all of the CPU cycles!
  </B></DT>
  <DD>
    You probably missed the semi-colon on a <CODE>while
    (condition);</CODE> statement. This will cause PHP3 to spin out of
    control because it is simply executing an empty body for your while
    loop!  Change the semi-colon to a colon and it should work correctly.
  <P>
  </DD>

  <DT><B>
    My user-functions don't work any more! I get a "Parse error (expecting '('"
    on the first line of the function.
  </B></DT>
  <DD>
    PHP3's function declaration now resembles C function declarations, so
    your function should look like:
    <PRE>
        function printsum($a, $b) {
           echo $a + $b;
        }
    </PRE>
    <P>You can also use old-style function declarations by use the 
    'old_function' designation, like so:
    <PRE>
        old_function printsum $a, $b (
           echo $a + $b;
        );
    </PRE>
    <P>
    </DD>
</DL>

<HR noshade>

<H2>Credits</H2>

<P>This FAQ was originally written by Jim Winstead. It is currently
maintained by the PHP Development Team.

<P>
      <!-- end body -->
     </TD>
    </TR>
   </TABLE>
  </TD>
 </TR>
 <TR valign=top BGCOLOR="#5B69A6">
  <TD ALIGN=left width="150">
   <IMG SRC='/gifs/spacer.gif' WIDTH=150 HEIGHT=1 BORDER=0 ALT=' '><BR>
  </TD>
  <TD ALIGN=left width="100%" BGCOLOR="#FFFFFF">
   <IMG SRC="/gifs/corner-bl.gif" WIDTH=12 HEIGHT=12 BORDER=0><BR>
  </TD>
 </TR>
 <TR valign=top>
  <TD ALIGN=left width="150" BGCOLOR="#5B69A6">
   <TABLE BORDER=0 CELLPADDING=0 CELLSPACING=0 WIDTH="150">
    <TR VALIGN=bottom>
     <TD ALIGN=left>
      <IMG SRC='/gifs/spacer.gif' WIDTH=1 HEIGHT=3 BORDER=0 ALT=' '><BR>
<A HREF="/credits.php3" onMouseover="change('cred',1);" 
 onMouseout="hide();"><IMG SRC="/gifs/b-credits-p.gif" 
 ALT="Who's responsible for this?" 
 WIDTH=129 HEIGHT=30 BORDER=0 
 NAME="cred" 
 HSPACE=10 VSPACE=0></A><BR>
<A HREF="#top" onMouseover="change('top',1);" 
 onMouseout="hide();"><IMG SRC="/gifs/b-top-p.gif" 
 ALT="Top of this page" 
 WIDTH=129 HEIGHT=30 BORDER=0 
 NAME="top" 
 HSPACE=10 VSPACE=0></A><BR>
      <IMG SRC="/gifs/cap-bl.gif" WIDTH=9 HEIGHT=9 BORDER=0><BR>
     </TD>
    </TR>
   </TABLE>
  </TD>
  <TD align=left width="100%">
   <TABLE BORDER=0 CELLPADDING=0 CELLSPACING=0 width="100%">
    <TR VALIGN=middle>
     <TD ALIGN=center BGCOLOR="#5B69A6">
      <TABLE BORDER=0 CELLPADDING=0 CELLSPACING=0>
       <TR VALIGN=middle>
        <TD align=right>
         <FONT FACE="tahoma, verdana, arial, helvetica, sans-serif" SIZE=1>
         <I>Site<BR>Hosting:</I><BR>
        </TD>
        <TD>
         <IMG SRC='/gifs/spacer.gif' WIDTH=5 HEIGHT=1 BORDER=0 ALT=' '><BR>
        </TD>
        <TD>
         <A HREF="http://BestHost.net/"><IMG SRC="/gifs/logo-besthost.gif" WIDTH=190 HEIGHT=48 BORDER=0 vspace=12></A><BR>
        </TD>
       </TR>
      </TABLE>
     </TD>
     <TD ALIGN=right BGCOLOR="#5B69A6">
      <TABLE BORDER=0 CELLPADDING=0 CELLSPACING=0>
       <TR VALIGN=middle>
        <TD align=center>
<FONT  FACE="tahoma, verdana, arial, helvetica, sans-serif" SIZE=2>
<FONT SIZE=1><I>Located in</I></FONT><BR>United States	  </TD>
        <TD><IMG SRC='/gifs/spacer.gif' WIDTH=5 HEIGHT=1 BORDER=0 ALT=' '></TD>
        <TD>
         <IMG SRC="/gifs/flag-us.gif" BORDER=0></TD>
        <TD>
         <IMG SRC="/gifs/cap-right2.gif" WIDTH=24 HEIGHT=72 BORDER=0></TD>
       </TR>
      </TABLE>
     </TD>
    </TR>
   </TABLE>
  </TD>
 </TR>
</TABLE>

</BODY>
</HTML>
