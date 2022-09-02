%global debug_package %{nil}
Name:		index-fm
Version:	2.2.0
Release:	0
Summary:	Maui File manager
Url:		https://invent.kde.org/kde/index-fm
Source0:        https://download.kde.org/stable/maui/index/%{version}/%{name}-%{version}.tar.xz
License:	GPLv3
Group:		Applications/Productivity
BuildRequires:  cmake(Qt5Qml)
BuildRequires:  cmake(Qt5QuickControls2)
BuildRequires:  cmake(KF5Archive)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  mauikit-devel
BuildRequires:  mauikit-filebrowsing-devel
BuildRequires:  extra-cmake-modules
Requires:	mauikit-filebrowsing
Requires:	hicolor-icon-theme
Requires: qt5-qtmultimedia
Requires: qmltermwidget

%description
Index is a file manager that works on desktops, Android and Plasma Mobile.
Index lets you browse your system files and applications and preview your music, text, image and video files and share them with external applications.

%prep
%autosetup -p1 -n %{name}-%{version}

%build
cmake -DCMAKE_INSTALL_PREFIX=/usr
make

%install
%make_install

%files
/usr/bin/index
/usr/share/*
