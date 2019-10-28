# Welcome to Johan's Gopherhole!

## Status

### 2019-10-26

Added a twtxt.file as my twtxt feed. Neat.

### 2019-10-20

Currently I am testing out running a Gopher server on this Raspberry Pi.

Installed **"pygopherd"**, a Perl based Gopher server.

Installed the OverbiteWX and OverbiteNX [FireFox addons](https://addons.mozilla.org/en-US/firefox/user/1605919/) to open gopher files.


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

### Git repo

hooks/post-receive

    GIT_WORK_TREE=/var/www/home.murphy-bove.net/html git checkout -f

> **TIP** Don't forget to `chmod +x hooks/post-receive` !