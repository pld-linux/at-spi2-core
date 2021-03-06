#
# Conditional build:
%bcond_without	apidocs		# API documentation
%bcond_with	static_libs	# static library

Summary:	Protocol definitions and daemon for D-Bus at-spi
Summary(pl-UTF-8):	Definicje protokołu oraz demon at-spi dla usługi D-Bus
Name:		at-spi2-core
Version:	2.38.0
Release:	1
License:	LGPL v2.1+
Group:		Daemons
Source0:	http://ftp.gnome.org/pub/GNOME/sources/at-spi2-core/2.38/%{name}-%{version}.tar.xz
# Source0-md5:	ae060dc0a042822b3f07c786c5d5aab7
URL:		https://wiki.linuxfoundation.org/accessibility/d-bus
BuildRequires:	dbus-devel >= 1.5
BuildRequires:	gettext-tools >= 0.19.8
BuildRequires:	glib2-devel >= 1:2.36.0
BuildRequires:	gobject-introspection-devel >= 1.32.0
%{?with_apidocs:BuildRequires:	gtk-doc >= 1.25}
BuildRequires:	meson >= 0.50.0
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXi-devel
BuildRequires:	xorg-lib-libXtst-devel
BuildRequires:	xz
Requires:	%{name}-libs = %{version}-%{release}
Requires:	dbus >= 1.5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
at-spi allows assistive technologies to access GTK-based applications.
Essentially it exposes the internals of applications for automation,
so tools such as screen readers, magnifiers, or even scripting
interfaces can query and interact with GUI controls.

This version of at-spi is a major break from previous versions. It has
been completely rewritten to use D-Bus rather than ORBIT / CORBA for
its transport protocol.

%description -l pl.UTF-8
at-spi pozwala na dostęp technik wspomagających do aplikacji partych
na bibliotece GTK+. W szczególności udostępnia wnętrzności aplikacji
na potrzeby automatyzacji, dzięki czemu narzędzia takie jak czytniki
ekranowe, lupy czy nawet interfejsy skryptowe mogą odpytywać i
współpracować interaktywnie z kontrolkami GUI.

Ta wersja at-spi to duża zmiana w stosunku do poprzednich wersji.
Została całkowicie przepisana z użyciem protokołu transportowego D-Bus
zamiast wcześniejszego ORBIT/CORBA.

%package libs
Summary:	at-spi2 core library
Summary(pl.UTF-8):	Główna biblioteka at-spi2
Group:		Libraries
Requires:	dbus-libs >= 1.5
Requires:	glib2 >= 1:2.36.0
Conflicts:	at-spi2-core < 2.2.1-2

%description libs
at-spi2 core library.

%description libs -l pl.UTF-8
Główna biblioteka at-spi2.

%package devel
Summary:	Header files for at-spi2 library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki at-spi2
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	dbus-devel >= 1.5
Requires:	glib2-devel >= 1:2.36.0
Requires:	xorg-lib-libX11-devel

%description devel
Header files for at-spi2 library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki at-spi2.

%package static
Summary:	Static at-spi2 library
Summary(pl.UTF-8):	Statyczna biblioteka at-spi2
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static at-spi2 library.

%description static -l pl.UTF-8
Statyczna biblioteka at-spi2.

%package apidocs
Summary:	at-spi2 library API documentation
Summary(pl.UTF-8):	Dokumentacja API biblioteki at-spi2
Group:		Documentation
Requires:	gtk-doc-common
BuildArch:	noarch

%description apidocs
at-spi2 library API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki at-spi2.

%prep
%setup -q

%build
%meson build \
	%{!?with_static_libs:--default-library='shared'} \
	%{?with_apidocs:-Ddocs=true} \
	-Dx11=yes

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%attr(755,root,root) %{_libexecdir}/at-spi-bus-launcher
%attr(755,root,root) %{_libexecdir}/at-spi2-registryd
%dir %{_datadir}/dbus-1/accessibility-services
%{_datadir}/dbus-1/accessibility-services/org.a11y.atspi.Registry.service
%{_datadir}/dbus-1/services/org.a11y.Bus.service
%dir %{_datadir}/defaults/at-spi2
%{_datadir}/defaults/at-spi2/accessibility.conf
%{_sysconfdir}/xdg/autostart/at-spi-dbus-bus.desktop
%{systemduserunitdir}/at-spi-dbus-bus.service

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libatspi.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libatspi.so.0
%{_libdir}/girepository-1.0/Atspi-2.0.typelib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libatspi.so
%{_includedir}/at-spi-2.0
%{_datadir}/gir-1.0/Atspi-2.0.gir
%{_pkgconfigdir}/atspi-2.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libatspi.a
%endif

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/libatspi
%endif
