Name: eigen2
Summary: Lightweight C++ template library for vector and matrix math, a.k.a. linear algebra
Version: 2.0.17
Release: 1
Epoch: 2
Group: System/Libraries
License: LGPLv3+ or GPLv2+
URL: http://eigen.tuxfamily.org/
Source: http://bitbucket.org/eigen/eigen/get/%{version}.tar.bz2
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

%setup -qn eigen-eigen-%{version}

%build
%cmake
%make

# this should be fixed later in cmake doc
(cd ..
 doxygen
)

(cd ../latex
 make refman.pdf
)

%install

%makeinstall_std -C build

#%check
#cd test
#%cmake
#make test
#cd -

%files
%doc COPYING COPYING.LESSER html/ 
%dir %{_includedir}/eigen2/
%{_includedir}/eigen2/*
%{_datadir}/pkgconfig/*.pc
