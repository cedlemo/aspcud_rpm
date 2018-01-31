Name:           clasp
Version:        3.3.3
Release:        1%{?dist}
Summary:        A conflict-driven nogood learning answer set solver

Group:          Applications/Engineering
License:        MIT
URL:            http://www.cs.uni-potsdam.de/clasp/
Source0:        https://github.com/potassco/clasp/releases/download/v%{version}/%{name}-%{version}-source.tar.gz

BuildRequires: cmake

%description
clasp is an answer set solver for (extended) normal and disjunctive logic
programs. It is part of the Potassco project for Answer Set Programming (ASP).
The primary algorithm of clasp relies on conflict-driven nogood learning, a
technique that proved very successful for satisfiability checking (SAT). clasp
has been genuinely developed for answer set solving but can also be applied as
a (Max-)SAT or PB solver or as a C++ library in another program. It provides
different reasoning modes and other advanced features.

%prep
%autosetup -n %{name}-%{version} [GitHub]

%build
%cmake . -DCLASP_BUILD_TESTS=ON
%make_build

%clean
rm -rf %{buildroot}

%install
%make_install

%files
%{_bindir}/clasp
%{_bindir}/lpconvert

%check
ctest -V %{?_smp_mflags}

%changelog
* Tue Jan 30 2018 Cedric Le Moigne <cedlemo@gmx.com> 3.3.3-0.fc27.R
- Initial version of the package
