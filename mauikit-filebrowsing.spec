%global debug_package %{nil}
Name:		mauikit-filebrowsing
Version:	2.1.1
Release:	0
Summary:	MauiKit File Browsing utilities and controls
Url:		https://invent.kde.org/kde/index-fm
Source0:        https://download.kde.org/stable/maui/%{name}/%{version}/%{name}-%{version}.tar.xz
License:	GPLv3
Group:		Applications/Productivity
BuildRequires:  cmake(Qt5Quick)
BuildRequires:  cmake(KF5I18n)
BuildRequires:	kf5-kio-devel
BuildRequires:  extra-cmake-modules
BuildRequires:	MauiKit
Requires:	MauiKit
Requires:	kf5-kio
Provides:	MauiKitFileBrowsing

%description
MauiKit File Browsing utilities and controls

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
/usr/include/MauiKit/FileBrowsing/*
/usr/lib/*
/usr/lib64/qt5/qml/org/mauikit/filebrowsing/*

%files devel
/usr/lib/cmake/MauiKitFileBrowsing/*
