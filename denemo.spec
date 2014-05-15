%define Werror_cflags %nil
Summary:	WYSIWYG musical score editor and frontend for Lilypond
Name:		denemo
Version:	1.0.2
Release:	1
License:	GPLv2+
Group:		Sound
URL:		http://www.denemo.org/HomePage
Source0:	http://ftp.gnu.org/gnu/denemo/%{name}-%{version}.tar.gz
BuildRequires:	pkgconfig(aubio)
BuildRequires:	pkgconfig(evince-view-3.0)
BuildRequires:	pkgconfig(fftw3)
BuildRequires:	pkgconfig(fluidsynth)
BuildRequires:	pkgconfig(fontconfig)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(gtksourceview-3.0)
BuildRequires:	pkgconfig(guile-1.8)
BuildRequires:	pkgconfig(librsvg-2.0)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(portaudio-2.0)
BuildRequires:	pkgconfig(samplerate)
BuildRequires:	portmidi-devel
BuildRequires:	desktop-file-utils
Requires:	fluidsynth
Requires:	lilypond
Requires:	playmidi
Requires:	TiMidity++

%description
Denemo is the GNU graphical musical score editor, and serves as a frontend
to Lilypond. Besides lilypond, it can also export music into ABC format.
as well as handling Csound score files playback and MIDI playback.

%prep
%setup -q
# fix debug linting
chmod a-x src/portmidiutil.h
chmod a-x src/portmidiutil.c



%build
%configure2_5x --disable-static --with-included-smf 
perl -pi -e "s|-lporttime||" src/Makefile
%make

%install
%makeinstall_std

desktop-file-install --vendor="" \
  --remove-category="Application" \
  --add-category="GTK" \
  --dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/*




%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS ChangeLog NEWS README*
%{_bindir}/%{name}
%{_bindir}/denemo_file_update.sh
%config(noreplace) %{_sysconfdir}/%{name}
%{_datadir}/%{name}
%{_datadir}/fonts/truetype/%{name}/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png