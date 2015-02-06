Summary:	Incrementally updates bind v8+ zone file serial numbers
Name:		dnstouch
Version:	0.4
Release:	17
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




%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 0.4-16mdv2011.0
+ Revision: 617862
- the mass rebuild of 2010.0 packages

* Thu Sep 03 2009 Thierry Vignaud <tv@mandriva.org> 0.4-15mdv2010.0
+ Revision: 428288
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.4-14mdv2009.0
+ Revision: 244441
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0.4-12mdv2008.1
+ Revision: 136369
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Fri Dec 22 2006 Oden Eriksson <oeriksson@mandriva.com> 0.4-12mdv2007.0
+ Revision: 101672
- bunzip patches
- Import dnstouch

* Wed Sep 13 2006 Oden Eriksson <oeriksson@mandriva.com> 0.4-11mdv2007.0
- rebuild

* Tue Jul 05 2005 Oden Eriksson <oeriksson@mandriva.com> 0.4-10mdk
- rebuild

* Mon Jun 07 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 0.4-9mdk
- rebuilt with gcc v3.4.x

* Mon May 17 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 0.4-8mdk
- build release

