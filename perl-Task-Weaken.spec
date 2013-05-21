%define upstream_name    Task-Weaken
%define upstream_version 1.04

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	6

License:	GPL+ or Artistic
Group:		Development/Perl
Summary:	Ensure that a platform has weaken support
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Task/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl(File::Spec)
BuildRequires:	perl(Scalar::Util)
BuildRequires:	perl(Test::More)
BuildRequires:	perl-devel
BuildArch:	noarch

%description
One recurring problem in modules that use the Scalar::Util manpage's
'weaken' function is that it is not present in the pure-perl variant.

While this isn't necesarily always a problem in a straight CPAN-based Perl
environment, some operating system distributions only include the pure-Perl
versions, don't include the XS version, and so weaken is then "missing"
from the platform, *despite* passing a dependency on the Scalar::Util
manpage successfully.

Most notably this is RedHat Linux at time of writing, but other come and go
and do the same thing, hence "recurring problem".

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc README LICENSE Changes
%{_mandir}/man3/*
%{perl_vendorlib}/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 1.40.0-4mdv2012.0
+ Revision: 765669
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 1.40.0-3
+ Revision: 764180
- rebuilt for perl-5.14.x

* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 1.40.0-2
+ Revision: 657469
- rebuild for updated spec-helper

* Thu Mar 10 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.40.0-1
+ Revision: 643492
- update to new version 1.04

* Sun Aug 01 2010 Funda Wang <fwang@mandriva.org> 1.30.0-3mdv2011.0
+ Revision: 564755
- rebuild for perl 5.12.1

* Tue Jul 13 2010 Jérôme Quelin <jquelin@mandriva.org> 1.30.0-2mdv2011.0
+ Revision: 551998
- rebuild
- using source0: instead of source:

* Thu Jun 18 2009 Jérôme Quelin <jquelin@mandriva.org> 1.30.0-1mdv2010.0
+ Revision: 386970
- update to 1.03
- using %%perl_convert_version
- fixed license tag

* Wed Dec 03 2008 Jérôme Quelin <jquelin@mandriva.org> 1.02-1mdv2009.1
+ Revision: 309770
- import perl-Task-Weaken


* Wed Dec 03 2008 cpan2dist 1.02-1mdv
- initial mdv release, generated with cpan2dist

