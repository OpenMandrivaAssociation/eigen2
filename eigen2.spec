%define unstable 1
%define svn 879783
Name: eigen2
Summary: Lightweight C++ template library for vector and matrix math, a.k.a. linear algebra
Version: 2.0
Release: %mkrel 0.beta1.2
Epoch: 1
Group: System/Libraries
License: LGPL
URL: http://eigen.tuxfamily.org/
# Tarball from kdesupport
Source: eigen-%{version}-beta1.%svn.tar.bz2
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
%setup -q -n %{name}

%build
%cmake

%make


%install
rm -rf %buildroot
make -C build DESTDIR=%buildroot install

%clean 
rm -rf %buildroot

