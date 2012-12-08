Name:		eigen2
Summary:	Lightweight C++ template library for vector and matrix math (linear algebra)
Version:	2.0.17
Release:	2
Epoch:		2
Group:		System/Libraries
License:	LGPLv3+ or GPLv2+
URL:		http://eigen.tuxfamily.org/
Source:		http://bitbucket.org/eigen/eigen/get/%{name}-%{version}.tar.bz2
BuildRequires:	cmake >= 2.6.1
BuildRequires:	doxygen
BuildRequires:	ghostscript-common
BuildRequires:	graphviz
BuildRequires:	blas-devel
BuildRequires:	pkgconfig(lapack)
BuildRequires:	pkgconfig(gsl)
BuildRequires:	qt4-devel
BuildArch:	noarch

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


%changelog
* Sun May 29 2011 Funda Wang <fwang@mandriva.org> 2:2.0.16-1mdv2011.0
+ Revision: 681333
- New version 2.0.16

* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 2:2.0.15-2
+ Revision: 664128
- mass rebuild

* Mon Aug 16 2010 Emmanuel Andry <eandry@mandriva.org> 2:2.0.15-1mdv2011.0
+ Revision: 570536
- New version 2.0.15
- drop p0 (merged upstream)

* Sun Nov 15 2009 Funda Wang <fwang@mandriva.org> 2:2.0.9-1mdv2010.1
+ Revision: 466154
- fix pkgconfig dir
- new version 2.0.9

* Tue Oct 06 2009 Funda Wang <fwang@mandriva.org> 2:2.0.6-3mdv2010.0
+ Revision: 454706
- fix obsoletes

* Tue Oct 06 2009 Funda Wang <fwang@mandriva.org> 2:2.0.6-2mdv2010.0
+ Revision: 454505
- add more obsoletes

* Sat Sep 26 2009 Frederik Himpe <fhimpe@mandriva.org> 2:2.0.6-1mdv2010.0
+ Revision: 449387
- Update to new version 2.0.6

* Mon Aug 24 2009 Frederik Himpe <fhimpe@mandriva.org> 2:2.0.5-1mdv2010.0
+ Revision: 420513
- Update to new version 2.0.5

* Sat Aug 01 2009 Frederik Himpe <fhimpe@mandriva.org> 2:2.0.4-1mdv2010.0
+ Revision: 407496
- Update to new version 2.0.4

* Fri Jun 26 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:2.0.3-1mdv2010.0
+ Revision: 389574
- Use latest stable release

* Mon May 25 2009 Funda Wang <fwang@mandriva.org> 1:2.0.52-2mdv2010.0
+ Revision: 379350
- move pkgconfig file into datadir

* Sun May 24 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:2.0.52-1mdv2010.0
+ Revision: 379213
- New version
  Disable tests for the moment
- Sync sources
- Update to 2.0.52

  + Funda Wang <fwang@mandriva.org>
    - 2.0.0 final

* Sun Jan 25 2009 Giuseppe Ghibò <ghibo@mandriva.com> 1:2.0-0.beta6.1mdv2009.1
+ Revision: 333396
- Update to release 2.0beta6.
- Add docs.
- Initial support for checking (trough --with build_check rpm flag).

* Tue Nov 04 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:2.0-0.beta1.2mdv2009.1
+ Revision: 299669
- Udpate eigen snapshot

* Thu Sep 18 2008 Helio Chissini de Castro <helio@mandriva.com> 1:2.0-0.beta1.1mdv2009.0
+ Revision: 285689
- Deploying eigen2
- This is eigen2.
- No need extra requires
- Eigen2 beta1 requires by koffice beta1

* Wed Aug 06 2008 Thierry Vignaud <tv@mandriva.org> 2.0-2.alpha4.1mdv2009.0
+ Revision: 264425
- rebuild early 2009.0 package (before pixel changes)

* Thu Apr 17 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 2.0-0.alpha4.1mdv2009.0
+ Revision: 195340
- Update to eigen 2 alpha4

* Mon Feb 18 2008 Thierry Vignaud <tv@mandriva.org> 1.0.5-2mdv2008.1
+ Revision: 170810
- rebuild
- fix "foobar is blabla" summary (=> "blabla") so that it looks nice in rpmdrake
- fix description-line-too-long
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Fri Jul 06 2007 Helio Chissini de Castro <helio@mandriva.com> 1.0.5-1mdv2008.0
+ Revision: 48943
- import eigen-1.0.5-1mdv2008.0

