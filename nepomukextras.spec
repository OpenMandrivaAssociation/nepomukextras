%define nepomukextras_major 0
%define libnepomukextras %mklibname nepomukextras %{nepomukextras_major}

Name:		nepomukextras
Version:	0.2.0
Release:	2
Summary:	Nepomuk support files
Group:		Graphical desktop/KDE
License:	GPLv2+
Url:		ftp://ftp.kde.org/pub/kde/unstable/nepomuk/
Source0:	ftp://ftp.kde.org/pub/kde/unstable/nepomuk/%{name}-%{version}.tar.bz2
Patch0:		nepomukextras-0.2.0-soprano.patch
Requires:	%{libnepomukextras} = %{version}-%{release}
BuildRequires:	kdelibs4-devel
BuildRequires:	tesseract-devel
BuildRequires:	kolena-devel

%description
Nepomuk support files.

%files -f %{name}.lang

#-------------------------------------------------------------------------

%package -n %{libnepomukextras}
Summary:	Nepomuk support library
Group:		System/Libraries

%description -n %{libnepomukextras}
Nepomuk support library.

%files -n %{libnepomukextras}
%{_kde_libdir}/libnepomukextras.so.%{nepomukextras_major}*

#-------------------------------------------------------------------------

%package devel
Summary:	Nepomuk support devel headers
Group:		Development/KDE and Qt
Requires:	%{libnepomukextras} = %{version}-%{release}

%description devel
Nepomuk support devel headers.

%files devel
%{_kde_includedir}/nepomuk/*
%{_kde_datadir}/cmake/NepomukExtras
%{_kde_libdir}/libnepomukextras.so

#-------------------------------------------------------------------------

%prep
%setup -q
%patch0 -p1

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

%find_lang %{name}

