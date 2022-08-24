Name:           apple-bce-kmod-common

Version:        53d14edd596a00ee4af7811be51400451e351614
Release:        1%{?dist}.1
Summary:        Common files for apple BCE kernel modules

Group:          System Environment/Kernel

License:        MIT
URL:            https://github.com/lleyton/apple-bce-drv
Source0:        https://github.com/lleyton/apple-bce-drv/archive/%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:	noarch

%description
A driver for MacBook models 2018 and newer, implementing the VHCI (required for mouse/keyboard/etc.) and audio functionality.

%prep
%setup -q -c -T -a 0

%files

%clean
rm -rf $RPM_BUILD_ROOT
