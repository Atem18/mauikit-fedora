%global debug_package %{nil}
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
BuildRequires: mauikit-filebrowsing
BuildRequires: extra-cmake-modules
BuildRequires: mauikit-devel
BuildRequires: poppler-qt5-devel

%description
Document and EBook collection manager

%package devel
Summary:  Development files for %{name}
Group:    Development/Libraries/C and C++
Requires: %{name} = %{version}-%{release}

%description devel
Development package to build MauiKit applications.

%prep
%autosetup -p1 -n %{name}-%{version}

%build
cmake -DCMAKE_INSTALL_PREFIX=/usr
make

%install
%make_install

%files
/usr/bin/shelf
/usr/share/icons/hicolor/scalable/apps/shelf.svg
/usr/include/Shelf/Poppler/shelfpoppler_version.h
/usr/lib64/cmake/ShelfPoppler/ShelfPopplerConfig.cmake
/usr/lib64/cmake/ShelfPoppler/ShelfPopplerConfigVersion.cmake
/usr/lib64/qt5/qml/org/shelf/poppler/PDFViewer.qml
/usr/lib64/qt5/qml/org/shelf/poppler/libShelfPoppler.so
/usr/lib64/qt5/qml/org/shelf/poppler/qmldir
/usr/share/applications/org.kde.shelf.desktop
/usr/share/locale/*
/usr/share/metainfo/org.kde.shelf.metainfo.xml

%files devel
/usr/lib/debug/usr/lib64/qt5/qml/org/shelf/poppler/*
