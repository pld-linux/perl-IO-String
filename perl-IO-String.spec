#
# Conditional build:
%bcond_without	tests	# unit tests
#
%define		pdir	IO
%define		pnam	String
Summary:	IO::String - emulate file interface for in-core strings
Summary(pl.UTF-8):	IO::String - emulacja interfejsu plikowego dla ciągów znaków
Name:		perl-IO-String
Version:	1.08
Release:	3
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	https://www.cpan.org/modules/by-module/IO/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	250e5424f290299fc3d6b5d1e9da3835
URL:		https://metacpan.org/dist/IO-String
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
IO::String module emulates the IO::File interface for in-core strings.

%description -l pl.UTF-8
Moduł Perla IO::String, emulujący interfejs IO::File dla ciągów
znaków.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/IO/String.pm
%{_mandir}/man3/IO::String.3pm*
