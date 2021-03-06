%define with_extra_symlinks 1

%if 0%{?suse_version} || 0%{?fedora} > 19
%define fixes_only 1
# For openSUSE 12.2 we only need the extra dependencies, no files
%if 0%{?suse_version} && 0%{?suse_version} < 1220
%define with_extra_symlinks 0
%endif
%endif

Name:           devscripts
Version:        2.12.6
Release:        0
License:        GPL-2.0+ and GPL-2.0 and GPL-3.0+ and GPL-3.0 and Artistic-2.0 and GPL-1.0+ or Artistic-1.0 and Public-Domain
Summary:        Scripts to make the life of a Debian Package maintainer easier
Url:            http://alioth.debian.org/projects/devscripts
%if 0%{?suse_version}
Group:          Development/Tools/Building
%else
Group:          Development/System
%endif
Source:         http://cdn.debian.net/debian/pool/main/d/devscripts/devscripts_%{version}.tar.gz
Source1:        README.fixes
# Patches auto-generated by git-buildpackage:
Patch0:     0001-Add-.gitignore.patch
Patch1:     0002-Makefile-Fix-install-layout-and-prefix.patch
Patch2:     0003-Makefile-configurable-xsl-stylesheet-path-for-manpag.patch
Patch3:     0004-Makefile-disable-manpage-translations.patch
Patch4:     0005-Makefile-fix-permissions-of-README-file.patch
Patch5:     0006-compatibility-remove-desktop2menu-tool.patch
Patch6:     0007-compatibility-disable-more-tools.patch
Patch7:     0008-Disable-tests.patch
Patch8:     0009-Fedora-HACK-fix-debchange.patch
Patch9:     0010-Fedora-enable-debchange-alias-dch.patch
Patch10:    0011-Fix-pod2man-error-with-newer-perl.patch
%if ! 0%{?fixes_only}
BuildRequires:  libxslt
BuildRequires:  python-setuptools
%if  0%{?fedora} && 0%{?fedora} < 19
BuildRequires:  docbook-xsl-stylesheets
%else
BuildRequires:  docbook-style-xsl
%endif
BuildRequires:  perl(Date::Parse)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(Pod::Checker)
%if 0%{?fedora}
%if 0%{?fedora} < 19
BuildRequires:  dpkg-devel
%else
BuildRequires:  dpkg-dev
BuildRequires:  dpkg-perl
Requires:       dpkg-dev
%endif
%endif
Requires:       dpkg
%endif
Requires:       perl(Date::Parse)
Requires:       perl(LWP::UserAgent)

%if 0%{?suse_version}
%define _man_xsl_stylesheet /usr/share/xml/docbook/stylesheet/nwalsh/current/manpages/docbook.xsl
%else
%define _man_xsl_stylesheet /usr/share/sgml/docbook/xsl-stylesheets/manpages/docbook.xsl
%endif

%description
Contains the following scripts, dependencies/recommendations shown in
brackets afterwards:
 - annotate-output: run a command and prepend time and stream (O for stdout,
   E for stderr) for every line of output
 - archpath: print tla/Bazaar package names [tla | bazaar]
 - bts: a command-line tool for manipulating the BTS [www-browser,
   libauthen-sasl-perl, libnet-smtp-ssl-perl, libsoap-lite-perl, libwww-perl,
   bsd-mailx | mailx]
 - build-rdeps: Searches for all packages that build-depend on a
   given package [dctrl-tools]
 - chdist: tool to easily play with several distributions [dctrl-tools]
 - checkbashisms: check whether a /bin/sh script contains any common
   bash-specific contructs
 - cowpoke: upload a Debian source package to a cowbuilder host and build it,
   optionally also signing and uploading the result to an incoming queue
   [ssh-client]
 - cvs-debi, cvs-debc: wrappers around debi and debc respectively (see below)
   which allow them to be called from the CVS working directory.
   [cvs-buildpackage]
 - cvs-debrelease: wrapper around debrelease which allows it to be called
   from the CVS working directory. [cvs-buildpackage, dupload | dput,
   ssh-client]
 - cvs-debuild: A wrapper for cvs-buildpackage to use debuild as its package
   building program. [cvs-buildpackage, fakeroot, lintian, gnupg]
 - dcmd: run a given command replacing the name of a .changes or .dsc file
   with each of the files referenced therein
 - dcontrol: remotely query package and source control files for all Debian
   distributions. [liburl-perl, libwww-perl]
 - dd-list: given a list of packages, pretty-print it ordered by maintainer
 - debc: display the contents of just-built .debs
 - debchange/dch: automagically add entries to debian/changelog files
   [libparse-debcontrol-perl, libsoap-lite-perl]
 - debcheckout: checkout the development repository of a Debian package
 - debclean: purge a Debian source tree [fakeroot]
 - debcommit: commit changes to cvs, darcs, svn, svk, tla, bzr, git, or hg,
   basing commit message on changelog
   [cvs | darcs | subversion | svk | tla | bzr | git-core | mercurial]
 - debdiff: compare two versions of a Debian package to check for
   added and removed files [wdiff, patchutils]
 - debi: install a just-built package
 - debpkg: dpkg wrapper to be able to manage/test packages without su
 - debrelease: wrapper around dupload or dput [dupload | dput, ssh-client]
 - debsign, debrsign: sign a .changes/.dsc pair without needing any of
   the rest of the package to be present; can sign the pair remotely
   or fetch the pair from a remote machine for signing [gnupg,
   debian-keyring, ssh-client]
 - debsnap: grab packages from http://snapshot.debian.org [libwww-perl,
   libjson-perl]
 - debuild: wrapper to build a package without having to su or worry
   about how to invoke dpkg to build using fakeroot.  Also deals
   with common environment problems, umask etc. [fakeroot,
   lintian, gnupg]
 - deb-reversion: increases a binary package version number and repacks the
   archive
 - dep3changelog: generate a changelog entry from a DEP3-style patch header
 - desktop2menu: produce a skeleton menu file from a freedesktop.org
   desktop file [libfile-desktopentry-perl]
 - dget: downloads Debian source and binary packages [wget | curl]
 - dpkg-depcheck, dpkg-genbuilddeps: determine the packages used during
   the build of a Debian package; useful for determining the Build-Depends
   control field needed [build-essential, strace]
 - diff2patches: extract patches from a .diff.gz file placing them  under
   debian/ or, if present, debian/patches [patchutils]
 - dscextract: extract a single file from a Debian source package [patchutils]
 - dscverify: verify the integrity of a Debian package from the
   .changes or .dsc files [gnupg, debian-keyring, libdigest-md5-perl]
 - edit-patch: add/edit a patch for a source package and commit the changes
   [quilt | dpatch | cdbs]
 - getbuildlog: download package build logs from Debian auto-builders [wget]
 - grep-excuses: grep the update_excuses.html file for your packages
   [libterm-size-perl, wget, w3m]
 - licensecheck: attempt to determine the license of source files
 - list-unreleased: searches for unreleased packages
 - manpage-alert: locate binaries without corresponding manpages [man-db]
 - mass-bug: mass-file bug reports [bsd-mailx | mailx]
 - mergechanges: merge .changes files from a package built on different
   architectures
 - mk-build-deps: Given a package name and/or control file, generate a binary
   package which may be installed to satisfy the build-dependencies of the
   given packages. [equivs]
 - namecheck: Check project names are not already taken.
 - nmudiff: mail a diff of the current package against the previous version
   to the BTS to assist in tracking NMUs [patchutils, mutt]
 - plotchangelog: view a nice plot of the data in a changelog file
   [libtimedate-perl, gnuplot]
 - pts-subscribe: subscribe to the PTS for a limited period of time
   [bsd-mailx | mailx, at]
 - rc-alert: list installed packages which have release-critical bugs [wget]
 - rmadison: remotely query the Debian archive database about packages
   [wget | curl, liburi-perl]
 - suspicious-source: output a list of files which are not common source
   files [python-magic]
 - svnpath: print svn repository paths [subversion]
 - tagpending: runs from a Debian source tree and tags bugs that are to
   be closed in the latest changelog as pending. [libsoap-lite-perl]
 - transition-check: Check a list of source packages for involvement in
   transitions for which uploads to unstable are currently blocked
   [libwww-perl, libyaml-syck-perl]
 - uscan: scan upstream sites for new releases of packages
   [libcrypt-ssleay-perl, libwww-perl, unzip, xz-utils]
 - uupdate: integrate upstream changes into a source package [patch]
 - what-patch: determine what patch system, if any, a source package is using
   [patchutils]
 - whodepends: check which maintainers' packages depend on a package
 - who-uploads: determine the most recent uploaders of a package to the Debian
   archive [gnupg, debian-keyring, wget]
 - wnpp-alert: list installed packages which are orphaned or up for
   adoption [wget]
 - wnpp-check: check whether there is an open request for packaging or
   intention to package bug for a package [wget]
 - wrap-and-sort: wrap long lines and sort items in packaging files
   [python-debian]

Also included are a set of example mail filters for filtering mail
from Debian mailing lists using exim, procmail, etc.

%if 0%{?fixes_only}
%package fixes
License:        GPL-2.0+
Summary:        Fixes for Debian devscripts
Requires:       devscripts
Requires:       perl(Date::Parse)
Requires:       perl(LWP::UserAgent)

%description fixes
Provides missing symlinks and requirements for Debian devscripts.

%endif


%prep
%setup -q
# 0001-Add-.gitignore.patch
%patch0 -p1
# 0002-Makefile-Fix-install-layout-and-prefix.patch
%patch1 -p1
# 0003-Makefile-configurable-xsl-stylesheet-path-for-manpag.patch
%patch2 -p1
# 0004-Makefile-disable-manpage-translations.patch
%patch3 -p1
# 0005-Makefile-fix-permissions-of-README-file.patch
%patch4 -p1
# 0006-compatibility-remove-desktop2menu-tool.patch
%patch5 -p1
# 0007-compatibility-disable-more-tools.patch
%if 0%{?fedora_version}
%patch6 -p1
%endif
# 0008-Disable-tests.patch
%patch7 -p1
# 0009-Fedora-HACK-fix-debchange.patch
%if 0%{?fedora_version} && 0%{?fedora_version} < 19
%patch8 -p1
%endif
# 0010-Fedora-enable-debchange-alias-dch.patch
%if 0%{?fedora_version}
%patch9 -p1
%endif
# 0011-Fix-pod2man-error-with-newer-perl.patch
%patch10 -p1
cp %{SOURCE1} .


%build
%if ! 0%{?fixes_only}
make %{?_smp_mflags} \
    DOCDIR=%{_docdir}/%{name} \
    MAN_XSL_STYLESHEET=%{_man_xsl_stylesheet}
%endif


%install
%if ! 0%{?fixes_only}
%make_install \
    DOCDIR=%{_docdir}/%{name} \
    MAN_XSL_STYLESHEET=%{_man_xsl_stylesheet}
%endif

# Create symlinks for binaries
%if %{with_extra_symlinks}
install -d %{buildroot}%{_bindir}
ln -s cvs-debi %{buildroot}%{_bindir}/cvs-debc
ln -s debchange %{buildroot}%{_bindir}/dch
ln -s debi %{buildroot}%{_bindir}/debc
ln -s pts-subscribe %{buildroot}%{_bindir}/pts-unsubscribe
%endif


%if ! 0%{?fixes_only}
%files
%defattr(-,root,root)
%doc debian/copyright
%{_bindir}/*
%{_prefix}/lib/%{name}
%{python_sitelib}/%{name}/
%{python_sitelib}/%{name}-*.egg-info/
%{_datadir}/%{name}
%doc %{_docdir}/%{name}
%doc %{_mandir}/man1/*
%config %{_sysconfdir}/bash_completion.d

%else

%files fixes
%defattr(-,root,root)
%doc README.fixes
%if %{with_extra_symlinks}
%{_bindir}/*
%endif

%endif
