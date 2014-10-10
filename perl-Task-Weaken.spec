%define modname	Task-Weaken
%define modver	1.04

Summary:	Ensure that a platform has weaken support
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	13
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/Task/%{modname}-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(Scalar::Util)
BuildRequires:	perl(Test::More)
BuildRequires:	perl-devel

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
%setup -qn %{modname}-%{modver}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc README LICENSE Changes
%{perl_vendorlib}/*
%{_mandir}/man3/*

