Name:		texlive-toptesi
Version:	6.1.12
Release:	1
Summary:	Bundle of files for typsetting theses
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/toptesi
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/toptesi.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/toptesi.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/toptesi.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This bundle contains everything is needed for typesetting a
bachelor, master or PhD thesis in Italian (or in any other
language supported by LaTeX: the bundle is constructed to
support multilingual use). The infix strings may be selected
and specified at will by means of a configuration file, so as
to customize the layout of the front page to the requirements
of a specific university. Thanks to its language management,
the bundle is suited for multilanguage theses that are becoming
more and more frequent thanks to the double degree programs of
the European Community Socrates programs. Toptesi is designed
to save the PDF version of a thesis in PDF/A-1b compliant mode
and with all the necessary metadata.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/toptesi
%doc %{_texmfdistdir}/doc/latex/toptesi
#- source
%doc %{_texmfdistdir}/source/latex/toptesi

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
