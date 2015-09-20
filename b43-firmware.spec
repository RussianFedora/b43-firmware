# new source http://www.lwfinger.com/b43-firmware/broadcom-wl-5.100.138.tar.bz2

Name:           b43-firmware
Version:        5.100.138
Release:        2%{?dist}
Summary:        Firmwares for broadcom wireless network adapters

Group:          System Environment/Kernel
License:        Redistributable, no modification permitted
URL:            http://www.lwfinger.com
#Source:        http://mirror2.openwrt.org/sources/broadcom-wl-%{version}_mipsel.tar.bz2
Source:         http://www.lwfinger.com/b43-firmware/broadcom-wl-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
Epoch:          1

BuildRequires:  b43-fwcutter > 018

%description
Package contains firmwares for broadcom wireless network adapters.


%prep
%setup -q -c -n %{name}-%{version}


%build
mkdir firmware
#b43-fwcutter -w firmware broadcom-wl-%{version}/linux/wl_apsta.o
/usr/bin/b43-fwcutter -w firmware broadcom-wl-%{version}/linux/wl_apsta.o


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/lib/firmware
cp -R firmware/* $RPM_BUILD_ROOT/lib/firmware


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
/lib/firmware/b43


%changelog
* Thu Aug 27 2015 Vasiliy N. Glazov <vascom2@gmail.com> 1:5.100.138-2.R
- Bump release

* Mon Nov 03 2014 Alexei Panov <me AT elemc DOT name> 1:5.100.138 -1%{?dist}
- Update for Fedora 20/21

* Thu Nov 10 2011 Alexei Panov <me AT elemc DOT name> - 1:5.10.56.27.3-1
- Regress to worked version for kernel < 3.2

* Sun Oct 30 2011 Alexei Panov <me AT elemc DOT name> - 5.100.138-1
- Update version to 5.100.138

* Fri Nov 12 2010 Arkady L. Shane <ashejn@yandex-team.ru> - 4.178.10.4-4
- fix release

* Fri Nov 12 2010 Arkady L. Shane <ashejn@yandex-team.ru> - 4.178.10.4-3
- do not obsolete b43-openfwwf

* Tue Oct 26 2010 Arkady L. Shane <ashejn@yandex-team.ru> - 4.178.10.4-2
- add P: b43-openfwwf and O: b43-openfwwf

* Tue Sep 22 2009 Arkady L. Shane <ashejn@yandex-team.ru> - 4.178.10.4-1
- update for kernel 2.6.31

* Tue Sep 09 2008 Nikolay Ulyanitsky <Nikolay.Ulyanitsky@asplinux.ru> - 4.150.10.5-1
- Initial build for ASPLinux
