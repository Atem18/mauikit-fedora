%global debug_package %{nil}
Name:		mauikit
Version:	2.0.2
Release:	0
Summary:	Library for developing MAUI applications
Url:        https://invent.kde.org/maui/mauikit
Source0:    https://download.kde.org/stable/maui/%{name}/%{version}/%{name}-%{version}.tar.xz
License:	LGPL-3.0
Group:		Applications/Productivity
BuildRequires: cmake
BuildRequires: cmake(Qt5Qml)
BuildRequires: cmake(Qt5Sql)
BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5Quick)
BuildRequires: cmake(Qt5Gui)
BuildRequires: cmake(Qt5Svg)
BuildRequires: cmake(Qt5QuickControls2)
BuildRequires: cmake(Qt5Network)
BuildRequires: cmake(Qt5DBus)
BuildRequires: cmake(Qt5Xml)
BuildRequires: cmake(Qt5X11Extras)
BuildRequires: cmake(KF5I18n)
BuildRequires: cmake(KF5Notifications)
BuildRequires: cmake(KF5Config)
BuildRequires: cmake(KF5Service)
BuildRequires: cmake(KF5KIO)
BuildRequires: cmake(KF5ConfigWidgets)
BuildRequires: cmake(KF5Plasma)
BuildRequires: cmake(KF5Declarative)
BuildRequires: cmake(KDecoration2)
BuildRequires: cmake(KF5SyntaxHighlighting)
BuildRequires: cmake(KF5Attica)
BuildRequires: extra-cmake-modules
BuildRequires: libxcb-devel
Provides:      cmake(MauiKit)

%description
Library for developing MAUI applications

MauiKit is a set of utilities and "templated" controls based on Kirigami and
QCC2 that follow the ongoing work on the Maui HIG.

It lets you quickly create a Maui application and access utilities and
widgets shared amoing the other Maui apps.


%package devel
Summary:  Development files for %{name}
Group:    Development/Libraries/C and C++
Requires: %{name} = %{version}-%{release}

%description devel
Development package to build MauiKit applications.

%prep
%autosetup -p1 -n %{name}-%{version}

%build
cmake \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DCMAKE_INSTALL_LIBDIR=/usr/lib
make

%install
%make_install

%files
%license LICENSE
%dir %{_kf5_qmldir}/QtQuick/Controls.2/
%{_kf5_qmldir}/QtQuick/Controls.2/maui-style/
%dir %{_kf5_qmldir}/org/
%{_kf5_qmldir}/org/mauikit/
%exclude %{_kf5_qmldir}/org/mauikit/controls/libs/appview.h

%files devel
%doc README.md
%{_includedir}/*
%{_libdir}/cmake/MauiKit/
%{_kf5_qmldir}/org/mauikit/controls/libs/appview.h