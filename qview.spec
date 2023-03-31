%define upstream_name qView

Name:           qview
Version:        5.0
Release:        2
Summary:        Simple Qt-based image viewer
License:        GPL3
Group:          Graphics
URL:            https://interversehq.com/qview
Source0:        https://github.com/jurplel/qView/releases/download/%{version}/%{upstream_name}-%{version}.tar.gz

BuildRequires:  qt5-devel
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Concurrent) >= 5.9
BuildRequires:  pkgconfig(Qt5Widgets) >= 5.9
BuildRequires:  pkgconfig(Qt5Network) >= 5.9
BuildRequires:  qmake5
BuildRequires:  qt5-qttools
BuildRequires:  qt5-qttranslations
BuildRequires:  qt5-linguist-tools

%description
Qt-based image viewer designed to be practical and minimal.

%prep
%setup -qn %{upstream_name}

%build
%qmake_qt5 PREFIX=/usr
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
