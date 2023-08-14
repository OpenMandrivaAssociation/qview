%define upstream_name qView
%define _empty_manifest_terminate_build 0

Name:           qview
Version:        6.0
Release:        2
Summary:        Simple Qt-based image viewer
License:        GPL3
Group:          Graphics
URL:            https://interversehq.com/qview
Source0:        https://github.com/jurplel/qView/releases/download/%{version}/%{upstream_name}-%{version}.tar.gz

#BuildRequires:  qt5-devel
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Concurrent)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Network)
#BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  qmake-qt6
BuildRequires:  qt6-qttools
#BuildRequires:  qt5-qttranslations
BuildRequires:  cmake(Qt6Linguist)

%description
Qt-based image viewer designed to be practical and minimal.

%prep
%setup -qn %{upstream_name}

%build
qmake-qt6 PREFIX=/usr
%make_build

%install
mkdir -p %{buildroot}%{_bindir}
%make_install INSTALL_ROOT=%{buildroot}

%files
%{_bindir}/%{name}
%{_datadir}/applications/com.interversehq.qView.desktop
%{_datadir}/licenses/%{name}
%{_datadir}/metainfo/com.interversehq.qView.appdata.xml
%{_iconsdir}/hicolor/symbolic/apps/com.interversehq.qView-symbolic.svg
%{_iconsdir}/hicolor/scalable/apps/com.interversehq.qView.svg
%{_iconsdir}/hicolor/*x*/apps/com.interversehq.qView.png
