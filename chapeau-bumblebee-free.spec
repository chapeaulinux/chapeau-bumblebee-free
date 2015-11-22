%define _use_internal_dependency_generator 0

Summary:	Chapeau meta-package for bumblebee nouveau drivers
Name:		chapeau-bumblebee-free
Version:	1
Release:	1%{?dist}
License:	GPL v2
Group:		Chapeau
URL:		http://chapeaulinux.org
BuildArch:	x86_64

Requires:	bumblebee-release
Requires:	libbsd-devel
Requires:	libbsd
Requires:	glibc-devel
Requires:	libX11-devel
Requires:	help2man
Requires:	autoconf
Requires:	git
Requires:	tar
Requires:	glib2
Requires:	glib2-devel
Requires:	kernel-devel
Requires:	kernel-headers
Requires:	automake
Requires:	gcc
Requires:	gtk2-devel
Requires:	bbswitch-dkms
Requires:	bumblebee-nouveau

%description
A meta package for the bumblebee nouveau drivers packages

%prep

%build

%clean 

%install

%post

%preun
[ $0 = 1 ] && rpm -e bumblebee-nouveau bbswitch-dkms 

%files 


%changelog
* Fri Nov 20 2014 Vince Pooley <vince@chapeaulinux.org>
- initial release

