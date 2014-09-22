Name: libibcm
Version: 1.0.5
Release: 9%{?dist}
Summary: Userspace InfiniBand Connection Manager

License: GPLv2 or BSD
Url: http://www.openfabrics.org/
Source: http://www.openfabrics.org/downloads/rdmacm/%{name}-%{version}.tar.gz
Source1: %{name}.rpmlintrc

BuildRequires: libibverbs-devel > 1.1.4, autoconf, automake, libtool
ExcludeArch: s390 s390x
%description
libibcm provides a userspace library that handles the majority of the low
level work required to open an RDMA connection between two machines.

%package devel
Summary: Development files for the libibcm library

Requires: %{name} = %{version}-%{release}, libibverbs-devel >= 1.1
%description devel
Development files for the libibcm library.

%package static
Summary: Static version of libibcm libraries

Requires: %{name}-devel = %{version}-%{release}
%description static
Static version of libibcm library.

%prep
%setup -q

%build
autoreconf -i
%configure2_5x --enable-static
make %{?_smp_mflags}

%install
%makeinstall
# remove unpackaged files from the buildroot
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

%files
%{_libdir}/libibcm*.so.*
%doc AUTHORS COPYING README

%files devel
%{_libdir}/lib*.so
%{_includedir}/*

%files static
%{_libdir}/*.a
