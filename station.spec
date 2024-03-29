%global debug_package %{nil}
Name:		station
Version:	2.2.0
Release:	0
Summary:	Convergent terminal emulator
Url:		https://invent.kde.org/maui/station
Source0:        https://download.kde.org/stable/maui/%{name}/%{version}/%{name}-%{version}.tar.xz
License:	GPLv3
Group:		Applications/Productivity
BuildRequires:  cmake(Qt5Qml)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:	extra-cmake-modules
BuildRequires:  mauikit-devel
BuildRequires:  mauikit-filebrowsing-devel
Requires:	hicolor-icon-theme
Requires:	mauikit-filebrowsing
Requires:       qmltermwidget

%description
Convergent terminal emulator

%prep
%autosetup -p1 -n %{name}-%{version}

%build
cmake -DCMAKE_INSTALL_PREFIX=/usr
make

%install
%make_install

%files
/usr/bin/station
/usr/share/*
