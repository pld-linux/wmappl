Summary:	Application launcher for the WindowMaker Dock
Summary(pl):	Program do uruchamiania aplikacji dla Doku WindowMakera
Name:		wmappl
Version:	0.61
Release:	1
License:	GPL
Group:		X11/Window Managers/Tools
Source0:	http://dl.sourceforge.net/wmappl/%{name}-%{version}.tar.gz
# Source0-md5:	d9c5edcf858826e51a10bbc2a231618c
Patch0:		%{name}-misc.patch
URL:		http://wmappl.sourceforge.net/
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
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name}/icons}

install wmappl $RPM_BUILD_ROOT%{_bindir}
install icons/*.xpm $RPM_BUILD_ROOT%{_datadir}/%{name}/icons

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG README TODO sample.wmapplrc
%attr(755,root,root) %{_bindir}/wmappl
%{_datadir}/%{name}
