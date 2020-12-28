%define version 1.0.0
%define commit f8b82be7380f56860920333ea668f3c450c7cb4b
%global debug_package %{nil}
Name:		shelf
Version:	%{version}
Release:	0
Summary:	Document and EBook collection manager
Url:		https://invent.kde.org/maui/shelf
Source0:	%{url}/-/archive/v%{version}/%{name}-%{version}.tar.gz
License:	GPLv3
Group:		Applications/Productivity
BuildRequires: cmake
BuildRequires: cmake(KF5I18n)
BuildRequires: cmake(KF5Notifications)
BuildRequires: cmake(KF5KIO)
BuildRequires: cmake(KF5Attica)
BuildRequires: cmake(MauiKit)
BuildRequires: cmake(Qt5Qml)
BuildRequires: cmake(Qt5Quick)
BuildRequires: cmake(Qt5Sql)
BuildRequires: cmake(Qt5Svg)
BuildRequires: cmake(Qt5QuickControls2)
BuildRequires: extra-cmake-modules
BuildRequires: mauikit-devel
BuildRequires: poppler-qt5-devel

%description
Document and EBook collection manager

%prep
%autosetup -p1 -n %{name}-v%{version}-%{commit}

%build
cmake -DCMAKE_INSTALL_PREFIX=/usr
make

%install
%make_install

%files
/usr/bin/shelf
/usr/share/applications/org.maui.shelf.desktop
/usr/share/icons/hicolor/scalable/apps/shelf.svg
