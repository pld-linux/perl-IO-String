%include	/usr/lib/rpm/macros.perl
%define	pdir	IO
%define	pnam	String
Summary:	IO::String perl module
Summary(pl):	Modu� perla IO::String
Name:		perl-IO-String
Version:	1.04
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	06252e259f0474133fe3136e9c3ce103
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
IO::String module emulates the IO::File interface for in-core strings.

%description -l pl
Modu� perla IO::String, emuluj�cy interfejs IO::File dla ci�g�w
znak�w.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}
%{__make} test

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/%{pdir}/%{pnam}.pm
%{_mandir}/man3/*
