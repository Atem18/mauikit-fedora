%global debug_package %{nil}
Name:		mauiman
Version:	1.0.0
Release:	0
Summary:	Maui Manager Library. Server and Library
Url:		https://invent.kde.org/maui/mauiman
Source0:    https://download.kde.org/stable/maui/%{name}/%{version}/%{name}-%{version}.tar.xz
License:	GPLv3
Group:		Applications/Productivity

BuildRequires:  gcc-c++
BuildRequires:  gcc
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
Provides:       MauiMan

%description
Maui Manager Library. Server and Library

%package devel
Summary:  Development files for %{name}
Group:    Development/Libraries/C and C++
Requires: %{name} = %{version}-%{release}

%description devel
Development package to build MauiKit applications.

%prep
%autosetup -p1 -n %{name}-%{version}

%build
cmake -DCMAKE_BUILD_TYPE="Release" \
    -DCMAKE_INSTALL_PREFIX="/usr" \
    -DBUNDLE_MAUI_STYLE=ON
make

%install
%make_install

%files
/usr/bin/MauiManServer
/usr/include/MauiMan/*
/usr/lib64/cmake/MauiMan/*
/usr/lib64/libMauiMan.so
