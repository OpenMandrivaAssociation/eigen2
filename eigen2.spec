Summary:	Lightweight C++ template library for vector and matrix math (linear algebra)
Name:		eigen2
Epoch:		2
Version:	2.0.17
Release:	3
Group:		System/Libraries
License:	LGPLv3+ or GPLv2+
Url:		http://eigen.tuxfamily.org/
Source0:	http://bitbucket.org/eigen/eigen/get/%{name}-%{version}.tar.bz2
BuildArch:	noarch

BuildRequires:	cmake >= 2.6.1
BuildRequires:	doxygen
BuildRequires:	ghostscript-common
BuildRequires:	graphviz
BuildRequires:	qt4-devel
BuildRequires:	pkgconfig(blas)
BuildRequires:	pkgconfig(gsl)
BuildRequires:	pkgconfig(lapack)

%description
Eigen is a lightweight C++ template library for vector and matrix
math, a.k.a. linear algebra.

%prep
%setup -q

%build
%cmake
%make

# this should be fixed later in cmake doc
(cd ..
 doxygen
)

%install
%makeinstall_std -C build

%files
%doc COPYING COPYING.LESSER html/
%dir %{_includedir}/eigen2/
%{_includedir}/eigen2/*
%{_datadir}/pkgconfig/*.pc

