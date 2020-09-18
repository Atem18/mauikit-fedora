%define version 1.1.1
%define commit a14928012787c090b98acef2e43d16121951bd32
%global debug_package %{nil}
Name:		station
Version:	%{version}
Release:	1
Summary:	Terminal Emulator using MauiKit
Url:		https://invent.kde.org/maui/station
Source0:	%{url}/-/archive/v%{version}/%{name}-%{version}.tar.gz
License:	GPLv3
Group:		Applications/Productivity
BuildRequires: cmake
BuildRequires: mauikit-devel
BuildRequires: cmake(KF5Config)
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
%license LICENSE
/usr/bin/station
/usr/share/applications/org.kde.station.desktop
