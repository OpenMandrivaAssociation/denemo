Summary:	WYSIWYG musical score editor and frontend for Lilypond
Name:		denemo
Version:	1.1.8
Release:	2
License:	GPLv2+
Group:		Sound
URL:		https://www.denemo.org/
Source0:	http://ftp.gnu.org/gnu/denemo/%{name}-%{version}.tar.gz
BuildRequires:	intltool
BuildRequires:	pkgconfig(aubio)
BuildRequires:	pkgconfig(evince-view-3.0)
BuildRequires:	pkgconfig(fftw3)
BuildRequires:	pkgconfig(fluidsynth)
BuildRequires:	pkgconfig(fontconfig)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(gtksourceview-3.0)
BuildRequires:	pkgconfig(guile-2.0)
BuildRequires:	pkgconfig(librsvg-2.0)
BuildRequires:	pkgconfig(rubberband)
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

%build
%configure \
	 --with-included-smf \
	 --enable-guile_2_0 \
	 --enable-gtk3
%make

%install
%makeinstall_std

desktop-file-install --vendor="" \
  --remove-category="Application" \
  --add-category="GTK" \
  --dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/*

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS ChangeLog NEWS
%{_bindir}/%{name}
%{_bindir}/cairo_svg2path
%{_bindir}/denemo_file_update
%{_bindir}/generate_source
%{_datadir}/appdata/denemo.appdata.xml
%{_datadir}/%{name}
%{_datadir}/fonts/truetype/%{name}/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

