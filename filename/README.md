rename.sh
=========

Simple script to rename ```.png``` and ```.jpg``` files in folders by index position (given by the iteration on the file system). In addition it is possible to specify a prefix that will be set before the index.

Usage : 
```bash
./rename.sh <path-to-folder> [prefix]
```

Example:

Assume we want to rename a bunch of JPG files in folder `${TARGET_DIR}` listed here:
```bash
$ ls -1 ${TARGET_DIR}
file_a.jpg
file_b.jpg
file_c.jpg
```

By default:
```bash
$ ./rename.sh ${TARGET_DIR}
```

The files will be renamed as follows:

```bash
$ ls -1 ${TARGET_DIR}
1.jpg
2.jpg
3.jpg
```

When executing the script with prefix `pre`:

```bash
$ ./rename.sh ${TARGET_DIR} hello-david
```

The files will be renamed as follows:

```bash
$ ls -1 ${TARGET_DIR}
pre-1.jpg
pre-2.jpg
pre-3.jpg
```


