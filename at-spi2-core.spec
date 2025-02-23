#
# Conditional build:
%bcond_without	apidocs		# API documentation
%bcond_without	static_libs	# static library
%bcond_without	systemd		# systemd

Summary:	Protocol definitions and daemon for D-Bus at-spi
Summary(pl-UTF-8):	Definicje protokołu oraz demon at-spi dla usługi D-Bus
Name:		at-spi2-core
Version:	2.54.1
Release:	1
License:	LGPL v2.1+
Group:		Daemons
Source0:	https://download.gnome.org/sources/at-spi2-core/2.54/%{name}-%{version}.tar.xz
# Source0-md5:	a05ad6cf4a49b19964cc5eec363d2310
URL:		https://wiki.linuxfoundation.org/accessibility/d-bus
BuildRequires:	dbus-devel >= 1.5
BuildRequires:	gettext-tools >= 0.19.8
BuildRequires:	glib2-devel >= 1:2.67.4
BuildRequires:	gobject-introspection-devel >= 1.32.0
%{?with_apidocs:BuildRequires:	gi-docgen >= 2021.1}
BuildRequires:	libxml2-devel >= 1:2.9.1
BuildRequires:	meson >= 0.63.0
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 2.042
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXi-devel
BuildRequires:	xorg-lib-libXtst-devel
BuildRequires:	xz
Requires(post,preun):	systemd-units >= 1:250.1
Requires:	%{name}-libs = %{version}-%{release}
Requires:	dbus >= 1.5
Requires:	systemd-units >= 1:250.1
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
Requires:	glib2 >= 1:2.67.4
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
Requires:	glib2-devel >= 1:2.67.4
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
BuildArch:	noarch

%description apidocs
at-spi2 library API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki at-spi2.

%package -n at-spi2-atk
Summary:	A GTK+ module that bridges ATK to D-Bus at-spi
Summary(pl.UTF-8):	Moduł GTK+ łączący ATK z at-spi jako usługą D-Bus
Group:		Libraries
Requires:	at-spi2-atk-libs = %{version}-%{release}
Requires:	atk = 1:%{version}-%{release}
Requires:	%{name} = %{version}-%{release}
Requires:	dbus >= 1.5

%description -n at-spi2-atk
This package provides a GTK+ module that bridges ATK to the new D-Bus
based at-spi.

%description -n at-spi2-atk -l pl.UTF-8
Ten pakiet dostarcza moduł GTK+ łączący ATK z nowym at-spi, opartym o
usługę D-Bus.

%package -n at-spi2-atk-libs
Summary:	Shared atk-bridge library
Summary(pl.UTF-8):	Biblioteka współdzielona atk-bridge
Group:		Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	atk = 1:%{version}-%{release}
Requires:	dbus-libs >= 1.5
Requires:	glib2 >= 1:2.32.0
Conflicts:	at-spi2-atk < 2.6.0-2

%description -n at-spi2-atk-libs
Shared atk-bridge library, providing ATK/D-Bus bridge.

%description -n at-spi2-atk-libs -l pl.UTF-8
Biblioteka współdzielona atk-bridge, zapewniająca pomost między ATK a
D-Bus.

%package -n at-spi2-atk-devel
Summary:	Header files for atk-bridge library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki atk-bridge
Group:		Development/Libraries
Requires:	at-spi2-atk-libs = %{version}-%{release}
Requires:	%{name}-devel = %{version}-%{release}
Requires:	glib2-devel >= 1:2.32.0

%description -n at-spi2-atk-devel
Header files for atk-bridge library.

%description -n at-spi2-atk-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki atk-bridge.

%package -n at-spi2-atk-static
Summary:	Static atk-bridge library
Summary(pl.UTF-8):	Biblioteka statyczna atk-bridge
Group:		Development/Libraries
Requires:	at-spi2-atk-devel = %{version}-%{release}

%description -n at-spi2-atk-static
Static atk-bridge library.

%description -n at-spi2-atk-static -l pl.UTF-8
Biblioteka statyczna atk-bridge.

%package -n atk
Summary:	ATK - Accessibility Toolkit
Summary(pl.UTF-8):	ATK - biblioteka ułatwiająca niepełnosprawnym korzystanie z komputerów
Summary(pt_BR.UTF-8):	Interfaces para suporte a acessibilidade
Epoch:		1
Group:		Libraries
Requires:	glib2 >= 1:2.38.0
Obsoletes:	libatk1.0_0 < 1:2

%description -n atk
The ATK library provides a set of interfaces for adding accessibility
support to applications and graphical user interface toolkits. By
supporting the ATK interfaces, an application or toolkit can be used
as tools such as screen readers and magnifiers, and alternative input
devices.

%description -n atk -l pl.UTF-8
Biblioteka ATK udostępnia zestaw interfejsów ułatwiających
niepełnosprawnym korzystanie z aplikacji i poszczególnych elementów
graficznego interfejsu użytkownika. Poprzez wykorzystanie interfejsów
ATK, aplikacja lub element interfejsu może być używany z takimi
narzędziami jak czytniki ekranu i narzędzia powiększające oraz
alternatywnymi urządzeniami wejściowymi.

%description -n atk -l pt_BR.UTF-8
A biblioteca ATK provê um conjunto de interfaces para adicionar
suporte a acessibilidade para aplicações e interfaces gráficas.
Suportando a interface ATK, uma aplicação ou interface gráfica pode
ser utilizada como ferramentas de leitura e aumento de tela,
dispositivos de entrada alternativos, etc.

%package -n atk-devel
Summary:	ATK - header files
Summary(pl.UTF-8):	ATK - pliki nagłówkowe
Summary(pt_BR.UTF-8):	Interfaces para suporte a acessibilidade
Epoch:		1
Group:		X11/Development/Libraries
Requires:	atk = 1:%{version}-%{release}
Requires:	glib2-devel >= 1:2.38.0
Obsoletes:	libatk1.0_0-devel < 1:2

%description -n atk-devel
ATK - header files.

%description -n atk-devel -l pl.UTF-8
ATK - pliki nagłówkowe.

%description -n atk-devel -l pt_BR.UTF-8
Interfaces para suporte a acessibilidade.

%package -n atk-static
Summary:	ATK static library
Summary(pl.UTF-8):	Biblioteka statyczna ATK
Summary(pt_BR.UTF-8):	Interfaces para suporte a acessibilidade
Epoch:		1
Group:		X11/Development/Libraries
Requires:	atk-devel = 1:%{version}-%{release}

%description -n atk-static
ATK static library.

%description -n atk-static -l pl.UTF-8
Biblioteka statyczna ATK.

%description -n atk-static -l pt_BR.UTF-8
Interfaces para suporte a acessibilidade.

%package -n atk-apidocs
Summary:	ATK API documentation
Summary(pl.UTF-8):	Dokumentacja API ATK
Epoch:		1
Group:		Documentation
BuildArch:	noarch

%description -n atk-apidocs
ATK API documentation.

%description -n atk-apidocs -l pl.UTF-8
Dokumentacja API ATK.

%prep
%setup -q

%build
%meson \
	%{!?with_static_libs:--default-library='shared'} \
	-Ddbus_daemon=/usr/bin/dbus-daemon \
%if %{with systemd}
	-Ddbus_broker=/usr/bin/dbus-broker-launch \
	-Ddefault_bus=dbus-broker \
%else
	-Ddefault_bus=dbus-daemon \
	-Duse_systemd=false \
%endif
	%{?with_apidocs:-Ddocs=true} \
	-Dx11=enabled

%meson_build

%install
rm -rf $RPM_BUILD_ROOT

%meson_install

%if %{with apidocs}
install -d $RPM_BUILD_ROOT%{_gidocdir}
%{__mv} $RPM_BUILD_ROOT%{_docdir}/{atk,libatspi} $RPM_BUILD_ROOT%{_gidocdir}
%endif

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%systemd_user_post at-spi-dbus-bus.service

%preun
%systemd_user_preun at-spi-dbus-bus.service

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%post	-n at-spi2-atk-libs -p /sbin/ldconfig
%postun	-n at-spi2-atk-libs -p /sbin/ldconfig

%post	-n atk -p /sbin/ldconfig
%postun	-n atk -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc MAINTAINERS NEWS README.md
%attr(755,root,root) %{_libexecdir}/at-spi-bus-launcher
%attr(755,root,root) %{_libexecdir}/at-spi2-registryd
%dir %{_datadir}/dbus-1/accessibility-services
%{_datadir}/dbus-1/accessibility-services/org.a11y.atspi.Registry.service
%{_datadir}/dbus-1/services/org.a11y.Bus.service
%dir %{_datadir}/defaults/at-spi2
%{_datadir}/defaults/at-spi2/accessibility.conf
%{_sysconfdir}/xdg/Xwayland-session.d/00-at-spi
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
%{_gidocdir}/libatspi
%endif

%files -n at-spi2-atk
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gtk-2.0/modules/libatk-bridge.so
%{_libdir}/gnome-settings-daemon-3.0/gtk-modules/at-spi2-atk.desktop

%files -n at-spi2-atk-libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libatk-bridge-2.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libatk-bridge-2.0.so.0

%files -n at-spi2-atk-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libatk-bridge-2.0.so
%{_includedir}/at-spi2-atk
%{_pkgconfigdir}/atk-bridge-2.0.pc

%if %{with static_libs}
%files -n at-spi2-atk-static
%defattr(644,root,root,755)
%{_libdir}/libatk-bridge-2.0.a
%endif

%files -n atk
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libatk-1.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libatk-1.0.so.0
%{_libdir}/girepository-1.0/Atk-1.0.typelib

%files -n atk-devel
%attr(755,root,root) %{_libdir}/libatk-1.0.so
%{_includedir}/atk-1.0
%{_pkgconfigdir}/atk.pc
%{_datadir}/gir-1.0/Atk-1.0.gir

%if %{with static_libs}
%files -n atk-static
%defattr(644,root,root,755)
%{_libdir}/libatk-1.0.a
%endif

%if %{with apidocs}
%files -n atk-apidocs
%defattr(644,root,root,755)
%{_gidocdir}/atk
%endif
