# new source http://www.lwfinger.com/b43-firmware/broadcom-wl-5.100.138.tar.bz2

Name:           b43-firmware
Version:        5.100.138
Release:        1%{?dist}
Summary:        Firmwares for broadcom wireless network adapters

Group:          System Environment/Kernel
License:        Redistributable, no modification permitted
URL:			http://www.lwfinger.com
Source:			http://www.lwfinger.com/b43-firmware/broadcom-wl-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch

BuildRequires:  b43-fwcutter > 014

%description
Package contains firmwares for broadcom wireless network adapters.


%prep
%setup -q -c -n %{name}-%{version}


%build
mkdir firmware
b43-fwcutter -w firmware broadcom-wl-%{version}/linux/wl_apsta.o


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
