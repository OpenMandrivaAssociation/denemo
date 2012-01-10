Summary:	WYSIWYG musical score editor and frontend for Lilypond
Name:		denemo
Version:	0.9.2
Release:	%mkrel 1
Source0:	ftp://ftp.gnu.org/gnu/denemo/%{name}-%{version}.tar.gz
Patch0:		denemo-0.9.2-fix-str-fmt.patch
Patch1:		denemo-0.9.2-glib.patch
URL:		http://www.denemo.org/
License:	GPLv2+
Group:		Sound
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires:	lilypond
Requires:	TiMidity++
Requires:	playmidi
Requires:	fluidsynth
BuildRequires:	gtk2-devel
BuildRequires:	libxml2-devel
BuildRequires: 	libfluidsynth-devel
BuildRequires:	bison
BuildRequires:	librsvg-devel
BuildRequires:	flex
BuildRequires:	gettext-devel
BuildRequires:	desktop-file-utils
BuildRequires:	cvs
BuildRequires:	aubio-devel
BuildRequires:	portaudio-devel
BuildRequires:	guile-devel
BuildRequires:	fftw-devel
BuildRequires:	libgtksourceview-2.0-devel

%description
Denemo is the GNU graphical musical score editor, and serves as a frontend
to Lilypond. Besides lilypond, it can also export music into ABC format.
as well as handling Csound score files playback and MIDI playback.

%prep
%setup -q
%patch0 -p0
%patch1 -p0

%build
%configure2_5x --with-included-smf
%make

%install
rm -rf %{buildroot}
%makeinstall_std

rm -fr %{buildroot}/%{_includedir}
rm -f %{buildroot}%{_libdir}/%{name}/*.{a,la}

desktop-file-install --vendor="" \
  --remove-category="Application" \
  --add-category="GTK" \
  --dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/*
%find_lang %name

%clean
rm -rf %{buildroot}

%files -f %name.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog NEWS README*
%{_bindir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}
%{_datadir}/%{name}
%{_datadir}/fonts/truetype/%{name}/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

