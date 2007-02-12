Summary:	Library of extensions to the Linux framebuffer subsystem
Summary(pl.UTF-8):   Biblioteka rozszerzeń linuksowego framebuffera
Name:		libfbx
Version:	0.2.0
Release:	1
License:	LGPL v2.1+
Group:		Libraries
# ftp.u4x.org doesn't exist now
Source0:	http://dl.sourceforge.net/u4x/%{name}-%{version}.tar.gz
# Source0-md5:	ed280a7f4f0675450dedb7d9cb0238aa
URL:		http://developer.u4x.org/libfbx/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libfbx is a library of extensions to the Linux framebuffer subsystem.
It provides a number of drawing primitives, and very basic text
drawing. It has no input routines (as those don't belong in a drawing
library). It's purpose is to provide a low-level access layer for the
creation of higher-level libraries and applications, such as a
windowing system, embedded graphics software, or other graphical
applications that need or want to be independant of X11.

libfbx-gui is a library of graphical extensions to libfbx. It will
offer such things as a complete widget set, mouse support, a message
handler, and so forth, upon completion.

%description -l pl.UTF-8
libfbx to biblioteka rozszerzeń linuksowego framebuffera. Udostępnia
funkcje rysujące wiele prymitywów i podstawowe wyświetlanie tekstu.
Nie ma funkcji wejścia (jako że nie należą do biblioteki rysującej).
Celem biblioteki jest udostępnienie warstwy niskopoziomowego dostępu
dla bibliotek i aplikacji wyższego poziomu, takich jak system
okienkowy, wbudowane oprogramowanie graficzne czy inne aplikacje
graficzne, które nie potrzebują lub nie chcą zależności od X11.

%package devel
Summary:	libfbx header files
Summary(pl.UTF-8):   Pliki nagłówkowe libfbx
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
libfbx header files.

%description devel -l pl.UTF-8
Pliki nagłówkowe libfbx.

%package static
Summary:	libfbx static libraries
Summary(pl.UTF-8):   Statyczne biblioteki libfbx
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
libfbx static libraries.

%description static -l pl.UTF-8
Statyczne biblioteki libfbx.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS BUGS CREDITS ChangeLog NEWS README TODO
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%dir %{_libdir}/libfbx
%dir %{_libdir}/libfbx/modules
%attr(755,root,root) %{_libdir}/libfbx/modules/lib*.??*

%files devel
%defattr(644,root,root,755)
%doc docs/libfbx-api.sgml
%attr(755,root,root) %{_bindir}/libfbx-config
%{_includedir}/libfbx
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_aclocaldir}/*.m4

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
%{_libdir}/libfbx/modules/lib*.a
