%define url_ver	%(echo %{version} | cut -d. -f1,2)
%define _disable_rebuild_configure 1

%define major	0
%define libname	%mklibname %{name} %{major}
%define devname	%mklibname %{name} -d

# exclude plugin .so from provides
%global __provides_exclude_from %{_libdir}/%{name}/plugins/.*\\.so

Name:		xfdashboard
Version:	0.9.1
Release:	1
Summary:	GNOME shell like dashboard for Xfce
Group:		Graphical desktop/Xfce
License:	GPLv2+
URL:		https://goodies.xfce.org/projects/applications/xfdashboard/start
Source0:	https://archive.xfce.org/src/apps/xfdashboard/%{url_ver}/xfdashboard-%{version}.tar.bz2
BuildRequires:	intltool
BuildRequires:	pkgconfig(clutter-1.0)
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(garcon-1)
BuildRequires:	pkgconfig(libwnck-3.0)
BuildRequires:	pkgconfig(xcomposite)
BuildRequires:	pkgconfig(xdamage)
BuildRequires:	xfce4-dev-tools
BuildRequires:  gettext-devel
BuildRequires:  gettext

%description
Xfdashboard provides a GNOME shell dashboard like interface for use with Xfce
desktop. It can be configured to run to any keyboard shortcut and when executed
provides an overview of applications currently open enabling the user to switch
between different applications. The search feature works like Xfce's app finder
which makes it convenient to search for and start applications.

%package -n %{libname}
Summary:	Shared libraries for %{name}
Group:		System/Libraries

%description -n %{libname}
This package contains the shared libraries for %{name}.

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/Other
Requires:	%{libname} = %{version}-%{release}

%description -n %{devname}
This package contains the development files and headers for %{name}.

%prep
%setup -q
%autopatch -p1

%build
#NOCONFIGURE=1
%configure
%make_build

%install
%make_install

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS ChangeLog README.md
%{_bindir}/xfdashboard*
%{_datadir}/%{name}/
%{_datadir}/themes/%{name}*/
%{_sysconfdir}/xdg/autostart/org.xfce.xfdashboard-autostart.desktop
%{_datadir}/applications/org.xfce.xfdashboard-settings.desktop
%{_datadir}/applications/org.xfce.xfdashboard.desktop
%{_datadir}/metainfo/org.xfce.xfdashboard.metainfo.xml
%{_iconsdir}/hicolor/*x*/apps/org.xfce.xfdashboard.png
%{_iconsdir}/hicolor/scalable/apps/org.xfce.xfdashboard.svg

#plugins
%dir %{_libdir}/%{name}/
%dir %{_libdir}/%{name}/plugins/
%{_libdir}/%{name}/plugins/clock-view.so
%{_libdir}/%{name}/plugins/gnome-shell-search-provider.so
#{_libdir}/%{name}/plugins/example-search-provider.so
%{_libdir}/%{name}/plugins/hot-corner.so
%{_libdir}/%{name}/plugins/middle-click-window-close.so

%files -n %{libname}
%{_libdir}/lib%{name}.so.%{major}
%{_libdir}/lib%{name}.so.%{major}.*

%files -n %{devname}
%{_includedir}/%{name}/
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/lib%{name}.pc
