%define version 0.8.12
%define rel	1	

Summary: 	WYSIWYG musical score editor and frontend for Lilypond
Name: 	 	denemo
Version: 	%{version}
Release: 	%mkrel %{rel}
Source0: 	http://download.savannah.gnu.org/releases/denemo/%{name}-%{version}.tar.gz
URL:     	http://www.denemo.org/
License: 	GPLv2+
Group:   	Sound
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires: 	lilypond
Requires: 	TiMidity++
Requires:	fluidsynth
Patch0:		denemo-0.8.8-fix-str-fmt.patch
BuildRequires:	gtk2-devel
BuildRequires:	libxml2-devel
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	gettext-devel
BuildRequires:	desktop-file-utils
BuildRequires:  cvs
BuildRequires:  aubio-devel
BuildRequires:  portaudio-devel
BuildRequires:  guile-devel
BuildRequires:  fftw-devel
BuildRequires:	libgtksourceview-2.0-devel

%description
Denemo is the GNU graphical musical score editor, and serves as a frontend
to Lilypond. Besides lilypond, it can also export music into ABC format.
as well as handling Csound score files playback and MIDI playback.

%prep
%setup -q -n %{name}-%{version}
%patch0 -p0

%build
%configure2_5x \
	--sysconfdir=%{_sysconfdir} \
	--enable-gtk2 \
	--with-plugins=analysis

%make

%install
rm -rf %{buildroot}
%makeinstall_std

# remove unneeded files
rm -fr %{buildroot}/%_includedir
rm -f %{buildroot}%{_libdir}/%{name}/*.{a,la}

#menu

desktop-file-install --vendor="" \
  --remove-category="Application" \
  --add-category="GTK" \
  --dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/*


%find_lang %name

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post
%update_menus
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%endif

%files -f %name.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog NEWS README*
%{_bindir}/%{name}
%{_bindir}/smfsh
%config(noreplace) %{_sysconfdir}/%{name}
%{_datadir}/%{name}
%{_datadir}/fonts/truetype/%{name}/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png




