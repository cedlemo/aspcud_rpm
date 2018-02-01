Name:           clingo
Version:        5.2.2
Release:        1%{?dist}
Summary:        A grounder and solver for logic programs.

Group:          Applications/Engineering
License:        MIT
URL:            http://www.cs.uni-potsdam.de/clingo/
Source0:        https://github.com/potassco/%{name}/archive/v%{version}.tar.gz

BuildRequires: cmake

%description
Clingo is part of the Potassco project for Answer Set Programming (ASP). ASP
offers a simple and powerful modeling language to describe combinatorial
problems as logic programs. The clingo system then takes such a logic program
and computes answer sets representing solutions to the given problem.

%prep
%autosetup -n %{name}-%{version} [GitHub]

%build
%cmake . -DCMAKE_BUILD_TYPE=Release -DCLINGO_BUILD_TESTS=ON
%make_build

%clean
rm -rf %{buildroot}

%install
%make_install

%files
%{_bindir}/clingo
%{_bindir}/gringo
%{_bindir}/reify

%check
ctest -V %{?_smp_mflags}

%changelog
* Tue Jan 31 2018 Cedric Le Moigne <cedlemo@gmx.com> 3.3.3-0.fc27.R
- Initial version of the package
