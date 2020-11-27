%define version 1.2.0
%define commit 3f4ac7629e4953c6d5a55f5163c6f7b987927ae6
%global debug_package %{nil}
Name:		station
Version:	%{version}
Release:	0
Summary:	Terminal Emulator using MauiKit
Url:		https://invent.kde.org/maui/station
Source0:	%{url}/-/archive/v%{version}/%{name}-%{version}.tar.gz
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
%license LICENSE
/usr/bin/station
/usr/share/applications/org.kde.station.desktop
/usr/share/icons/hicolor/scalable/apps/station.svg