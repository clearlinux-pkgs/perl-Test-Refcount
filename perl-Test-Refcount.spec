#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Test-Refcount
Version  : 0.08
Release  : 6
URL      : https://cpan.metacpan.org/authors/id/P/PE/PEVANS/Test-Refcount-0.08.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/P/PE/PEVANS/Test-Refcount-0.08.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libt/libtest-refcount-perl/libtest-refcount-perl_0.08-3.debian.tar.xz
Summary  : 'assert reference counts on objects'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Test-Refcount-license = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
NAME
`Test::Refcount' - assert reference counts on objects
SYNOPSIS
use Test::More tests => 2;
use Test::Refcount;

%package dev
Summary: dev components for the perl-Test-Refcount package.
Group: Development
Provides: perl-Test-Refcount-devel = %{version}-%{release}

%description dev
dev components for the perl-Test-Refcount package.


%package license
Summary: license components for the perl-Test-Refcount package.
Group: Default

%description license
license components for the perl-Test-Refcount package.


%prep
%setup -q -n Test-Refcount-0.08
cd ..
%setup -q -T -D -n Test-Refcount-0.08 -b 1
mkdir -p deblicense/
mv %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/Test-Refcount-0.08/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Test-Refcount
cp LICENSE %{buildroot}/usr/share/package-licenses/perl-Test-Refcount/LICENSE
cp deblicense/copyright %{buildroot}/usr/share/package-licenses/perl-Test-Refcount/deblicense_copyright
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.1/Test/Refcount.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Test::Refcount.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Test-Refcount/LICENSE
/usr/share/package-licenses/perl-Test-Refcount/deblicense_copyright
