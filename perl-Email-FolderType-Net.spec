#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Email
%define	pnam	FolderType-Net
Summary:	Email::FolderType::Net - Recognize folder types for network based message protocols
Summary(pl):	Email::FolderType::Net - Rozpoznawanie typu folderu dla protoko³ów sieciowych
Name:		perl-%{pdir}-%{pnam}
Version:	1.02
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	7b4ab80e9e5d85c8bc10d7097dd5e07c
URL:		http://search.cpan.org/dist/Email-FolderType-Net/
%if %{with tests}
BuildRequires:	perl-Email-LocalDelivery
%endif
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Registers several mail folder types that are known as network based
messaging protocols. Folder names for these protocols should be
specified using a URI syntax.

%description -l pl
Ta klasa rejestruje kilka rodzajów folderów pocztowych znanych jako
sieciowe protoko³y komunikacji. Nazwy folderów dla tych protoko³ów
powinny byæ podawane przy u¿yciu sk³adni URI.

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
%{perl_vendorlib}/Email/FolderType/Net.pm
%{_mandir}/man3/*
