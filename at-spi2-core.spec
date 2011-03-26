Summary:	Protocol definitions and daemon for D-Bus at-spi
Name:		at-spi2-core
Version:	1.91.93
Release:	1
License:	LGPL v2
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/at-spi2-core/1.91/%{name}-%{version}.tar.bz2
# Source0-md5:	efadee156a68ec269779321aceb100a3
URL:		http://www.linuxfoundation.org/en/AT-SPI_on_D-Bus
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.9
BuildRequires:	dbus-devel >= 1.0
BuildRequires:	dbus-glib-devel
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.26.0
BuildRequires:	gobject-introspection-devel >= 0.10.0
BuildRequires:	gtk-doc >= 1.2
BuildRequires:	intltool >= 0.40.0
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXevie-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXi-devel
BuildRequires:	xorg-lib-libXtst-devel
Requires:	dbus
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
at-spi allows assistive technologies to access GTK-based applications.
Essentially it exposes the internals of applications for automation,
so tools such as screen readers, magnifiers, or even scripting
interfaces can query and interact with GUI controls.

This version of at-spi is a major break from previous versions. It has
been completely rewritten to use D-Bus rather than ORBIT / CORBA for
its transport protocol.

%package devel
Summary:	Header files for at-spi2 library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki at-spi2
Group:		Development/Libraries
Requires:	glib2-devel >= 1:2.26.0

%description devel
Header files for at-spi2 library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki at-spi2.

%package apidocs
Summary:	at-spi2 library API documentation
Summary(pl.UTF-8):	Dokumentacja API biblioteki at-spi2
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
at-spi2 library API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki at-spi2.

%prep
%setup -q

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-gtk-doc \
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libexecdir}/at-spi-bus-launcher
%attr(755,root,root) %{_libexecdir}/at-spi2-registryd
%attr(755,root,root) %{_libdir}/libatspi.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libatspi.so.0
%{_libdir}/girepository-1.0/Atspi-2.0.typelib
%{_datadir}/dbus-1/services/org.a11y.atspi.Registry.service
%{_datadir}/dbus-1/services/org.a11y.Bus.service
%dir %{_sysconfdir}/at-spi2
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/at-spi2/accessibility.conf
%{_sysconfdir}/xdg/autostart/at-spi-dbus-bus.desktop

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libatspi.so
%{_includedir}/at-spi-2.0
%{_datadir}/gir-1.0/Atspi-2.0.gir
%{_pkgconfigdir}/atspi-2.pc

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/libatspi
