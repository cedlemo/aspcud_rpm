# Aspcud package for opam on fedora 27

https://github.com/ocaml/opam/issues/2953
https://github.com/ocaml/opam/issues/1235
https://github.com/potassco/aspcud

dependencies:

https://github.com/potassco/clasp
https://github.com/potassco/libpotassco
https://github.com/potassco/clingo

https://cottsay.fedorapeople.org/
https://bugzilla.redhat.com/show_bug.cgi?id=1093522

extract src.rpm : `rpm2cpio ../hoge.src.rpm | cpio -i` to confimr

https://cottsay.fedorapeople.org/clasp/
https://cottsay.fedorapeople.org/aspcud/
https://cottsay.fedorapeople.org/clingo/
https://cottsay.fedorapeople.org/potassco/

https://fedoraproject.org/wiki/How_to_create_an_RPM_package

sudo dnf install cmake cmake-rpm-macros

build:
spectool -g clasp.spec
fedpkg --release f27 mockbuild
