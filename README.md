# Arch Linux VM Installation Documentation

This document outlines the steps taken to install Arch Linux in a virtual machine, along with customizations and troubleshooting encountered during the process.

## Table of Contents
- [Arch Linux VM Installation Documentation](#arch-linux-vm-installation-documentation)
  - [Table of Contents](#table-of-contents)
  - [Install WMware Workstation](#install-wmware-workstation)
    - [Download WMware Workstation Installer](#download-wmware-workstation-installer)
    - [Installation Setup](#installation-setup)
  - [User Accounts](#user-accounts)
  - [Desktop Environment](#desktop-environment)
  - [Customizations](#customizations)
  - [Issues Encountered](#issues-encountered)
  - [Commands Used](#commands-used)
  - [References](#references)

---
## Install WMware Workstation
### Download WMware Workstation Installer
- Go to [https://support.broadcom.com/](https://support.broadcom.com/), login/register for the portal. 
- Go to *WMWare Cloud Foundation* 
  
![Installing](./resources/img/WMware%20Foundation.png)
- Go to *My Donwloads*, find *VMware Workstation Pro* and choose the latest version for *Personal Use*
- Check the properties shown below

![Installing](./resources/img/SHA2.png)
- Complete the installation, see the screenshots below.

<img src="./resources/img/1.png" width="50%"  style="display:block;margin: auto;" />
<img src="./resources/img/2.png" width="50%" style="display:block;margin: auto;" />
<img src="./resources/img/3.png" width="50%" style="display:block;margin: auto;" />
<img src="./resources/img/4.png" width="50%" style="display:block;margin: auto;" />
<img src="./resources/img/5.png" width="50%" style="display:block;margin: auto;" />
<img src="./resources/img/6.png" width="50%" style="display:block;margin: auto;" />
<img src="./resources/img/7.png" width="50%" style="display:block;margin: auto;" />
<img src="./resources/img/8.png" width="50%" style="display:block;margin: auto;" />


### Installation Setup

1. **Download Arch Linux ISO**  
Download the latest Arch Linux ISO from [archlinux.org](https://archlinux.org/download/). This installation uses archlinux.doridian.net.
  ![arch-linux](./resources/img/arch-linux.png)  
   
2. **Set Up VM**  
Use VMware to create a VM. Allocate at least 4GB of RAM and 20GB of disk space. See the steps below.
<img src="./resources/img/1.1.png" width="75%"  style="display:block;margin: auto;" />
<img src="./resources/img/1.2.png" width="50%" style="display:block;margin: auto;" />
<img src="./resources/img/1.3.png" width="50%" style="display:block;margin: auto;" />
<img src="./resources/img/1.4.png" width="50%" style="display:block;margin: auto;" />
<img src="./resources/img/1.6.png" width="50%" style="display:block;margin: auto;" />
<img src="./resources/img/1.5.png" width="50%" style="display:block;margin: auto;" />
<img src="./resources/img/1.7.png" width="50%" style="display:block;margin: auto;" />
<img src="./resources/img/1.8.png" width="50%" style="display:block;margin: auto;" />

3. **Boot into Arch ISO**  
Boot the VM using the downloaded ISO.
<img src="./resources/img/2.1.png" width="75%" style="display:block;margin: auto;" />
<img src="./resources/img/2.2.png" width="75%" style="display:block;margin: auto;" />
<img src="./resources/img/2.3.png" width="75%" style="display:block;margin: auto;" />

4. **Partition the Disk**  
Use `fdisk` or `cfdisk` to create partitions:
- `/dev/sda1` - 1G - for /boot
- `/dev/sda2` - 5G - for root
- `/dev/sda3` - 1G - for swap

First, run the below command to find out the device identifier:
```bash
  fdisk -l
```

<img src="./resources/img/3.1.png" width="75%" style="display:block;margin: auto;" />

Then, with the device identifier, run the below command to start partitioning your disk. Make sure to change `/dev/sda` as per your system.
```bash
  cfdisk /dev/sda
```
<img src="./resources/img/3.2.png" width="75%" style="display:block;margin: auto;" />

Select `label type = dos` in the next prompt.

Select the free space and choose option NEW from the bottom. 

<img src="./resources/img/3.3.png" width="75%" style="display:block;margin: auto;" />

Run the below command to check before you proceed to see in three partitions are listed.

```bash
  fdisk -l
```
<img src="./resources/img/3.4.png" width="75%" style="display:block;margin: auto;" />

Run the following commands in sequence to format and create an ext4 file system in the newly created partition above. Make sure you change the /dev/sda1 and /dev/sda2 as per your need.
```bash
  mkfs.fat -F32 /dev/sda1
  mkfs.ext4 /dev/sda2
  mount /dev/sda2 /mnt
  mkdir /mnt/boot
  mount /dev/sda1 /mnt/boot
```

After completion, mount the system and create the necessary directories.

```bash
  mount /dev/sda2 /mnt
  mkdir /mnt/boot /mnt/var /mnt/home
  mount /dev/sda1 /mnt/boot
```
<img src="./resources/img/3.5.png" width="75%" style="display:block;margin: auto;" />

5. **Install Essential Packages**  
Install base packages:
  ```bash
  pacman -Syy
  pacstrap /mnt base base-devel linux linux-firmware nano dhcpcd net-tools grub
   ```
6. **Configure the System**  
Generate fstab and configure hostname, timezone, and locale:
  ```bash
  genfstab -U /mnt >> /mnt/etcfstab
  arch-chroot /mnt
  ln -sf /usr/share/zoneinfoRegion/Chicago /etc/localtime
  hwclock --systohc
  echo "en_US.UTF-8 UTF-8" > etc/    locale.gen
  locale-gen
  echo "nuraiym" > /etchostname
   ```

  The next step is to set up the root user password, create an admin user, and add the user to the sudoers file.

  Follow the below commands in sequence. Make sure to change the user name from debugpoint to something else as per your need.
  ```bash
  passwd root
  useradd -m -g users -G wheel -s /bin/bash nuraiym
  passwd nuraiym
   ```

  Open the sudoers file and add the below lines.

  ```bash
  nano /etc/sudoers
   ```

  Add below lines. As you already created the root user, the entry should be there.
  ```bash
  root ALL=(ALL) ALL
  nuraiym ALL=(ALL) ALL
   ```
7. **Install Bootloader**  
Install grub, setup the initial ramdisk environment, unmount the system using the below commands in sequence.
  ```bash
  grub-install /dev/sda
  grub-mkconfig -o /boot/grub/grub.cfg
  mkinitcpio -p linux
   ```
  Then reboot the system.
  ```bash
  umount /mnt/boot
  umount /mnt
  reboot
   ```


8. **Install LXQt Desktop**   
After reboot, choose Arch Linux from grub. In the Arch Linux prompt, start running the following commands in sequence. These commands install the Xorg server, display manager, LXQt desktop components, controller packages, and additional applications.

  For all the commands, use the default, i.e. press enter when asked.

- Install Xorg
```bash
sudo pacman -S --needed xorg
```
- Install display manager, lxqt desktop. Approx install size is 100 MB.
```bash
sudo pacman -S --needed lxqt xdg-utils ttf-freefont sddm
```
- Install additional components (approx 80 MB)
```bash
sudo pacman -S --needed libpulse libstatgrab libsysstat lm_sensors network-manager-applet oxygen-icons pavucontrol-qt
```
- Install applications
```bash
sudo pacman -S --needed firefox vlc filezilla leafpad xscreensaver archlinux-wallpaper
```
- Now it’s time to enable the display manager and network manager as a service. So that, the next time you log on, they can run automatically by systemd.
```bash
systemctl enable sddm
systemctl enable NetworkManager
```
- Reboot the system using the reboot command.
```bash
reboot
```

You should see a nice login prompt on the LXQt desktop if all goes well.

And you can now log in using the user id and password which you just created. A Nice and superfast LXQt desktop will greet you after a successful login.

<img src="./resources/img/3.6.png" style="display:block;margin: auto;" />



**Note:** If some of the commands are not working, you may need to put sudo before running it.


## User Accounts
1. Create User Accounts
Add user accounts for yourself, justin, and codi:
   ```bash 
   useradd -m -G wheel -s /bin/bash <your-username>
   useradd -m -G wheel -s /bin/  bash  justin
   useradd -m -G wheel -s /bin/  bash  codi
   ```
2. Set Passwords
Assign passwords to users and enforce a password change on the first login:
   ```bash 
  passwd <your-username>
  passwd justin
  passwd codi
  chage -d 0 justin
  chage -d 0 codi
   ```
3. Configure sudo
Edit the sudoers file to grant sudo permissions:
  ```bash 
  visudo
  ```
Uncomment:
  ```bash 
  %wheel ALL=(ALL:ALL) ALL
  ```

## Desktop Environment
1. Install a Desktop Environment
Install LXQt or another lightweight desktop environment:
  ```bash 
  pacman -S xorg lxqt
  ```
2. Enable the Display Manager
Enable LightDM as the display manager:
  ```bash 
  pacman -S lightdm lightdm-gtk-greeter
systemctl enable lightdm
  ```
3. **Reboot**
  Reboot the system to verify the installation:
  ```bash 
  reboot
  ```

## Customizations
1. **Install a Different Shell**
Install and configure zsh:
  ```bash 
  pacman -S zsh
  chsh -s /bin/zsh <your-username>
  ```
2. Enable Terminal Colors
Enable color coding in the terminal by editing .zshrc or `.bashrc`:
  ```bash 
  alias ls='ls --color=auto'
  ```

3. Set Up Aliases
Add custom aliases to .zshrc or `.bashrc`:
  ```bash 
alias update='sudo pacman -Syu'
alias cls='clear'
alias ..='cd ..'
  ```
4. Install and Configure SSH
Install SSH and start it at boot
  ```bash 
pacman -S openssh
systemctl enable sshd
systemctl start sshd
  ```

## Issues Encountered
1. Partitioning
I initially forgot to create the EFI partition. I resolved this by going back and using fdisk to create a new partition for /dev/sda1 as the EFI boot partition.

2. GRUB Installation Failure
GRUB failed to install because I did not mount the EFI directory. After mounting /boot, I was able to install GRUB successfully.

## Commands Used
Here is a summary of important commands used during the installation process:

- `pacstrap /mnt base linux linux-firmware` - Install essential packages.
- `genfstab -U /mnt >> /mnt/etc/fstab` - Generate the filesystem table.
- `grub-install --target=x86_64-efi --efi-directory=/boot --bootloader-id=GRUB` - Install GRUB bootloader.


## References
- [Arch Linux Installation Wiki](https://wiki.archlinux.org/title/Installation_guide)
- [Arch User Repository (AUR)](https://aur.archlinux.org/)
- [ZSH Documentation](https://zsh.sourceforge.io/Doc/Release/)
