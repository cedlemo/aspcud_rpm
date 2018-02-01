# Aspcud package for opam on fedora 27

## Context

opam need aspcud as a dependency and there is no package for rpm linux distribution.
The idea is to try to create packages for the dependencies and eventually
create a rpm for opam.

### opam issues about missing opam package.

https://github.com/ocaml/opam/issues/2953
https://github.com/ocaml/opam/issues/1235

### aspcud and dependencies:

https://github.com/potassco/aspcud
https://github.com/potassco/clasp
https://github.com/potassco/libpotassco
https://github.com/potassco/clingo

## Rpm packaging

### Previous packaging

https://cottsay.fedorapeople.org/
https://cottsay.fedorapeople.org/clasp/
https://cottsay.fedorapeople.org/aspcud/
https://cottsay.fedorapeople.org/clingo/
https://cottsay.fedorapeople.org/potassco/
https://bugzilla.redhat.com/show_bug.cgi?id=1093522

### Fedora wiki
https://fedoraproject.org/wiki/How_to_create_an_RPM_package
http://fedoraproject.org/wiki/Using_Mock_to_test_package_builds#Building_packages_that_depend_on_packages_not_in_a_repository
http://fedoraproject.org/wiki/Packaging:Cmake

### For package that need cmake to be build:

the needed package are `cmake` and `cmake-rpm-macros`, the following instruction
is sufficient:

    BuildRequires: cmake

mock will install in its chroot cmake and cmake-rpm-macros as dependency.

### Build a src rpm from a spec file:

```bash
spectool -g clasp.spec
# download the package listed as source0
fedpkg --release f27 mockbuild
# build both the src rpm and the rpm
```

### Add local rpm to mock repository.
