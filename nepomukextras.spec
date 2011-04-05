%define nepomukextras_major 0
%define libnepomukextras %mklibname nepomukextras %nepomukextras_major

Name:          nepomukextras
Version:       0.2.0
Release:       1
Summary:       Nepomuk support files
Group:         Graphical desktop/KDE
License:       GPLv2+
Url:           ftp://ftp.kde.org/pub/kde/unstable/nepomuk/
Source0:       ftp://ftp.kde.org/pub/kde/unstable/nepomuk/%{name}-%{version}.tar.bz2
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires:      %libnepomukextras = %version-%release
BuildRequires: kdelibs4-devel
BuildRequires: tesseract-devel
BuildRequires: kolena-devel

%description
Nepomuk support files

%files -f %name.lang
%defattr(-,root,root)

#-------------------------------------------------------------------------

%package -n %libnepomukextras
Summary:    Ktorrent libbrary
Group:      System/Libraries

%description -n %libnepomukextras
KTorrent library.

%files -n %libnepomukextras
%defattr(-,root,root)
%_kde_libdir/libnepomukextras.so.%{nepomukextras_major}*

#-------------------------------------------------------------------------

%package devel
Summary: Ktorrent plugin devel headers
Group: Networking/File transfer
Requires: %{libnepomukextras} = %{version}

%description devel
Ktorrent plugin devel headers.

%files devel
%defattr(-,root,root)
%_kde_includedir/nepomuk/*
%_kde_datadir/cmake/NepomukExtras
%_kde_libdir/libnepomukextras.so

#-------------------------------------------------------------------------

%prep
%setup -q -n %name-%version

%build
%cmake_kde4 
%make
 
%install
rm -rf %buildroot
%makeinstall_std -C build
%find_lang %name
