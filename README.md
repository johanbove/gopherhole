# Welcome to Johan's Gopherhole!

This is a _Gopher burrow_ or _Gopher space_ running on PygoPherd.

> Make sure to keep the gophermap files as these contain most of the content!

## Status

### 2020-04-13

Still keeping this Gopher site going.

### 2019-11-02

Mirroring everything on [a private GitHub
repo](https://github.com/johanbove/gopherhole) as backup for the files on my
RaspBerry Pi and also to be able to remote edit files; even if publishing is not
possible until I get home.

### 2019-10-26

Added a twtxt.file as my twtxt feed. Neat.

### 2019-10-20

Currently I am testing out running a Gopher server on this Raspberry Pi.

Installed **"pygopherd"**, a Perl based Gopher server.

Installed the OverbiteWX and OverbiteNX [FireFox
addons](https://addons.mozilla.org/en-US/firefox/user/1605919/) to
open gopher files.

## Resources

- [The history of Gopher](https://prgmr.com/blog/gopher/2018/08/23/gopher.html)
- <gopher://gopher.floodgap.com/1/new>
- [The overbite Project](https://gopher.floodgap.com/overbite/)
- [Why is Gover still relevant?](https://gopher.floodgap.com/overbite/relevance.html)
- <https://gopher.zone/posts/running-a-gopher-server-in-2018/>

## Tips

- <https://stackoverflow.com/questions/1675688/make-vim-show-all-white-spaces-as-a-character>
- <https://stackoverflow.com/questions/6951672/how-can-i-insert-a-real-tab-character-in-vim>

## Configuration

The configuration file for Pygopherd is kept in:

  /etc/pygophred/pygopherd.conf

## Starting and stopping the server

  sudo /etc/init.d/pygopherd start

  sudo /etc/init.d/pygopherd stop

## Opening up public access

Use UFW to open TCP access on port 70.

## Set up fixed IP with DuckDNS

My home ip changes so I need to monitor these changes.
www.duckdns.org provide a free IP monitor.

## Set up domain forwarding

Add a CNAME entry in your domain name settings.

## Publishing

This site is published with a command of which I made an alias, in my
~/.bashrc file.

   gopherpublish   

The command `$ gopherpublish` is aliased to:

  `git add . && git commit -a -m "update content" && git push origin'

Once the code is published to the repository on the rapsberrypi.local
machine, git will execute this post-receive hook to deploy the
updated files into the `/var/gopher` folder.

Script `hooks/post-receive` :

	GIT_WORK_TREE=/var/gopher git checkout -f

> **TIP** Don't forget to `chmod +x hooks/post-receive` !

## To Do

- Set up a back up system in case the RaspBerryPi is foobarred.
- Forward visitors of social.johanbove.info:70 to
  gopher.johanbove.info
- Add more useful content to the site.
