%define snapshot ec2bf657f89d633c7cd74abfaec0b6e0afe1955f
%global debug_package %{nil}
Name:		mauikit
Version:	%{snapshot}
Release:	1
Summary:	Library for developing MAUI applications
Url:		http://mauikit.org/
Source0:	https://invent.kde.org/kde/mauikit/-/archive/master/mauikit-%{snapshot}.tar.bz2
License:	GPLv3
Group:		Applications/Productivity
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  qt5-qtwebengine
BuildRequires: qt5-qtbase-devel
Requires:   qt5-qtbase
Requires:   qt5-qtdeclarative
Requires:   qt5-qtsvg
Requires:   qt5-qtquickcontrols2
Requires:   kf5-kio

%description
Library for developing MAUI applications

MauiKit is a set of utilities and "templated" controls based on Kirigami and
QCC2 that follow the ongoing work on the Maui HIG.

It lets you quickly create a Maui application and access utilities and
widgets shared amoing the other Maui apps.

%prep
%autosetup -p1 -n %{name}-master-%{snapshot}

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
