%define	api_version	2
%define api		2.0
%define major		17

%define libname		%mklibname %{name} %{api_version} %{major}
%define develname	%mklibname -d %{name} %{api_version}

Summary:	Package containing code shared among mate-panel, mate-session-manager etc
Name:		mate-desktop
Version:	1.2.0
Release:	1
License:	GPLv2+ and LGPLv2+
Group:		Graphical desktop/GNOME
URL:		http://mate-desktop.org
Source0:	http://pub.mate-desktop.org/releases/1.2/%{name}-%{version}.tar.xz

BuildRequires:	docbook-dtd412-xml
BuildRequires:	gtk-doc
BuildRequires:	intltool
BuildRequires:	ldetect-lst
BuildRequires:	mate-common
BuildRequires:	mate-conf
BuildRequires:	pkgconfig(gdk-pixbuf-2.0)
BuildRequires:	pkgconfig(glib-2.0)
#BuildRequires:	pkgconfig(gsettings-desktop-schemas)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(libstartup-notification-1.0)
BuildRequires:	pkgconfig(mateconf-2.0)
BuildRequires:	pkgconfig(mate-doc-utils)
BuildRequires:	pkgconfig(unique-1.0)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xext)
BuildRequires:	pkgconfig(xrandr)

Requires:	ldetect-lst

%description
This package contains some data files and other shared components of the
GNOME user environment.

%package -n %{libname}
Summary:	%{summary}
Group:		System/Libraries

%description -n %{libname}
This package contains an internal library
(libgnomedesktop) used to implement some portions of the GNOME
desktop.

%package -n %{develname}
Summary:	Development libraries, include files for %{name}
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{develname}
Development libraries, include files for internal library %{name}.

%prep
%setup -q

%build
NOCONFIGURE=yes ./autogen.sh
%configure2_5x \
	--disable-static \
	--disable-scrollkeeper \
	--with-pnp-ids-path=%{_datadir}/misc/pnp.ids

%make LIBS='-lm'

%install
%makeinstall_std 

%find_lang %{name}-%{api} --with-gnome --all-name
#for d in `ls -1 %{buildroot}%{_datadir}/gnome/help/`; do
#  %find_lang $d --with-gnome
#  cat $d.lang >> %{name}-%{api}.lang
#done

%files -f %{name}-%{api}.lang
%doc AUTHORS COPYING ChangeLog NEWS README
%{_bindir}/mate-about
%{_datadir}/pixmaps/*
%{_datadir}/applications/mate-about.desktop
# this is a new help dir for mate and should be removed once
# properly found with find-lang.sh
%{_datadir}/mate/help/*
%{_mandir}/man1/mate-about.1*

%files -n %{libname}
%{_libdir}/libmate-desktop-%{api_version}.so.%{major}*

%files -n %{develname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%doc %{_datadir}/gtk-doc/html/*

