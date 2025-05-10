Name:           dmz-cursor-theme
Version:        0.4.5.2
Release:        1
Summary:        Style neutral cursors themes
License:        CC-BY-SA-3.0
URL:            https://packages.debian.org/sid/dmz-cursor-theme
Source0:        http://ftp.debian.org/debian/pool/main/d/dmz-cursor-theme/dmz-cursor-theme_%{version}.tar.xz
Patch0:         dmz-cursor-theme-symbolic-links.patch
Patch1:         dmz-cursor-theme-name.patch
BuildArch:      noarch
BuildRequires:  xcursorgen

%description
Scalable, style-neutral cursor themes based on the Industrial cursors designed
by Jakub Steiner for the Ximian GNOME Desktop.

%prep
%autosetup -p1 -n dmz-cursor-theme-%{version}

%build
for color in White Black; do
    cd %{_builddir}/dmz-cursor-theme-%{version}/DMZ-$color/pngs
    ./make.sh
done

%install
for color in White Black; do
    install -d %{buildroot}%{_datadir}/icons/DMZ-$color/cursors
    install -m644 DMZ-$color/cursor.theme %{buildroot}%{_datadir}/icons/DMZ-$color/
    install -m644 DMZ-$color/index.theme %{buildroot}%{_datadir}/icons/DMZ-$color/
    install -m644 DMZ-$color/xcursors/* -t %{buildroot}%{_datadir}/icons/DMZ-$color/cursors/
done

%files
%doc debian/copyright
%{_datadir}/icons/DMZ-White/
%{_datadir}/icons/DMZ-Black/
