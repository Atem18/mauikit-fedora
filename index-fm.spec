Name:		index-fm
Version:	2.0.2
Release:	0
Summary:	Maui File manager
Url:		https://invent.kde.org/kde/index-fm
Source0:    https://download.kde.org/stable/maui/%{name}/%{version}/%{name}-%{version}.tar.xz
License:	GPLv3
Group:		Applications/Productivity
BuildRequires: cmake
BuildRequires: cmake(KF5I18n)
BuildRequires: cmake(KF5Service)
BuildRequires: cmake(KF5Notifications)
BuildRequires: cmake(KF5KIO)
BuildRequires: cmake(KF5Attica)
BuildRequires: cmake(KF5Archive)
BuildRequires: cmake(KF5SyntaxHighlighting)
BuildRequires: cmake(MauiKit)
BuildRequires: cmake(Qt5Qml)
BuildRequires: cmake(Qt5Quick)
BuildRequires: cmake(Qt5Sql)
BuildRequires: cmake(Qt5Svg)
BuildRequires: cmake(Qt5QuickControls2)
BuildRequires: cmake(Qt5WebEngine)
BuildRequires: extra-cmake-modules
Requires: qmltermwidget

%description
Index is a file manager that works on desktops, Android and Plasma Mobile.
Index lets you browse your system files and applications and preview your music, text, image and video files and share them with external applications.

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
