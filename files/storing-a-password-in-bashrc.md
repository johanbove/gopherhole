# Storing a password safely using .bashrc and openssl encryption ####

You need to keep entering a password in the terminal or as part of a
bash script? This how-to will explain how you can safely store your
password without worrying about accidentally sharing it.

## Instructions

[Source](https://stackoverflow.com/a/10115394)

### Terminal Tip

Use space at the start to avoid history registration -> set `export
HISTCONTROL=ignorespace` in your bashrc first.

### Instructions for PC

If you have Git installed on your PC, you should find the OpenSSL
executable in this folder: C:\Program Files\Git\usr\bin\openssl.exe

[Source](https://stackoverflow.com/a/51757939)

### Encrypting your password

Encrypt the password string using openssl:

  $ echo 'mypass' | openssl aes-256-cbc -a -salt

Enter an easy to remember password to encrypt and decrypt the string
and confirm it again.

Save the resulting hash string (the key) as `__PassWord` in your
~/.bashrc file.

```
" Add aliases to .bashrc
export __UserName={yourusername}
export __PassWord=U2FXXXXXXXXXXXXXXXXXXXXXXXXXXXX=
```

Use the password in docker login in a secure way; running this will
ask for the decryption password.

Define the terminal alias:

  alias dockerLogin='echo $__PassWord | openssl aes-256-cbc -a -d \
  -salt | docker login --username $__UserName --password-stdini \
  docker-scf.domain'

Now you can call `dockerLogin` whenever you need to authenticate with
Docker.

The openssl decryption process will request you for the unlock
password which won't be stored anywhere.

