Summary:	HLP - Interactive help system
Summary(pl.UTF-8):	HLP - interaktywny system pomocy
Name:		starlink-hlp
Version:	3.3_6.218
Release:	1
License:	GPL
Group:		Applications/Text
Source0:	ftp://ftp.starlink.rl.ac.uk/pub/ussc/store/hlp/hlp.tar.Z
# Source0-md5:	ce5d0d3859e31f37429b60f10e8200be
URL:		http://www.starlink.rl.ac.uk/static_www/soft_further_HLP.html
BuildRequires:	gcc-g77
BuildRequires:	sed >= 4.0
BuildRequires:	starlink-htx
Requires:	starlink-htx
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		stardir		/usr/lib/star

%description
The Starlink HLP system is a set of subprograms and utilities which
allows an application program to retrieve named items from a
hierarchically-arranged library of text.

The facility is functionally very similar to the VAX/VMS Help system.
The major differences are that the Starlink HLP system:
- is implemented in a portable way and is not tied to the VAX, and
- allows independent creation of multiple libraries which are bound
  together at run-time and appear to the user as a single ``tree''. The
  system is written in a free-standing manner and does not call any
  other Starlink packages.

%description -l pl.UTF-8
System Starlink HLP to zbiór podprogramów i narzędzi pozwalających
aplikacjom uzyskiwać nazwy elementów z hierarchicznie zorganizowanej
biblioteki tekstu.

Ułatwieniem jest funkcjonalność bardzo podobna do tej z systemu pomocy
systemów VAX/VMS. Główne różnice polegają na tym, że system Starlink
HLP:
- jest zaimplementowany w sposób przenośny, nie przywiązany do VAX-a
- pozwala na niezależne tworzenie wielu bibliotek wiązanych razem w
  czasie działania, pokazujących się użytkownikowi jako pojedyncze
  "drzewo". System jest napisany jako samodzielny i nie wywołuje innych
  pakietów Starlinka.

%package devel
Summary:	Development files for HLP library
Summary(pl.UTF-8):	Pliki programistyczne biblioteki HLP
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Development files for HLP library.

%description devel -l pl.UTF-8
Pliki programistyczne biblioteki HLP.

%package static
Summary:	Static Starlink HLP library
Summary(pl.UTF-8):	Statyczna biblioteka Starlink HLP
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static Starlink HLP library.

%description static -l pl.UTF-8
Statyczna biblioteka Starlink HLP.

%prep
%setup -q -c

sed -i -e 's/ -O / %{rpmcflags} /;s/ ld -shared -soname / g77 -shared -Wl,-soname=/' mk
sed -i -e 's/-L\. \$(OBJECT_LIBRARIES)/-L. -l\$(PKG_NAME)/' makefile

%build
LD_LIBRARY_PATH=. \
SYSTEM=ix86_Linux \
./mk build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{stardir}/help

SYSTEM=ix86_Linux \
./mk install \
	STARLINK=%{stardir} \
	INSTALL=$RPM_BUILD_ROOT%{stardir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc hlp.news
%attr(755,root,root) %{stardir}/bin/hlib
%attr(755,root,root) %{stardir}/bin/???hlp
%{stardir}/dates/*
%docdir %{stardir}/docs
%{stardir}/docs/sun*
%attr(755,root,root) %{stardir}/share/*.so

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{stardir}/bin/hlp_link*

%files static
%defattr(644,root,root,755)
%{stardir}/lib/*.a
