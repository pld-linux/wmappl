Summary:	Application launcher for the WindowMaker Dock
Summary(pl):	Program do uruchamiania aplikacji dla Doku WindowMakera
Name:		wmappl
Version:	0.2
Release:	2
License:	GPL
Group:		X11/Window Managers/Tools
Source0:	http://www.pobox.com/~charkins/wmappl/%{name}-%{version}.tar.gz
Patch0:		%{name}-misc.patch
URL:		http://www.pobox.com/~charkins/wmappl.html
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
WMAppl is a simple application launcher for the WindowMaker Dock.

%description -l pl
WMAppl jest prostym programem do uruchamiania aplikacji, przeznaczonym
dla Doku WindowMakera.

%prep
%setup -q
%patch -p1

%build
%{__make} \
	OPTFLAGS="%{rpmcflags}" \
	CC=%{__cc}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README CHANGELOG
%attr(755,root,root) %{_bindir}/wmappl

%{_datadir}/wmappl
