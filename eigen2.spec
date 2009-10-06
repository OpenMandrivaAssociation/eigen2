Name: eigen2
Summary: Lightweight C++ template library for vector and matrix math, a.k.a. linear algebra
Version: 2.0.6
Release: %mkrel 3
Epoch: 2
Group: System/Libraries
License: LGPLv3+ or GPLv2+
URL: http://eigen.tuxfamily.org/
Source: http://bitbucket.org/eigen/%{name}/get/%{version}.tar.bz2
Patch0: eigen-2.0.52-fix-build.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: cmake >= 2.6.1
BuildRequires: doxygen
BuildRequires: ghostscript-common
BuildRequires: graphviz
BuildRequires: tetex-dvips
BuildRequires: tetex-latex
BuildRequires: blas-devel
BuildRequires: lapack-devel
BuildRequires: gsl-devel
BuildRequires: qt4-devel
BuildArch: noarch
Obsoletes: eigen
Obsoletes: eigen-devel

%description 
Eigen is a lightweight C++ template library for vector and matrix
math, a.k.a. linear algebra.

%prep
%setup -q -n %name
#%patch0 -p0

%build
export CXXFLAGS="$CXXFLAGS -fpermissive"
export CFLAGS="$CFLAGS -fpermissive"
export CPPFLAGS="$CPPFLAGS -fpermissive"

%cmake 
#-DEIGEN_BUILD_TESTS=ON
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
%makeinstall_std -C build

# %check
# cd build/test
# ctest
# cd -

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc COPYING COPYING.LESSER html/ 
#latex/refman.pdf
%dir %{_includedir}/eigen2/
%{_includedir}/eigen2/*
