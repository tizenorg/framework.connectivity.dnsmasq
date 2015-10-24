Name:       dnsmasq
Summary:    dnsmasq, DNS forwarder.
Version:    2.57_11
Release:    7
Group:      System/Network
License:    GPL-2.0+ or GPL-3.0+
Source0:    %{name}-%{version}.tar.gz
BuildRequires: cmake
BuildRequires: pkgconfig(dbus-1)

%description
Dnsmasq is a lightweight, easy to configure DNS forwarder and DHCP server.

%prep
%setup -q

%build
cmake . -DCMAKE_INSTALL_PREFIX=%{_prefix}
make %{?jobs:-j%jobs}

%post
mkdir -p /opt/var/lib/misc

%install
rm -rf %{buildroot}
%make_install

mkdir -p %{buildroot}/usr/share/license
cp COPYING %{buildroot}/usr/share/license/dnsmasq

%files
%manifest dnsmasq.manifest
%{_bindir}/dnsmasq
/usr/share/license/dnsmasq
