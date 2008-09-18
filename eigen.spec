%define unstable 1

Name: eigen
Summary: Lightweight C++ template library for vector and matrix math, a.k.a. linear algebra
Version: 2.0
Release: %mkrel 0.beta1.1
Epoch: 1
Group: System/Libraries
License: LGPL
URL: http://eigen.tuxfamily.org/
# Tarball from kdesupport
Source: eigen-%{version}-beta1.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: cmake >= 2.4.6

%description
Eigen is a lightweight C++ template library for vector and matrix math, a.k.a.
linear algebra.

%files
%defattr(-,root,root)
%dir %_includedir/eigen2/
%_includedir/eigen2/*

#---------------------------------------------------------------------------------

%prep
%setup -q -n %{name}2

%build
%cmake

%make


%install
rm -rf %buildroot
make -C build DESTDIR=%buildroot install

%clean 
rm -rf %buildroot

