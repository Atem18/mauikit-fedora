%define version 1.1.1
%define commit 066576b873a547e2fec56e149565b5fc8bfb5084
%global debug_package %{nil}
Name:		mauikit
Version:	%{version}
Release:	1
Summary:	Library for developing MAUI applications
Url:		https://invent.kde.org/kde/mauikit
Source0:	%{url}/-/archive/v%{version}/%{name}-%{version}.tar.gz
License:	GPLv3
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
Requires: %{name} = %{version}

%description devel
Development package to build MauiKit applications.

%prep
%autosetup -p1 -n %{name}-v%{version}-%{commit}

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
/usr/share/maui/csd
%dir %{_kf5_qmldir}/QtQuick/Controls.2
%dir %{_kf5_qmldir}/org
%dir %{_kf5_qmldir}/org/kde
/usr/lib64/qt5/qml/org/kde/appletdecoration
%{_kf5_qmldir}/QtQuick/Controls.2/maui-style/
%{_kf5_qmldir}/org/kde/mauikit/
/usr/lib/libMauiKit.so

%files devel
/usr/lib/cmake/MauiKit
%{_includedir}/MauiKit
