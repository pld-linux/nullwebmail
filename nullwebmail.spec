Summary:	Simple webmail using POP3 or IMAP
Summary(pl):	Prosty webmail u¿ywaj±cy POP3 lub IMAP
Name:		nullwebmail
Version:	0.8.4
Release:	1
License:	GPL v2+
Group:		Applications/Mail
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	718fbbb7b445e033c42ddad61908e326
Patch0:		%{name}-config.patch
URL:		http://nullwebmail.sourceforge.net/
BuildRequires:	autoconf
Requires:	webserver
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_httpdir	/home/services/httpd

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
%{__aclocal}
%{__autoconf}

%configure

%{__make} CFLAGS="-Wall -I../include %{rpmcflags}"
mv webmail.cgi webmail-en.cgi

perl -pi -e 's#strings-en#strings-pl#' include/config.h
%{__make} clean all CFLAGS="-Wall -I../include %{rpmcflags}"
mv webmail.cgi webmail-pl.cgi

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_httpdir}/{cgi-bin,html},%{_sysconfdir}/nullwebmail}

install webmail*.cgi $RPM_BUILD_ROOT%{_httpdir}/cgi-bin
install webmail.cfg $RPM_BUILD_ROOT%{_sysconfdir}/nullwebmail
cp -a webmail $RPM_BUILD_ROOT%{_httpdir}/html

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%dir %{_sysconfdir}/nullwebmail
%config %verify(not md5 size mtime) %{_sysconfdir}/nullwebmail/webmail.cfg
%attr(755,root,root) %{_httpdir}/cgi-bin/*.cgi
%{_httpdir}/html/webmail
