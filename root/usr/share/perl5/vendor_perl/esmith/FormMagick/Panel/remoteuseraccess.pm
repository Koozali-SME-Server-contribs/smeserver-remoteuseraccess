#----------------------------------------------------------------------
#  remoteuseraccess.pm
#  support@dungog.net
#----------------------------------------------------------------------

package esmith::FormMagick::Panel::remoteuseraccess;

use strict;
use warnings;

use esmith::util;
use esmith::FormMagick;
use esmith::AccountsDB;
use esmith::ConfigDB;

use Exporter;
use Carp qw(verbose);

use HTML::Tabulate;

our @ISA = qw(esmith::FormMagick Exporter);

our @EXPORT = qw();

our $db  = esmith::ConfigDB->open();
our $adb = esmith::AccountsDB->open();

our $PanelUser = $ENV{'REMOTE_USER'} ||'';
$PanelUser = $1 if ($PanelUser =~ /^([a-z][\-a-z0-9]*)$/);

sub new {
    shift;
    my $self = esmith::FormMagick->new();
    $self->{calling_package} = (caller)[0];
    bless $self;
    return $self;
}

#server-manager functions
sub user_accounts_exist
{
    return scalar $adb->users;
}

sub print_table
{
    my $self = shift;
    my $q = $self->{cgi};

    my $user_table =
    {
       title => $self->localise('USER_LIST_CURRENT'),

       stripe => '#D4D0C8',

       fields => [ qw(User FullName shell sudo keys chroot vpn Modify) ],

       labels => 1,

       field_attr => {
                       User          => {
                                           label_escape => 0,
                                           label => $self->localise('ACCOUNT')
                                        },
                       FullName      => {
                                           label_escape => 0,
                                           label => $self->localise('USER_NAME')
                                        },
                       shell         => {
                                           label_escape => 0,
                                           label => $self->localise('SHELL_ACCESS')
                                        },
                       sudo          => {
                                           label_escape => 0,
                                           label => $self->localise('SUDO')
                                        },
                       keys          => {
                                           label_escape => 0,
                                           label => $self->localise('SSH_KEYS')
                                        },
                       chroot        => {
                                           label_escape => 0,
                                           label => $self->localise('CHROOT_PATH')
                                        },
                       vpn           => {
                                           label_escape => 0,
                                           label => $self->localise('VPN_ACCESS')
                                        },
                       Modify        => {
                                           label_escape => 0,
                                           label => $self->localise('MODIFY'),
                                           link  => \&modify_link
                                        },
                      }
    };

    my @data = ();
    my @users = $adb->users;

    return $self->localise("ACCOUNT_USER_NONE") if (@users == 0);

    for my $user (@users)
    {
        my $username = $user->key;
        # make clearer by only showing yes and localise
        my $vpn = $user->prop('VPNClientAccess') || '';
        if ($vpn eq 'yes') { $vpn = 'YES'; } else { $vpn = ''; }
        my $sudo = $user->prop('Sudoer') || '';
        if ($sudo eq 'yes') { $sudo = 'YES'; } else { $sudo = ''; }
        my $keys = '';
        my $file = "/home/e-smith/files/users/$username/.ssh/authorized_keys2";
        if (( -e $file ) && (! -z $file ))
        { $keys = 'YES'; }

        my $shell = $user->prop('Shell') || '';
        if ($shell eq '/usr/bin/scponly')  { $shell = ''; }

        my $ChrootDir  = $user->prop('ChrootDir')  || "";
        $ChrootDir =~ s:/home/e-smith/files/ibays/::;
        $ChrootDir =~ s:/home/e-smith/files/users/$username/home:home:;

        push @data,
            { User            => $user->key,
              FullName        => $user->prop('FirstName') . " " .
                                 $user->prop('LastName'),
              Sudoer          => $user->prop('Sudoer') || 'no',
              VPNClientAccess => $user->prop('VPNClientAccess') || 'no',
              shell           => $shell,
              chroot          => $ChrootDir,
              ChrootDir       => $user->prop('ChrootDir')  || "/home/e-smith/files/users/$username/home",
              sudo            => $self->localise($sudo),
              keys            => $self->localise($keys),
              vpn             => $self->localise($vpn),
              Modify          => $self->localise('MODIFY'),
            }
    }

    my $t = HTML::Tabulate->new($user_table);

    $t->render(\@data, $user_table);
}

sub modify_link
{
    my ($data_item, $row, $field) = @_;

    return "remoteuseraccess?" .
        join("&",
        "page=0",
        "page_stack=",
        "Next=Next",
        "User="     .        $row->{User},
        "FullName=" .        $row->{FullName},
        "Sudoer=" .          $row->{Sudoer},
        "Shell=" .           $row->{shell},
        "ChrootDir=" .       $row->{ChrootDir},
        "VPNClientAccess=" . $row->{VPNClientAccess},
        "wherenext=PAGE_MODIFY");
}

sub get_chroot_dir
{
    my $self = shift;
    my %existingAccounts = ('' => '',
                            'home' => ". ~/home" ,
                            '/home/e-smith/files'=> '.. /home/e-smith/files' );

    foreach my $account ($adb->get_all)
    {
        if ($account->prop('type') =~ /(ibay)/)
        {
            $existingAccounts{"/home/e-smith/files/ibays/" . $account->key} = $account->key;
            $existingAccounts{"/home/e-smith/files/ibays/" . $account->key . "/html"} = $account->key . "/html";
            $existingAccounts{"/home/e-smith/files/ibays/" . $account->key . "/files"} = $account->key. "/files";
        }
     }

    return(\%existingAccounts);
}

sub get_keys_text
{
    my $self = shift;
    my $q = $self->{cgi};

    my $user = $q->param('User');

    my $file = "/home/e-smith/files/users/$user/.ssh/authorized_keys2";

    my $sshKeys = '';
    # if exists and is not empty
    if (( -e $file ) && (! -z $file ))
    {
        open (SSHKEY, "<$file")
          or die "Error: Could not open file: $file\n";
	    my @sshTemp = <SSHKEY>;
	    $sshKeys = join ("", @sshTemp);

	    close SSHKEY;
    }

    return $sshKeys;
}

sub change_settings
{
    my $self = shift;
    my $q = $self->{cgi};
    my $Shell           = $q->param ('Shell');
    my $Sudoer          = $q->param ('Sudoer');
    my $VPNClientAccess = $q->param ('VPNClientAccess');
    my $ChrootDir       = $q->param ('ChrootDir');
    my $ChrootDir2      = $q->param ('ChrootDir2');

    my $user = $q->param('User');

    if ($user =~ /^([a-z][\-a-z0-9]*)$/)
    {
	   $user = $1;
    }

    my $sshKeys = $q->param ('sshKeys');
    if ($sshKeys ne '')
    {
        my $file = "/home/e-smith/files/users/$user/.ssh/authorized_keys2";
        my $dir = "/home/e-smith/files/users/$user/.ssh";

        # delete .ssh/authorized_keys2
        if ($sshKeys =~ /deletekeys/)
        {
            system ("/bin/rm -rf $file") == 0
              or die ("Error deleting $file.\n");
        }
        else
        {
            # Strip out DOS Carriage Returns (CR)
            $sshKeys =~ s/\r//g;

	        unless ( -e $file )
	        { system ("/bin/mkdir -p $dir") == 0
                  or die ("Error creating ssh directory.\n");  }

            unlink $file;

            open (SSHKEY, ">$file")
	         or die ("Error saving SSH Keys.\n");

            print SSHKEY "$sshKeys\n";
            close SSHKEY;

            system ("/bin/chown -R $user.$user $dir") == 0
              or die ("Error chown .ssh directory.\n");
        }
    }

    # if the drop down is blank and field is valid
    # set the field to the drop down, save the drop down
    if (($ChrootDir2 eq '' ) && ($ChrootDir ne ''))
    {
       $ChrootDir2 = $ChrootDir || '';
    }

    if (($Sudoer eq 'yes') or ($Shell eq '/bin/bash'))
    {
      $adb->set_prop($user, 'Shell', '/bin/bash');
    } else {
      $adb->set_prop($user, 'Shell', '/usr/bin/scponly');
    }

    $adb->set_prop($user, 'Sudoer', $Sudoer);
    $adb->set_prop($user, 'ChrootDir', $ChrootDir2);
    $adb->set_prop($user, 'VPNClientAccess', $VPNClientAccess);

    system ("/sbin/e-smith/signal-event", "user-modify", $user) == 0
        or die ("Error occurred updating user access\n");

    return $self->success("SUCCESS");
}

#userpanel functions
sub get_panel_user
{
    return $PanelUser;
}

sub get_full_name
{
    return  $adb->get_prop($PanelUser, "FirstName") . " " .
            $adb->get_prop($PanelUser, "LastName");
}

sub userpanel_keys_text
{
    my $self = shift;
    my $q = $self->{cgi};

    my $file = "/home/e-smith/files/users/$PanelUser/.ssh/authorized_keys2";

    if ($PanelUser eq 'admin')
    {  $file = "/root/.ssh/authorized_keys2"; }

	my $sshKeys = '';
    # if exists and is not empty
    if (( -e $file ) && (! -z $file ))
    {
        open (SSHKEY, "<$file")
          or die "Error: Could not open file: $file\n";
	    my @sshTemp = <SSHKEY>;
	    $sshKeys = join ("", @sshTemp);

	    close SSHKEY;
    }

    return $sshKeys;
}

sub userpanel_change_settings
{
    my $self = shift;
    my $q = $self->{cgi};
    my $Shell           = $q->param ('Shell');
    my $Sudoer          = $q->param ('Sudoer');
    my $VPNClientAccess = $q->param ('VPNClientAccess');
    my $ChrootDir       = $q->param ('ChrootDir');
    my $ChrootDir2      = $q->param ('ChrootDir2');

    my $user      = $PanelUser;

    if ($user =~ /^([a-z][\-a-z0-9]*)$/)
    {
	   $user = $1;
    }

    my $sshKeys = $q->param ('sshKeys');
    if ($sshKeys ne '')
    {
        my $file = "/home/e-smith/files/users/$user/.ssh/authorized_keys2";
        my $dir = "/home/e-smith/files/users/$user/.ssh";
        if ($user eq 'admin')
        {  $file = "/root/.ssh/authorized_keys2";
           $dir = "/root/.ssh"; }

        # delete .ssh/authorized_keys2
        if ($sshKeys =~ /deletekeys/)
        {
            system ("/bin/rm -rf $file") == 0
              or die ("Error deleting $file.\n");
        }
        else
        {
            # Strip out DOS Carriage Returns (CR)
            $sshKeys =~ s/\r//g;

	        unless ( -e $file )
	        { system ("/bin/mkdir -p $dir") == 0
                  or die ("Error creating ssh directory.\n");  }

            unlink $file;

            open (SSHKEY, ">$file")
	         or die ("Error saving SSH Keys.\n");

            print SSHKEY "$sshKeys\n";
            close SSHKEY;

            system ("/bin/chown -R $user.$user $dir") == 0
              or die ("Error chown .ssh directory.\n");
        }
    }

    # if the drop down is blank and field is valid
    # set the field to the drop down, save the drop down
    if (($ChrootDir2 eq '' ) && ($ChrootDir ne ''))
    {
       $ChrootDir2 = $ChrootDir || '';
    }

    if (($Sudoer eq 'yes') or ($Shell eq '/bin/bash'))
    {
      $adb->set_prop($user, 'Shell', '/bin/bash');
    } else {
      $adb->set_prop($user, 'Shell', '/usr/bin/rssh');
    }

    $adb->set_prop($user, 'Sudoer', $Sudoer);
    $adb->set_prop($user, 'ChrootDir', $ChrootDir2);
    $adb->set_prop($user, 'VPNClientAccess', $VPNClientAccess);

    system ("/sbin/e-smith/signal-event", "user-modify", $user) == 0
        or die ("Error occurred updating user access\n");

    return $self->success("SUCCESS");
}

sub CheckChrootDirExists
{
    my $self = shift;
    my $q = $self->{cgi};

    my $ChrootDir   = $q->param ('ChrootDir')  || '';
    my $ChrootDir2  = $q->param ('ChrootDir2') || '';

    if ($ChrootDir2 eq '') 
    {
      if ($ChrootDir eq '')
      {
        return "CHROOT_PATH_NOT_GIVEN"; 
      }
      else
      {  
        if ((-e $ChrootDir ) || ($ChrootDir eq 'home'))
        { return "OK"; }
        else
        { return "CHROOT_PATH_NON_EXISTANT"; }
      } 
    }
    else
    { return "OK"; }
}

1;
