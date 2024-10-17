Name:		texlive-vtable
Version:	51126
Release:	2
Summary:	Vertical alignement of table cells
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/vtable
License:	mit
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/vtable.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/vtable.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package allows vertical alignement of table cell by
providing: Z, L, C, R, J and I column types \nextRow and \lb
commands \setMultiColRow, \setMultiColumn, \setMultiRow and
\tableFormatedCell commands for tabular and similar
environment.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/vtable
%doc %{_texmfdistdir}/doc/latex/vtable

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
