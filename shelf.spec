Name:		shelf
Version:	2.2.0
Release:	0
Summary:	Document and EBook collection manager
Url:		https://invent.kde.org/maui/shelf
Source0:    https://download.kde.org/stable/maui/%{name}/%{version}/%{name}-%{version}.tar.xz
License:	GPLv3
Group:		Applications/Productivity
BuildRequires: cmake
BuildRequires: cmake(KF5I18n)
BuildRequires: cmake(KF5Notifications)
BuildRequires: cmake(KF5KIO)
BuildRequires: cmake(KF5Attica)
BuildRequires: cmake(Qt5Qml)
BuildRequires: cmake(Qt5Quick)
BuildRequires: cmake(Qt5Sql)
BuildRequires: cmake(Qt5Svg)
BuildRequires: cmake(Qt5QuickControls2)
BuildRequires: cmake(MauiKitFileBrowsing)
BuildRequires: extra-cmake-modules
BuildRequires: mauikit-devel
BuildRequires: poppler-qt5-devel

%description
Document and EBook collection manager

%prep
%autosetup -p1 -n %{name}-%{version}

%build
cmake -DCMAKE_INSTALL_PREFIX=/usr
make

%install
%make_install

%files
/usr/bin/shelf
/usr/share/applications/org.maui.shelf.desktop
/usr/share/icons/hicolor/scalable/apps/shelf.svg
