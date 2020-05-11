%define snapshot 90d2d9ea930483f4b2c29e8d6cf4d70f38e0c0ae
%global debug_package %{nil}
Name:		mauikit
Version:	%{snapshot}
Release:	1
Summary:	Library for developing MAUI applications
Url:		https://invent.kde.org/kde/mauikit
Source0:	%{url}/-/archive/%{snapshot}/mauikit-%{snapshot}.tar.gz
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
BuildRequires: extra-cmake-modules

%description
Library for developing MAUI applications

MauiKit is a set of utilities and "templated" controls based on Kirigami and
QCC2 that follow the ongoing work on the Maui HIG.

It lets you quickly create a Maui application and access utilities and
widgets shared amoing the other Maui apps.

%prep
%autosetup -p1 -n %{name}-%{snapshot}

%build
cmake \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DCMAKE_INSTALL_LIBDIR=/usr/lib
make

%install
%make_install

%files
/usr/include/MauiKit
/usr/lib/cmake/MauiKit
/usr/lib/libMauiKit.so
/usr/lib64/qt5/qml/org/kde/mauikit
/usr/lib64/qt5/qml/QtQuick/Controls.2/maui-style
/usr/share/maui
