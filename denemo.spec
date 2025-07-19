# Avoid conflicts with lilypond fonts
%global	__provides_exclude 'font\\\(.*\\\)|font\\\(:lang=.*\\\)'

Summary:	WYSIWYG musical score editor and frontend for Lilypond
Name:	denemo
Version:	2.6.0
Release:	1
License:	GPLv2+
Group:		Sound
Url:		https://www.denemo.org/
Source0:	https://ftp.gnu.org/gnu/denemo/%{name}-%{version}.tar.gz
#Source0:	%%{name}-%%{version}.tar.xz
Source1:	docs_denemomanual.pdf
#Source100:	denemo.rpmlintrc
Patch0:	denemo-2.6.0-fix-desktop-file.patch
Patch1:	denemo-2.6.0-fix-includes.patch
Patch2:	denemo-2.6.0-add-missing-type-specifier.patch
BuildRequires:	bison
BuildRequires:	chrpath
#BuildRequires:	desktop-file-utils
BuildRequires:	flex
BuildRequires:	gettext
BuildRequires:	gtk-doc
BuildRequires:	gtk-doc-mkpdf
BuildRequires:	guile22
BuildRequires:	guile22-runtime
BuildRequires:	intltool
BuildRequires:	libmusicxml-devel
BuildRequires:	pkgconfig(aubio)
BuildRequires:	pkgconfig(cairo)
BuildRequires:	pkgconfig(dbus-1)
BuildRequires:	pkgconfig(evince-view-3.0)
BuildRequires:	pkgconfig(fftw3)
BuildRequires:	pkgconfig(fluidsynth)
BuildRequires:	pkgconfig(fontconfig)
BuildRequires:	pkgconfig(freetype2)
BuildRequires:	pkgconfig(gthread-2.0) >= 2.10.0
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(gtksourceview-3.0)
BuildRequires:	pkgconfig(guile-2.2)
BuildRequires:	pkgconfig(jack)
BuildRequires:	pkgconfig(libinstpatch-1.0)
BuildRequires:	pkgconfig(librsvg-2.0)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(mount)
BuildRequires:	pkgconfig(opus)
BuildRequires:	pkgconfig(portaudio-2.0)
BuildRequires:	pkgconfig(portmidi)
BuildRequires:	pkgconfig(libpipewire-0.3)
BuildRequires:	pkgconfig(rubberband) >= 1.0.8
BuildRequires:	pkgconfig(samplerate)
#BuildRequires:	pkgconfig(smf) >= 1.3
BuildRequires:	pkgconfig(sndfile) >= 1.0
BuildRequires:	pkgconfig(uuid)
BuildRequires:	pkgconfig(x11)
Requires:	fluidsynth
Requires:	lilypond
Requires:	playmidi
# For EvinceDocument pdf
Recommends:		evince

%description
Denemo is the GNU graphical musical score editor, and serves as a front-end
to Lilypond. Besides Lilypond, it can also export music into ABC format.
as well as handling Csound score files playback and MIDI playback.

%files -f %{name}.lang
%doc AUTHORS ChangeLog NEWS
%doc docs_denemomanual.pdf
%{_bindir}/%{name}
%{_bindir}/annotator
%{_bindir}/cairo_svg2path
%{_bindir}/%{name}_file_update
%{_bindir}/pageswitcher
%{_bindir}/pageturner
%{_bindir}/twopageturner
#{_bindir}/generate_source
%{_datadir}/appdata/org.%{name}.Denemo.appdata.xml
%{_datadir}/%{name}
%{_datadir}/fonts/truetype/%{name}/*.ttf
%{_datadir}/gtk-doc/html/%{name}
%{_datadir}/applications/org.%{name}.Denemo.desktop
%{_datadir}/pixmaps/org.%{name}.Denemo.png

#-----------------------------------------------------------------------------

%prep
%autosetup -p1

find docs/images -name "*.png" |xargs chmod 644
find docs  -size 0 -delete

install -m 0644 %{SOURCE1} .


%build
autoreconf -vfi
%configure \
	--disable-static \
	--enable-aubio \
	--enable-alsa \
	--enable-jack \
	--enable-fluidsynth \
	--enable-portaudio \
	--enable-portmidi \
	--enable-rubberband \
	--enable-gtk3 \
	--enable-evince \
	--enable-doc \
	--enable-gtk-doc \
	--enable-gtk-doc-html \
	--enable-guile_2_2

%make_build

chmod 644 actions/*.scm
chrpath -d src/%{name}


%install
%make_install

%if 0
desktop-file-install --vendor="" \
  --remove-category="Application" \
  --add-category="GTK" \
  --dir %{buildroot}%{_datadir}/applications 
  %{buildroot}%{_datadir}/applications/*
%endif
  
%find_lang %{name}
