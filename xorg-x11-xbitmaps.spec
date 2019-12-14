%global debug_package %{nil}

Name:           xorg-x11-xbitmaps
Version:        1.1.1
Release:        16
Summary:        X11 application bitmaps of X.Org
License:        MIT
URL:            http://www.x.org
Source0:        http://ftp.yz.yamagata-u.ac.jp/pub/X11/x.org/individual/data/xbitmaps-%{version}.tar.bz2
BuildArch:      noarch
BuildRequires:  gcc automake 
Requires:       pkgconfig

%description
X11 application bitmaps of X.Org project.

%prep
%autosetup -n xbitmaps-%{version} -p1

%build
%configure
%make_build

%install
%make_install

%files
%license COPYING ChangeLog
%{_includedir}/X11
%{_datadir}/pkgconfig/xbitmaps.pc

%changelog
* Tue Dec 3 2019 openEuler Buildteam <buildteam@openeuler.org> - 1.1.1-16
- Package init
