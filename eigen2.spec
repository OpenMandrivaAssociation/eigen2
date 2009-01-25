%define unstable 1
%define rel beta6

# svn co svn://anonsvn.kde.org/home/kde/trunk/kdesupport/eigen2
%define svn 910059
# other infos at
# https://bugzilla.redhat.com/show_bug.cgi?id=459705

%define build_check     0
%{?_with_build_check: %{expand: %%global build_check 1}}
%{?_without_build_check: %{expand: %%global build_check 0}}

# cmake still requires here:
#-- Could NOT find SUPERLU  (missing:  SUPERLU_INCLUDES SUPERLU_LIBRARIES)
#-- Could NOT find GOOGLEHASH  (missing:  GOOGLEHASH_INCLUDES)
%if %{build_check}
%define extrabuild	-DEIGEN_BUILD_TESTS:BOOL=ON
%else
%define extrabuild	%{nil}
%endif

Name: eigen2
Summary: Lightweight C++ template library for vector and matrix math, a.k.a. linear algebra
Version: 2.0
Release: %mkrel 0.beta6.1
Epoch: 1
Group: System/Libraries
License: LGPL
URL: http://eigen.tuxfamily.org/
Source: eigen-%{version}-%{rel}.tar.bz2
Patch0: eigen-2.0-beta6-cmake261.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: cmake >= 2.6.1
BuildRequires: doxygen
BuildRequires: ghostscript-common
BuildRequires: graphviz
BuildRequires: tetex-dvips
BuildRequires: tetex-latex
%if %{build_check}
BuildRequires: blas-devel
BuildRequires: cholmod-devel
BuildRequires: superlu
BuildRequires: umfpack-devel
%endif

%description 
Eigen is a lightweight C++ template library for vector and matrix
math, a.k.a. linear algebra.

%prep
%setup -q -n %{name}
%patch0 -p1 -b .261

%build
%cmake %{extrabuild}
%make

# this should be fixed later in cmake doc
(cd ..
 doxygen
)

(cd ../latex
 make refman.pdf
)

%install
rm -rf %{buildroot}
make -C build DESTDIR=%{buildroot} install

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc COPYING COPYING.LESSER html/ latex/refman.pdf
%dir %{_includedir}/eigen2/
%{_includedir}/eigen2/*
