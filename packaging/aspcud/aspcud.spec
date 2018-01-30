Name:           aspcud
Version:        1.9.4
Release:        1%{?dist}
Summary:        A solver for package problems in CUDF format using ASP

Group:          Applications/Engineering
License:        MIT
URL:            http://www.cs.uni-potsdam.de/%{name}/
Source0:        https://github.com/potassco/%{name}/archive/v%{version}.tar.gz

BuildRequires: cmake boost-devel

%description
The aspcud project provides the converter/preprocessor cudf2lp to translate a
CUDF specification into a set of facts. These facts together with an encoding
can then be passed to an ASP grounder and solver to solve the package problem.
The small C program aspcud takes care of this, calling the necessary tools and
printing the result in CUDF format.

%prep
%autosetup -n %{name}-%{version} [GitHub]

%build
%cmake . -DCMAKE_BUILD_TYPE=Release
%make_build

%clean
rm -rf %{buildroot}

%install
%make_install

%files
%{_bindir}/aspcud
%{_bindir}/cudf2lp
/usr/share/aspcud/misc2012.lp
/usr/share/aspcud/specification.lp
/usr/share/man/man1/aspcud.1.gz
/usr/share/man/man1/cudf2lp.1.gz

%changelog
* Tue Jan 30 2018 Cedric Le Moigne <cedlemo@gmx.com> 1.9.4-0.fc27.R
- Initial version of the package
