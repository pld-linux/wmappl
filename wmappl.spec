Summary:	Application launcher for the WindowMaker Dock
Summary(pl):	Program do uruchamiania aplikacji dla Doku WindowMakera
Name: 		wmappl
Version: 	0.2
Release: 	1
Copyright: 	GPL
Group:          X11/Window Managers/Tools
Group(pl):	X11/Zarz±dcy Okien/Narzêdzia
Source: 	http://www.upl.cs.wisc.edu:80/%7Echarkins/wmappl/%{name}-%{version}.tar.gz
Patch:		wmappl-misc.patch
BuildRequires:	XFree86-devel
BuildRequires:	xpm-devel
BuildRoot:	/tmp/%{name}-%{version}-root

%define 	_prefix 	/usr/X11R6

%description
WMAppl is a simple application launcher for the WindowMaker Dock.

%description -l pl
WMAppl jest prostym programem do uruchamiania aplikacji, przeznaczonym
dla Doku WindowMakera.

%prep
%setup -q
%patch -p1

%build
make OPTFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README CHANGELOG

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {README,CHANGELOG}.gz
%attr(755,root,root) %{_bindir}/wmappl

%{_datadir}/wmappl
