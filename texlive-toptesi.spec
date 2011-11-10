# revision 24466
# category Package
# catalog-ctan /macros/latex/contrib/toptesi
# catalog-date 2011-10-30 23:05:47 +0100
# catalog-license lppl1.3
# catalog-version 5.59c
Name:		texlive-toptesi
Version:	5.59c
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
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

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

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/toptesi/topcoman.sty
%{_texmfdistdir}/tex/latex/toptesi/topfront.sty
%{_texmfdistdir}/tex/latex/toptesi/toptesi.cfg
%{_texmfdistdir}/tex/latex/toptesi/toptesi.cls
%{_texmfdistdir}/tex/latex/toptesi/toptesi.sty
%doc %{_texmfdistdir}/doc/latex/toptesi/FrontespiziAssemblati.pdf
%doc %{_texmfdistdir}/doc/latex/toptesi/LPPL.tex
%doc %{_texmfdistdir}/doc/latex/toptesi/README
%doc %{_texmfdistdir}/doc/latex/toptesi/manifest.txt
%doc %{_texmfdistdir}/doc/latex/toptesi/toptesi-doc-xetex-a.pdf
%doc %{_texmfdistdir}/doc/latex/toptesi/toptesi-doc-xetex-def.ps
%doc %{_texmfdistdir}/doc/latex/toptesi/toptesi-doc-xetex.pdf
%doc %{_texmfdistdir}/doc/latex/toptesi/toptesi-doc-xetex.tex
%doc %{_texmfdistdir}/doc/latex/toptesi/toptesi-example-xetex.pdf
%doc %{_texmfdistdir}/doc/latex/toptesi/toptesi-example-xetex.tex
%doc %{_texmfdistdir}/doc/latex/toptesi/toptesi-example.pdf
%doc %{_texmfdistdir}/doc/latex/toptesi/toptesi-example.tex
%doc %{_texmfdistdir}/doc/latex/toptesi/toptesi-example.xmpdata
%doc %{_texmfdistdir}/doc/latex/toptesi/toptesi.pdf
#- source
%doc %{_texmfdistdir}/source/latex/toptesi/toptesi.dtx
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
