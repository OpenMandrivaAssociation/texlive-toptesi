%global tl_name toptesi
%global tl_revision 73464

Name:		texlive-%{tl_name}
Epoch:		1
Version:	6.4.07
Release:	%{tl_revision}.1
Summary:	Bundle for typesetting multilanguage theses
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/toptesi
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/toptesi.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/toptesi.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/toptesi.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This bundle contains everything needed for typesetting a bachelor,
master, or PhD thesis in Italian (or in any other language supported by
LaTeX: the bundle is constructed to support multilingual use). The infix
strings may be selected and specified at will by means of a
configuration file, so as to customize the layout of the front page to
the requirements of a specific university. Thanks to its language
management, the bundle is suited for multilanguage theses that are
becoming more and more frequent thanks to the double degree programs of
the European Community Socrates programs. Toptesi is designed to save
the PDF version of a thesis in PDF/A-1b compliant mode and with all the
necessary metadata.

