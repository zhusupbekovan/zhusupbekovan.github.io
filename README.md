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

![Installing](./resources/img/1.png)
![Installing](./resources/img/2.png)
![Installing](./resources/img/3.png)
![Installing](./resources/img/4.png)
![Installing](./resources/img/5.png)
![Installing](./resources/img/6.png)
![Installing](./resources/img/7.png)
![Installing](./resources/img/8.png)


## Installation Setup

1. **Download Arch Linux ISO**  
  Download the latest Arch Linux ISO from [archlinux.org](https://archlinux.org/download/).
   
1. **Set Up VM**  
Use your preferred hypervisor (e.g., VirtualBox, VMware) to create a VM. Allocate at least 2GB of RAM and 20GB of disk space.
1. **Boot into Arch ISO**  
Boot the VM using the downloaded ISO.

1. **Partition the Disk**  
Use `fdisk` or `cfdisk` to create partitions:
- `/dev/sda1` for the EFI partition (512MB).
- `/dev/sda2` for the root partition (remaining space).
  ```bash
  mkfs.fat -F32 /dev/sda1
  mkfs.ext4 /dev/sda2
  mount /dev/sda2 /mnt
  mkdir /mnt/boot
  mount /dev/sda1 /mnt/boot
  ```
1. **Install Essential Packages**  
Install base packages:
  ```bash
  pacstrap /mnt base linuxlinux-firmware
   ```
1. **Configure the System**  
Generate fstab and configure hostname, timezone, and locale:
  ```bash
  genfstab -U /mnt >> /mnt/etcfstab
  arch-chroot /mnt
  ln -sf /usr/share/zoneinfoRegion/    City /etc/localtime
  hwclock --systohc
  echo "en_US.UTF-8 UTF-8" > etc/    locale.gen
  locale-gen
  echo "myhostname" > /etchostname
   ```


1. **Install Bootloader**  
Install and configure GRUB bootloader:
  ```bash
  pacman -S grub efibootmgr
  grub-install--target=x86_64-efi   --efi-directory=/boot  --bootloader-id=GRUB
  grub-mkconfig -o /boot/grubgrub.   cfg
   ```

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
