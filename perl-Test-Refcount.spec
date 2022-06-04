#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Test-Refcount
Version  : 0.10
Release  : 25
URL      : https://cpan.metacpan.org/authors/id/P/PE/PEVANS/Test-Refcount-0.10.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/P/PE/PEVANS/Test-Refcount-0.10.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libt/libtest-refcount-perl/libtest-refcount-perl_0.08-3.debian.tar.xz
Summary  : 'assert reference counts on objects'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Test-Refcount-license = %{version}-%{release}
Requires: perl-Test-Refcount-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Module::Build)

%description
NAME
Test::Refcount - assert reference counts on objects
SYNOPSIS
use Test::More tests => 2;
use Test::Refcount;

use Some::Class;

my $object = Some::Class->new();

is_oneref( $object, '$object has a refcount of 1' );

my $otherref = $object;

is_refcount( $object, 2, '$object now has 2 references' );

%package dev
Summary: dev components for the perl-Test-Refcount package.
Group: Development
Provides: perl-Test-Refcount-devel = %{version}-%{release}
Requires: perl-Test-Refcount = %{version}-%{release}

%description dev
dev components for the perl-Test-Refcount package.


%package license
Summary: license components for the perl-Test-Refcount package.
Group: Default

%description license
license components for the perl-Test-Refcount package.


%package perl
Summary: perl components for the perl-Test-Refcount package.
Group: Default
Requires: perl-Test-Refcount = %{version}-%{release}

%description perl
perl components for the perl-Test-Refcount package.


%prep
%setup -q -n Test-Refcount-0.10
cd %{_builddir}
tar xf %{_sourcedir}/libtest-refcount-perl_0.08-3.debian.tar.xz
cd %{_builddir}/Test-Refcount-0.10
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/Test-Refcount-0.10/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Test-Refcount
cp %{_builddir}/Test-Refcount-0.10/LICENSE %{buildroot}/usr/share/package-licenses/perl-Test-Refcount/ae5457947130c5a7a05fc82ca7baf0570bf57d00
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-Test-Refcount/9fc71e0e36d5040f660a2d715d7bd3c8e83a3364
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

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Test::Refcount.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Test-Refcount/9fc71e0e36d5040f660a2d715d7bd3c8e83a3364
/usr/share/package-licenses/perl-Test-Refcount/ae5457947130c5a7a05fc82ca7baf0570bf57d00

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
