%global debug_package %{nil}
Name:		mauikit
Version:	2.2.0
Release:	0
Summary:	Library for developing MAUI applications
Url:            https://invent.kde.org/maui/mauikit
Source0:        https://download.kde.org/stable/maui/%{name}/%{version}/%{name}-%{version}.tar.xz
License:	LGPL-3.0
Group:		Applications/Productivity
BuildRequires:  cmake(Qt5Qml)
BuildRequires:  cmake(Qt5QuickControls2)
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  cmake(Qt5X11Extras)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5Kirigami2)
BuildRequires:  cmake(KF5Notifications)
BuildRequires:  cmake(KF5WindowSystem)
BuildRequires:  extra-cmake-modules
BuildRequires:  xcb-util-wm-devel
Requires:       cmake(Qt5Svg)
Requires:       cmake(KF5I18n)
Requires:       cmake(KF5Kirigami2)
Requires:       cmake(KF5Notifications)
Provides:       MauiKit

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
/usr/include/MauiKit/Core/*
/usr/lib/libMauiKit.so
/usr/lib64/qt5/qml/*
/usr/share/org.mauikit.controls/csd/*

%files devel
/usr/lib/cmake/MauiKit/
