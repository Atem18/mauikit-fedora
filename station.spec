Name:		station
Version:	2.0.0
Release:	0
Summary:	Terminal Emulator using MauiKit
Url:		https://invent.kde.org/maui/station
Source0:	station-%{version}.tar.xz
License:	GPLv3
Group:		Applications/Productivity
BuildRequires: cmake
BuildRequires: extra-cmake-modules
BuildRequires: cmake(Qt5Qml)
BuildRequires: cmake(Qt5Quick)
BuildRequires: cmake(Qt5Sql)
BuildRequires: cmake(Qt5Svg)
BuildRequires: cmake(Qt5QuickControls2)
BuildRequires: cmake(KF5I18n)
BuildRequires: cmake(KF5Notifications)
BuildRequires: cmake(KF5CoreAddons)
BuildRequires: mauikit-devel
Requires: qmltermwidget

%description
Terminal Emulator using MauiKit

%prep
%autosetup -p1 -n %{name}-v%{version}-%{commit}

%build
cmake -DCMAKE_INSTALL_PREFIX=/usr
make

%install
%make_install

%files
/usr/bin/station
/usr/share/applications/org.kde.station.desktop
