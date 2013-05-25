Summary:	Utility to control ethernet cards
Name:		ethtool
Version:	3.9
Release:	1
License:	GPL
Group:		Networking/Admin
Source0:	http://www.kernel.org/pub/software/network/ethtool/%{name}-%{version}.tar.xz
# Source0-md5:	5777759e85b3323917c6cc9327f5d99c
URL:		http://www.kernel.org/pub/software/network/ethtool/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ethtool is a small utility for examining and tuning your
ethernet-based network interface.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man?/*

