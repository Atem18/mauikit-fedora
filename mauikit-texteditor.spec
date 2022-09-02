Name:           mauikit-texteditor
Version:        2.2.0
Release:        0
License:        LGPL-2.1-or-later,CC0-1.0,BSD-2-Clause
Summary:        MauiKit Text Editor components
Url:            https://mauikit.org
Source:         https://download.kde.org/stable/maui/%{name}/%{version}/%{name}-%{version}.tar.xz

Provides:       mauikit-texteditor = %{version}
Provides:       cmake(MauiKitTextEditor) = %{version}

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  hicolor-icon-theme
BuildRequires:  fdupes

BuildRequires:  cmake(Qt5QuickCompiler)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Qml)
BuildRequires:  cmake(Qt5Quick)

BuildRequires:  cmake(KF5Kirigami2)
BuildRequires:  cmake(KF5SyntaxHighlighting)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5CoreAddons)

Requires:       qt5-qtquickcontrols2
BuildRequires:  qt5-qtquickcontrols2

BuildRequires:  mauikit-devel = %{version}
BuildRequires:  cmake(MauiKit) = %{version}

%description
MauiKit Text Editor components.

Kit for developing MAUI Apps.
MauiKit is a set of utilities and "templated" controls based on Kirigami and QCC2 that follow the ongoing work on the Maui HIG.
It let you quickly create a Maui application and access utilities and widgets shared among the other Maui apps.

%package devel
Summary:        Development package for MauiKit Text Editor components
Group:          Development/Libraries/KDE
Requires:       %{name} = %{version}

%description devel
MauiKit Text Editor components.

Kit for developing MAUI Apps.
MauiKit is a set of utilities and "templated" controls based on Kirigami and QCC2 that follow the ongoing work on the Maui HIG.
It let you quickly create a Maui application and access utilities and widgets shared among the other Maui apps.

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
%license LICENSES/*
%doc README.md
%dir %{_kf5_libdir}/qt5/qml/org/mauikit/texteditor
%{_kf5_libdir}/qt5/qml/org/mauikit/texteditor/qmldir

%files devel
%defattr(-,root,root,-)
%dir %{_kf5_libdir}/cmake/MauiKitTextEditor
%{_kf5_libdir}/cmake/MauiKitTextEditor/MauiKitTextEditorConfig*
%{_kf5_libdir}/qt5/qml/org/mauikit/texteditor/libMauiKitTextEditor.so