%define debug_package %{nil}

Name:           qview
Version:        2.0
Release:        1
Summary:        Qt-based image viewer designed to be practical and minimal
License:        GPL3
Group:          Graphics
URL:            https://interversehq.com/qview
Source0:        https://github.com/jurplel/qView/releases/download/%{version}/qView-%{version}.tar.gz
BuildRequires:  qt5-devel
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  qmake5
BuildRequires:  qt5-tools
BuildRequires:  qt5-qttranslations
BuildRequires:  qt5-linguist-tools

%description
Qt-based image viewer designed to be practical and minimal.

%prep
%setup -qn qView

%build
%qmake_qt5 PREFIX=/usr
%make

%install
mkdir -p %{buildroot}%{_bindir}
%makeinstall_std INSTALL_ROOT=%{buildroot}

%files
%{_bindir}/%{name}
%{_datadir}/applications/qView.desktop
%{_datadir}/licenses/%{name}
%{_iconsdir}/hicolor/*/apps/%{name}.*
