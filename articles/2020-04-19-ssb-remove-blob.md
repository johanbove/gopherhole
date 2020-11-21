# Removing a blob on Secure Scuttlebutt 

See: <https://github.com/fraction/ssb-blob-prune>

```bash
johan@Surface:~/.ssb/scripts$ fname=~/.ssb/blobs/sha256/{blobpath}
johan@Surface:~/.ssb/scripts$ rm -f $fname
johan@Surface:~/.ssb/scripts$ touch $fname
johan@Surface:~/.ssb/scripts$ ./ssb-prune-blobs.sh
```
## ssb-prune-blobs.sh

```bash
#!/usr/bin/env bash

# written by @RuNxm8SRujPcJx6GjtTQHp6hprAFv5voEkcvoAkB8Pk=.ed25519
# inspired by %f8Q7v98rcHPa/YDJZH82jVsidVL4Erq1n83ykeQ8wk4=.sha256

BLOBS=~/.${ssb_appname:-ssb}/blobs/sha256

verbose=''
# comment out the following line in order to always go silent
verbose='v'

HOURS=$(date '+%H')

case "$HOURS" in
 # Don't say a thing if invoked at night
  00 | 01 | 02 | 03 | 04 | 05 )
   verbose=''
  ;;
esac

# === you needn't change antything below this line ===

[[ -d "$BLOBS/." ]] || {
  echo "cannot find blobs directory: $BLOBS" >&2
  exit 1
}

# http://redsymbol.net/articles/unofficial-bash-strict-mode/
set -euo pipefail

remove_by_size_and_mtime () {
  local size="$1"
  local days="$2"
  local plural='s'

  [[ -n "$verbose" ]] && {
    [[ "$days" == "1" ]] && plural=''
    printf '# size > %5s and age > %3d day%s\n' "$size" "$days" "$plural"
  }

  # you will probably need gnu findutils for this
  find "$BLOBS" -type f -size "+$size" -mtime "+$days" -print0 \
  | xargs -r0 rm -${verbose}f
}

  # Please modify these to suit your storage policy:

  # remove blobs over 5M after a day
  remove_by_size_and_mtime 5120k 1

  # remove blobs over 4M after a week
  remove_by_size_and_mtime 4096k 7

  # remove blobs over 3M after two weeks
  remove_by_size_and_mtime 3072k 14

  # remove blobs over 2M after a moon
  remove_by_size_and_mtime 2048k 28

  # remove blobs over 1M after a quarter of a year
  remove_by_size_and_mtime 1024k 91

  # remove blobs over 512k after a year 
  remove_by_size_and_mtime  512k 365

  # remove empty blobs
  [[ -n "$verbose" ]] && echo 'empty blobs, regardless of age'

  find "$BLOBS" -type f -size 0c -print0 \
  | xargs -r0 rm -${verbose}f
  :

  # eof

```

