%undefine _debugsource_packages
%define module argparse-manpage
%define oname argparse_manpage

Name:		python-argparse-manpage
Version:	4.7
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/a/%{module}/%{oname}-%{version}.tar.gz#/%{name}-%{version}.tar.gz
Summary:	Build manual page from python's ArgumentParser object
URL:		https://pypi.org/project/argparse-manpage/
License:	Apache-2.0
Group:		Development/Python
BuildSystem:	python
BuildArch:	noarch
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(packaging)
BuildRequires:	python%{pyver}dist(wheel)

%description
Build manual page from python's ArgumentParser object.

%prep -a
# Remove bundled egg-info
rm -rf %{oname}.egg-info

%files
%{_bindir}/*
%{py_sitedir}/build_manpages
%{py_sitedir}/%{oname}
%{py_sitedir}/%{oname}-%{version}.dist-info
%{_mandir}/man1/*
