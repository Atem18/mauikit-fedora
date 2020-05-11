%define snapshot 4f135ff7f6f83629f44bad5fd13731c30ae14a9d
%global debug_package %{nil}
Name:		index-fm
Version:	%{snapshot}
Release:	1
Summary:	File manager using MauiKit
Url:		https://invent.kde.org/kde/index-fm
Source0:	%{url}/-/archive/%{snapshot}/index-fm-%{snapshot}.tar.gz
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

%description
Index is a file manager made using MauiKit.

%prep
%autosetup -p1 -n %{name}-%{snapshot}

%build
cmake -DCMAKE_INSTALL_PREFIX=/usr
make

%install
%make_install

%files
%{_bindir}/index
%{_kf5_applicationsdir}/org.kde.index.desktop
%{_kf5_iconsdir}/hicolor/scalable/apps/index.svg
