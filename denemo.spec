%define version 0.8.2
#define beta beta1
%{?beta:%global release %mkrel -c %beta 1}
%{?!beta:%global release %mkrel 2}

Summary: 	WYSIWYG musical score editor and frontend for Lilypond
Name: 	 	denemo
Version: 	%{version}
Release: 	%{release}
Source0: 	http://download.savannah.gnu.org/releases/%{name}/%{name}-%{version}%{?beta:%beta}.tar.gz
#Patch0:		denemo-0.7.4-gettext.patch
URL:     	http://www.denemo.org/
License: 	GPLv2+
Group:   	Sound
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires: 	lilypond
Requires: 	TiMidity++
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

%description
Denemo is the GNU graphical musical score editor, and serves as a frontend
to Lilypond. Besides lilypond, it can also export music into ABC format.
as well as handling Csound score files playback and MIDI playback.

%prep
%setup -q -n %{name}-%{version}%{?beta:%beta}
#%patch0 -p1 -b .gettext

# regen everything because of patch
#ACLOCAL=aclocal-1.8 AUTOMAKE=automake-1.8 autoreconf --force --install

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
%config(noreplace) %{_sysconfdir}/%{name}
%{_datadir}/%{name}
%{_datadir}/fonts/truetype/%{name}/Denemo.ttf
%{_datadir}/applications/%{name}.desktop
%{_iconsdir}/%{name}.png




