Summary:	Simple webmail using POP3 or IMAP
Summary(pl):	Prosty webmail u¿ywaj±cy POP3 lub IMAP
Name:		nullwebmail
Version:	0.7.1
Release:	1
License:	GPL v2+
Group:		Applications/Mail
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Patch0:		%{name}-pl.patch
URL:		http://www.nulllogic.com/webmail/
Requires:	webserver
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Null Webmail is a simple yet powerful POP3/IMAP/SMTP Webmail CGI
written in C. It's small, fast, complete, and a breeze to install and
use.

%description -l pl
Null Webmail jest prostym interfejsem webmail dla serwerów
POP3/IMAP/SMTP napisanym w C. Jest ma³y, szybki i banalny w instalacji
i u¿ytkowaniu.

%prep
%setup -q
%patch0 -p1

%build
%{__make} CFLAGS="-Wall -I./include %{rpmcflags}"
mv webmail.cgi webmail-en.cgi

perl -pi -e 's#strings-en#strings-pl#' include/config.h
%{__make} clean all CFLAGS="-Wall -I./include %{rpmcflags}"
mv webmail.cgi webmail-pl.cgi

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/home/services/httpd/{cgi-bin,html}

install webmail*.c* $RPM_BUILD_ROOT/home/services/httpd/cgi-bin
cp -a webmail $RPM_BUILD_ROOT/home/services/httpd/html

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%config %verify(not md5 size mtime) /home/services/httpd/cgi-bin/webmail.cfg
%attr(755,root,root) /home/services/httpd/cgi-bin/*.cgi
/home/services/httpd/html/webmail
