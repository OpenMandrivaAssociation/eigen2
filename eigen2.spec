Name: eigen2
Summary: Lightweight C++ template library for vector and matrix math, a.k.a. linear algebra
Version: 2.0
Release: %mkrel 0.rc1.1
Epoch: 1
Group: System/Libraries
License: LGPL
URL: http://eigen.tuxfamily.org/
Source: http://download.tuxfamily.org/eigen/eigen-%{version}-rc1.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: cmake >= 2.6.1
BuildRequires: doxygen
BuildRequires: ghostscript-common
BuildRequires: graphviz
BuildRequires: tetex-dvips
BuildRequires: tetex-latex
BuildRequires: blas-devel
BuildRequires: cholmod-devel
BuildRequires: superlu
BuildRequires: umfpack-devel

%description 
Eigen is a lightweight C++ template library for vector and matrix
math, a.k.a. linear algebra.

%prep
%setup -q -n %name

%build
export CXXFLAGS="$CXXFLAGS -fpermissive"
export CFLAGS="$CFLAGS -fpermissive"
export CPPFLAGS="$CPPFLAGS -fpermissive"

%cmake -DEIGEN_BUILD_TESTS=ON
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
%makeinstall_std -C

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc COPYING COPYING.LESSER html/ latex/refman.pdf
%dir %{_includedir}/eigen2/
%{_includedir}/eigen2/*

