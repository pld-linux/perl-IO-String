%include	/usr/lib/rpm/macros.perl
%define	pdir	IO
%define	pnam	String
Summary:	IO::String perl module
Summary(pl):	Modu� perla IO::String
Name:		perl-IO-String
Version:	1.02
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-16
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
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_sitelib}/IO/String.pm
%{_mandir}/man3/*
