Name:           apple-bce-kmod-common

Version:        f93c6566f98b3c95677de8010f7445fa19f75091
Release:        1%{?dist}.1
Summary:        Common files for apple BCE kernel modules

Group:          System Environment/Kernel

License:        MIT
URL:            https://github.com/t2linux/apple-bce-drv
Source0:        https://github.com/t2linux/apple-bce-drv/archive/%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:	noarch

%description
A driver for MacBook models 2018 and newer, implementing the VHCI (required for mouse/keyboard/etc.) and audio functionality.

%prep
%setup -q -c -T -a 0

%files

%clean
rm -rf $RPM_BUILD_ROOT
