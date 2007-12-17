%define version 0.7.6
#define beta beta1
%{?beta:%global release %mkrel -c %beta 1}
%{?!beta:%global release %mkrel 1}

Summary: 	WYSIWYG musical score editor and frontend for Lilypond
Name: 	 	denemo
Version: 	%{version}
Release: 	%{release}
Source0: 	http://prdownloads.sourceforge.net/%{name}/%{name}-%{version}%{?beta:%beta}.tar.bz2
Patch0:		denemo-0.7.4-gettext.patch
Patch1:		denemo-0.7.3-plugin-option.patch
URL:     	http://denemo.sourceforge.net/
License: 	GPL
Group:   	Sound
Requires: 	lilypond
BuildRequires:	gtk2-devel
BuildRequires:	libxml2-devel
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	automake1.8
BuildRequires:	gettext-devel
BuildRequires:	desktop-file-utils
BuildRequires:  cvs

%description
Denemo is the GNU graphical musical score editor, and serves as a frontend
to Lilypond. Besides lilypond, it can also export music into ABC format.
as well as handling Csound score files playback and MIDI playback.

%prep
%setup -q -n %{name}-%{version}%{?beta:%beta}
%patch0 -p1 -b .gettext
%patch1 -p1 -b .plugin

# regen everything because of patch
ACLOCAL=aclocal-1.8 AUTOMAKE=automake-1.8 autoreconf --force --install


%build
%configure2_5x \
	--sysconfdir=%{_sysconfdir}/%{name} \
	--enable-gtk2 \
	--with-plugins=analysis

%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

# remove unneeded files
rm -fr $RPM_BUILD_ROOT/%_includedir
rm -f $RPM_BUILD_ROOT%{_libdir}/%{name}/*.{a,la}

#menu
mkdir -p $RPM_BUILD_ROOT%{_menudir}
cat << EOF > $RPM_BUILD_ROOT%{_menudir}/%{name}
?package(%{name}): \
 command="%{name}" \
 icon="sound_section.png" \
 needs="x11" \
 title="Denemo" \
 longtitle="Musical score editor" \
 section="Multimedia/Sound" \
 xdg="true"
EOF

desktop-file-install --vendor="" \
  --remove-category="Application" \
  --add-category="GTK" \
  --add-category="X-Mandrakelinux-Multimedia-Sound" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/*

# remove unneeded files

%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_menus

%postun
%clean_menus

%files -f %name.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog DESIGN* GOALS NEWS README* TODO
%{_bindir}/%{name}
#%config(noreplace) %{_sysconfdir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_libdir}/%{name}
%{_menudir}/%{name}
%{_iconsdir}/%{name}.png



