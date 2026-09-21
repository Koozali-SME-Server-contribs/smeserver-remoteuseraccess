# $Id: smeserver-remoteuseraccess.spec,v 1.5 2021/08/23 07:42:21 terryfage Exp $
# Authority: dungog
# Name: Stephen Noble

Summary: Smeserver module to configure Shell and FTP access for individual users
%define name smeserver-remoteuseraccess
Name: %{name}
%define version 11.0.0
%define release 10
Version: %{version}
Release: %{release}%{?dist}
License: GNU GPL version 2
URL: http://www.dungog.net/sme
Group: Networking/Daemons
Source: %{name}-%{version}.tar.xz

BuildRoot: /var/tmp/e-smith-buildroot
BuildRequires: smeserver-devtools
BuildArchitectures: noarch
Requires: smeserver-release >= 7
Requires: smeserver-proftpd >= 1.12.0-6
Requires: smeserver-openssh >= 1.11.0-24
Requires: smeserver-formmagick >= 1.4.0-12
Requires: scponly
Obsoletes: dungog-proftpd-chroot
Obsoletes: e-smith-usershellaccess
Obsoletes: smeserver-sshkeys
AutoReqProv: no

%description
SME server enhancement to provide a server-manager panel under security
where you can enable shell access on a user by user basis.

Shells available bash, optionally with sudo
or scponly which allows scp, or using sshd for sftp only 

Also sets Chroots FTP access, VPN Client Access, 
and allows you to enter ssh keys  

%changelog
* Sun Sep 20 2026 Brian Read <brianr@koozali.org> 11.0.0-10.sme
- Update non en languages to align with en lex files, generate po files [SME: 13747]
- Update nl.po file specifically [SME: 13747]

* Mon Jul 20 2026 Brian Read <brianr@koozali.org> 11.0.0-9.sme
- Add UTF8 where needed in DB open calls [SME: 13666]

* Sun Jun 28 2026 Jean-Philippe Pialasse <jpp@koozali.org> 11.0.0-8.sme
- drop rssh support [SME: 12508]
- use scponly instead.but sftp-only from sshd could be an option

* Thu May 28 2026 Jean-Philippe Pialasse <jpp@koozali.org> 11.0.0-7.sme
- move panel translation; keeping those for user-manager panel

* Wed Feb 25 2026 Jean-Philippe Pialasse <jpp@koozali.org> 11.0.0-5.sme
- remove sm1 support except for user-manager panel 

* Wed Dec 03 2025 Brian Read <brianr@koozali.org> 11.0.0-4.sme
- Add a few enhancements to the panel - more shells, js to copy path to text, update .lex  [SME: 13372]

* Mon Dec 01 2025 Brian Read <brianr@koozali.org> 11.0.0-3.sme
- Finish conversion to SM2 [SME: 13179]

* Mon Oct 06 2025 Brian Read <brianr@koozali.org> 11.0.0-2.sme
- Add UTF8 and avoid potential DB caching problems [SME: 13209]

* Mon May 19 2025 Brian Read <brianr@koozali.org> 11.0.0-1.sme
- Add in SM2 panels

* Sun Sep 08 2024 fix-e-smith-pkg.sh by Trevor Batley <trevor@batley.id.au> 1.3-8.sme
- Fix e-smith references in smeserver-remoteuseraccess [SME: 12732]

* Sat Sep 07 2024 cvs2git.sh aka Brian Read <brianr@koozali.org> 1.3-7.sme
- Roll up patches and move to git repo [SME: 12338]

* Sat Sep 07 2024 BogusDateBot
- Eliminated rpmbuild "bogus date" warnings due to inconsistent weekday,
  by assuming the date is correct and changing the weekday.
  Sat Mar 07 2008 --> Sat Mar 01 2008 or Fri Mar 07 2008 or Sat Mar 08 2008 or ....
  Thu May 21 2008 --> Thu May 15 2008 or Wed May 21 2008 or Thu May 22 2008 or ....

* Mon Aug 23 2021 Terry Fage <terry.fage@gmail.com> 1.3-6.sme
- apply locale 2021-08-23 patch

* Wed Feb 24 2021 Jean-Philipe Pialasse <tests@pialasse.com> 1.3-5.sme
- fix encoding issue in table display [SME: 11396]

* Wed Feb 24 2021 Jean-Philipe Pialasse <tests@pialasse.com> 1.3-4.sme
- add empty -update event [SME: 11056]

* Mon Oct 26 2020 Brian Read <brianr@bjsystems.co.uk> 1.3-3.sme
- Initial import to SME10 tree [SME: 11056]

* Wed Mar 09 2016 JP Pialasse <tests@pialasse.com> 1.3-2.sme
- apply locale 2016-03-09 patch

* Tue Nov 12 2013 Daniel Berteaud <daniel@firewall-services.com> 1.3-1.sme
- Rebuild for SME9

* Sun Jul 14 2013 JP Pialasse <tests@pialasse.com> 1.2-38.sme
- apply locale 2013-07-14 patch

* Sun Mar 06 2011 SME Translation Server <translations@contribs.org> 1.2-37.sme
- apply locale 2011-03-06 patch

* Tue Mar 02 2010 SME Translation Server <translations@contribs.org> 1.2-36.sme
- apply locale 2010-03-02 patch

* Tue Oct 27 2009 SME Translation Server <translations@contribs.org> 1.2-35.sme
- apply locale 2009-10-27 patch

* Mon Aug 24 2009 SME Translation Server <translations@contribs.org> 1.2-34.sme
- apply locale 2009-08-24 patch

* Sat Jun 13 2009 Stephen Noble <support@dungog.net> 1.2-33
- chroot path not displayed in panel [SME: 5360]

* Mon Apr 27 2009 SME Translation Server <translations@contribs.org> 1.2-32
- apply locale 2009-04-27 patch

* Sun Mar  1 2009 Jonathan Martens <smeserver-contribs@snetram.nl> 1.2-30
- Apply  1 Mar 2009 locale patch [SME: 5018]

* Thu Jan  1 2009 Jonathan Martens <smeserver-contribs@snetram.nl> 1.2-29
- Apply  1 Jan 2009 locale patch [SME: 4900]

* Sun Nov 30 2008 Jonathan Martens <smeserver-contribs@snetram.nl> 1.2-28
- Apply 30 Nov 2008 locale patch

* Tue Oct 14 2008 Jonathan Martens <smeserver-contribs@snetram.nl> 1.2-27
- Apply 14 Oct 2008 locale patch

* Sat Sep 27 2008 Stephen Noble <support@dungog.net> - 1.2-26
- Apply locale patch

* Tue Jul 1 2008 Jonathan Martens <smeserver-contribs@snetram.nl> 1.2-25
- Apply 1 July 2008 locale patch

* Wed May 21 2008 Jonathan Martens <smeserver-contribs@snetram.nl> 1.2-24
  Thu May 21 2008 --> Thu May 15 2008 or Wed May 21 2008 or Thu May 22 2008 or ....
- Apply 21 May 2008 locale patch

* Mon May 5 2008 Jonathan Martens <smeserver-contribs@snetram.nl> 1.2-23
- Apply 5 May 2008 locale patch

* Sat Apr 26 2008 Jonathan Martens <smeserver-contribs@snetram.nl> 1.2-22
- Add common <base> tags to e-smith-formmagick's general

* Tue Apr 22 2008 Jonathan Martens <smeserver-contribs@snetram.nl> 1.2-21
- Forgot to apply patch

* Tue Apr 22 2008 Jonathan Martens <smeserver-contribs@snetram.nl> 1.2-20
- Apply 22 April 2008 locale patch

* Tue Apr 1 2008 Shad L. Lords <slords@mail.com> 1.2-19
- Update to UTF-8 translations

* Tue Mar 11 2008 Stephen Noble <support@dungog.net> - 1.2-18
- update locale 2008-03-11

* Sat Mar 07 2008 Stephen Noble <support@dungog.net> - 1.2-17
- prepare en lexicons for pootle translations

* Fri Jan 11 2008 Stephen Noble <support@dungog.net> 1.2-16
- remove duplicate event rssh.conf [SME 3470]

* Thu Dec 20 2007 Stephen Noble <support@dungog.net>
- french menu fix 1.2-14

* Thu Dec 20 2007 Stephen Noble <support@dungog.net>
- french translation, thanks Sylvain 1.2-13

* Wed Jun 13 2007 Stephen Noble <support@dungog.net>
- apply changes from 1.2-2 to 1.2-12

* Sun Apr 29 2007 Shad L. Lords <slords@mail.com>
- Clean up spec so package can be built by koji/plague

* Sun Feb 18 2007 Stephen Noble <support@dungog.net>
- swedish translation, thanks Chrille
- [1.2-12]

* Tue Jan 23 2007 Stephen Noble <support@dungog.net>
- spanish translation, thanks Gene
- requires e-smith-proftpd >= 1.12.0-6, custom template removed
- default set, ftp{ChrootDir} = home
- [1.2-11]

* Thu Dec 07 2006 Shad L. Lords <slords@mail.com>
- Update to new release naming.  No functional changes.
- Make Packager generic

* Thu Nov 23 2006 Stephen Noble <support@dungog.net>
- chroot path fix when home set [sme 2084]
- [1.2-10]

* Fri Nov 10 2006 Stephen Noble <support@dungog.net>
- fix textarea bug  [sme 1088]
- requires perl-CGI-FormMagick-0.92-08
- [1.2-9]

* Fri Nov 10 2006 Stephen Noble <support@dungog.net>
- chroot path fix [sme 2046]
- [1.2-8]

* Fri Nov 3 2006 Stephen Noble <support@dungog.net>
- german translation fix
- [1.2-7]

* Fri Aug 25 2006 Stephen Noble <support@dungog.net>
- empty chroot path defaults to home [sme 1249]
- [1.2-6]

* Thu Aug 24 2006 Stephen Noble <support@dungog.net>
- now finds correct sshkeys when used under userpanel
- [1.2-5]

* Wed May 10 2006 Stephen Noble <support@dungog.net>
- German translation fixed [sme 1258]
- [1.2-4]

* Wed May 10 2006 Stephen Noble <support@dungog.net>
- RSSH access uses VPNAccess property
- German translation added, thanks Dietmar
- [1.2-3]

* Mon Apr 24 2006 Stephen Noble <support@dungog.net> 
- Description Display fixed
- [1.2-2]

* Fri Apr 14 2006 Stephen Noble <support@dungog.net> 
- FormMagick Version
- [1.2-1]

* Thu Apr 13 2006 Stephen Noble <support@dungog.net> 
- merged sshkeys panel and functions
- [1.0-13]

* Wed Apr 12 2006 Stephen Noble <support@dungog.net> 
- possible fix for Insecure dependency on rc1
- [1.0-12]

* Wed Apr 12 2006 Stephen Noble <support@dungog.net> 
- option to set VPN Client Access
- uses user-modify event
- [1.0-11]

* Thu Feb 23 2006 Stephen Noble <support@dungog.net>
- proftp.conf/05chroot added as custom template for now
- defaults all users to ~/home
- Shell db settings changed was LoginShell
- [1.0-10]

* Thu Feb 23 2006 Stephen Noble <support@dungog.net>
- global/individual rssh clarified
- global reset removed
- chroot db settings changed
- [1.0-9]

* Tue Feb 21 2006 Stephen Noble <support@dungog.net>
- SME 7 pre3 version
- [1.0-8]

* Thu Aug 11 2005 Stephen Noble <support@dungog.net>
- SME 7 release
- [1.0-7]

* Sun Jul 17 2005 Stephen Noble <support@dungog.net>
- Merge of e-smith-usershellaccess & dungog-chroot-proftp
- original elements by Daniel van Raay & Damien Curtain
- [1.0-1]

%prep
%setup

mkdir -p root/etc/e-smith/events/smeserver-remoteuseraccess-update

%build
perl createlinks

LEXICONS=$(find root/etc/e-smith/{locale/,web/functions/} -type f )

for lexicon in $LEXICONS
do
    /sbin/e-smith/validate-lexicon $lexicon
done

LINKS=$(find root/etc/e-smith/locale/ -type d -maxdepth 1 | sed 's/root\/etc\/e-smith\/locale\///')
for link in $LINKS
do
 /bin/ln -s remoteuseraccess root/etc/e-smith/locale/$link/etc/e-smith/web/functions/userpanel-sshkeys
done

%install
rm -rf $RPM_BUILD_ROOT
(cd root   ; find . -depth -print | cpio -dump $RPM_BUILD_ROOT)
rm -f %{name}-%{version}-filelist
/sbin/e-smith/genfilelist $RPM_BUILD_ROOT > %{name}-%{version}-filelist
echo "%doc COPYING"          >> %{name}-%{version}-filelist

%clean
cd ..
rm -rf %{name}-%{version}

%pre
%preun
%post

%postun
#uninstalls not upgrades
if [ $1 = 0 ] ; then
 echo "uninstall"
fi

%files -f %{name}-%{version}-filelist
%defattr(-,root,root)
