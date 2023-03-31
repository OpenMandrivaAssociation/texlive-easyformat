Name:		texlive-easyformat
Version:	44543
Release:	2
Summary:	Easily add boldface, italics and smallcaps
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/easyformat
License:	gpl3+
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/easyformat.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/easyformat.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package allows the use of underscores and circumflexes to
begin resp. end italic, bold or SMALLCAPS formatting, as an
alternative to the standard LaTeX \textit{...}, \textbf{...}
and/or \textsc{...}. The meaning of underscore and circumflex
in mathmode remain the same.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/easyformat
%doc %{_texmfdistdir}/doc/latex/easyformat

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
