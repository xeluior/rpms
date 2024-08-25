# SPEC file overview:
# https://docs.fedoraproject.org/en-US/quick-docs/creating-rpm-packages/#con_rpm-spec-file-overview
# Fedora packaging guidelines:
# https://docs.fedoraproject.org/en-US/packaging-guidelines/


Name:    folly
Version: v2024.08.19.00
Release: 0%{?dist}
Summary: An open-source C++ library developed by and used at Facebook

License: Apache-2.0
URL:     https://github.com/facebook/folly
Source0: https://github.com/facebook/folly/releases/download/%{version}/%{name}-%{version}.tar.gz

BuildRequires: binutils-devel
BuildRequires: boost-devel
BuildRequires: bzip2-devel
BuildRequires: cmake
BuildRequires: double-conversion-devel
BuildRequires: fast_float-devel
BuildRequires: fmt-devel
BuildRequires: g++
BuildRequires: gflags-devel
BuildRequires: glog-devel
BuildRequires: gmock-devel
BuildRequires: gtest-devel
BuildRequires: libaio-devel
BuildRequires: libdwarf-devel
BuildRequires: libevent-devel
BuildRequires: libsodium-devel
BuildRequires: libunwind-devel
BuildRequires: liburing-devel
BuildRequires: libzstd-devel
BuildRequires: lz4-devel
BuildRequires: openssl-devel
BuildRequires: snappy-devel
BuildRequires: xz-devel
BuildRequires: zlib-ng-compat-devel

%description
Folly (acronymed loosely after Facebook Open Source Library) is a library of
C++17 components designed with practicality and efficiency in mind.

%package devel
Summary:    Development files for folly

%description devel
The folly-devel package contains header files for developing applications that
use folly.

%prep
%setup -q -c

%build
%cmake -DCMAKE_INSTALL_DIR=%{_libdir}/cmake/folly
%cmake_build

%install
%cmake_install

%files
%doc
%license
%{_libdir}/libfolly*

%files devel
%{_includedir}/folly
%{_libdir}/pkgconfig/libfolly.pc
%{_libdir}/cmake/folly

%changelog
* Sun Aug 25 2024 Robert Gingras <developer@three-point-five.dev>

- Initial commit
