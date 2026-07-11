%global tl_name vtable
%global tl_revision 51126

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	Vertical alignement of table cells
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/vtable
License:	mit
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/vtable.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/vtable.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package allows vertical alignement of table cell by providing: Z, L,
C, R, J and I column types \nextRow and \lb commands \setMultiColRow,
\setMultiColumn, \setMultiRow and \tableFormatedCell commands for
tabular and similar environment.

