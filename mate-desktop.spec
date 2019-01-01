%define url_ver %(echo %{version}|cut -d. -f1,2)

%define	api_version	2
%define api		2.0
%define major		17
%define libname	%mklibname %{name} %{api_version} %{major}
%define devname	%mklibname -d %{name} %{api_version}
%define girname %mklibname %{name}-gir %{api}

Summary:	Package containing code shared among mate-panel, mate-session-manager etc
Name:		mate-desktop
Version:	1.20.4
Release:	1
License:	GPLv2+ and LGPLv2+
Group:		Graphical desktop/Other
Url:		http://mate-desktop.org
Source0:	http://pub.mate-desktop.org/releases/%{url_ver}/%{name}-%{version}.tar.xz

BuildRequires:	desktop-file-utils
BuildRequires:	gtk-doc
BuildRequires:	intltool
BuildRequires:	ldetect-lst
BuildRequires:	mate-common
BuildRequires:	pkgconfig(dconf)
BuildRequires:	pkgconfig(gdk-pixbuf-2.0)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(gtk-doc)
BuildRequires:	pkgconfig(libstartup-notification-1.0)
BuildRequires:	pkgconfig(unique-1.0)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xext)
BuildRequires:	pkgconfig(xrandr)
BuildRequires:	yelp-tools

Requires:	ldetect-lst
Requires:	mate-control-center
Requires:	mate-notification-daemon
Requires:	mate-panel
Requires:	xdg-user-dirs-gtk
Requires:       %{name}-schemas = %{version}-%{release}

Suggests:	mate-user-guide
Suggests:	yelp

%description
The MATE Desktop Environment is the continuation of GNOME 2. It provides an
intuitive and attractive desktop environment using traditional metaphors for
Linux and other Unix-like operating systems.

MATE is under active development to add support for new technologies while
preserving a traditional desktop experience.

This package contains some data files and other shared components of the
MATE user environment.

%files -f %{name}.lang
%doc AUTHORS COPYING ChangeLog NEWS README
%{_bindir}/mate-about
%{_bindir}/mate-color-select
%{_datadir}/applications/mate-about.desktop
%{_datadir}/applications/mate-color-select.desktop
%dir %{_datadir}/mate-about
%{_datadir}/mate-about/mate-version.xml
%{_iconsdir}/*/*/*/mate*
%{_mandir}/man1/*.1*

#---------------------------------------------------------------------------

%package -n %{libname}
Summary:	%{summary}
Group:		System/Libraries

%description -n %{libname}
This package contains libraries used by %{name}.

%files -n %{libname}
%{_libdir}/libmate-desktop-%{api_version}.so.%{major}*

#---------------------------------------------------------------------------

%package -n %{girname}
Summary: GObject introspection interface library for %{name}
Group: System/Libraries
Requires: %{libname} = %{EVRD}

%description -n %{girname}
This package contains GObject Introspection interface library for %{name}.

%files -n %{girname}
%{_libdir}/girepository-1.0/MateDesktop-%{api}.typelib

#---------------------------------------------------------------------------

%package -n %{devname}
Summary:	Development libraries, include files for %{name}
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{EVRD}

%description -n %{devname}
This package contains libraries and includes files for developing programs
based on %{name}.

%files -n %{devname}
%doc COPYING COPYING-DOCS
%doc %{_datadir}/gtk-doc/html/*
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_datadir}/gir-1.0/MateDesktop-%{api}.gir

#---------------------------------------------------------------------------

%package schemas
Summary:	Gsettings schema files for %{name}
Group:		Graphical desktop/Other
BuildArch:	noarch

%description schemas
This package provides the gsettings schemas for %{name}.

%files schemas
%{_datadir}/glib-2.0/schemas/org.mate.*.gschema.xml

#---------------------------------------------------------------------------

%prep
%setup -q

%build
#NOCONFIGURE=yes ./autogen.sh
%configure \
	--disable-schemas-compile \
	--enable-gtk-doc \
	--with-pnp-ids-path=%{_datadir}/misc/pnp.ids \
	%{nil}
%make 

%install
%makeinstall_std 

# locales
%find_lang %{name} --with-gnome --all-name

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/mate-about.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/mate-color-select.desktop

