#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v4
# autospec commit: da8b975
#
# Source0 file verified with key 0x58D0EE648A48B3BB (faure@kde.org)
#
Name     : kirigami2
Version  : 5.115.0
Release  : 81
URL      : https://download.kde.org/stable/frameworks/5.115/kirigami2-5.115.0.tar.xz
Source0  : https://download.kde.org/stable/frameworks/5.115/kirigami2-5.115.0.tar.xz
Source1  : https://download.kde.org/stable/frameworks/5.115/kirigami2-5.115.0.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause CC0-1.0 GPL-2.0 LGPL-2.0 LGPL-2.1 LGPL-3.0
Requires: kirigami2-data = %{version}-%{release}
Requires: kirigami2-lib = %{version}-%{release}
Requires: kirigami2-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : cmake
BuildRequires : extra-cmake-modules-data
BuildRequires : git
BuildRequires : pkgconfig(Qt5Quick)
BuildRequires : pkgconfig(Qt5QuickControls2)
BuildRequires : pkgconfig(Qt5QuickTest)
BuildRequires : pkgconfig(Qt5Svg)
BuildRequires : qt6base-dev
BuildRequires : qtbase-dev mesa-dev
BuildRequires : qttools-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
Add here, with either a script that does a git checkout
or as git submodules the two projects:

%package data
Summary: data components for the kirigami2 package.
Group: Data

%description data
data components for the kirigami2 package.


%package dev
Summary: dev components for the kirigami2 package.
Group: Development
Requires: kirigami2-lib = %{version}-%{release}
Requires: kirigami2-data = %{version}-%{release}
Provides: kirigami2-devel = %{version}-%{release}
Requires: kirigami2 = %{version}-%{release}

%description dev
dev components for the kirigami2 package.


%package lib
Summary: lib components for the kirigami2 package.
Group: Libraries
Requires: kirigami2-data = %{version}-%{release}
Requires: kirigami2-license = %{version}-%{release}

%description lib
lib components for the kirigami2 package.


%package license
Summary: license components for the kirigami2 package.
Group: Default

%description license
license components for the kirigami2 package.


%prep
%setup -q -n kirigami2-5.115.0
cd %{_builddir}/kirigami2-5.115.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1707694462
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake ..
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake ..
make  %{?_smp_mflags}
popd
mkdir -p clr-build-apx
pushd clr-build-apx
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
GOAMD64=v3
CC=gcc-14
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -mapxf -mavx10.1 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -mapxf -mavx10.1 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 -mapxf -mavx10.1 "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1707694462
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kirigami2
cp %{_builddir}/kirigami2-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/kirigami2/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0 || :
cp %{_builddir}/kirigami2-%{version}/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kirigami2/20079e8f79713dce80ab09774505773c926afa2a || :
cp %{_builddir}/kirigami2-%{version}/LICENSES/LGPL-2.1-only.txt %{buildroot}/usr/share/package-licenses/kirigami2/3c3d7573e137d48253731c975ecf90d74cfa9efe || :
cp %{_builddir}/kirigami2-%{version}/LICENSES/LGPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/kirigami2/757b86330df80f81143d5916b3e92b4bcb1b1890 || :
cp %{_builddir}/kirigami2-%{version}/templates/kirigami/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/kirigami2/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c || :
cp %{_builddir}/kirigami2-%{version}/templates/kirigami/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/kirigami2/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0 || :
cp %{_builddir}/kirigami2-%{version}/templates/kirigami/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kirigami2/3e8971c6c5f16674958913a94a36b1ea7a00ac46 || :
export GOAMD64=v2
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
GOAMD64=v3
pushd clr-build-apx
%make_install_va  || :
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py apx %{buildroot}-va %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/kdevappwizard/templates/kirigami.tar.bz2
/usr/share/locale/ar/LC_MESSAGES/libkirigami2plugin_qt.qm
/usr/share/locale/az/LC_MESSAGES/libkirigami2plugin_qt.qm
/usr/share/locale/bg/LC_MESSAGES/libkirigami2plugin_qt.qm
/usr/share/locale/ca/LC_MESSAGES/libkirigami2plugin_qt.qm
/usr/share/locale/ca@valencia/LC_MESSAGES/libkirigami2plugin_qt.qm
/usr/share/locale/cs/LC_MESSAGES/libkirigami2plugin_qt.qm
/usr/share/locale/da/LC_MESSAGES/libkirigami2plugin_qt.qm
/usr/share/locale/de/LC_MESSAGES/libkirigami2plugin_qt.qm
/usr/share/locale/el/LC_MESSAGES/libkirigami2plugin_qt.qm
/usr/share/locale/en_GB/LC_MESSAGES/libkirigami2plugin_qt.qm
/usr/share/locale/eo/LC_MESSAGES/libkirigami2plugin_qt.qm
/usr/share/locale/es/LC_MESSAGES/libkirigami2plugin_qt.qm
/usr/share/locale/et/LC_MESSAGES/libkirigami2plugin_qt.qm
/usr/share/locale/eu/LC_MESSAGES/libkirigami2plugin_qt.qm
/usr/share/locale/fi/LC_MESSAGES/libkirigami2plugin_qt.qm
/usr/share/locale/fr/LC_MESSAGES/libkirigami2plugin_qt.qm
/usr/share/locale/gl/LC_MESSAGES/libkirigami2plugin_qt.qm
/usr/share/locale/hi/LC_MESSAGES/libkirigami2plugin_qt.qm
/usr/share/locale/hu/LC_MESSAGES/libkirigami2plugin_qt.qm
/usr/share/locale/ia/LC_MESSAGES/libkirigami2plugin_qt.qm
/usr/share/locale/id/LC_MESSAGES/libkirigami2plugin_qt.qm
/usr/share/locale/it/LC_MESSAGES/libkirigami2plugin_qt.qm
/usr/share/locale/ja/LC_MESSAGES/libkirigami2plugin_qt.qm
/usr/share/locale/ka/LC_MESSAGES/libkirigami2plugin_qt.qm
/usr/share/locale/ko/LC_MESSAGES/libkirigami2plugin_qt.qm
/usr/share/locale/lt/LC_MESSAGES/libkirigami2plugin_qt.qm
/usr/share/locale/ml/LC_MESSAGES/libkirigami2plugin_qt.qm
/usr/share/locale/nl/LC_MESSAGES/libkirigami2plugin_qt.qm
/usr/share/locale/nn/LC_MESSAGES/libkirigami2plugin_qt.qm
/usr/share/locale/pa/LC_MESSAGES/libkirigami2plugin_qt.qm
/usr/share/locale/pl/LC_MESSAGES/libkirigami2plugin_qt.qm
/usr/share/locale/pt/LC_MESSAGES/libkirigami2plugin_qt.qm
/usr/share/locale/pt_BR/LC_MESSAGES/libkirigami2plugin_qt.qm
/usr/share/locale/ro/LC_MESSAGES/libkirigami2plugin_qt.qm
/usr/share/locale/ru/LC_MESSAGES/libkirigami2plugin_qt.qm
/usr/share/locale/sk/LC_MESSAGES/libkirigami2plugin_qt.qm
/usr/share/locale/sl/LC_MESSAGES/libkirigami2plugin_qt.qm
/usr/share/locale/sr/LC_MESSAGES/libkirigami2plugin_qt.qm
/usr/share/locale/sr@ijekavian/LC_MESSAGES/libkirigami2plugin_qt.qm
/usr/share/locale/sr@ijekavianlatin/LC_MESSAGES/libkirigami2plugin_qt.qm
/usr/share/locale/sr@latin/LC_MESSAGES/libkirigami2plugin_qt.qm
/usr/share/locale/sv/LC_MESSAGES/libkirigami2plugin_qt.qm
/usr/share/locale/ta/LC_MESSAGES/libkirigami2plugin_qt.qm
/usr/share/locale/tg/LC_MESSAGES/libkirigami2plugin_qt.qm
/usr/share/locale/tr/LC_MESSAGES/libkirigami2plugin_qt.qm
/usr/share/locale/uk/LC_MESSAGES/libkirigami2plugin_qt.qm
/usr/share/locale/zh_CN/LC_MESSAGES/libkirigami2plugin_qt.qm
/usr/share/locale/zh_TW/LC_MESSAGES/libkirigami2plugin_qt.qm

%files dev
%defattr(-,root,root,-)
/usr/include/KF5/Kirigami2/Kirigami/KirigamiPluginFactory
/usr/include/KF5/Kirigami2/Kirigami/PlatformTheme
/usr/include/KF5/Kirigami2/Kirigami/TabletModeWatcher
/usr/include/KF5/Kirigami2/Kirigami/Units
/usr/include/KF5/Kirigami2/Kirigami/VirtualKeyboardWatcher
/usr/include/KF5/Kirigami2/KirigamiPluginFactory
/usr/include/KF5/Kirigami2/PlatformTheme
/usr/include/KF5/Kirigami2/TabletModeWatcher
/usr/include/KF5/Kirigami2/Units
/usr/include/KF5/Kirigami2/kirigami/kirigami2_export.h
/usr/include/KF5/Kirigami2/kirigami/kirigamipluginfactory.h
/usr/include/KF5/Kirigami2/kirigami/platformtheme.h
/usr/include/KF5/Kirigami2/kirigami/tabletmodewatcher.h
/usr/include/KF5/Kirigami2/kirigami/units.h
/usr/include/KF5/Kirigami2/kirigami/virtualkeyboardwatcher.h
/usr/include/KF5/Kirigami2/kirigamipluginfactory.h
/usr/include/KF5/Kirigami2/platformtheme.h
/usr/include/KF5/Kirigami2/tabletmodewatcher.h
/usr/include/KF5/Kirigami2/units.h
/usr/lib64/cmake/KF5Kirigami2/KF5Kirigami2Config.cmake
/usr/lib64/cmake/KF5Kirigami2/KF5Kirigami2ConfigVersion.cmake
/usr/lib64/cmake/KF5Kirigami2/KF5Kirigami2Macros.cmake
/usr/lib64/cmake/KF5Kirigami2/KF5Kirigami2Targets-relwithdebinfo.cmake
/usr/lib64/cmake/KF5Kirigami2/KF5Kirigami2Targets.cmake
/usr/lib64/libKF5Kirigami2.so
/usr/lib64/qt5/mkspecs/modules/qt_Kirigami2.pri

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libKF5Kirigami2.so.5.115.0
/V3/usr/lib64/qt5/qml/org/kde/kirigami.2/libKirigamiPlugin.so
/usr/lib64/libKF5Kirigami2.so.5
/usr/lib64/libKF5Kirigami2.so.5.115.0
/usr/lib64/qt5/qml/org/kde/kirigami.2/AboutItem.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/AboutPage.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/AbstractApplicationHeader.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/AbstractApplicationItem.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/AbstractApplicationWindow.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/AbstractCard.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/AbstractChip.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/AbstractItemViewHeader.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/AbstractListItem.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/Action.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/ActionTextField.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/ActionToolBar.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/ApplicationHeader.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/ApplicationItem.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/ApplicationWindow.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/Avatar.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/BasicListItem.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/Card.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/CardsGridView.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/CardsLayout.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/CardsListView.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/CheckableListItem.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/Chip.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/ContextDrawer.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/Dialog.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/FlexColumn.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/FormLayout.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/GlobalDrawer.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/Heading.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/Hero.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/InlineMessage.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/ItemViewHeader.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/Label.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/LinkButton.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/ListItemDragHandle.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/ListSectionHeader.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/LoadingPlaceholder.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/MenuDialog.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/NavigationTabBar.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/NavigationTabButton.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/OverlayDrawer.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/OverlaySheet.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/Page.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/PagePoolAction.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/PageRow.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/PasswordField.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/PlaceholderMessage.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/PromptDialog.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/RouterWindow.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/ScrollablePage.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/SearchField.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/SelectableLabel.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/Separator.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/ShadowedImage.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/SwipeListItem.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/ToolBarApplicationHeader.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/UrlButton.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/libKirigamiPlugin.so
/usr/lib64/qt5/qml/org/kde/kirigami.2/plugins.qmltypes
/usr/lib64/qt5/qml/org/kde/kirigami.2/private/ActionButton.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/private/ActionIconGroup.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/private/ActionMenuItem.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/private/ActionsMenu.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/private/BannerImage.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/private/CardsGridViewPrivate.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/private/ContextDrawerActionItem.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/private/CornerShadow.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/private/DefaultCardBackground.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/private/DefaultChipBackground.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/private/DefaultListItemBackground.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/private/DefaultPageTitleDelegate.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/private/EdgeShadow.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/private/GlobalDrawerActionItem.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/private/PageActionPropertyGroup.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/private/PrivateActionToolButton.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/private/SwipeItemEventFilter.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/private/globaltoolbar/AbstractPageHeader.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/private/globaltoolbar/BreadcrumbControl.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/private/globaltoolbar/PageRowGlobalToolBarStyleGroup.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/private/globaltoolbar/PageRowGlobalToolBarUI.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/private/globaltoolbar/TabBarControl.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/private/globaltoolbar/TitlesPageHeader.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/private/globaltoolbar/ToolBarPageHeader.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/qmldir
/usr/lib64/qt5/qml/org/kde/kirigami.2/settingscomponents/CategorizedSettings.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/settingscomponents/SettingAction.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/styles/Material/AbstractListItem.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/styles/Material/InlineMessage.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/styles/Material/Label.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/styles/Material/SwipeListItem.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/styles/Material/Theme.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/styles/org.kde.desktop/AbstractApplicationHeader.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/styles/org.kde.desktop/AbstractListItem.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/styles/org.kde.desktop/SwipeListItem.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/styles/org.kde.desktop/Theme.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/swipenavigator/PageTab.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/swipenavigator/PrivateSwipeHighlight.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/swipenavigator/PrivateSwipeProgress.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/swipenavigator/PrivateSwipeStack.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/swipenavigator/PrivateSwipeTab.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/swipenavigator/PrivateSwipeTabBar.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/swipenavigator/SwipeNavigator.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/swipenavigator/TabViewLayout.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/swipenavigator/templates/PageTab.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/templates/AbstractApplicationHeader.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/templates/AbstractCard.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/templates/AbstractChip.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/templates/AbstractListItem.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/templates/ApplicationHeader.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/templates/InlineMessage.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/templates/OverlayDrawer.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/templates/OverlaySheet.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/templates/SingletonHeaderSizeGroup.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/templates/SwipeListItem.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/templates/private/BackButton.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/templates/private/BorderPropertiesGroup.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/templates/private/ContextIcon.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/templates/private/ForwardButton.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/templates/private/GenericDrawerIcon.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/templates/private/IconPropertiesGroup.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/templates/private/MenuIcon.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/templates/private/PassiveNotificationsManager.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/templates/qmldir

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kirigami2/20079e8f79713dce80ab09774505773c926afa2a
/usr/share/package-licenses/kirigami2/3c3d7573e137d48253731c975ecf90d74cfa9efe
/usr/share/package-licenses/kirigami2/3e8971c6c5f16674958913a94a36b1ea7a00ac46
/usr/share/package-licenses/kirigami2/757b86330df80f81143d5916b3e92b4bcb1b1890
/usr/share/package-licenses/kirigami2/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0
/usr/share/package-licenses/kirigami2/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c
