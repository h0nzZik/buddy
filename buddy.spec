Name:    buddy
Version: 2.4
Release: 1%{?dist}
Summary: A Binary Decision Diagram library

License: MIT
URL: https://sourceforge.net/projects/buddy
Source0: %{name}-%{version}.tar.gz

BuildRequires: autoconf automake libtool

%description
A simple program to greet the user, Texas style.

%license

               Copyright (C) 1996-2002 by Jorn Lind-Nielsen
                            All rights reserved

    Permission is hereby granted, without written agreement and without
    license or royalty fees, to use, reproduce, prepare derivative
    works, distribute, and display this software and its documentation
    for any purpose, provided that (1) the above copyright notice and
    the following two paragraphs appear in all copies of the source code
    and (2) redistributions, including without limitation binaries,
    reproduce these notices in the supporting documentation. Substantial
    modifications to this software may be copyrighted by their authors
    and need not follow the licensing terms described here, provided
    that the new terms are clearly indicated in all files where they apply.

    IN NO EVENT SHALL JORN LIND-NIELSEN, OR DISTRIBUTORS OF THIS
    SOFTWARE BE LIABLE TO ANY PARTY FOR DIRECT, INDIRECT, SPECIAL,
    INCIDENTAL, OR CONSEQUENTIAL DAMAGES ARISING OUT OF THE USE OF THIS
    SOFTWARE AND ITS DOCUMENTATION, EVEN IF THE AUTHORS OR ANY OF THE
    ABOVE PARTIES HAVE BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

    JORN LIND-NIELSEN SPECIFICALLY DISCLAIM ANY WARRANTIES, INCLUDING,
    BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND
    FITNESS FOR A PARTICULAR PURPOSE. THE SOFTWARE PROVIDED HEREUNDER IS
    ON AN "AS IS" BASIS, AND THE AUTHORS AND DISTRIBUTORS HAVE NO
    OBLIGATION TO PROVIDE MAINTENANCE, SUPPORT, UPDATES, ENHANCEMENTS, OR
    MODIFICATIONS.


%prep
%autosetup

%build
autoreconf --install
%configure
make %{?_smp_mflags}

%install
%make_install

%files
   %{_includedir}/bdd.h
   %{_includedir}/bvec.h
   %{_includedir}/fdd.h
   #%{_prefix}/lib/debug/usr/lib64/libbdd.so.0.0.0-2.4-1.git.79.5d36cc6.fc32.x86_64.debug
   /usr/lib/debug/usr/lib64/libbdd.so.*.debug
   %{_libdir}/libbdd.la
   %{_libdir}/libbdd.a
   %{_libdir}/libbdd.so
   %{_libdir}/libbdd.so.0
   %{_libdir}/libbdd.so.0.0.0

%changelog
* Tue Oct 20 2020 Jan Tusil <jenda.tusil@gmail.com> 2.4-1
- new package built with tito



