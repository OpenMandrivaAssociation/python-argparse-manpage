%undefine _debugsource_packages
Name:		python-argparse-manpage
Version:	4.5
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/a/argparse-manpage/argparse-manpage-%{version}.tar.gz
Summary:	Build manual page from python's ArgumentParser object
URL:		https://pypi.org/project/argparse-manpage/
License:	Apache-2.0
Group:		Development/Python
BuildRequires:	python%{pyver}dist(pip)
BuildArch:	noarch

%description
Build manual page from python's ArgumentParser object.

%prep
%autosetup -p1 -n argparse-manpage-%{version}

%build
%py_build

%install
%py_install

%files
%{_bindir}/*
%{py_sitedir}/argparse_manpage
%{py_sitedir}/build_manpages
%{py_sitedir}/argparse_manpage-*.*-info
%{_mandir}/man1/*
