%global tl_name easyformat
%global tl_revision 44543

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.4.0
Release:	%{tl_revision}.1
Summary:	Easily add boldface, italics and smallcaps
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/easyformat
License:	gpl3+
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/easyformat.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/easyformat.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package allows the use of underscores and circumflexes to begin
resp. end italic, bold or SMALLCAPS formatting, as an alternative to the
standard LaTeX \textit{...}, \textbf{...} and/or \textsc{...}. The
meaning of underscore and circumflex in mathmode remain the same.

