%define version 1.2.0
%define commit 9fb6d8d4b4c1e863172b4e27a6d731fd7a2bac6b
%global debug_package %{nil}
Name:		index-fm
Version:	%{version}
Release:	1
Summary:	File manager using MauiKit
Url:		https://invent.kde.org/kde/index-fm
Source0:	%{url}/-/archive/v%{version}/%{name}-%{version}.tar.gz
License:	GPLv3
Group:		Applications/Productivity
BuildRequires: cmake
BuildRequires: cmake(KF5I18n)
BuildRequires: cmake(KF5Service)
BuildRequires: cmake(KF5Notifications)
BuildRequires: cmake(KF5KIO)
BuildRequires: cmake(KF5Attica)
BuildRequires: cmake(KF5SyntaxHighlighting)
BuildRequires: cmake(MauiKit)
BuildRequires: cmake(Qt5Qml)
BuildRequires: cmake(Qt5Quick)
BuildRequires: cmake(Qt5Sql)
BuildRequires: cmake(Qt5Svg)
BuildRequires: cmake(Qt5QuickControls2)
BuildRequires: cmake(Qt5WebEngine)
BuildRequires: extra-cmake-modules
Requires: kf5-kirigami2

%description
Index is a file manager made using MauiKit.

%prep
%autosetup -p1 -n %{name}-v%{version}-%{commit}

%build
cmake -DCMAKE_INSTALL_PREFIX=/usr
make

%install
%make_install

%files
/usr/bin/index
/usr/share/applications/org.kde.index.desktop
/usr/share/icons/hicolor/scalable/apps/index.svg
