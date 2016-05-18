Name:           devilspie2
Version:        0.41 
Release:        1%{?dist}
Summary:        A window-matching utility 

Group:          User Interface/X
License:        GPLv3+
URL:            http://www.gusnan.se/devilspie2   
Source0:        http://download.savannah.gnu.org/releases/devilspie2/devilspie2_%{version}-src.tar.gz 
BuildRequires:  pkgconfig gtk3-devel lua-devel glib2-devel libwnck3-devel gettext

%global _hardened_build 1

%description

%{name} is a window matching utility, allowing the user to perform
scripted actions on windows as they are created. For example you can
script a terminal program to always be positioned at a specific screen
position, or position a window on a specific workspace.
.
It is a continuation of Ross Burtons project Devilspie, with the most
significant change that the symbolic expressions of that project are
replaced with a LUA interpreter..

%prep

%setup -q

%build

make PREFIX=%{_prefix} %{?_smp_mflags}

%install

%make_install PREFIX=%{_prefix}

install -dm 755 %{buildroot}/%{_mandir}/man1
install -m 644 %{name}.1 -t %{buildroot}/%{_mandir}/man1

%find_lang %{name}

%clean

rm -rf %{buildroot}

%files -f %{name}.lang

%doc README INSTALL ChangeLog AUTHORS
%{_bindir}/%{name}
%{_mandir}/man1/*

%changelog

* Wed May 11 2016 Daniel Miranda
- Update to latest upstream version
* Sun Oct 12 2014 Daniel Miranda
- Update to latest upstream version
* Sat Sep 27 2014 Daniel Miranda
- Update to latest upstream version
* Thu Dec 26 2013 Daniel Miranda
- Initial Packaging
