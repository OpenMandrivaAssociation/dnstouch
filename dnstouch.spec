Summary:	Incrementally updates bind v8+ zone file serial numbers
Name:		dnstouch
Version:	0.4
Release:	%mkrel 12
License:	GPL
Group:		Networking/Other
URL:		http://uranus.it.swin.edu.au/~jn/linux/dns.htm
Source0:	http://uranus.it.swin.edu.au/~jn/linux/ndu-%{version}.tar.bz2
Source1:	ndu.conf
Patch0:		ndu-opt.patch
Patch1:		ndu-verbose.patch
Requires:	ed bind 
BuildRoot:	%{_tmppath}/%{name}-buildroot

%description
dnstouch incrementally updates bind v8+ zone file serial numbers.

%prep

%setup -q -n ndu-%{version}
%patch0 -p0
%patch1 -p0 

%build
export CFLAGS="%{optflags}"
export CC="g++"
make CC="g++" CFLAGS="%{optflags}" -C src dnstouch

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_sysconfdir}

install -m0755 src/dnstouch %{buildroot}%{_bindir}/dnstouch
install -m0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README INSTALL
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/ndu.conf
%attr(0755,root,root) %{_bindir}/dnstouch


