%define upstream_name    Task-Weaken
%define upstream_version 1.03

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

License:    GPL+ or Artistic
Group:      Development/Perl
Summary:    Ensure that a platform has weaken support
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Task/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(File::Spec)
BuildRequires: perl(Scalar::Util)
BuildRequires: perl(Test::More)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc README LICENSE Changes
%{_mandir}/man3/*
%perl_vendorlib/*

