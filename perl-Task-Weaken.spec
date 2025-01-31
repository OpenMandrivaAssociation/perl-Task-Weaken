%define modname	Task-Weaken

Summary:	Ensure that a platform has weaken support
Name:		perl-%{modname}
Version:	1.06
Release:	1
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/pod/Task::Weaken
Source0:	http://www.cpan.org/modules/by-module/Task/%{modname}-%{version}.tar.gz
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
%autosetup -p1 -n %{modname}-%{version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make_build

%check
make test

%install
%make_install

%files
%doc README LICENSE Changes
%{perl_vendorlib}/*
%{_mandir}/man3/*
