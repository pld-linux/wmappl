Summary:	Application launcher for the WindowMaker Dock
Summary(pl):	Program do uruchamiania aplikacji dla Doku WindowMakera
Name:		wmappl
Version:	0.70
Release:	2
License:	GPL
Group:		X11/Window Managers/Tools
Source0:	http://dl.sourceforge.net/wmappl/%{name}-%{version}.tar.gz
# Source0-md5:	af48340de0dae4999ebe5fa0e8f424f3
Source1:	%{name}.desktop
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

%build
%configure 
%{__make} 

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_applnkdir}/DockApplets

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/DockApplets

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README 
%attr(755,root,root) %{_bindir}/wmappl
%{_applnkdir}/DockApplets/*
%{_datadir}/%{name}
%{_mandir}/*
