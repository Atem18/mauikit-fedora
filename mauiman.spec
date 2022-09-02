Name:           mauiman
Version:        1.0.0
Release:        0
License:        GPL-3.0-or-later
Summary:        Maui Manager Library. Server and public library API.
URL:            https://mauikit.org/
Source:         https://download.kde.org/stable/maui/%{name}/%{version}/%{name}-%{version}.tar.xz
Group:          System Environment/Libraries

Provides:       mauiman = %{version}
Provides:       cmake(MauiMan) = %{version}

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  hicolor-icon-theme

BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5DBus)

%description
Maui Manager Library. Server and public library API.

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
%defattr(-,root,root,-)
%doc README.md
%{_bindir}/MauiManServer
%{_kf5_libdir}/libMauiMan.so
%{_kf5_libdir}/cmake/MauiMan
%{_includedir}/MauiMan

%changelog